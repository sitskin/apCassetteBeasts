from typing import NamedTuple, Optional

from BaseClasses import Item, ItemClassification as IC

from .Data.tape_data import monsters

CB_BASE_ID = 1

class CassetteBeastsItem(Item):
	game = "Cassette Beasts"

class CassetteBeastsItemData(NamedTuple):
	cb_name: str
	code: int
	type: IC = IC.filler
	amount: int = 1 #   how many of this item is given
	count: int = 1  #   how many instances of this item is in the pool
	requires: Optional[callable] = None#function that if true automatically adds to the item pool

def counter(start=1):
	while True:
		yield start
		start += 1
c = counter()

cb_abilities = {
	"Progressive Glide": CassetteBeastsItemData("ap_progressive_glide", next(c), IC.progression, 1, 2),
	"Progressive Dash": CassetteBeastsItemData("ap_progressive_dash", next(c), IC.progression, 1, 2),
	"Progressive Magnetism": CassetteBeastsItemData("ap_progressive_magnet", next(c), IC.progression, 1, 2),
	"Swim": CassetteBeastsItemData("ap_swim", next(c), IC.progression),
	"Progressive Climb": CassetteBeastsItemData("ap_progressive_climb", next(c), IC.progression, 1, 2),
}

cb_key_items = {
	"Captain Badge": CassetteBeastsItemData("captain_badge", next(c), IC.progression),
	"Coin": CassetteBeastsItemData("captain_cleeo_coin", next(c), IC.progression),
	"Azure Keystone": CassetteBeastsItemData("keystone", next(c), IC.progression, 1, 2),
	"Mourningtown Key": CassetteBeastsItemData("key_commune", next(c), IC.progression),
	"White Rabbit Key": CassetteBeastsItemData("key_dungeon_meadow", next(c), IC.progression),
	"Harbourtown Gate Key": CassetteBeastsItemData("key_harbourtown", next(c), IC.progression, 1, 1),
	"Landkeeper Window Key": CassetteBeastsItemData("key_landkeeper", next(c), IC.progression),
	"Waterloop Key": CassetteBeastsItemData("key_waterloop", next(c), IC.progression),
	"Machine Part": CassetteBeastsItemData("machinepart", next(c), IC.progression),
	"Envelope for Meredith": CassetteBeastsItemData("meredith_envelope", next(c), IC.progression),
	"Train Ticket (Glowcester)": CassetteBeastsItemData("trainticket_glowshroom", next(c), IC.progression),
	"Train Ticket (Aldgrave Tomb)": CassetteBeastsItemData("trainticket_graveyard", next(c), IC.progression),
	"Valve Handel": CassetteBeastsItemData("valve", next(c), IC.progression, 1, 2),
	"Captain Wallace Stamp": CassetteBeastsItemData("ap_captain_wallace_stamp", next(c), IC.progression),
	"Captain Skip Stamp": CassetteBeastsItemData("ap_captain_skip_stamp", next(c), IC.progression),
	"Captain Zedd Stamp": CassetteBeastsItemData("ap_captain_zedd_stamp", next(c), IC.progression),
	"Captain Judas Stamp": CassetteBeastsItemData("ap_captain_judas_stamp", next(c), IC.progression),
	"Captain Clee-o Stamp": CassetteBeastsItemData("ap_captain_cleeo_stamp", next(c), IC.progression),
	"Captain Lodestein Stamp": CassetteBeastsItemData("ap_captain_lodestein_stamp", next(c), IC.progression),
	"Captain Penny Dreadful Stamp": CassetteBeastsItemData("ap_captain_dreadful_stamp", next(c), IC.progression),
	"Captain Gladiola Stamp": CassetteBeastsItemData("ap_captain_gladiola_stamp", next(c), IC.progression),
	"Captain Heather Stamp": CassetteBeastsItemData("ap_captain_heather_stamp", next(c), IC.progression),
	"Captain Buffy Stamp": CassetteBeastsItemData("ap_captain_buffy_stamp", next(c), IC.progression),
	"Captain Cybil Stamp": CassetteBeastsItemData("ap_captain_cybil_stamp", next(c), IC.progression),
	"Captain Codey Stamp": CassetteBeastsItemData("ap_captain_codey_stamp", next(c), IC.progression),
	"Song Part (Oldgante)": CassetteBeastsItemData("aa_oldgante", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 10),
	"Song Part (Puppetox)": CassetteBeastsItemData("aa_puppet", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Mourningstar)": CassetteBeastsItemData("aa_mourningstar", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Nowhere Monarch)": CassetteBeastsItemData("aa_monarch", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Heckahedron)": CassetteBeastsItemData("aa_cube", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Alice)": CassetteBeastsItemData("aa_alice", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Robin Goodfellow)": CassetteBeastsItemData("aa_robin", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Mammon)": CassetteBeastsItemData("aa_mammon", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Lamento Mori)": CassetteBeastsItemData("aa_lamento_mori", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 8),
	"Song Part (Babelith)": CassetteBeastsItemData("aa_tower", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 9),
	"Song Part (Kuneko)": CassetteBeastsItemData("aa_kuneko", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 11),
	"Song Part (Averevoir)": CassetteBeastsItemData("aa_averevoir", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 12),
	"Song Part (Helia)": CassetteBeastsItemData("aa_helia", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 13),
	"Song Part (Lenna)": CassetteBeastsItemData("aa_lenna", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 14),
	"Song Part (Finalgante)": CassetteBeastsItemData("aa_finalgante", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 15),
	"Song Part (Gwenivar)": CassetteBeastsItemData("aa_clown", next(c), IC.progression, 1, 1,
		lambda options: options.song_part_count >= 16),
	"Ranger Handbook": CassetteBeastsItemData("tutorial", next(c), IC.progression, 1, 1),
	"Type Chart": CassetteBeastsItemData("type_chart", next(c), IC.filler, 1, 1),
	"Landkeeper Card Key": CassetteBeastsItemData("key_landkeeper2", next(c), IC.progression, 1, 2),
	"Stamina Increase": CassetteBeastsItemData("ap_stamina", next(c), IC.progression, 1, 12),
	"Prize Ticket": CassetteBeastsItemData("pier_ticket", next(c), IC.progression, 1, 20,
		lambda options: options.use_pier == True),
	"Attraction Pass(The Witch House)": CassetteBeastsItemData("pier_pass_hauntedhouse", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Attraction Pass(Cosmic Zone)": CassetteBeastsItemData("pier_pass_spaceworld", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Attraction Pass(Funworld)": CassetteBeastsItemData("pier_pass_funhouse", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Ruby Key": CassetteBeastsItemData("key_hauntedhouse_1", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Library Key": CassetteBeastsItemData("key_hauntedhouse_2", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Green Engine Key": CassetteBeastsItemData("key_hauntedhouse_3", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Solar Key": CassetteBeastsItemData("key_spaceworld_1", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Lunar Key": CassetteBeastsItemData("key_spaceworld_2", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Red Engine Key": CassetteBeastsItemData("key_spaceworld_3", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
	"Warehouse Key": CassetteBeastsItemData("key_warehouse", next(c), IC.progression, 1, 1,
		lambda options: options.use_pier == True),
}

cb_regular_items = {
	"Ritual Candle": CassetteBeastsItemData("bootleg_ritual_candle", next(c), IC.filler, 1, 0),
	"Canned Ice Latte": CassetteBeastsItemData("coffee1", next(c), IC.filler, 1, 1),
	"Americano-To-Go": CassetteBeastsItemData("coffee2", next(c), IC.filler, 1, 0),
	"Espresso Express": CassetteBeastsItemData("coffee3", next(c), IC.filler, 1, 0),
	"Double Espresso": CassetteBeastsItemData("coffee4", next(c), IC.filler, 1, 0),
	"Cure-All": CassetteBeastsItemData("cure_all", next(c), IC.filler, 1, 0),
	"Berserk Cure": CassetteBeastsItemData("cure_berserk", next(c), IC.filler, 1, 0),
	"Burn Cure": CassetteBeastsItemData("cure_burned", next(c), IC.filler, 1, 0),
	"Coating Cure": CassetteBeastsItemData("cure_coating", next(c), IC.filler, 1, 0),
	"Conductive Cure": CassetteBeastsItemData("cure_conductive", next(c), IC.filler, 1, 0),
	"Confusion Cure": CassetteBeastsItemData("cure_confused", next(c), IC.filler, 1, 0),
	"Leech Cure": CassetteBeastsItemData("cure_leeched", next(c), IC.filler, 1, 0),
	"Petrification Cure": CassetteBeastsItemData("cure_petrified", next(c), IC.filler, 1, 0),
	"Poison Cure": CassetteBeastsItemData("cure_poisoned", next(c), IC.filler, 1, 0),
	"Resonance Cure": CassetteBeastsItemData("cure_resonance", next(c), IC.filler, 1, 0),
	"Sleep Cure": CassetteBeastsItemData("cure_sleep", next(c), IC.filler, 1, 0),
	"Stat Cure": CassetteBeastsItemData("cure_stat", next(c), IC.filler, 1, 0),
	"Skelly Jelly": CassetteBeastsItemData("jelly", next(c), IC.filler, 1, 0),
	"Old Book": CassetteBeastsItemData("old_book", next(c), IC.filler, 1, 1),
	"Olive-Up!": CassetteBeastsItemData("olive_up", next(c), IC.useful, 1, 0),
	"Pear Fusilli": CassetteBeastsItemData("pear_fusilli", next(c), IC.useful, 1, 0),
	"Reoderant": CassetteBeastsItemData("reodorant", next(c), IC.filler, 1, 0),
	"Respool": CassetteBeastsItemData("respool", next(c), IC.filler, 1, 0),
	"Rewind": CassetteBeastsItemData("rewind", next(c), IC.filler, 1, 0),
	"Smoke Bomb": CassetteBeastsItemData("smoke_bomb", next(c), IC.filler, 1, 0),
	"Upgrape": CassetteBeastsItemData("upgrape", next(c), IC.useful, 1, 0),
	"Full English (Vegan)": CassetteBeastsItemData("full_english", next(c), IC.filler, 1, 0)
}

cb_resource_items = {
	"Cyber Material": CassetteBeastsItemData("cyber_material", next(c), IC.filler, 1, 0),
	"Cyber Material x20": CassetteBeastsItemData("cyber_material", next(c), IC.filler, 20, 0),
	"Fused Material": CassetteBeastsItemData("fused_material", next(c), IC.filler, 1, 16),
	"Fused Material x5": CassetteBeastsItemData("fused_material", next(c), IC.filler, 5, 0),
	"Fused Material x10": CassetteBeastsItemData("fused_material", next(c), IC.filler, 10, 0),
	"Fused Material x20": CassetteBeastsItemData("fused_material", next(c), IC.filler, 20, 0),
	"Metal": CassetteBeastsItemData("metal", next(c), IC.filler, 1, 3),
	"Metal x5": CassetteBeastsItemData("metal", next(c), IC.filler, 5, 1),
	"Metal x100": CassetteBeastsItemData("metal", next(c), IC.filler, 100, 2),
	"Plastic": CassetteBeastsItemData("plastic", next(c), IC.filler, 1, 0),
	"Plastic x2": CassetteBeastsItemData("plastic", next(c), IC.filler, 2, 1),
	"Plastic x5": CassetteBeastsItemData("plastic", next(c), IC.filler, 5, 2),
	"Plastic x10": CassetteBeastsItemData("plastic", next(c), IC.filler, 10, 1),
	"Plastic x20": CassetteBeastsItemData("plastic", next(c), IC.filler, 20, 1),
	"Plastic x25": CassetteBeastsItemData("plastic", next(c), IC.filler, 25, 1),
	"Plastic x120": CassetteBeastsItemData("plastic", next(c), IC.filler, 120, 1),
	"Pulp": CassetteBeastsItemData("pulp", next(c), IC.filler, 1, 0),
	"Pulp x100": CassetteBeastsItemData("pulp", next(c), IC.filler, 100, 0),
	"Wheat": CassetteBeastsItemData("wheat", next(c), IC.filler, 1, 0),
	"Wheat x100": CassetteBeastsItemData("wheat", next(c), IC.filler, 100, 0),
	"Wood": CassetteBeastsItemData("wood", next(c), IC.filler, 1, 0),
	"Wood x15": CassetteBeastsItemData("wood", next(c), IC.filler, 15, 1),
	"Wood x20": CassetteBeastsItemData("wood", next(c), IC.filler, 20, 1),
	"Wood x50": CassetteBeastsItemData("wood", next(c), IC.filler, 50, 1),
	"Wood x52": CassetteBeastsItemData("wood", next(c), IC.filler, 52, 1),
	"Wood x55": CassetteBeastsItemData("wood", next(c), IC.filler, 55, 1),
	"Wood x100": CassetteBeastsItemData("wood", next(c), IC.filler, 100, 2),
	"Wood x120": CassetteBeastsItemData("wood", next(c), IC.filler, 120, 1),
	"Wood x150": CassetteBeastsItemData("wood", next(c), IC.filler, 150, 1),
}

cb_tape_items = {
	"Basic Tape x5": CassetteBeastsItemData("tape_basic", next(c), IC.filler, 5, 2),
	"Chrome Tape x5": CassetteBeastsItemData("tape_chrome", next(c), IC.useful, 5, 1),
	"Optical Laser Tape": CassetteBeastsItemData("tape_optical_laser", next(c), IC.useful, 1, 0),
	"Aerosol Tape": CassetteBeastsItemData("tape_air", next(c), IC.filler, 1, 0),
	"Ethereal Tape": CassetteBeastsItemData("tape_astral", next(c), IC.filler, 1, 0),
	"Faux Fur Tape": CassetteBeastsItemData("tape_beast", next(c), IC.filler, 1, 0),
	"Ceramic Tape": CassetteBeastsItemData("tape_earth", next(c), IC.filler, 1, 0),
	"Toaster Tape": CassetteBeastsItemData("tape_fire", next(c), IC.filler, 1, 0),
	"Ice-IX Tape": CassetteBeastsItemData("tape_ice", next(c), IC.filler, 1, 0),
	"Superconductive Tape": CassetteBeastsItemData("tape_lightning", next(c), IC.filler, 1, 0),
	"Ferrichrome Tape": CassetteBeastsItemData("tape_metal", next(c), IC.filler, 1, 0),
	"Treebark Tape": CassetteBeastsItemData("tape_plant", next(c), IC.filler, 1, 0),
	"Recycled Tape": CassetteBeastsItemData("tape_plastic", next(c), IC.filler, 1, 0),
	"Snakeskin Tape": CassetteBeastsItemData("tape_poison", next(c), IC.filler, 1, 0),
	"Water-Filled Tape": CassetteBeastsItemData("tape_water", next(c), IC.filler, 1, 0),
	"Basic Tape": CassetteBeastsItemData("tape_basic", next(c), IC.filler, 1, 0),
	"Chrome Tape": CassetteBeastsItemData("tape_chrome", next(c), IC.useful, 1, 0),
}

cb_bootleg_tape_items = {
	"Black Shuck's Tape": CassetteBeastsItemData("tape_black_shuck", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Blizzard Tape": CassetteBeastsItemData("ap_tape_blizzard", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Contagion Tape": CassetteBeastsItemData("ap_tape_contagion", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Damascus Tape": CassetteBeastsItemData("ap_tape_damascus", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Deluge Tape": CassetteBeastsItemData("ap_tape_deluge", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Earthquake Tape": CassetteBeastsItemData("ap_tape_earthquake", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Ferocious Tape": CassetteBeastsItemData("ap_tape_ferocious", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Glitter Bomb Tape": CassetteBeastsItemData("ap_tape_glitter_bomb", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Inferno Tape": CassetteBeastsItemData("ap_tape_inferno", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Maelstrom Tape": CassetteBeastsItemData("ap_tape_maelstrom", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Overgrowth Tape": CassetteBeastsItemData("ap_tape_overgrowth", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Plastic Tape": CassetteBeastsItemData("ap_tape_plastic", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Tornado Tape": CassetteBeastsItemData("ap_tape_tornado", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
	"Trinitite Tape": CassetteBeastsItemData("ap_tape_trinitite", next(c), IC.useful, 1, 1,
		lambda options: options.add_bootleg_tapes),
}

cb_remaster_sticker_items = {
	"Close Encounter Sticker": CassetteBeastsItemData("sticker:close_encounter", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity == "percentage" or options.bootlegsanity != "none"),
	"Gear Shear Sticker": CassetteBeastsItemData("sticker:gear_shear", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity != "specific"),
	"Ice Coating Sticker": CassetteBeastsItemData("sticker:ice_coating", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity == "percentage" or options.bootlegsanity != "none"),
	"Magic Tome Sticker": CassetteBeastsItemData("sticker:magic_tome", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity == "percentage" or options.bootlegsanity != "none"),
	"Toy Hammer Sticker": CassetteBeastsItemData("sticker:toy_hammer", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity == "percentage" or options.bootlegsanity != "none"),
	"Zephyr Sticker": CassetteBeastsItemData("sticker:zephyr", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity == "percentage" or options.bootlegsanity != "none"),
	"Carnivore Sticker": CassetteBeastsItemData("sticker:carnivore", next(c), IC.progression, 1, 1,
		lambda options: options.tapesanity == "percentage" or options.bootlegsanity != "none"),
}

cb_upgrade_items = {
	"Miniature Refrigerator": CassetteBeastsItemData("carry_more_coffee", next(c), IC.useful, 1, 7,
		lambda options: options.shopsanity),
	"First Aid Pouch": CassetteBeastsItemData("carry_more_cures", next(c), IC.useful, 1, 17,
		lambda options: options.shopsanity),
	"Resealable Plastic Tub": CassetteBeastsItemData("carry_more_pear_fusilli", next(c), IC.useful, 1, 17,
		lambda options: options.shopsanity),
	"Scent-Absorbing Pouch": CassetteBeastsItemData("carry_more_reodorant", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Respool Pouch": CassetteBeastsItemData("carry_more_respools", next(c), IC.useful, 1, 4,
		lambda options: options.shopsanity),
	"Rewind Pouch": CassetteBeastsItemData("carry_more_rewinds", next(c), IC.useful, 1, 20,
		lambda options: options.shopsanity),
	"Bomb Compartment": CassetteBeastsItemData("carry_more_smoke_bombs", next(c), IC.useful, 1, 4,
		lambda options: options.shopsanity),
	"Critical Mod": CassetteBeastsItemData("fusion_meter_critical", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Fusion Meter Mod": CassetteBeastsItemData("fusion_meter_fill_rate", next(c), IC.useful, 1, 20,
		lambda options: options.shopsanity),
	"Recording Mod": CassetteBeastsItemData("fusion_meter_recording", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Chemistry Mod": CassetteBeastsItemData("fusion_meter_type_advantage", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Victory Mod": CassetteBeastsItemData("fusion_meter_victory", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Extra Gym Point x5": CassetteBeastsItemData("gym_points", next(c), IC.useful, 5, 10,
		lambda options: options.shopsanity),
	"Merchant's Guild Membership": CassetteBeastsItemData("merchant_discounts", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Additional Coffee Stock": CassetteBeastsItemData("merchant_stock_coffee", next(c), IC.useful, 1, 3,
		lambda options: options.shopsanity),
	"Additional Cure Stock": CassetteBeastsItemData("merchant_stock_cures", next(c), IC.useful, 1, 9,
		lambda options: options.shopsanity),
	"Additional Sticker Stock": CassetteBeastsItemData("merchant_stock_stickers", next(c), IC.useful, 1, 5,
		lambda options: options.shopsanity),
	"Microphone Upgrade": CassetteBeastsItemData("recording_success_rate", next(c), IC.useful, 1, 10,
		lambda options: options.shopsanity),
}

cb_loot_table_items = {
	"Miscellaneous Loot": CassetteBeastsItemData("chest_misc", next(c), IC.filler, 1, 87,
		lambda options: options.shuffle_chest_loot_tables),
	"Miscellaneous Loot without Tapes": CassetteBeastsItemData("chest_misc_no_tapes", next(c), IC.filler, 1, 0),# unused?
	"Farm Loot": CassetteBeastsItemData("chest_farm", next(c), IC.filler, 1, 2,
		lambda options: options.shuffle_chest_loot_tables),
	"Mt Wirral Loot": CassetteBeastsItemData("chest_mt_wirral", next(c), IC.filler, 1, 4,
		lambda options: options.shuffle_chest_loot_tables),
	"In Graveyard Loot": CassetteBeastsItemData("chest_in_graveyard", next(c), IC.filler, 1, 1,
		lambda options: options.shuffle_chest_loot_tables),
	"Cast Iron Shore Loot": CassetteBeastsItemData("chest_cast_iron_shore", next(c), IC.filler, 1, 3,
		lambda options: options.shuffle_chest_loot_tables),
	"At Sea Loot": CassetteBeastsItemData("chest_at_sea", next(c), IC.filler, 1, 0,
		lambda options: options.shuffle_chest_loot_tables),# miscounted?
	"Spider Cave Loot": CassetteBeastsItemData("chest_spider_cave", next(c), IC.filler, 1, 1,
		lambda options: options.shuffle_chest_loot_tables),
	"Cherry Cross Station Loot": CassetteBeastsItemData("chest_dugeon_meadow", next(c), IC.filler, 1, 2,
		lambda options: options.shuffle_chest_loot_tables),
	"Titania Shipwreck Insomnia Loot": CassetteBeastsItemData("chest_shipwreck_insomnia", next(c), IC.filler, 1, 1,
		lambda options: options.shuffle_chest_loot_tables),
	"Station Loot": CassetteBeastsItemData("chest_station", next(c), IC.filler, 1, 8,
		lambda options: options.shuffle_chest_loot_tables),
	"Kayliegh's Home Loot": CassetteBeastsItemData("chest_kayleigh_home", next(c), IC.filler, 1, 1,
		lambda options: options.shuffle_chest_loot_tables),
	"Office Loot": CassetteBeastsItemData("chest_office", next(c), IC.filler, 1, 5,
		lambda options: options.shuffle_chest_loot_tables),
}

cb_trap_items = {
	"Traffikrab Trap": CassetteBeastsItemData("ap_trap_solo_traffikrab", next(c), IC.trap, 1, 0),
	"Lobstacle Trap": CassetteBeastsItemData("ap_trap_solo_lobstacle", next(c), IC.trap, 1, 0),
	"Trapwurm Trap": CassetteBeastsItemData("ap_trap_solo_trapwurm", next(c), IC.trap, 1, 0),
	"Miss Mimic Trap": CassetteBeastsItemData("ap_trap_solo_miss_mimic", next(c), IC.trap, 1, 0),
	"Traffikrab Swarm Trap": CassetteBeastsItemData("ap_trap_swarm_traffikrab", next(c), IC.trap, 1, 0),
	"Bulletino Swarm Trap": CassetteBeastsItemData("ap_trap_swarm_bulletino", next(c), IC.trap, 1, 0),
	"Starters Battle Trap": CassetteBeastsItemData("ap_trap_special_starters", next(c), IC.trap, 1, 0),
	"Partners Battle Trap": CassetteBeastsItemData("ap_trap_special_partners", next(c), IC.trap, 1, 0),
}
cb_trap_item_weights = [50, 20, 30, 5, 10, 5, 1, 1]

item_data_table = cb_abilities|cb_key_items|cb_regular_items|cb_resource_items|\
				  cb_tape_items|cb_bootleg_tape_items|cb_remaster_sticker_items|\
				  cb_upgrade_items|cb_loot_table_items|cb_trap_items

item_table = {name: data.code
	for name, data in item_data_table.items()
	if data.code is not None}

def shouldAddItem(options, name) -> bool:
	return item_data_table[name].requires == None or item_data_table[name].requires(options)