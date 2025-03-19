
from .Items import cb_abilities, cb_key_items, cb_regular_items, cb_resource_items,\
	cb_tape_items, cb_remaster_sticker_items, cb_upgrade_items, cb_loot_table_items,\
	cb_trap_items

from .Locations import chest_loot_locations, shopsanity_locations, trainersanity_locations,\
	tapesanity_locations, tapesanity_percentage_locations,\
	bootlegsanity_per_tape_locations, bootlegsanity_specific_locations, bootlegsanity_percentage_locations,\
	fusionsanity_locations


item_groups = {
	"song fragments": {
		"Song Fragment (Oldgante)",
		"Song Fragment (Puppetox)",
		"Song Fragment (Mourningstar)",
		"Song Fragment (Nowhere Monarch)",
		"Song Fragment (Heckahedron)",
		"Song Fragment (Alice)",
		"Song Fragment (Robin Goodfellow)",
		"Song Fragment (Mammon)",
		"Song Fragment (Lamento Mori)",
		"Song Fragment (Babelith)",
		"Song Fragment (Kuneko)"
	},
	"abilities": {k for k in cb_abilities.keys()},
	"key items": {k for k in cb_key_items.keys()},
	"regular items": {k for k in cb_regular_items.keys()},
	"resource items": {k for k in cb_resource_items.keys()},
	"tapes": {k for k in cb_tape_items.keys()},
	"remaster stickers": {k for k in cb_remaster_sticker_items.keys()},
	"upgrades": {k for k in cb_upgrade_items.keys()},
	"chest loot": {k for k in cb_loot_table_items.keys()},
	"traps": {k for k in cb_trap_items.keys()},
}

location_groups = {
	"chest loot": {k for k in chest_loot_locations.keys()},
	"shop items": {k for k in shopsanity_locations.keys()},
	"trainers": {k for k in trainersanity_locations.keys()},
	"recorded tapes": {k for k in tapesanity_locations.keys()},
	"recorded percentage tapes": {k for k in tapesanity_percentage_locations.keys()},
	"recorded bootlegs": {k for k in bootlegsanity_per_tape_locations.keys()},
	"recorded specific bootlegs": {k for k in bootlegsanity_specific_locations.keys()},
	"recorded percentage bootlegs": {k for k in bootlegsanity_percentage_locations.keys()},
	"seen fusions": {k for k in fusionsanity_locations.keys()},
}