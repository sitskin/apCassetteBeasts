from math import ceil
from typing import NamedTuple, Optional

from BaseClasses import Location

from .Regions import region_data_table
from .Data.tape_data import types, monsters, monsterCount

class CassetteBeastsLocation(Location):
	game = "Cassette Beasts"

class CassetteBeastsLocationData(NamedTuple):
	cb_name: str
	region: str
	address: int
	rules: Optional[callable] = None
	requires: Optional[callable] = None

class CassetteBeastsEventData(NamedTuple):
	region: str
	item: str
	rules: Optional[callable] = None
	requires: Optional[callable] = None

def counter(start: int=1) -> int:
	while True:
		yield start
		start += 1
c = counter()

def addLocationRequires(table: dict, req: callable) -> None:
	for key, data in table.items():
		table[key] = CassetteBeastsLocationData(data.cb_name, data.region, data.address,
			data.rules, req)

def getMonsterRules(monster_data, loc_data_table) -> callable:
	rules = []
	for location in monster_data.locations:
		if location in region_data_table.keys():
			rules.append(lambda state, player, loc=location: state.can_reach_region(loc, player))
		elif location in loc_data_table.keys():
			rules.append(lambda state, player, loc=location: state.can_reach_location(loc, player))
		elif location in event_data_table.keys():
			rules.append(lambda state, player, loc=location: state.has(loc, player))
		elif location.startswith("remaster"):
			s = location.split("_")
			if len(s[0].split("-")) == 1:
				# regular remaster
				rules.append(lambda state, player: state.can_reach_location(f"Recorded {s[1]}", player))
			elif s[0].split("-")[1] in types:
				# requires bootleg
				rules.append(lambda state, player: state.can_reach_location(f"Recorded {s[0].split('-')[1].capitalize()} {s[1]}", player))
			elif len(s[0].split("-")) == 2:
				# requires move
				rules.append(lambda state, player: state.can_reach_location(f"Recorded {s[1]}", player) and \
					state.has(s[0].split("-")[1]+" Sticker", player))
		elif location == "farm_jelly":
			rules.append(lambda state, player: state.has("Skelly Jelly", player, 2) and state.can_reach_region("Piper Farm", player))
		elif location == "warehouse":
			rules.append(lambda state, player: state.has("Warehouse Key", player) and state.can_reach_region("Brightside Pier", player))
	return lambda state, player: any([rule(state, player) for rule in rules])

base_locations = {
	"Defeat Oldgante": 
		CassetteBeastsLocationData("ap_encounter_aa_oldgante", "Harbourtown Station", next(c)),
	"Defeat Poppetox": 
		CassetteBeastsLocationData("ap_encounter_aa_puppet", "Glowcester Road Station", next(c),
			lambda state, player: state.has("Train Ticket (Glowcester)", player)),
	"Defeat Mourningstar": 
		CassetteBeastsLocationData("ap_encounter_aa_mourningstar", "Mourningstar Crescent Station", next(c)),
	"Defeat Nowhere Monarch": 
		CassetteBeastsLocationData("ap_encounter_aa_monarch", "Falldown Mall", next(c)),
	"Defeat Heckahedron": 
		CassetteBeastsLocationData("ap_encounter_aa_cube", "Waterloop Station", next(c)),
	"Defeat Alice": 
		CassetteBeastsLocationData("ap_encounter_aa_alice", "Cherry Cross Station", next(c),
			lambda state, player: state.has("White Rabbit Key", player)),
	"Defeat Robin Goodfellow": 
		CassetteBeastsLocationData("ap_encounter_aa_robin", "Bard Street Station", next(c)),
	"Defeat Mammon": 
		CassetteBeastsLocationData("ap_encounter_aa_mammon", "Landkeeper HQ", next(c),
			lambda state, player: clearedOffices(state, player)),
	"Defeat Lamento Mori": 
		CassetteBeastsLocationData("ap_encounter_aa_lamento_mori", "Aldgrave Tomb Station", next(c),
			lambda state, player: state.has("Train Ticket (Aldgrave Tomb)", player)),
	"Defeat Babelith": 
		CassetteBeastsLocationData("ap_encounter_aa_tower", "Icelington Station", next(c)),
	"Defeat Shining Kuneko": 
		CassetteBeastsLocationData("ap_encounter_aa_kuneko", "Cherry Meadow", next(c),
			lambda state, player: state.has("Recruited Felix", player) and state.has("Swim", player)),
	"Defeat Averevoir":
		CassetteBeastsLocationData("ap_encounter_aa_averevoir", "Mt Wirral", next(c)),
	"Defeat Morgante": 
		CassetteBeastsLocationData("ap_encounter_aa_finalgante", "Postgame", next(c)),
	"Defeat Helia": 
		CassetteBeastsLocationData("ap_encounter_aa_helia", "Postgame", next(c)),
	"Defeat Lenna": 
		CassetteBeastsLocationData("ap_encounter_aa_lenna", "Postgame", next(c),
			lambda state, player: state.has("Progressive Glide", player, 2)),
	"Beat Wallace": 
		CassetteBeastsLocationData("encounter_captain_wallace", "New Wirral Park", next(c)),
	"Beat Skip": 
		CassetteBeastsLocationData("encounter_captain_skip", "Harbourtown West", next(c),
			lambda state, player: state.has("Swim", player) or state.has("Progressive Glide", player, 2)),
	"Beat Zedd": 
		CassetteBeastsLocationData("encounter_captain_zedd", "Autumn Hill", next(c),
			lambda state, player: state.can_reach_location("Recorded Bulletino", player)),
	"Beat Judas": 
		CassetteBeastsLocationData("encounter_captain_judas", "Southern Isles", next(c)),
	"Beat Clee-o": 
		CassetteBeastsLocationData("encounter_captain_cleeo", "Eastham Woods", next(c),
			lambda state, player: state.has("Coin", player)),
	"Beat Lodestein": 
		CassetteBeastsLocationData("encounter_captain_lodestein", "Ham", next(c),
			lambda state, player: state.has("Progressive Dash", player) and state.has("Progressive Magnetism", player)),
	"Beat Penny Dreadful": 
		CassetteBeastsLocationData("encounter_captain_dreadful", "New London", next(c)),
	"Beat Gladiola": 
		CassetteBeastsLocationData("encounter_captain_gladiola", "West Mire Sea", next(c)),
	"Beat Heather": 
		CassetteBeastsLocationData("encounter_captain_heather", "West Mire Sea", next(c)),
	"Beat Buffy": 
		CassetteBeastsLocationData("encounter_captain_buffy", "Cherry Meadow", next(c),
			lambda state, player: state.has("Progressive Dash", player) or state.has("Progressive Climb", player)),
	"Beat Cybil": 
		CassetteBeastsLocationData("encounter_captain_cybil", "The Marshes", next(c)),
	"Beat Codey": 
		CassetteBeastsLocationData("encounter_captain_codey", "Mt Wirral", next(c)),
	"Beat Ianthe": 
		CassetteBeastsLocationData("encounter_ianthe", "New Wirral Park", next(c),
			lambda state, player: hasAllStamps(state, player)),
	"Harbourtown Chest under Crate on Flour Mill (0,-1)": 
		CassetteBeastsLocationData("OVERWORLD_0_-1_CHEST", "Harbourtown East", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Upper Path Magnet Platform Chest (0,-2)": 
		CassetteBeastsLocationData("overworld_0_-2_chest", "Upper Path", next(c),
			lambda state, player: state.has("Progressive Magnetism", player) and state.has("Progressive Glide", player, 1)),
	"Thirstaton Lake Underwater Chest (0,-3)": 
		CassetteBeastsLocationData("overworld_0_-3_chest", "Thirstaton Lake", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Eastham Woods Lift Rock Chest (0,-6)": 
		CassetteBeastsLocationData("chest_overworld_0_-6", "Eastham Woods", next(c)),
	"Eastham Woods Chest Near Ham (0,-7)": 
		CassetteBeastsLocationData("chest_overworld_0_-7", "Eastham Woods", next(c)),
	"Harbourtown Chest on Top of House (1,-1)": 
		CassetteBeastsLocationData("overworld_1_-1_chest", "Harbourtown East", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Eastham Woods Three Lights Chest (1,-6)": 
		CassetteBeastsLocationData("chest_overworld_1_-6", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Harbourtown Outskirts Break Rock Chest (2,-2)": 
		CassetteBeastsLocationData("overworld_2_-2_rock_chest", "Harbourtown Outskirts", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"New Wirral Park Chest Under Bridge by Lake (2,-3)": 
		CassetteBeastsLocationData("chest_overworld_2_-3", "New Wirral Park", next(c)),
	"New Wirral Park Chest Lift Box in Pond (3,-3)": 
		CassetteBeastsLocationData("chest_overworld_3_-3", "New Wirral Park", next(c)),
	"New Wirral Park Chest Behind Ranger Station (2,-4)": 
		CassetteBeastsLocationData("chest_overworld_2_-4", "New Wirral Park", next(c)),
	"Eastham Woods Magnet Button Chest (2,-6)": 
		CassetteBeastsLocationData("overworld_2_-6_chest", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Harbourtown Beach Chest (3,0)": 
		CassetteBeastsLocationData("chest_overworld_3_0", "Harbourtown Beach", next(c)),
	"Harbourtown Outskirts Chest Near Lamppost (3,-2)": 
		CassetteBeastsLocationData("chest_overworld_3_-2", "Harbourtown Outskirts", next(c)),
	"Eastham Woods Chest on Cliff Below Mall (3,-7)": 
		CassetteBeastsLocationData("chest_overworld_3_-7", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Eastham Woods Chest on Mall Roof (3,-7)": 
		CassetteBeastsLocationData("chest_overworld_3_-7_mall_roof", "Eastham Woods Cliff", next(c)),
	"Deadlands Floor Button Chest (4,-2)": 
		CassetteBeastsLocationData("chest_overworld_4_-2", "Deadlands", next(c)),
	"New Wirral Park Break Rock Chest in Wall (4,-5)": 
		CassetteBeastsLocationData("overworld_4_-5_chest1", "New Wirral Park", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Eastham Woods Levitator Magnet Chest (4,-6)": 
		CassetteBeastsLocationData("chest_overworld_4_-6", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Eastham Woods Four Button Chest (4,-7)": 
		CassetteBeastsLocationData("chest_overworld_4_-7", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Deadlands Coast Button Chest (5,-1)": 
		CassetteBeastsLocationData("overworld_5_-1_chest", "Deadlands Coast", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"New London Three Button Chest (5,-2)": 
		CassetteBeastsLocationData("overworld_5_-2_chest", "New London", next(c)),
	"New Wirral Park Lower Platform Chest (5,-3)": 
		CassetteBeastsLocationData("chest_overworld_5_-3", "New Wirral Park", next(c)),
	"Eastham Woods Chest in Pond (5,-5)": 
		CassetteBeastsLocationData("chest_overworld_5_-5", "Eastham Woods", next(c)),
	"Eastham Woods Levitator Magnet Lever Chest (5,-7)": 
		CassetteBeastsLocationData("chest_overworld_5_-7", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Progressive Magnetism", player)),
	"Southern Isles Chest Washed Up on Island (6,0)": 
		CassetteBeastsLocationData("overworld_6_0_chest", "Southern Isles", next(c),
			lambda state, player: state.has("Swim", player)),
	"New London Chest in House (6,-2)": 
		CassetteBeastsLocationData("overworld_6_-2_chest", "New London", next(c),
			lambda state, player: state.has("Progressive Climb", player)),
	"Deadlands Coast Gust Chest (6,-2)": 
		CassetteBeastsLocationData("overworld_6_-2_chest_2", "Deadlands Coast", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Autumn Hill Lever Chest in Lake (6,-3)": 
		CassetteBeastsLocationData("chest_overworld_6_-3", "Autumn Hill", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Autumn Hill Chest with Button in Eastham Woods (6,-5)": 
		CassetteBeastsLocationData("chest_overworld_6_-5", "Autumn Hill", next(c)),
	"Southern Isles Underwater Chest (7,0)": 
		CassetteBeastsLocationData("overworld_7_0_chest", "Southern Isles", next(c),
			lambda state, player: state.has("Swim", player) and state.has("Progressive Dash", player)),
	"Deadlands Coast Lift Rock Chest (7,-1)": 
		CassetteBeastsLocationData("overworld_7_-1_chest", "Deadlands Coast", next(c)),
	"New London Statue Puzzle Chest (7,-2)": 
		CassetteBeastsLocationData("overworld_7_-2_chest_1", "New London", next(c)),
	"New London 2 Button Chest (7,-2)": 
		CassetteBeastsLocationData("overworld_7_-2_chest_2", "New London", next(c)),
	"Autumn Hill Shortcut Chest (7,-3)": 
		CassetteBeastsLocationData("chest_overworld_7_-3", "Autumn Hill", next(c)),
	"Autumn Hill Peak Break Rock Chest (7,-4)": 
		CassetteBeastsLocationData("chest_overworld_7_-4", "Autumn Hill", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Deadlands Coast Chest Near Dino Quarry (8,-1)": 
		CassetteBeastsLocationData("overworld_8_-1_chest_1", "Deadlands Coast", next(c)),
	"Deadlands Coast Place Two Rocks Chest (8,-1)": 
		CassetteBeastsLocationData("overworld_8_-1_chest_2", "Deadlands Coast", next(c)),
	"Autumn Hill Button Chest (8,-3)": 
		CassetteBeastsLocationData("chest_overworld_8_-3", "Autumn Hill", next(c)),
	"Autumn Hill Elevator Chest (8,-5)": 
		CassetteBeastsLocationData("chest_overworld_8_-5", "Autumn Hill", next(c)),
	"Autumn Hill Underwater Chest (8,-6)": 
		CassetteBeastsLocationData("chest_overworld_8_-6", "Autumn Hill", next(c),
			lambda state, player: state.has("Progressive Glide", player) or state.has("Swim", player)),
	"NE Mire Sea Chest (8,-7)": 
		CassetteBeastsLocationData("chest_overworld_8_-7", "NE Mire Sea", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Progressive Magnetism", player)),
	"Upper Path Chest on Wall Before Harbourtown West (-1,-2)": 
		CassetteBeastsLocationData("chest_overworld_-1_-2", "Upper Path", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Progressive Magnetism", player)),
	"Lakeside Chest by Waterfall (-1,-6)": 
		CassetteBeastsLocationData("overworld_-1_-6_chest_1", "Lakeside", next(c)),
	"Lakeside Four Button Chest Near Ham (-1,-6)": 
		CassetteBeastsLocationData("overworld_-1_-6_chest_2", "Lakeside", next(c)),
	"Ham Chest Near Mt Wirral (-1,-7)": 
		CassetteBeastsLocationData("overworld_-1_-7_chest_1", "Ham", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Ham Chest Fall from Mt Wirral (-1,-7)": 
		CassetteBeastsLocationData("overworld_-1_-7_chest_2", "Ham", next(c),
			lambda state, player: state.can_reach_region("Mt Wirral", player)),
	"Thirstaton Lake Statue Puzzle Chest (-2,-3)": 
		CassetteBeastsLocationData("overworld_-2_-3_chest", "Thirstaton Lake", next(c)),
	"Cherry Meadow Chest Over Thirstaton Lake (-2,-3)": 
		CassetteBeastsLocationData("overworld_-2_-3_chest_2", "Cherry Meadow", next(c)),
	"Thirstaton Lake Chest in Wall (-2,-5)": 
		CassetteBeastsLocationData("overworld_-2_-5_chest", "Thirstaton Lake", next(c)),
	"Mt Wirral Lower Platform with Button Chest (-2,-6)": 
		CassetteBeastsLocationData("overworld_-2_-6_chest", "Mt Wirral", next(c)),
	"Behind Mt Wirral Chest (-2,-7)": 
		CassetteBeastsLocationData("overworld_2_-7_chest_1", "Ham", next(c)),
	"East of Graveyard Lever Chest (-3,0)": 
		CassetteBeastsLocationData("chest_overworld_-3_0", "Lost Hearts Graveyard", next(c)),
	"Piper Farm Chest (-3,-1)": 
		CassetteBeastsLocationData("chest_overworld_-3_-1_a", "Piper Farm", next(c)),
	"Piper Farm Climb Chest (-3,-1)": 
		CassetteBeastsLocationData("chest_overworld_-3_-1_b", "Piper Farm", next(c),
			lambda state, player: state.has("Progressive Climb", player)),
	"Marshes Lift Crate in Cherry Meadow Chest (-3,-3)": 
		CassetteBeastsLocationData("chest_overworld_-3_-3", "The Marshes", next(c)),
	"Cherry Meadow Chest Near Captain Buffy (-3,-5)": 
		CassetteBeastsLocationData("chest_overworld_-3_-5", "Cherry Meadow", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Mt Wirral Chest Above Big Entrance (-3,-6)": 
		CassetteBeastsLocationData("chest_overworld_-3_-6", "Mt Wirral", next(c)),
	"Mt Wirral Chest at River Source (-3,-7)": 
		CassetteBeastsLocationData("chest_overworld_-3_-7", "Mt Wirral", next(c)),
	"Graveyard Chest in Puddle (-4,0)": 
		CassetteBeastsLocationData("chest_overworld_-4_0", "Lost Hearts Graveyard", next(c)),
	"Marshes 4 Rocks in a Line Chest (-4,-3)": 
		CassetteBeastsLocationData("chest_overworld_-4_-3", "The Marshes", next(c)),
	"Mt Wirral Elevator Chest (-4,-6)": 
		CassetteBeastsLocationData("chest_overworld_-4_-6", "Mt Wirral", next(c)),
	"Marshes Chest Near Landkeeper Office (-5,-3)": 
		CassetteBeastsLocationData("chest_overworld_-5_-3", "The Marshes", next(c)),
	"Cherry Meadow Button Chest (-5,-4)": 
		CassetteBeastsLocationData("overworld_-5_-4_chest", "Cherry Meadow", next(c),
			lambda state, player: state.has("Progressive Dash", player) or state.has("Progressive Climb", player)),
	"Mt Wirral Base Chest Near Cast Iron Shore (-5,-6)": 
		CassetteBeastsLocationData("chest_overworld_-5_-6_a", "Mt Wirral", next(c)),
	"Mt Wirral Button Chest (-5,-6)": 
		CassetteBeastsLocationData("chest_overworld_-5_-6_b", "Mt Wirral", next(c)),
	"Mt Wirral Chest Near Brokenhead (-5,-7)": 
		CassetteBeastsLocationData("chest_overworld_-5_-7", "Mt Wirral", next(c)),
	"Marshes Coast Button Chest (-6,-1)": 
		CassetteBeastsLocationData("chest_overworld_-6_-1", "The Marshes", next(c)),
	"Marshes Three Underwater Buttons Chest (-6,-2)": 
		CassetteBeastsLocationData("chest_overworld_-6_-2", "The Marshes", next(c)),
	"Cast Iron Shore Magnet Button Chest (-6,-4)": 
		CassetteBeastsLocationData("chest_overworld_-6_-4", "Cast Iron Shore", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Cast Iron Shore Two Magnet Button Chest (-6,-5)": 
		CassetteBeastsLocationData("chest_overworld_-6_-5", "Cast Iron Shore", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"West Mire Sea Chest Near Captain Gladiola (-7,0)": 
		CassetteBeastsLocationData("chest_overworld_-7_0", "West Mire Sea", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"West Mire Sea Button Chest on Pillar (-7,-3)": 
		CassetteBeastsLocationData("chest_overworld_-7_-3", "West Mire Sea", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Brokenhead Chest on Henge (-7,-7)": 
		CassetteBeastsLocationData("chest_overworld_-7_-7_a", "Brokenhead", next(c)),
	"Brokenhead Chest Under Henge (-7,-7)": 
		CassetteBeastsLocationData("chest_overworld_-7_-7_b", "Brokenhead", next(c)),
	"Autumn Gate Cave Chest (6,-4)": 
		CassetteBeastsLocationData("chest_autumn_hill_gate_autumn_cave_1", "Autumn Hill", next(c)),
	"Averevoir Cave Chest (-3,-6)": 
		CassetteBeastsLocationData("chest_cave_averevoir", "Mt Wirral", next(c)),
	"Deadlands Cave Chest (6,-1)": 
		CassetteBeastsLocationData("cave_deadlands_1_chest", "Deadlands Coast", next(c),
            lambda state, player: state.has("Progressive Dash", player) or state.has("Progressive Climb", player)),
	"Deadlands Cave Break Rock Chest (6,-2)": 
		CassetteBeastsLocationData("cave_deadlands_3_chest", "Deadlands Coast", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Autumn Hill Gear Cave Chest (7,-6)": 
		CassetteBeastsLocationData("chest_autumn_hill_gear_cave", "Autumn Hill", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Progressive Dash", player)),
	"Lake Cave Chest (-1,-2)": 
		CassetteBeastsLocationData("cave_lake_1_chest", "Thirstaton Lake", next(c)),
	"Marsh Cave Chest (-5,-1)": 
		CassetteBeastsLocationData("cave_marsh_1_chest", "The Marshes", next(c)),
	"Marsh Cave Chest (-7,-1)": 
		CassetteBeastsLocationData("cave_marsh_2_chest", "The Marshes", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Cherry Meadow Cave Chest (-4,-6)": 
		CassetteBeastsLocationData("chest_cave_meadow_1", "Cherry Meadow", next(c)),
	"Mt Wirral Waterfall Cave Chest (-2,-7)": 
		CassetteBeastsLocationData("cave_mt_wirral_1_chest", "Mt Wirral", next(c)),
	"Mt Wirral Cave Bridge Chest (-3,-7)": 
		CassetteBeastsLocationData("cave_mt_wirral_2_chest", "Mt Wirral", next(c)),
	"Harbourtown Outskirts Pipe Chest (1,-1)": 
		CassetteBeastsLocationData("cave_outskirts_pipe_chest", "Harbourtown Outskirts", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Progressive Dash", player)),
	"New Wirral Park Track Cave Chest(3,-5)": 
		CassetteBeastsLocationData("cave_new_wirral_park_1_chest", "New Wirral Park", next(c)),
	"New Wirral Park Cave Chest (4,-3)": 
		CassetteBeastsLocationData("chest_parkcave2_1", "New Wirral Park", next(c),
			lambda state, player: state.has("Progressive Glide", player) or state.has("Progressive Climb", player)),
	"New Wirral Park Cave Break Rock Chest (4,-3)": 
		CassetteBeastsLocationData("chest_parkcave2_2", "New Wirral Park", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"New Wirral Park Under Ranger Station Cave Chest (2,-4)": 
		CassetteBeastsLocationData("chest_parkcave3_1", "New Wirral Park", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Thirsaton Lake Waterfall Cave Chest (-1,-5)": 
		CassetteBeastsLocationData("cave_lakeside_2_chest", "Thirstaton Lake", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Spider Cave Chest (-6,-1)": 
		CassetteBeastsLocationData("spider_cave_3_chest_1", "Spider Cave", next(c)),
	"Eastham Woods Cave Chest (2,-6)": 
		CassetteBeastsLocationData("chest_woods_cave_1", "Eastham Woods", next(c),
			lambda state, player: state.has("Progressive Magnetism", player)),
	"Mourningtown Chest (7,-5)": 
		CassetteBeastsLocationData("chest_commune_key_rusted", "Mourningtown", next(c)),
	"Glowcester Road Station Cave Chest (5,-4)": 
		CassetteBeastsLocationData("dungeon_glowshroom_cave2_chest", "Glowcester Road Station", next(c)),
	"Falldown Mall Bookshop Chest (3,-7)": 
		CassetteBeastsLocationData("mall_chest_bookshop", "Falldown Mall", next(c)),
	"Falldown Mall Empty Shop Chest (3,-7)": 
		CassetteBeastsLocationData("mall_empty_shop_chest", "Falldown Mall", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Falldown Mall Crate Room Chest (3,-7)": 
		CassetteBeastsLocationData("mall_shop_miscshop_chest", "Falldown Mall", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Cherry Cross Station Giant Chest (-4,-4)": 
		CassetteBeastsLocationData("chest_dungeon_meadow_garden", "Cherry Cross Station", next(c)),
	"Cherry Cross Station Tiny Chest (-4,-4)": 
		CassetteBeastsLocationData("chest_dungeon_meadow_room2", "Cherry Cross Station", next(c)),
	"Icelington Station Chest (-3,-7)": 
		CassetteBeastsLocationData("chest_station_mountain_entrance", "Icelington Station", next(c)),
	"Titania Shipwreck Valve 1 (-6,-6)": 
		CassetteBeastsLocationData("shipwreck_valve_1", "Titania Shipwreck", next(c)),
	"Titania Shipwreck Valve 2 (-6,-6)": 
		CassetteBeastsLocationData("shipwreck_valve_2", "Titania Shipwreck", next(c),
			lambda state, player: state.has("Valve Handle", player)),
	"Titania Shipwreck Chest (-6,-6)": 
		CassetteBeastsLocationData("shipwreck_chest_1", "Titania Shipwreck", next(c),
			lambda state, player: state.has("Valve Handle", player)),
	"Waterloop Station Break Polyhedron Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_optional_dash_reward", "Waterloop Station", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Waterloop Station Statues Off Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_switch_grid_off", "Waterloop Station", next(c)),
	"Waterloop Station Statues On Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_switch_grid_on", "Waterloop Station", next(c)),
	"Waterloop Station Lying Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_lying_right", "Waterloop Station", next(c)),
	"Harbourtown Apartment Chest (-1,0)": 
		CassetteBeastsLocationData("harbourtown_apartment3_chest", "Harbourtown West", next(c)),
	"Harbourtown Red House Fridge (-1,0)": 
		CassetteBeastsLocationData("HouseWest3_fridge", "Harbourtown West", next(c)),
	"Harbourtown Kayliegh's Home Chest (1,0)": 
		CassetteBeastsLocationData("chest_kayleigh_home", "Harbourtown East", next(c)),
	"Harbourtown Town Hall Cabinet (0,0)": 
		CassetteBeastsLocationData("cabinet_town_hall", "Harbourtown East", next(c),
			lambda state, player: state.has("Met Ianthe", player)),
	"Landkeeper Office 1 Cabinet (4,-1)": 
		CassetteBeastsLocationData("chest_office1", "Harbourtown Outskirts", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Landkeeper Office 2 Cabinet (7,-3)": 
		CassetteBeastsLocationData("chest_office2", "Autumn Hill", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Landkeeper Office 3 Cabinet (7,-7)": 
		CassetteBeastsLocationData("chest_office3", "NE Mire Sea", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Landkeeper Office 4 Cabinet (1,-7)": 
		CassetteBeastsLocationData("chest_office4", "Eastham Woods Cliff", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Landkeeper Office 5 Cabinet (-6,-3)": 
		CassetteBeastsLocationData("chest_office5", "The Marshes", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Harbourtown Station Chest (1,-2)": 
		CassetteBeastsLocationData("harbourtown_station_chest1", "Harbourtown Station", next(c)),
	"Night's Bridge Station Clockhands Chest (?,?)": 
		CassetteBeastsLocationData("room_1A_chest_1", "Night's Bridge Station", next(c),
			lambda state, player: state.has("Progressive Climb", player)),
	"Night's Bridge Station Right Azure Keystone Chest (?,?)": 
		CassetteBeastsLocationData("room_1A_chest_2", "Night's Bridge Station", next(c)),
	"Night's Bridge Station Left Azure Keystone Chest (?,?)": 
		CassetteBeastsLocationData("room_2A_chest_1", "Night's Bridge Station", next(c)),
	"Titania Shipwreck Chest on Chimney (-6,-6)":
		CassetteBeastsLocationData("chest_shipyard_ship_chimney", "Cast Iron Shore", next(c),
			lambda state, player: state.has("Progressive Climb", player)),
	"Ranger Handbook":
		CassetteBeastsLocationData("Ranger Handbook", "Harbourtown East", next(c)),
	"Type Chart":
		CassetteBeastsLocationData("Type Chart", "Menu", next(c),
			lambda state, player: state.has("Ranger Handbook", player)),
	"Harbourtown Gate Key":
		CassetteBeastsLocationData("Harbourtown Gate Key", "Harbourtown Beach", next(c)),
	"Train Ticket (Glowcester)":
		CassetteBeastsLocationData("Train Ticket (Glowcester)", "Glowcester Road Station", next(c),
			lambda state, player: state.has("Machine Part", player)),
	"Train Ticket (Aldgrave Tomb)":
		CassetteBeastsLocationData("Train Ticket (Aldgrave Tomb)", "Aldgrave Tomb Station", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Captain Clee-o Coin":
		CassetteBeastsLocationData("Captain Clee-o Coin", "Eastham Woods", next(c)),
	"Envelope for Meredith":
		CassetteBeastsLocationData("Envelope for Meredith", "Harbourtown East", next(c),
			lambda state, player: state.has("Met Meredith", player)),
	"Landkeeper Key":
		CassetteBeastsLocationData("Landkeeper Key", "Harbourtown Outskirts", next(c),
			lambda state, player: state.has("Progressive Glide", player)),
	"Landkeeper Secret Hideout Button Chest (-4,-1)":
		CassetteBeastsLocationData("dungeon_landkeeper_secret_chest_1", "New Landkeeper Hideout", next(c)),
	"Landkeeper Secret Hideout Pillar Chest (-4,-1)":
		CassetteBeastsLocationData("dungeon_landkeeper_secret_chest_2", "New Landkeeper Hideout", next(c)),
}

pier_locations = {
	"Defeat Gwenivar": 
		CassetteBeastsLocationData("ap_encounter_aa_clown", "Brightside Pier", next(c),
			None,# TODO add pier of the unknown locations
			lambda options: options.use_pier == True),
}

chest_loot_locations = {
	loc.replace("Chest", "Chest Loot").replace("Cabinet", "Cabinet Loot").replace("Fridge", "Fridge Loot"):
	CassetteBeastsLocationData("loot_"+data.cb_name, data.region, next(c), data.rules,
		lambda options, f=data.requires: (f and f(options)) and options.shuffle_chest_loot)\
	for loc, data in (base_locations|pier_locations).items() if
		any(["Chest" in loc, "Cabinet" in loc, "Fridge" in loc])
}

shopsanity_locations = {
	
}
addLocationRequires(shopsanity_locations, lambda options: options.shopsanity)


trainersanity_locations = {
	"Thirstaton Lake Traveler Battle (0,-4)": 
		CassetteBeastsLocationData("encounter_overworld_0_-4_battler", "Thirstaton Lake", next(c)),
	"Lakeside Camper Battle (0,-5)": 
		CassetteBeastsLocationData("encounter_overworld_0_-5_battler", "Lakeside", next(c)),
	"Diogenes Battle (0,-5)": 
		CassetteBeastsLocationData("encounter_overworld_0_-5_battler_diogenes", "Lakeside", next(c)),
	"Eastham Woods Soldier Battle Near Ham (0,-6)": 
		CassetteBeastsLocationData("encounter_overworld_0_-6_battler", "Eastham Woods", next(c)),
	"Thirstaton Lake Researcher Battle (1,-4)": 
		CassetteBeastsLocationData("encounter_overworld_1_-4_battler", "Thirstaton Lake", next(c)),
	"Lakeside Traveler Battle (1,-5)": 
		CassetteBeastsLocationData("encounter_overworld_1_-5_battler", "Lakeside", next(c)),
	"Decartes Battle (1,-6)": 
		CassetteBeastsLocationData("encounter_overworld_1_-6_battler_decartes", "Eastham Woods", next(c)),
	"Eastham Landkeeper Battle 1 (1,-7)": 
		CassetteBeastsLocationData("encounter_overworld_1_-7_landkeeper", "Eastham Woods Cliff", next(c)),
	"Eastham Landkeeper Battle 2 (1,-7)": 
		CassetteBeastsLocationData("encounter_overworld_1_-7_landkeeper2", "Eastham Woods Cliff", next(c)),
	"Ranger Wannabe Battle Near Ranger Station (2,-4)": 
		CassetteBeastsLocationData("encounter_nwp_ranger_wannabe_2_-4", "New Wirral Park", next(c)),
	"Ranger Recruiter Battle Near Ranger Station (2,-4)": 
		CassetteBeastsLocationData("encounter_nwp_ranger_recruiter_2_-4", "New Wirral Park", next(c)),
	"New Wirral Park Ranger Battle (2,-5)": 
		CassetteBeastsLocationData("encounter_overworld_2_-5_ranger", "New Wirral Park", next(c)),
	"Eastham Landkeeper Battle 3 (2,-7)": 
		CassetteBeastsLocationData("encounter_overworld_2_-7_landkeeper", "Eastham Woods Cliff", next(c)),
	"New Wirral Park Landkeeper Battle (3,-4)": 
		CassetteBeastsLocationData("encounter_overworld_3_-4_landkeeper", "New Wirral Park", next(c)),
	"New Wirral Park Ranger Wannabe Duo Battle (3,-4)": 
		CassetteBeastsLocationData("encounter_overworld_3_-4_wannabe", "New Wirral Park", next(c)),
	"New Wirral Park Madman Battle (3,-4)": 
		CassetteBeastsLocationData("encounter_overworld_3_-4_madman", "New Wirral Park", next(c)),# has unique name? NWP_MADMAN_3_-4_NAME
	"New Wirral Park Rocker Battle (3,-5)": 
		CassetteBeastsLocationData("encounter_overworld_3_-5_battler", "New Wirral Park", next(c)),
	"Eastham Woods Cultist Battle (3,-6)": 
		CassetteBeastsLocationData("encounter_overworld_3_-6_cultist", "Eastham Woods", next(c)),
	"Treasure Seeker Battle Near Mall (3,-7)": 
		CassetteBeastsLocationData("encounter_overworld_3_-7_battler", "Eastham Woods Cliff", next(c)),
	"New Wirral Park Ranger Wannabe Battle (4,-3)": 
		CassetteBeastsLocationData("encounter_overworld_4_-3_wannabe", "New Wirral Park", next(c)),
	"New Wirral Park Cultist Battle 1 (4,-4)": 
		CassetteBeastsLocationData("encounter_nwp_4_-4_cultist", "New Wirral Park", next(c)),
	"New Wirral Park Battle (4,-5)": 
		CassetteBeastsLocationData("encounter_overworld_4_-5_battler", "New Wirral Park", next(c)),# has unique name? OVERWORLD_4_-5_BATTLER_NAME
	"Aristotle Battle (4,-6)": 
		CassetteBeastsLocationData("encounter_overworld_4_-6_battler_aristotle", "Eastham Woods", next(c)),
	"Eastham Woods Landkeeper Battle 4 (4,-7)": 
		CassetteBeastsLocationData("encounter_overworld_4_-7_landkeeper", "Eastham Woods", next(c)),
	"Southern Isles Traveler Battle (5,0)": 
		CassetteBeastsLocationData("encounter_overworld_5_0_battler", "Southern Isles", next(c)),
	"Deadlands Coast Treasure Seeker Battle (5,-1)": 
		CassetteBeastsLocationData("encounter_overworld_5_-1_battler", "Deadlands Coast", next(c)),
	"Deadlands Ranger Trainee Battle (5,-2)": 
		CassetteBeastsLocationData("encounter_overworld_5_-2_battler", "Deadlands", next(c)),
	"New Wirrl Park Duo Battle (5,-3)": 
		CassetteBeastsLocationData("encounter_overworld_5_-3_battler_pair", "New Wirral Park", next(c)),# OVERWORLD_5_-3_BATTLER_PAIR_NAME1 OVERWORLD_5_-3_BATTLER_PAIR_NAME2
	"New Wirral Park Cultist Battle 2 (5,-4)": 
		CassetteBeastsLocationData("encounter_nwp_5_-4_cultist", "New Wirral Park", next(c)),
	"Darwin Battle (5,-5)": 
		CassetteBeastsLocationData("encounter_overworld_5_-5_battler_darwin", "New Wirral Park", next(c)),
	"Eastham Woods Soldier Battle (5,-6)": 
		CassetteBeastsLocationData("encounter_overworld_5_-6_battler", "Eastham Woods", next(c)),
	"Eastham Woods Duo Battle (5,-7)": 
		CassetteBeastsLocationData("encounter_overworld_5_-7_battler_pair", "Eastham Woods", next(c)), # OVERWORLD_5_-7_BATTLER_PAIR_NAME1 OVERWORLD_5_-7_BATTLER_PAIR_NAME2
	"Southern Isles Treasure Seeker Battle (6,0)": 
		CassetteBeastsLocationData("encounter_overworld_6_0_battler", "Southern Isles", next(c)),
	"Deadlands Coast Historian Battle 1 (6,-1)": 
		CassetteBeastsLocationData("encounter_overworld_6_-1_battler", "Deadlands Coast", next(c)),
	"New London Landkeeper Battle (6,-2)": 
		CassetteBeastsLocationData("encounter_overworld_6_-2_landkeeper", "New London", next(c)),
	"New London Historian Battle (6,-2)": 
		CassetteBeastsLocationData("encounter_overworld_6_-2_historian", "New London", next(c)),
	"Autumn Hill Traveler Battle (6,-3)": 
		CassetteBeastsLocationData("encounter_overworld_6_-3_battler", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Battle Before Gate (6,-4)": 
		CassetteBeastsLocationData("encounter_overworld_6_-4_cultist", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Battle After Gate (6,-5)": 
		CassetteBeastsLocationData("encounter_overworld_6_-5_cultist", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Battle Near Sign (6,-6)": 
		CassetteBeastsLocationData("encounter_overworld_6_-6_cultist", "Autumn Hill", next(c)),
	"Nevermort Fan Battle (7,-1)": 
		CassetteBeastsLocationData("encounter_overworld_7_-1_nevermort_fan_npc", "Deadlands Coast", next(c)),# SD_NEVERMORT_TRAINER_NAME
	"New London Ranger Battle (7,-2)": 
		CassetteBeastsLocationData("encounter_overworld_7_-2_battler", "New London", next(c)),
	"New Wirral Park Battle (7,-3)": 
		CassetteBeastsLocationData("encounter_overworld_7_-3_battler", "New Wirral Park", next(c)),# OVERWORLD_7_-3_BATTLER_NAME
	"New Wirral Park Landkeeper Battle Near Office (7,-3)": 
		CassetteBeastsLocationData("encounter_overworld_7_-3_landkeeper", "New Wirral Park", next(c)),
	"Autumn Hill Cultist Newbie Battle (7,-3)": 
		CassetteBeastsLocationData("encounter_overworld_7_-3_cultist_newbie", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Newbie Battle Near Post (7,-4)": 
		CassetteBeastsLocationData("encounter_overworld_7_-4_cultist_newbie", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Duo Battle (7,-6)": 
		CassetteBeastsLocationData("encounter_overworld_7_-6_cultist_pair", "Autumn Hill", next(c)),
	"NE Mire Sea Landkeeper Battle (7,-7)": 
		CassetteBeastsLocationData("encounter_overworld_7_-7_landkeeper", "NE Mire Sea", next(c)),
	"Southern Isles Ranger Wannabe Battle (8,0)": 
		CassetteBeastsLocationData("encounter_overworld_8_0_battler", "Southern Isles", next(c)),
	"Epicurus Battle (8,-1)": 
		CassetteBeastsLocationData("encounter_overworld_8_-1_battler_epicurus", "Deadlands Coast", next(c)),
	"Deadlands Coast Historian Battle 2 (8,-2)": 
		CassetteBeastsLocationData("encounter_overworld_8_-2_battler", "Deadlands Coast", next(c)),
	"Autumn Hill Cultist Battle (8,-3)": 
		CassetteBeastsLocationData("encounter_overworld_8_-3_cultist", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Battle Near Zedd (8,-5)": 
		CassetteBeastsLocationData("encounter_overworld_8_-5_cultist", "Autumn Hill", next(c)),
	"Autumn Hill Cultist Battle Near NE Mire Sea (8,-6)": 
		CassetteBeastsLocationData("encounter_overworld_8_-6_cultist", "Autumn Hill", next(c)),
	"Thirstaton Lake Landkeeper Battle (-1,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-1_-3_landkeeper", "Thirstaton Lake", next(c)),
	"Jackie Battle (-1,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-1_-6_battler_jackie", "Lakeside", next(c)),# OVERWORLD_-1_-6_BATTLER_NAME
	"Lakeside Researcher Battle (-1,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-1_-6_battler2", "Lakeside", next(c)),
	"Landkeeper Battle West of Harbourtown (-2,-1)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-1_landkeeper", "Harbourtown West", next(c)),
	"Thirstaton Historian Battle (-2,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-3_battler", "Thirstaton Lake", next(c)),
	"Diveana Battle (-2,-4)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-4_battler_diveal_keeper", "Thirstaton Lake", next(c)),
	"Zhuangzi Battle (-2,-5)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-5_battler_zhuangzi", "Lakeside", next(c)),# ZHUANGZI_NAME
	"Mt Wirral Landkeeper Battle (-2,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-6_landkeeper", "Mt Wirral", next(c)),
	"Mt Wirral Ranger Wannabe Battle Near Ham (-2,-7,)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-7_battler", "Mt Wirral", next(c)),
	"Creep Battle Below Piper Farm (-3,0)": 
		CassetteBeastsLocationData("encounter_overworld_-3_0", "Piper Farm", next(c)),
	"Cherry Meadow Ranger Trainee Battle (-4,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-4_-3_battler", "Cherry Meadow", next(c)),
	"Cherry Meadow Ranger Trainee Battle Near Buffy (-4,-4)": 
		CassetteBeastsLocationData("encounter_overworld_-4_-4_battler", "Cherry Meadow", next(c),
			lambda state, player: state.has("Progressive Dash", player)),
	"Socrates and Plato Battle (-5,-5)": 
		CassetteBeastsLocationData("encounter_socrates_and_plato", "Cherry Meadow", next(c)),
	"Mt Wirral Traveler Battle (-4,-7)": 
		CassetteBeastsLocationData("encounter_overworld_-4_-7_battler", "Mt Wirral", next(c)),
	"Mt Wirral Traveler Battle Near Brokenhead (-5,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-5_-6_battler", "Mt Wirral", next(c)),
	"The Marshes Landkeeper Battle Near Spider Cave (-6,-1)": 
		CassetteBeastsLocationData("encounter_overworld_-6_-1_landkeeper1", "The Marshes", next(c)),
	"The Marshes Landkeeper Battle Near Office (-6,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-6_-3_landkeeper1", "The Marshes", next(c)),
	"The Marshes Lankeeper Battle Near West Mire Sea (-7,-2)": 
		CassetteBeastsLocationData("encounter_overworld_-7_-2_landkeeper", "The Marshes", next(c)),
	"Brokenhead Tamer Battle (-7,-7)": 
		CassetteBeastsLocationData("encounter_overworld_-7_-7_battler", "Brokenhead", next(c)),
	"Mourningtown Cultist Battle 1 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_1", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 2 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_2", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 3 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_3", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 4 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_4", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 5 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_5", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 6 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_6", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 7 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_7", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 8 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_8", "Mourningtown", next(c)),
	"Mourningtown Cultist Battle 9 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_9", "Mourningtown", next(c)),
	"Aldgrave Tomb Station Landkeeper Battle (-5,0)": 
		CassetteBeastsLocationData("encounter_dungeon_graveyard_landkeeper", "Aldgrave Tomb Station", next(c)),
	"Landkeeper Office 1 Battle (4,-1)": 
		CassetteBeastsLocationData("encounter_office_1", "Harbourtown Outskirts", next(c)),
	"Landkeeper Office 2 Battle (7,-3)": 
		CassetteBeastsLocationData("encounter_office_2", "Autumn Hill", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Landkeeper Office 3 Battle (7,-7)": 
		CassetteBeastsLocationData("encounter_office_3", "NE Mire Sea", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Landkeeper Office 4 Battle (1,-7)": 
		CassetteBeastsLocationData("encounter_office_4", "Eastham Woods Cliff", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
	"Landkeeper Office 5 Battle (-6,-3)": 
		CassetteBeastsLocationData("encounter_office_5", "The Marshes", next(c),
			lambda state, player: state.has("Progressive Glide", player) and state.has("Landkeeper Window Key", player)),
}
addLocationRequires(trainersanity_locations, lambda options: options.trainersanity)

tapesanity_locations = {
	f"Recorded {monster}":
	CassetteBeastsLocationData(f"record_{data.id}", "Menu", next(c), None,
		lambda options, f=data.requires: (not f or f(options)) and options.tapesanity == "specific")
	for monster, data in monsters().items()
}

tapesanity_percentage_locations = {
	f"Recorded {i+1} Monsters":
	CassetteBeastsLocationData(f"record_{i+1}", "Menu", next(c),
		lambda state, player, n=i+1: reachableMonsterCount(state, player) >= n,
		lambda options, n=i+1: n in percentageLocationNumbers(options, "tapesanity") and options.tapesanity == "percentage")
	for i in range(monsterCount(None))
}

bootlegsanity_per_tape_locations = {
	f"Recorded Bootleg {monster}":
	CassetteBeastsLocationData(f"record_bootleg_{data.id}", "Menu", next(c), None,
		lambda options, f=data.requires: (not f or f(options)) and options.bootlegsanity == "per_tape")
	for monster, data in monsters().items()
}

bootlegsanity_specific_locations = {
	f"Recorded {_type.capitalize()} Bootleg {monster}":
	CassetteBeastsLocationData(f"record_{_type}_{data.id}", "Menu", next(c), None,
		lambda options, f=data.requires: (not f or f(options)) and options.bootlegsanity == "specific")
	for monster, data in monsters().items() for _type in types
}

bootlegsanity_percentage_locations = {
	f"Recorded {i+1} Bootleg Monsters":
	CassetteBeastsLocationData(f"record_bootleg_{i+1}", "Menu", next(c),
		lambda state, player, n=i+1: reachableMonsterCount(state, player)*14 >= n,
		lambda options, n=i+1: n in percentageLocationNumbers(options, "bootlegsanity") and options.bootlegsanity in ["percentage_tape", "percentage_all"])
	for i in range(monsterCount()*14)
}

fusionsanity_locations = {
	f"Seen Some Fusions {i+1}":
	CassetteBeastsLocationData(f"seen_fusions_{i+1}", "Postgame", next(c), None,
		lambda options, n=i+1: n in percentageLocationNumbers(options, "fusionsanity") and options.fusionsanity)
	for i in range(1024)
}

event_data_table = {
	"Recruited Kayleigh": CassetteBeastsEventData("Harbourtown Station", "Recruited Kayleigh"),
	"Recruited Eugene": CassetteBeastsEventData("Harbourtown East", "Recruited Eugene"),
	"Recruited Meredith": CassetteBeastsEventData("Harbourtown East", "Recruited Meredith",
		lambda state, player: state.has("Met Meredith", player) and state.has("Envelope for Meredith", player)),
	"Recruited Felix": CassetteBeastsEventData("Lakeside", "Recruited Felix"),
	"Recruited Viola": CassetteBeastsEventData("The Marshes", "Recruited Viola"),
	"Recruited Barkley": CassetteBeastsEventData("Mt Wirral", "Recruited Barkley",
		lambda state, player: state.has("Progressive Climb", player)),
	"Defeated Oldgante": CassetteBeastsEventData("Harbourtown Station", "Defeated Oldgante"),
	"Defeated Poppetox": CassetteBeastsEventData("Glowcester Road Station", "Defeated Poppetox",
		lambda state, player: state.can_reach_location("Defeat Poppetox", player)),
	"Defeated Mourningstar": CassetteBeastsEventData("Mourningstar Crescent Station", "Defeated Mourningstar",
		lambda state, player: state.can_reach_location("Defeat Mourningstar", player)),
	"Defeated Nowhere Monarch": CassetteBeastsEventData("Falldown Mall", "Defeated Nowhere Monarch",
		lambda state, player: state.can_reach_location("Defeat Nowhere Monarch", player)),
	"Defeated Heckahedron": CassetteBeastsEventData("Waterloop Station", "Defeated Heckahedron",
		lambda state, player: state.can_reach_location("Defeat Heckahedron", player)),
	"Defeated Alice": CassetteBeastsEventData("Cherry Cross Station", "Defeated Alice",
		lambda state, player: state.can_reach_location("Defeat Alice", player)),
	"Defeated Robin Goodfellow": CassetteBeastsEventData("Bard Street Station", "Defeated Robin Goodfellow",
		lambda state, player: state.can_reach_location("Defeat Robin Goodfellow", player)),
	"Defeated Mammon": CassetteBeastsEventData("Landkeeper HQ", "Defeated Mammon",
		lambda state, player: state.can_reach_location("Defeat Mammon", player)),
	"Defeated Lamento Mori": CassetteBeastsEventData("Aldgrave Tomb Station", "Defeated Lamento Mori",
		lambda state, player: state.can_reach_location("Defeat Lamento Mori", player)),
	"Defeated Babelith": CassetteBeastsEventData("Icelington Station", "Defeated Babelith",
		lambda state, player: state.can_reach_location("Defeat Babelith", player)),
	"Defeated Shining Kuneko": CassetteBeastsEventData("Cherry Meadow", "Defeated Shining Kuneko",
		lambda state, player: state.can_reach_location("Defeat Shining Kuneko", player)),
	"Defeated Morgante": CassetteBeastsEventData("Postgame", "Defeated Morgante",
		lambda state, player: state.can_reach_location("Defeat Morgante", player)),
	"Defeated Helia": CassetteBeastsEventData("Postgame", "Defeated Helia",
		lambda state, player: state.can_reach_location("Defeat Helia", player)),
	"Defeated Lenna": CassetteBeastsEventData("Postgame", "Defeated Lenna",
		lambda state, player: state.can_reach_location("Defeat Lenna", player)),
	"Defeated Gwenivar": CassetteBeastsEventData("Brightside Pier", "Defeated Gwenivar",
		lambda state, player: state.can_reach_location("Defeat Gwenivar", player),
		lambda options: options.use_pier == True),
	"Defeated Averevoir": CassetteBeastsEventData("Mt Wirral", "Defeated Averevoir"),
	"Met Ianthe": CassetteBeastsEventData("New Wirral Park", "Met Ianthe"),
	"Met Meredith": CassetteBeastsEventData("New Wirral Park", "Met Meredith",
		lambda state, player: state.has("Progressive Glide", player)),
	"Cleared Landkeeper Offices": CassetteBeastsEventData("The Marshes", "Cleared Landkeeper Offices",
		lambda state, player: clearedOffices(state, player)),
	"Defeated Aleph": CassetteBeastsEventData("Night's Bridge Station", "Defeated Aleph"),# set in Rules.set_rules
	"Became Captain": CassetteBeastsEventData("Harbourtown East", "Became Captain",
		lambda state, player: state.can_reach_location("Beat Ianthe", player)),
	"Recruited Sunny": CassetteBeastsEventData("Mt Wirral", "Recruited Sunny",
		lambda state, player: state.has("Defeated Aleph", player) and state.has("Defeated Mammon", player)),
	"Quest People are People": CassetteBeastsEventData("New Landkeeper Hideout", "Quest People are People"),
}

location_data_table = base_locations|pier_locations|chest_loot_locations|shopsanity_locations|trainersanity_locations|tapesanity_locations|\
						tapesanity_percentage_locations|bootlegsanity_per_tape_locations|bootlegsanity_specific_locations|\
						bootlegsanity_percentage_locations|fusionsanity_locations

# monsters reference the location_data_table, so access rules must be created afterwards
for monster, data in monsters().items():
	rules = getMonsterRules(data, location_data_table)
	data = tapesanity_locations[f"Recorded {monster}"]
	tapesanity_locations[f"Recorded {monster}"] = CassetteBeastsLocationData(
		data.cb_name, data.region, data.address, lambda state, player, f=rules: f(state, player), data.requires)
	data = bootlegsanity_per_tape_locations[f"Recorded Bootleg {monster}"]
	bootlegsanity_per_tape_locations[f"Recorded Bootleg {monster}"] = CassetteBeastsLocationData(
		data.cb_name, data.region, data.address, lambda state, player, f=rules: f(state, player), data.requires)
	for _type in types:
		data = bootlegsanity_specific_locations[f"Recorded {_type.capitalize()} Bootleg {monster}"]
		bootlegsanity_specific_locations[f"Recorded {_type.capitalize()} Bootleg {monster}"] = CassetteBeastsLocationData(
			data.cb_name, data.region, data.address, lambda state, player, f=rules: f(state, player), data.requires)

location_data_table = base_locations|pier_locations|chest_loot_locations|shopsanity_locations|trainersanity_locations|tapesanity_locations|\
						tapesanity_percentage_locations|bootlegsanity_per_tape_locations|bootlegsanity_specific_locations|\
						bootlegsanity_percentage_locations|fusionsanity_locations

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}

def getLocationCount(options, subset=[]) -> int:
	res = 0
	if subset == []:
		locations = location_data_table
	else:
		locations = {k: v for k, v in s.items() for s in locals() if s in subset}

	for location in locations.values():
		if location.requires == None or location.requires(options):
			res += 1

	return res

def hasAllStamps(state, player) -> bool:
	return state.has("Captain Wallace Stamp",        player) and\
		   state.has("Captain Skip Stamp",           player) and\
		   state.has("Captain Zedd Stamp",           player) and\
		   state.has("Captain Judas Stamp",          player) and\
		   state.has("Captain Clee-o Stamp",         player) and\
		   state.has("Captain Lodestein Stamp",      player) and\
		   state.has("Captain Penny Dreadful Stamp", player) and\
		   state.has("Captain Gladiola Stamp",       player) and\
		   state.has("Captain Heather Stamp",        player) and\
		   state.has("Captain Buffy Stamp",          player) and\
		   state.has("Captain Cybil Stamp",          player) and\
		   state.has("Captain Codey Stamp",          player)

def clearedOffices(state, player) -> bool:
	return state.can_reach_location("Landkeeper Office 1 Cabinet (4,-1)",    player) and\
		   state.can_reach_location("Landkeeper Office 2 Cabinet (7,-3)",    player) and\
		   state.can_reach_location("Landkeeper Office 3 Cabinet (7,-7)",    player) and\
		   state.can_reach_location("Landkeeper Office 4 Cabinet (1,-7)",    player) and\
		   state.can_reach_location("Landkeeper Office 5 Cabinet (-6,-3)",   player)

def reachableMonsterCount(state, player, options=None) -> int:
	res = 0
	for monster in monsters(options).keys():
		try:
			if state.can_reach_location(f"Recorded {monster}", player):
				res += 1
		except:
			if state.has(f"Recorded {monster}", player):
				res += 1
	return res

def percentageLocationNumbers(options, option) -> list[int]:
	if option == "tapesanity":
		loc_count = options.tapesanity_percentage_item_count
		last_loc  = ceil(options.tapesanity_percentage_item_count.range_end*(options.tapesanity_percentage/100))
		return [int(i*last_loc/loc_count) for i in range(1,loc_count+1)]
	if option == "bootlegsanity":
		loc_count = options.bootlegsanity_percentage_item_count
		mon_count = monsterCount(options)
		if options.bootlegsanity == "percentage_all":
			mon_count *= 14
		last_loc  = ceil(mon_count*(options.bootlegsanity_percentage/100))
		return [int(i*last_loc/loc_count) for i in range(1,loc_count+1)]
	if option == "fusionsanity":
		return [i for i in range(1, options.fusionsanity_item_count+1)]
