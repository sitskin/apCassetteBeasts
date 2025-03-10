
from math import ceil
from random import choices

from BaseClasses import Location, Region, ItemClassification as IC
from worlds.AutoWorld import WebWorld, World

from .Items import CassetteBeastsItem, item_table, item_data_table, cb_regular_items, cb_resource_items, cb_tape_items, cb_trap_items, shouldAddItem
from .Locations import CassetteBeastsLocation, location_table, location_data_table, event_data_table, getLocationCount, isLocation
from .Options import CassetteBeastsOptions
from .Regions import region_data

from .Data.tape_data import monsterCount

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
			# TODO add dlc option to monsterCount
			count = monsterCount() if self.options.tapesanity == "specific" else self.options.tapesanity_percentage_item_count
			#print(f"Tapesanity count: {count}")
			if count >= 14:
				for name in cb_tape_items.keys():
					if name in ["Basic Tape x5", "Chrome Tape x5", "Optical Laser Tape", "Black Shuck's Tape"]:
						continue
					item_pool += [self.create_item(n) for n in [name]*(count//14)]
			item_pool += [self.create_item(c) for c in choices([*cb_tape_items.keys()], k=count%14)]

		# Bootlegsanity
		if self.options.bootlegsanity != "none":
			# TODO add dlc option to monsterCount
			count = monsterCount()*14 if self.options.bootlegsanity == "specific" else self.options.bootlegsanity_percentage_item_count
			#print(f"Bootlegsanity count: {count}")
			items = ["Ritual Candle", "Cyber Material x20", "Black Shuck's Tape"]
			item_pool += [self.create_item(c) for c in choices(items, weights=[1,3,2], k=count)]

		# Fusionsanity
		if self.options.fusionsanity:
			for i in range(self.options.fusionsanity_item_count):
				#print(i)
				item_pool += [CassetteBeastsItem("Pear Fusilli", IC.filler, item_data_table["Pear Fusilli"].code, self.player)]

		# Add Traps
		if self.options.traps != "none":
			remaining = getLocationCount(self.options)-len(item_pool)
			if self.options.traps.value == "few":
				count = min(max(4, remaining//20), remaining)
			elif self.options.traps.value == "some":
				count = min(max(5, remaining//5), remaining)
			elif self.options.traps.value == "many":
				count = min(max(6, remaining//2), remaining)
			item_pool += [self.create_item(c) for c in choices([*cb_trap_items.keys()], [5,2,3,1], k=remaining)]

		# Randomized Filler
		item_pool += [self.create_item(c)
			for c in choices([*cb_regular_items.keys()|cb_resource_items.keys()|cb_tape_items.keys()], k=getLocationCount(self.options)-len(item_pool))
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
			region = self.multiworld.get_region(data.region, self.player)
			event = CassetteBeastsLocation(self.player, name, None, region)
			event.place_locked_item(CassetteBeastsItem(data.item, IC.progression_skip_balancing, None, self.player))
			region.locations += [event]

		self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


	def get_filler_item_name(self):
		return "Cyber Material"

	def set_rules(self):
		from .Rules import set_rules
		set_rules(self)

	def generate_early(self):
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
			locs = int(self.options.fusionsanity_amount)
			if count > locs:
				print(f"Too many items for Fusionsanity: reducing from {count} to {locs}")
				self.options.fusionsanity_item_count.value = locs

	def fill_slot_data(self):
		
		return {
			"item_id_to_name": {value.code: (value.cb_name, value.amount) for value in item_data_table.values()},
			"location_name_to_id": {value.cb_name: value.address for value in location_data_table.values()},
			"settings": {
			"death_link": self.options.death_link.value,
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
			"fusionsanity__item_count": self.options.fusionsanity_item_count.value,
			},
		}