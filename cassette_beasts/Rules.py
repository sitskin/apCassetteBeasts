from worlds.generic.Rules import set_rule

from .Locations import location_data_table, event_data_table, reachableMonsterCount,\
	tapesanity_locations, bootlegsanity_per_tape_locations, bootlegsanity_specific_locations, fusionsanity_locations 
from .Regions import region_data_table
from .Data.tape_data import monsterCount, monsters, types


def set_rules(cbworld) -> None:
	multiworld = cbworld.multiworld
	player = cbworld.player
	options = cbworld.options

	# Region Rules
	for name, data in region_data_table.items():
		for e in multiworld.get_region(name, player).exits:
			if e.connected_region.name in data.exit_rules.keys():
				f = data.exit_rules[e.connected_region.name]
				set_rule(e, lambda state, rule=f: rule(state, player))

	# Location Rules
	for name, data in location_data_table.items():
		if data.rules != None and (data.requires == None or data.requires(options)):
			set_rule(multiworld.get_location(name, player),
				lambda state, rule=data.rules: rule == None or rule(state, player))

	# Event Rules
	for name, data in event_data_table.items():
		if data.rules != None and (data.requires == None or data.requires(options)):
			set_rule(multiworld.get_location(name, player),
				lambda state, rule=data.rules: rule == None or rule(state, player))

	# Special Cases
	set_rule(multiworld.get_location("Defeated Aleph", player),
		lambda state: state.has("Azure Keystone", player, 2) and \
			friendCount(state, player) >= options.final_battle_friend_count.value)

	if options.fusionsanity:
		mult = options.fusionsanity_amount // options.fusionsanity_item_count
		for i, location in enumerate(fusionsanity_locations.keys(), 1):
			if i > options.fusionsanity_item_count:
				break
			set_rule(multiworld.get_location(location, player),
				lambda state, f=reachableMonsterCount, n=i: f(state, player, options)**2 >= n*mult)


def friendCount(state, player) -> bool:
	return sum([
		state.has("Recruited Kayleigh", player),
		state.has("Recruited Eugene", player) and state.has("Defeated Mammon", player),
		state.has("Recruited Meredith", player) and state.has("Defeated Nowhere Monarch", player),
		state.has("Recruited Felix", player) and state.has("Defeated Shining Kuneko", player),
		state.has("Recruited Viola", player) and state.has("Defeated Robin Goodfellow", player),
		state.has("Recruited Barkley", player) and state.has("Defeated Averevoir", player)
		])