from math import ceil
from random import choices

from BaseClasses import Location, Region, ItemClassification as IC
from worlds.AutoWorld import WebWorld, World

from .Groups import item_groups, location_groups
from .Items import CassetteBeastsItem, item_table, item_data_table, cb_regular_items, cb_resource_items, cb_tape_items, cb_bootleg_tape_items,\
					cb_trap_items, cb_remaster_sticker_items, shouldAddItem, cb_trap_item_weights
from .Locations import CassetteBeastsLocation, location_table, location_data_table, event_data_table, getLocationCount
from .Options import CassetteBeastsOptions
from .Regions import region_data_table

from .Data.tape_data import monsters



class CassetteBeastsWebWorld(WebWorld):
	theme = "grass"


class CassetteBeastsWorld(World):
	"""Collect awesome monsters to use during turn-based battles in this open-world RPG.
	Combine any two monster forms using Cassette Beasts’ Fusion System to create
	unique and powerful new ones!"""

	game = "Cassette Beasts"
	web = CassetteBeastsWebWorld()
	options_dataclass = CassetteBeastsOptions
	options: CassetteBeastsOptions
	item_name_to_id = item_table
	location_name_to_id = location_table
	item_name_groups = item_groups
	location_name_groups = location_groups

	def create_item(self, name: str) -> CassetteBeastsItem:
		return CassetteBeastsItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

	def create_items(self) -> None:
		start_inventory = self.options.start_inventory.value
		item_pool = []
		for item_name, item_data in item_data_table.items():
			count = item_data.count
			if item_name in start_inventory.keys():
				count -= start_inventory[item_name]
				if count <= 0:
					continue
			if shouldAddItem(self.options, item_name):
				item_pool += [self.create_item(item_name) for _ in range(count)]

		# Trainersanity
		if self.options.trainersanity:
			count = getLocationCount(self.options, "trainersanity_locations")
			trainersanity_items = [name for name in ["Olive-Up!", "Respool", "Rewind", "Upgrape"]]
			item_pool += [self.create_item(c) for c in choices(trainersanity_items, weights=[1,2,3,1], k=count)]

		# Tapesanity
		if self.options.tapesanity != "none":
			count = 0
			if self.options.tapesanity == "specific":
				monster_data = monsters(self.options).values()
				for monster in monster_data:
					if monster.tapesanity_item == None:
						count += 1
					else:
						item_pool += [self.create_item(monster.tapesanity_item)]
			else:
				count += self.options.tapesanity_percentage_item_count

			count -= 2 # skelly jellies
			item_pool += [CassetteBeastsItem("Skelly Jelly", IC.progression, item_data_table["Skelly Jelly"].code, self.player)
							for i in range(2)]
			filler = cb_tape_items
			if self.options.add_bootleg_tapes:
				filler |= cb_bootleg_tape_items
			item_pool += [self.create_item(c) for c in choices([*filler.keys()], k=count)]

		# Bootlegsanity
		if self.options.bootlegsanity != "none":
			per_tape = self.options.bootlegsanity in ["per_tape", "percentage_tape"]
			percentage = self.options.bootlegsanity in ["percentage_tape", "percentage_all"]
			pool = ["Cyber Material x20", "Ritual Candle"] + [*cb_bootleg_tape_items]
			if not percentage:
				count = 0
				for monster in monsters(self.options).values():
					if monster.bootlegsanity_item == "bootleg_tape":
						if per_tape:
							item_pool += [self.create_item(choices([*cb_bootleg_tape_items.keys()], k=1)[0])]
						else:
							item_pool += [self.create_item(key) for key in cb_bootleg_tape_items.keys()]
					elif monster.bootlegsanity_item == None:
						count += 1 if per_tape else 14
					else:
						item_pool += [self.create_item(monster.bootlegsanity_item) for i in range(1 if per_tape else 14)]
				count -= 2 if per_tape else 28 # skelly jellies
				item_pool += [CassetteBeastsItem("Skelly Jelly", IC.useful, item_data_table["Skelly Jelly"].code, self.player)
							for i in range(2 if per_tape else 28)]
				item_pool += [self.create_item(c) for c in choices(pool, weights=[5,2]+[1]*14, k=count)]
			else:
				item_pool += [self.create_item(c) for c in choices(pool, weights=[5,2]+[1]*14, k=self.options.bootlegsanity_percentage_item_count)]

		# Fusionsanity
		if self.options.fusionsanity:
			for i in range(max(self.options.fusionsanity_item_count-2, 1)):
				item_pool += [CassetteBeastsItem("Pear Fusilli", IC.filler, item_data_table["Pear Fusilli"].code, self.player)]
			item_pool += [CassetteBeastsItem("Skelly Jelly", IC.progression, item_data_table["Skelly Jelly"].code, self.player)
							for i in range(2)]

		# Add Traps
		if self.options.traps != "none":
			remaining = getLocationCount(self.options)-len(item_pool)
			if self.options.traps == "few":
				count = min(max(4, remaining//20), remaining)
			elif self.options.traps == "some":
				count = min(max(5, remaining//5), remaining)
			elif self.options.traps == "many":
				count = min(max(6, remaining//2), remaining)
			item_pool += [self.create_item(c) for c in choices([*cb_trap_items.keys()], cb_trap_item_weights, k=count)]

		# Randomized Filler
		filler_items = cb_regular_items.keys()|cb_resource_items.keys()|cb_tape_items.keys()
		if self.options.add_bootleg_tapes:
			filler_items |= cb_bootleg_tape_items.keys()

		item_pool += [self.create_item(c)
			for c in choices(
				[*filler_items],
				k=getLocationCount(self.options)-len(item_pool)-len(self.get_pre_fill_items()))
			]

		self.multiworld.itempool += item_pool

	def create_regions(self) -> None:
		# Create Regions
		for name in region_data_table.keys():
			self.multiworld.regions.append(Region(name, self.player, self.multiworld))

		# Create Locations
		for name, data in region_data_table.items():
			region = self.multiworld.get_region(name, self.player)
			region.add_locations({
				loc_name: loc_data.address for loc_name, loc_data in location_data_table.items()
				if loc_data.region == name and (loc_data.requires == None or loc_data.requires(self.options))
				}, CassetteBeastsLocation)
			region.add_exits([exit for exit, rules in data.exit_rules.items()])

		# Create Events
		for name, data in event_data_table.items():
			if not (data.requires == None or data.requires(self.options)):
				continue
			region = self.multiworld.get_region(data.region, self.player)
			event = CassetteBeastsLocation(self.player, name, None, region)
			event.place_locked_item(CassetteBeastsItem(data.item, IC.progression_skip_balancing, None, self.player))
			region.locations += [event]

		# For tapesanity percentage, bootlegsanity, and fusionsanity, and Captain Zedd we need Recorded of each monster
		if self.options.tapesanity != "specific":
			for monster in monsters(self.options).keys():
				region = self.multiworld.get_region("Menu", self.player)
				event = CassetteBeastsLocation(self.player, f"Recorded {monster}", None, region)
				event.place_locked_item(CassetteBeastsItem(f"Recorded {monster}", IC.progression_skip_balancing, None, self.player))
				region.locations += [event]

		self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

	def get_filler_item_name(self) -> str:
		return "Cyber Material"

	def set_rules(self) -> None:
		from .Rules import set_rules
		set_rules(self)
		self.set_victory()

	def generate_early(self) -> None:
		# Check if Tapesanity Percentage has too many items and fix
		if self.options.tapesanity == "percentage":
			count = self.options.tapesanity_percentage_item_count
			locs = ceil(self.options.tapesanity_percentage_item_count.range_end*(self.options.tapesanity_percentage/100))
			if count > locs:
				print(f"Too many items for Tapesanity: reducing from {count} to {locs}")
				self.options.tapesanity_percentage_item_count.value = locs

		# Check if Bootlegsanity has too many items and fix
		if self.options.bootlegsanity in ["percentage_tape", "percentage_all"]:
			count = self.options.bootlegsanity_percentage_item_count
			locs = ceil(self.options.bootlegsanity_percentage_item_count.range_end*(self.options.bootlegsanity_percentage/100))
			if count > locs:
				print(f"Too many items for Bootlegsanity: reducing from {count} to {locs}")
				self.options.bootlegsanity_percentage_item_count.value = locs

		# Check if Fusionsanity has too many items
		if self.options.fusionsanity:
			count = self.options.fusionsanity_item_count
			locs = self.options.fusionsanity_amount
			if locs > 16384 and not self.options.use_pier:
				locs = 16384
			if count > locs:
				print(f"Too many items for Fusionsanity: reducing from {count} to {locs}")
				self.options.fusionsanity_item_count.value = locs

	def pre_fill(self) -> None:
		if self.options.exclude_postgame:
			for loc in self.multiworld.get_region("Postgame", self.player).locations:
				loc.progress_type = 3 # Excluded

	def set_victory(self) -> None:
		conditions = []
		for goal in self.options.goal.value:
			match goal:
				case "Escape":
					conditions.append(lambda state: state.has("Defeated Aleph", self.player))
				case "Captain":
					conditions.append(lambda state: state.has("Became Captain", self.player))
		self.multiworld.completion_condition[self.player] = lambda state: all([c(state) for c in conditions])

	def fill_slot_data(self) -> dict:
		# Fix empty goal set
		if self.options.goal.value == {}:
			self.options.goal.value = {"Escape"}
		return {
			"item_apName_to_cbItemData": {name: (data.cb_name, data.amount) for name, data in item_data_table.items()},
			"location_cbName_to_apName": {data.cb_name: name for name, data in location_data_table.items()
											if (data.requires == None or data.requires(self.options))},
			"giveItemAction_to_location": {
				"tutorial": "Ranger Handbook",
				"type_chart": "Type Chart",
				"key_harbourtown": "Harbourtown Gate Key",
				"meredith_envelope": "Envelope for Meredith",
				"key_landkeeper": "Landkeeper Key",
				"captain_badge": "encounter_ianthe",
			},
			"itemDrop_to_location": {
				"trainticket_glowshroom": "Train Ticket (Glowcester)",
				"trainticket_graveyard": "Train Ticket (Aldgrave Tomb)",
				"captain_cleeo_coin": "Captain Clee-o Coin",
			},
			"settings": {
				"goal": self.options.goal.value,
				"song_part_count": self.options.song_part_count.value,
				"final_battle_friend_count": self.options.final_battle_friend_count.value,
				# archangel_hunt_count not required to be sent to Cassette Beasts
				# exclude_postgame" not required to be sent to Cassette Beasts
				"experience_multiplier": self.options.experience_multiplier.value,
				"friendship_multiplier": self.options.friendship_multiplier.value,
				"battle_loot_multiplier": self.options.battle_loot_multiplier.value,
				"bootleg_multiplier": self.options.bootleg_multiplier.value,
				# use_pier not required to be sent to Cassette Beasts
				"shuffle_chest_loot_tables": self.options.shuffle_chest_loot_tables.value,
				# traps not required to be sent to Cassette Beasts
				"shopsanity": self.options.shopsanity.value,
				"trainersanity": self.options.trainersanity.value,
				"tapesanity": self.options.tapesanity.value,
				"tapesanity_percentage": self.options.tapesanity_percentage.value,
				"tapesanity_percentage_item_count": self.options.tapesanity_percentage_item_count.value,
				# add_bootleg_tapes not required to be sent to Cassette Beasts
				"bootlegsanity": self.options.bootlegsanity.value,
				"bootlegsanity_percentage": self.options.bootlegsanity_percentage.value,
				"bootlegsanity_percentage_item_count": self.options.bootlegsanity_percentage_item_count.value,
				"fusionsanity": self.options.fusionsanity.value,
				"fusionsanity_amount": self.options.fusionsanity_amount.value,
				"fusionsanity_item_count": self.options.fusionsanity_item_count.value,
				# special_monsters not required to be sent to Cassette Beasts
				"death_link": self.options.death_link.value,
			},
		}