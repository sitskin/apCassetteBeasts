
from math import ceil
from random import choices

from BaseClasses import Location, Region, ItemClassification as IC
from worlds.AutoWorld import WebWorld, World

from .Groups import item_groups, location_groups
from .Items import CassetteBeastsItem, item_table, item_data_table, cb_regular_items, cb_resource_items, cb_tape_items, cb_trap_items, cb_remaster_sticker_items, shouldAddItem
from .Locations import CassetteBeastsLocation, location_table, location_data_table, event_data_table, getLocationCount, isLocation
from .Options import CassetteBeastsOptions
from .Regions import region_data

from .Data.tape_data import monsterCount, monsters

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

	def create_item(self, name):
		
		return CassetteBeastsItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

	def create_items(self):
		item_pool = []

		for item_name, item_data in item_data_table.items():
			#TODO code for managing starting items and ignoring them when adding items
			if shouldAddItem(self.options, item_name):
				item_pool += [self.create_item(item_name) for _ in range(item_data.count)]

		# Trainersanity
		if self.options.trainersanity:
			count = 88 # TODO de-magic this number
			trainersanity_items = [name for name in ["Olive-Up!", "Respool", "Rewind", "Upgrape"]]
			item_pool += [self.create_item(c) for c in choices(trainersanity_items, weights=[3,2,1,1], k=count)]

		# Tapesanity
		if self.options.tapesanity != "none":
			count = monsterCount(self.options) if self.options.tapesanity == "specific" else self.options.tapesanity_percentage_item_count
			count -= 8 # remaster stickers except gear shear and 2 skelly jelly
			item_pool += [CassetteBeastsItem("Skelly Jelly", IC.progression, item_data_table["Skelly Jelly"].code, self.player)
							for i in range(2)]
			item_pool += [self.create_item(item_name) for item_name, item_data in cb_remaster_sticker_items.items() if item_data.count == 0]
			if count >= 14:
				for name in cb_tape_items.keys():
					if name in ["Basic Tape x5", "Chrome Tape x5", "Optical Laser Tape", "Black Shuck's Tape"]:
						continue
					item_pool += [self.create_item(n) for n in [name]*(count//14)]
			item_pool += [self.create_item(c) for c in choices([*cb_tape_items.keys()], k=count%14)]

		# Bootlegsanity
		if self.options.bootlegsanity != "none":
			count = monsterCount(self.options)*14 if self.options.bootlegsanity == "specific" else self.options.bootlegsanity_percentage_item_count
			items = ["Ritual Candle", "Cyber Material x20", "Black Shuck's Tape"]
			item_pool += [self.create_item(c) for c in choices(items, weights=[1,3,2], k=count)]

		# Fusionsanity
		if self.options.fusionsanity:
			for i in range(self.options.fusionsanity_item_count):
				item_pool += [CassetteBeastsItem("Pear Fusilli", IC.filler, item_data_table["Pear Fusilli"].code, self.player)]

		if self.options.tapesanity == "none" and (self.options.bootlegsanity != "none" or self.options.fusionsanity):
			# Add remaster stickers except gear shear if not using tapesanity caused them to be skipped
			item_pool += [self.create_item(item_name) for item_name, item_data in cb_remaster_sticker_items.items() if item_data.count == 0]

		# Add Traps
		if self.options.traps != "none":
			remaining = getLocationCount(self.options)-len(item_pool)
			if self.options.traps == "few":
				count = min(max(4, remaining//20), remaining)
			elif self.options.traps == "some":
				count = min(max(5, remaining//5), remaining)
			elif self.options.traps == "many":
				count = min(max(6, remaining//2), remaining)
			item_pool += [self.create_item(c) for c in choices([*cb_trap_items.keys()], [5,2,3,1], k=count)]

		# Randomized Filler
		item_pool += [self.create_item(c)
			for c in choices(
				[*cb_regular_items.keys()|cb_resource_items.keys()|cb_tape_items.keys()],
				k=getLocationCount(self.options)-len(item_pool)-len(self.get_pre_fill_items()))
			]

		self.multiworld.itempool += item_pool

	def create_regions(self):
		# Create Regions
		for region_name in region_data.keys():
			region = Region(region_name, self.player, self.multiworld)
			self.multiworld.regions.append(region)

		# Create Locations
		for region_name, region_exits in region_data.items():
			region = self.multiworld.get_region(region_name, self.player)
			region.add_locations({
				location_name: location_data.address for location_name, location_data in location_data_table.items()
				if location_data.region == region_name and isLocation(self.options, location_name)
				}, CassetteBeastsLocation)
			region.add_exits(region_exits)

		# Create Events
		for name, data in event_data_table.items():
			if data.dlc:
				if data.dlc == "pier" and not self.options.use_pier:
					continue
			region = self.multiworld.get_region(data.region, self.player)
			event = CassetteBeastsLocation(self.player, name, None, region)
			event.place_locked_item(CassetteBeastsItem(data.item, IC.progression_skip_balancing, None, self.player))
			region.locations += [event]

		# For tapesanity percentage, bootlegsanity, and fusionsanity we need Recorded of each monster
		if self.options.tapesanity != "specific" and\
		(self.options.tapesanity == "percentage" or self.options.bootlegsanity != "none" or self.options.fusionsanity):
			for monster in monsters(self.options).keys():
				region = self.multiworld.get_region("Menu", self.player)
				event = CassetteBeastsLocation(self.player, f"Recorded {monster}", None, region)
				event.place_locked_item(CassetteBeastsItem(f"Recorded {monster}", IC.progression_skip_balancing, None, self.player))
				region.locations += [event]

		self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


	def get_filler_item_name(self):
		return "Cyber Material"

	def set_rules(self):
		from .Rules import set_rules
		set_rules(self)
		self.set_victory()
		# from Utils import visualize_regions
		# visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

	def generate_early(self):
		#print(self.fill_slot_data())
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

	def pre_fill(self):
		if self.options.exclude_postgame:
			for loc in self.multiworld.get_region("Postgame", self.player).locations:
				loc.progress_type = 3 # Excluded

	def get_pre_fill_items(self):
		return [
			
		]

	def set_victory(self):
		conditions = []
		for goal in self.options.goal.value:
			match goal:
				case "Escape":
					conditions.append(lambda state: state.has("Defeated Aleph", self.player))
				case "Captain":
					conditions.append(lambda state: state.has("Became Captain", self.player))
		self.multiworld.completion_condition[self.player] = lambda state: all([c(state) for c in conditions])


	def fill_slot_data(self):
		# Fix empty goal set
		if self.options.goal.value == {}:
			self.options.goal.value = {"Escape"}
		return {
			"item_apName_to_cbItemData": {key: (value.cb_name, value.amount) for key, value in item_data_table.items()},
			"location_cbName_to_apName": {value.cb_name: name for name, value in location_data_table.items() if isLocation(self.options, name)},
			"giveItemAction_to_location": {
				"tutorial": "Ranger Handbook",
				"type_chart": "Type Chart",
				"key_harbourtown": "Harbourtown Gate Key",
				"meredith_envelope": "Envelope for Meredith",
				"key_landkeeper": "Landkeeper Key",
				"captain_badge": "Beat Ianthe",
			},
			"itemDrop_to_location": {
				"trainticket_glowshroom": "Train Ticket (Glowcester)",
				"trainticket_graveyard": "Train Ticket (Aldgrave Tomb)",
				"captain_cleeo_coin": "Captain Clee-o Coin",
			},
			"settings": {
				"goal": self.options.goal.value,
				"final_battle_friend_count": self.options.final_battle_friend_count.value,
				"archangel_hunt_count": self.options.archangel_hunt_count.value,
				"exclude_postgame": self.options.exclude_postgame.value,
				"experience_multiplier": self.options.experience_multiplier.value,
				"bootleg_multiplier": self.options.bootleg_multiplier.value,
				"use_pier": self.options.use_pier.value,
				"shuffle_chest_loot_tables": self.options.shuffle_chest_loot_tables.value,
				"traps": self.options.traps != "none",
				"shopsanity": self.options.shopsanity.value,
				"trainersanity": self.options.trainersanity.value,
				"tapesanity": self.options.tapesanity.value,
				"tapesanity_percentage": self.options.tapesanity_percentage.value,
				"tapesanity_percentage_item_count": self.options.tapesanity_percentage_item_count.value,
				"bootlegsanity": self.options.bootlegsanity.value,
				"bootlegsanity_percentage": self.options.bootlegsanity_percentage.value,
				"bootlegsanity_percentage_item_count": self.options.bootlegsanity_percentage_item_count.value,
				"fusionsanity": self.options.fusionsanity.value,
				"fusionsanity_amount": self.options.fusionsanity_amount.value,
				"fusionsanity_item_count": self.options.fusionsanity_item_count.value,
				"death_link": self.options.death_link.value,
			},
		}