from typing import NamedTuple, Optional

from BaseClasses import Item, ItemClassification as IC

CB_BASE_ID = 0

class CassetteBeastsItem(Item):
	game = "Cassette Beasts"

class CassetteBeastsItemData(NamedTuple):
	cb_name: Optional[str] = None
	code: Optional[int] = None
	type: IC = IC.filler
	amount: int = 1# how many of this item is given - ie 50 wood
	count: int = 1# how many instances of this item is in the pool

cb_abilities = {
	"Progressive Glide": CassetteBeastsItemData("AP_progressive_glide", CB_BASE_ID+0, IC.progression, 1, 2),
	"Progressive Dash": CassetteBeastsItemData("AP_progressive_dash", CB_BASE_ID+1, IC.progression, 1, 2),
	"Progressive Magnetism": CassetteBeastsItemData("AP_progressive_magnet", CB_BASE_ID+2, IC.progression, 1, 2),
	"Swim": CassetteBeastsItemData("AP_swim", CB_BASE_ID+3, IC.progression),
	"Progressive Climb": CassetteBeastsItemData("AP_progressive_climb", CB_BASE_ID+4, IC.progression, 1, 2),
}

id_off = len(cb_abilities)
cb_key_items = {
	"Captain Badge": CassetteBeastsItemData("captain_badge", id_off+0, IC.progression),
	"Coin": CassetteBeastsItemData("captain_cleeo_coin", id_off+1, IC.progression),
	"Azure Keystone": CassetteBeastsItemData("keystone", id_off+2, IC.progression, 1, 2),
	"Mourningtown Key": CassetteBeastsItemData("key_commune", id_off+3, IC.progression),
	"White Rabbit Key": CassetteBeastsItemData("key_dungeon_meadow", id_off+4, IC.progression),
	"Harbourtown Gate Key": CassetteBeastsItemData("key_harbourtown", id_off+5, IC.progression),
	"Landkeeper Window Key": CassetteBeastsItemData("key_landkeeper", id_off+6, IC.progression),
	"Waterloop Key": CassetteBeastsItemData("key_waterloop", id_off+7, IC.progression),
	"Machine Part": CassetteBeastsItemData("machinepart", id_off+8, IC.progression),
	"Envelope for Meredith": CassetteBeastsItemData("meredith_envelope", id_off+9, IC.progression),
	"Train Ticket (Glowcester)": CassetteBeastsItemData("trainticket_glowshroom", id_off+10, IC.progression),
	"Train Ticket (Aldgrave Tomb)": CassetteBeastsItemData("trainticket_graveyard", id_off+11, IC.progression),
	"Valve Handel": CassetteBeastsItemData("valve", id_off+12, IC.progression, 1, 2),
	"Captain Wallace Stamp": CassetteBeastsItemData("AP_wallace_stamp", id_off+13, IC.progression),
	"Captain Skip Stamp": CassetteBeastsItemData("AP_skip_stamp", id_off+14, IC.progression),
	"Captain Zedd Stamp": CassetteBeastsItemData("AP_zedd_stamp", id_off+15, IC.progression),
	"Captain Judas Stamp": CassetteBeastsItemData("AP_judas_stamp", id_off+16, IC.progression),
	"Captain Clee-o Stamp": CassetteBeastsItemData("AP_clee-o_stamp", id_off+17, IC.progression),
	"Captain Lodestein Stamp": CassetteBeastsItemData("AP_lodestein_stamp", id_off+18, IC.progression),
	"Captain Penny Dreadful Stamp": CassetteBeastsItemData("AP_penny_dreadful_stamp", id_off+19, IC.progression),
	"Captain Gladiola Stamp": CassetteBeastsItemData("AP_gladiola_stamp", id_off+20, IC.progression),
	"Captain Heather Stamp": CassetteBeastsItemData("AP_heather_stamp", id_off+21, IC.progression),
	"Captain Buffy Stamp": CassetteBeastsItemData("AP_buffy_stamp", id_off+22, IC.progression),
	"Captain Cybil Stamp": CassetteBeastsItemData("AP_cybil_stamp", id_off+23, IC.progression),
	"Captain Codey Stamp": CassetteBeastsItemData("AP_codey_stamp", id_off+24, IC.progression),
	"Song Fragment (Oldgante)": CassetteBeastsItemData("aa_oldgante", id_off+25, IC.progression, 1, 1),
	"Song Fragment (Puppetox)": CassetteBeastsItemData("aa_puppet", id_off+26, IC.progression, 1, 1),
	"Song Fragment (Mourningstar)": CassetteBeastsItemData("aa_mourningstar", id_off+27, IC.progression, 1, 1),
	"Song Fragment (Nowhere Monarch)": CassetteBeastsItemData("aa_monarch", id_off+28, IC.progression, 1, 1),
	"Song Fragment (Heckahedron)": CassetteBeastsItemData("aa_cube", id_off+29, IC.progression, 1, 1),
	"Song Fragment (Alice)": CassetteBeastsItemData("aa_alice", id_off+30, IC.progression, 1, 1),
	"Song Fragment (Robin Goodfellow)": CassetteBeastsItemData("aa_robin", id_off+31, IC.progression, 1, 1),
	"Song Fragment (Mammon)": CassetteBeastsItemData("aa_mammon", id_off+32, IC.progression, 1, 1),
	"Song Fragment (Lamento Mori)": CassetteBeastsItemData("aa_lamento_mori", id_off+33, IC.progression, 1, 1),
	"Song Fragment (Babelith)": CassetteBeastsItemData("aa_tower", id_off+34, IC.progression, 1, 1),
	"Song Fragment (Kuneko)": CassetteBeastsItemData("aa_kuneko", id_off+35, IC.progression, 1, 1),
}

id_off += len(cb_key_items)
cb_regular_items = {
	"Ritual Candle": CassetteBeastsItemData("bootleg_ritual_candle", id_off+0, IC.filler, 1, 0),
	"Canned Ice Latte": CassetteBeastsItemData("coffee1", id_off+1, IC.filler, 1, 1),
	"Americano-To-Go": CassetteBeastsItemData("coffee2", id_off+2, IC.filler, 1, 0),
	"Espresso Express": CassetteBeastsItemData("coffee3", id_off+3, IC.filler, 1, 0),
	"Double Espresso": CassetteBeastsItemData("coffee4", id_off+4, IC.filler, 1, 0),
	"Cure-All": CassetteBeastsItemData("cure_all", id_off+5, IC.filler, 1, 0),
	"Berserk Cure": CassetteBeastsItemData("cure_berserk", id_off+6, IC.filler, 1, 0),
	"Burn Cure": CassetteBeastsItemData("cure_burned", id_off+7, IC.filler, 1, 0),
	"Coating Cure": CassetteBeastsItemData("cure_coating", id_off+8, IC.filler, 1, 0),
	"Conductive Cure": CassetteBeastsItemData("cure_conductive", id_off+9, IC.filler, 1, 0),
	"Confusion Cure": CassetteBeastsItemData("cure_confused", id_off+10, IC.filler, 1, 0),
	"Leech Cure": CassetteBeastsItemData("cure_leeched", id_off+11, IC.filler, 1, 0),
	"Petrification Cure": CassetteBeastsItemData("cure_petrified", id_off+12, IC.filler, 1, 0),
	"Poison Cure": CassetteBeastsItemData("cure_poisoned", id_off+13, IC.filler, 1, 0),
	"Resonance Cure": CassetteBeastsItemData("cure_resonance", id_off+14, IC.filler, 1, 0),
	"Sleep Cure": CassetteBeastsItemData("cure_sleep", id_off+15, IC.filler, 1, 0),
	"Stat Cure": CassetteBeastsItemData("cure_stat", id_off+16, IC.filler, 1, 0),
	"Skelly Jelly": CassetteBeastsItemData("jelly", id_off+17, IC.filler, 1, 0),
	"Old Book": CassetteBeastsItemData("old_book", id_off+18, IC.filler, 1, 1),
	"Olive-Up!": CassetteBeastsItemData("olive_up", id_off+19, IC.useful, 1, 0),
	"Pear Fusilli": CassetteBeastsItemData("pear_fusilli", id_off+20, IC.useful, 1, 0),
	"Reoderant": CassetteBeastsItemData("reodorant", id_off+21, IC.filler, 1, 0),
	"Respool": CassetteBeastsItemData("respool", id_off+22, IC.filler, 1, 0),
	"Rewind": CassetteBeastsItemData("rewind", id_off+23, IC.filler, 1, 0),
	"Smoke Bomb": CassetteBeastsItemData("smoke_bomb", id_off+24, IC.filler, 1, 0),
	"Upgrape": CassetteBeastsItemData("upgrape", id_off+25, IC.useful, 1, 0),
	"Full English (Vegan)": CassetteBeastsItemData("full_english", id_off+26, IC.filler, 1, 0)#unused, functionality not tested
}

id_off += len(cb_regular_items)
cb_resource_items = {
	"Cyber Material": CassetteBeastsItemData("cyber_material", id_off+0, IC.filler, 1, 0),
	"Cyber Material x20": CassetteBeastsItemData("cyber_material", id_off+1, IC.filler, 20, 0),
	"Fused Material": CassetteBeastsItemData("fused_material", id_off+2, IC.filler, 1, 16),
	"Fused Material x5": CassetteBeastsItemData("fused_material", id_off+3, IC.filler, 5, 0),
	"Fused Material x10": CassetteBeastsItemData("fused_material", id_off+4, IC.filler, 10, 0),
	"Metal": CassetteBeastsItemData("metal", id_off+5, IC.filler, 1, 3),
	"Metal x5": CassetteBeastsItemData("metal", id_off+6, IC.filler, 5, 1),
	"Metal x100": CassetteBeastsItemData("metal", id_off+7, IC.filler, 100, 2),
	"Plastic": CassetteBeastsItemData("plastic", id_off+8, IC.filler, 1, 0),
	"Plastic x2": CassetteBeastsItemData("plastic", id_off+9, IC.filler, 2, 1),
	"Plastic x5": CassetteBeastsItemData("plastic", id_off+10, IC.filler, 5, 2),
	"Plastic x10": CassetteBeastsItemData("plastic", id_off+11, IC.filler, 10, 1),
	"Plastic x20": CassetteBeastsItemData("plastic", id_off+12, IC.filler, 20, 1),
	"Plastic x25": CassetteBeastsItemData("plastic", id_off+13, IC.filler, 25, 1),
	"Plastic x120": CassetteBeastsItemData("plastic", id_off+14, IC.filler, 120, 1),
	"Pulp": CassetteBeastsItemData("pulp", id_off+15, IC.filler, 1, 0),
	"Pulp x100": CassetteBeastsItemData("pulp", id_off+16, IC.filler, 100, 0),
	"Wheat": CassetteBeastsItemData("wheat", id_off+17, IC.filler, 1, 0),
	"Wheat x100": CassetteBeastsItemData("wheat", id_off+18, IC.filler, 100, 0),
	"Wood": CassetteBeastsItemData("wood", id_off+19, IC.filler, 1, 0),
	"Wood x15": CassetteBeastsItemData("wood", id_off+20, IC.filler, 15, 1),
	"Wood x20": CassetteBeastsItemData("wood", id_off+21, IC.filler, 20, 1),
	"Wood x50": CassetteBeastsItemData("wood", id_off+22, IC.filler, 50, 1),
	"Wood x52": CassetteBeastsItemData("wood", id_off+23, IC.filler, 52, 1),
	"Wood x55": CassetteBeastsItemData("wood", id_off+24, IC.filler, 55, 1),
	"Wood x100": CassetteBeastsItemData("wood", id_off+25, IC.filler, 100, 2),
	"Wood x120": CassetteBeastsItemData("wood", id_off+26, IC.filler, 120, 1),
	"Wood x150": CassetteBeastsItemData("wood", id_off+27, IC.filler, 150, 1),
}

id_off += len(cb_resource_items)
cb_tape_items = {
	"Basic Tape x5": CassetteBeastsItemData("tape_basic", id_off+0, IC.filler, 5, 2),
	"Chrome Tape x5": CassetteBeastsItemData("tape_chrome", id_off+1, IC.useful, 5, 1),
	"Optical Laser Tape": CassetteBeastsItemData("tape_optical_laser", id_off+2, IC.useful, 1, 0),
	"Black Shuck's Tape": CassetteBeastsItemData("tape_black_shuck", id_off+3, IC.useful, 1, 0),
	"Aerosol Tape": CassetteBeastsItemData("tape_air", id_off+4, IC.filler, 1, 0),
	"Ethereal Tape": CassetteBeastsItemData("tape_astral", id_off+5, IC.filler, 1, 0),
	"Faux Fur Tape": CassetteBeastsItemData("tape_beast", id_off+6, IC.filler, 1, 0),
	"Ceramic Tape": CassetteBeastsItemData("tape_earth", id_off+7, IC.filler, 1, 0),
	"Toaster Tape": CassetteBeastsItemData("tape_fire", id_off+8, IC.filler, 1, 0),
	"Ice-IX Tape": CassetteBeastsItemData("tape_ice", id_off+9, IC.filler, 1, 0),
	"Superconductive Tape": CassetteBeastsItemData("tape_lightning", id_off+10, IC.filler, 1, 0),
	"Ferrichrome Tape": CassetteBeastsItemData("tape_metal", id_off+11, IC.filler, 1, 0),
	"Treebark Tape": CassetteBeastsItemData("tape_plant", id_off+12, IC.filler, 1, 0),
	"Recycled Tape": CassetteBeastsItemData("tape_plastic", id_off+13, IC.filler, 1, 0),
	"Snakeskin Tape": CassetteBeastsItemData("tape_poison", id_off+14, IC.filler, 1, 0),
	"Water-Filled Tape": CassetteBeastsItemData("tape_water", id_off+15, IC.filler, 1, 0),
	"Basic Tape": CassetteBeastsItemData("tape_basic", id_off+16, IC.filler, 1, 0),
	"Chrome Tape": CassetteBeastsItemData("tape_chrome", id_off+17, IC.useful, 1, 0),
}

id_off += len(cb_tape_items)
cb_remaster_sticker_items = {
	"Close Encounter Sticker": CassetteBeastsItemData("AP_sticker_close-encounter", id_off+0, IC.progression, 1, 0),
	"Gear Shear Sticker": CassetteBeastsItemData("AP_sticker_gear-shear", id_off+1, IC.progression, 1, 1),
	"Ice Coating Sticker": CassetteBeastsItemData("AP_sticker_ice-coating", id_off+2, IC.progression, 1, 0),
	"Magic Tome Sticker": CassetteBeastsItemData("AP_sticker_magic-tome", id_off+3, IC.progression, 1, 0),
	"Toy Hammer Sticker": CassetteBeastsItemData("AP_sticker_toy-hammer", id_off+4, IC.progression, 1, 0),
	"Zephyr Sticker": CassetteBeastsItemData("AP_sticker_zephyr", id_off+5, IC.progression, 1, 0),
	"Carnivore Sticker": CassetteBeastsItemData("AP_sticker_carnivore", id_off+6, IC.progression, 1, 0),
}

id_off += len(cb_remaster_sticker_items)
cb_upgrade_items = {
	"Miniature Refrigerator": CassetteBeastsItemData("carry_more_coffee", id_off+0, IC.useful, 1, 7),
	"First Aid Pouch": CassetteBeastsItemData("carry_more_cures", id_off+1, IC.useful, 1, 17),
	"Resealable Plastic Tub": CassetteBeastsItemData("carry_more_pear_fusilli", id_off+2, IC.useful, 1, 17),
	"Scent-Absorbing Pouch": CassetteBeastsItemData("carry_more_reodorant", id_off+3, IC.useful, 1, 5),
	"Respool Pouch": CassetteBeastsItemData("carry_more_respools", id_off+4, IC.useful, 1, 4),
	"Rewind Pouch": CassetteBeastsItemData("carry_more_rewinds", id_off+5, IC.useful, 1, 20),
	"Bomb Compartment": CassetteBeastsItemData("carry_more_smoke_bombs", id_off+6, IC.useful, 1, 4),
	"Critical Mod": CassetteBeastsItemData("fusion_meter_critical", id_off+7, IC.useful, 1, 5),
	"Fusion Meter Mod": CassetteBeastsItemData("fusion_meter_fill_rate", id_off+8, IC.useful, 1, 20),
	"Recording Mod": CassetteBeastsItemData("fusion_meter_recording", id_off+9, IC.useful, 1, 5),
	"Chemistry Mod": CassetteBeastsItemData("fusion_meter_type_advantage", id_off+10, IC.useful, 1, 5),
	"Victory Mod": CassetteBeastsItemData("fusion_meter_victory", id_off+11, IC.useful, 1, 5),
	"Extra Gym Point x5": CassetteBeastsItemData("gym_points", id_off+12, IC.useful, 5, 10),
	"Merchant's Guild Membership": CassetteBeastsItemData("merchant_discounts", id_off+13, IC.useful, 1, 5),
	"Additional Coffee Stock": CassetteBeastsItemData("merchant_stock_coffee", id_off+14, IC.useful, 1, 3),
	"Additional Cure Stock": CassetteBeastsItemData("merchant_stock_cures", id_off+15, IC.useful, 1, 9),
	"Additional Sticker Stock": CassetteBeastsItemData("merchant_stock_stickers", id_off+16, IC.useful, 1, 5),
	"Microphone Upgrade": CassetteBeastsItemData("recording_success_rate", id_off+17, IC.useful, 1, 10),
}

id_off += len(cb_upgrade_items)
cb_loot_table_items = {
	"Miscellaneous Loot": CassetteBeastsItemData("chest_misc", id_off+0, IC.filler, 1, 87),
	"Miscellaneous Loot without Tapes": CassetteBeastsItemData("chest_misc_no_tapes", id_off+1, IC.filler, 1, 0),#unused?
	"Farm Loot": CassetteBeastsItemData("chest_farm", id_off+2, IC.filler, 1, 2),
	"Mt Wirral Loot": CassetteBeastsItemData("chest_mt_wirral", id_off+3, IC.filler, 1, 4),
	"In Graveyard Loot": CassetteBeastsItemData("chest_in_graveyard", id_off+4, IC.filler, 1, 1),
	"Cast Iron Shore Loot": CassetteBeastsItemData("chest_cast_iron_shore", id_off+5, IC.filler, 1, 2),
	"At Sea Loot": CassetteBeastsItemData("chest_at_sea", id_off+6, IC.filler, 1, 0),
	"Spider Cave Loot": CassetteBeastsItemData("chest_spider_cave", id_off+7, IC.filler, 1, 1),
	"Cherry Cross Station Loot": CassetteBeastsItemData("chest_dugeon_meadow", id_off+8, IC.filler, 1, 2),
	"Titania Shipwreck Insomnia Loot": CassetteBeastsItemData("chest_shipwreck_insomnia", id_off+9, IC.filler, 1, 1),
	"Station Loot": CassetteBeastsItemData("chest_station", id_off+10, IC.filler, 1, 8),
	"Kayliegh's Home Loot": CassetteBeastsItemData("chest_kayleigh_home", id_off+11, IC.filler, 1, 1),
	"Office Loot": CassetteBeastsItemData("chest_office", id_off+12, IC.filler, 1, 5),
}

id_off += len(cb_loot_table_items)
cb_trap_items = {
	"Traffikrab Trap": CassetteBeastsItemData("AP_trap_traffikrab", id_off+0, IC.trap, 1, 0),
	"Lobstacle Trap": CassetteBeastsItemData("AP_trap_lobstacle", id_off+1, IC.trap, 1, 0),
	"Trapwurm Trap": CassetteBeastsItemData("AP_trap_trapwurm", id_off+2, IC.trap, 1, 0),
	"Miss Mimic Trap": CassetteBeastsItemData("AP_trap_mimic", id_off+3, IC.trap, 1, 0),
}

item_data_table = cb_abilities|cb_key_items|cb_regular_items|cb_resource_items|\
				  cb_tape_items|cb_remaster_sticker_items|cb_upgrade_items|\
				  cb_loot_table_items|cb_trap_items
item_table = {name: data.code
	for name, data in item_data_table.items()
	if data.code is not None}

def shouldAddItem(options, name):
	return  (name in cb_abilities.keys()) or\
			(name in cb_key_items.keys()) or\
			(name in cb_regular_items.keys()) or\
			(name in cb_tape_items.keys()) or\
			(name in cb_remaster_sticker_items.keys() and (options.tapesanity != "none" or options.bootlegsanity != "none" or options.fusionsanity)) or\
			(name in cb_upgrade_items.keys() and options.shopsanity == True) or\
			(name in cb_loot_table_items.keys() and options.shuffle_chest_loot_tables == True)

progression_mapping = {
	"Mothwing Glide": ("Progressive Glide", 1),
	"Avereoir Flight": ("Progressive Glide", 2),
	"Bulletino Dash": ("Progressive Dash", 1),
	"Bulletino Cartridge Shard": ("Progressive Dash", 1),
	"Electromagnetism": ("Progressive Magnetism", 1),
	"Boltam Fur": ("Progressive Magnetism", 2),
	"Pumpkin Vine Ball": ("Progressive Climb", 1),
	"Jumpkin Seed": ("Progressive Climb", 2),
}

# progressive_item_cb_name = {
# 	"Mothwing Glide": "",
# 	"Avereoir Flight": "flight",
# 	"Bulletino Dash": "dash",
# 	"Bulletino Cartridge Shard": "ability_advantage_dash",
# 	"Electromagnetism":  "magnetism",
# 	"Boltam Fur": "ability_advantage_magnetism",
# 	"Pumpkin Vine Ball": "climb",
# 	"Jumpkin Seed": "ability_advantage_climb",
# }