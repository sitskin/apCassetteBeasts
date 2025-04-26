from math import ceil
from typing import NamedTuple, Optional

from BaseClasses import Location

from .Data.tape_data import types, monsters, monsterCount

CB_BASE_ID = 1

class CassetteBeastsLocation(Location):
	game = "Cassette Beasts"

class CassetteBeastsLocationData(NamedTuple):
	cb_name: str
	region: str
	address: Optional[int] = None

class CassetteBeastsEventData(NamedTuple):
	region: str
	item: str
	dlc: Optional[str] = None


base_locations = {
	"Defeat Oldgante": 
		CassetteBeastsLocationData("ap_encounter_aa_oldgante", "Harbourtown Station", CB_BASE_ID+0),
	"Defeat Poppetox": 
		CassetteBeastsLocationData("ap_encounter_aa_puppet", "Glowcester Road Station", CB_BASE_ID+1),
	"Defeat Mourningstar": 
		CassetteBeastsLocationData("ap_encounter_aa_mourningstar", "Mourningstar Crescent Station", CB_BASE_ID+2),
	"Defeat Nowhere Monarch": 
		CassetteBeastsLocationData("ap_encounter_aa_monarch", "Falldown Mall", CB_BASE_ID+3),
	"Defeat Heckahedron": 
		CassetteBeastsLocationData("ap_encounter_aa_cube", "Waterloop Station", CB_BASE_ID+4),
	"Defeat Alice": 
		CassetteBeastsLocationData("ap_encounter_aa_alice", "Cherry Cross Station", CB_BASE_ID+5),
	"Defeat Robin Goodfellow": 
		CassetteBeastsLocationData("ap_encounter_aa_robin", "Bard Street Station", CB_BASE_ID+6),
	"Defeat Mammon": 
		CassetteBeastsLocationData("ap_encounter_aa_mammon", "Landkeeper HQ", CB_BASE_ID+7),
	"Defeat Lamento Mori": 
		CassetteBeastsLocationData("ap_encounter_aa_lamento_mori", "Aldgrave Tomb Station", CB_BASE_ID+8),
	"Defeat Babelith": 
		CassetteBeastsLocationData("ap_encounter_aa_tower", "Icelington Station", CB_BASE_ID+9),
	"Defeat Shining Kuneko": 
		CassetteBeastsLocationData("ap_encounter_aa_kuneko", "Cherry Meadow", CB_BASE_ID+10),
	"Beat Wallace": 
		CassetteBeastsLocationData("encounter_captain_wallace", "New Wirral Park", CB_BASE_ID+11),
	"Beat Skip": 
		CassetteBeastsLocationData("encounter_captain_skip", "Harbourtown West", CB_BASE_ID+12),
	"Beat Zedd": 
		CassetteBeastsLocationData("encounter_captain_zedd", "Autumn Hill", CB_BASE_ID+13),
	"Beat Judas": 
		CassetteBeastsLocationData("encounter_captain_judas", "Southern Isles", CB_BASE_ID+14),
	"Beat Clee-o": 
		CassetteBeastsLocationData("encounter_captain_cleeo", "Eastham Woods", CB_BASE_ID+15),
	"Beat Lodestein": 
		CassetteBeastsLocationData("encounter_captain_lodestein", "Ham", CB_BASE_ID+16),
	"Beat Penny Dreadful": 
		CassetteBeastsLocationData("encounter_captain_dreadful", "New London", CB_BASE_ID+17),
	"Beat Gladiola": 
		CassetteBeastsLocationData("encounter_captain_gladiola", "West Mire Sea", CB_BASE_ID+18),
	"Beat Heather": 
		CassetteBeastsLocationData("encounter_captain_heather", "West Mire Sea", CB_BASE_ID+19),
	"Beat Buffy": 
		CassetteBeastsLocationData("encounter_captain_buffy", "Cherry Meadow", CB_BASE_ID+20),
	"Beat Cybil": 
		CassetteBeastsLocationData("encounter_captain_cybil", "The Marshes", CB_BASE_ID+21),
	"Beat Codey": 
		CassetteBeastsLocationData("encounter_captain_codey", "Mt Wirral", CB_BASE_ID+22),
	"Beat Ianthe": 
		CassetteBeastsLocationData("encounter_ianthe", "New Wirral Park", CB_BASE_ID+23),
	"Harbourtown Chest under Crate on Flour Mill (0,-1)": 
		CassetteBeastsLocationData("OVERWORLD_0_-1_CHEST", "Harbourtown East", CB_BASE_ID+24),
	"Upper Path Magnet Platform Chest (0,-2)": 
		CassetteBeastsLocationData("overworld_0_-2_chest", "Upper Path", CB_BASE_ID+25),
	"Thirstaton Lake Underwater Chest (0,-3)": 
		CassetteBeastsLocationData("overworld_0_-3_chest", "Thirstaton Lake", CB_BASE_ID+26),
	"Eastham Woods Lift Rock Chest (0,-6)": 
		CassetteBeastsLocationData("chest_overworld_0_-6", "Eastham Woods", CB_BASE_ID+27),
	"Eastham Woods Chest Near Ham (0,-7)": 
		CassetteBeastsLocationData("chest_overworld_0_-7", "Eastham Woods", CB_BASE_ID+28),
	"Harbourtown Chest on Top of House (1,-1)": 
		CassetteBeastsLocationData("overworld_1_-1_chest", "Harbourtown East", CB_BASE_ID+29),
	"Eastham Woods Three Lights Chest (1,-6)": 
		CassetteBeastsLocationData("chest_overworld_1_-6", "Eastham Woods", CB_BASE_ID+30),
	"Harbourtown Outskirts Break Rock Chest (2,-2)": 
		CassetteBeastsLocationData("overworld_2_-2_rock_chest", "Harbourtown Outskirts", CB_BASE_ID+31),
	"New Wirral Park Chest Under Bridge by Lake (2,-3)": 
		CassetteBeastsLocationData("chest_overworld_2_-3", "New Wirral Park", CB_BASE_ID+32),
	"New Wirral Park Chest Lift Box in Pond (3,-3)": 
		CassetteBeastsLocationData("chest_overworld_3_-3", "New Wirral Park", CB_BASE_ID+33),
	"New Wirral Park Chest Behind Ranger Station (2,-4)": 
		CassetteBeastsLocationData("chest_overworld_2_-4", "New Wirral Park", CB_BASE_ID+34),
	"Eastham Woods Magnet Button Chest (2,-6)": 
		CassetteBeastsLocationData("overworld_2_-6_chest", "Eastham Woods", CB_BASE_ID+35),
	"Harbourtown Beach Chest (3,0)": 
		CassetteBeastsLocationData("chest_overworld_3_0", "Harbourtown Beach", CB_BASE_ID+36),
	"Harbourtown Outskirts Chest Near Lamppost (3,-2)": 
		CassetteBeastsLocationData("chest_overworld_3_-2", "Harbourtown Outskirts", CB_BASE_ID+37),
	"Eastham Woods Chest on Cliff Below Mall (3,-7)": 
		CassetteBeastsLocationData("chest_overworld_3_-7", "Eastham Woods", CB_BASE_ID+38),
	"Eastham Woods Chest on Mall Roof (3,-7)": 
		CassetteBeastsLocationData("chest_overworld_3_-7_mall_roof", "Eastham Woods Cliff", CB_BASE_ID+39),
	"Deadlands Floor Button Chest (4,-2)": 
		CassetteBeastsLocationData("chest_overworld_4_-2", "Deadlands", CB_BASE_ID+40),
	"New Wirral Park Break Rock Chest in Wall (4,-5)": 
		CassetteBeastsLocationData("overworld_4_-5_chest1", "New Wirral Park", CB_BASE_ID+41),
	"Eastham Woods Levitator Magnet Chest (4,-6)": 
		CassetteBeastsLocationData("chest_overworld_4_-6", "Eastham Woods", CB_BASE_ID+42),
	"Eastham Woods Four Button Chest (4,-7)": 
		CassetteBeastsLocationData("chest_overworld_4_-7", "Eastham Woods", CB_BASE_ID+43),
	"Deadlands Coast Button Chest (5,-1)": 
		CassetteBeastsLocationData("overworld_5_-1_chest", "Deadlands Coast", CB_BASE_ID+44),
	"New London Three Button Chest (5,-2)": 
		CassetteBeastsLocationData("overworld_5_-2_chest", "New London", CB_BASE_ID+45),
	"New Wirral Park Lower Platform Chest (5,-3)": 
		CassetteBeastsLocationData("chest_overworld_5_-3", "New Wirral Park", CB_BASE_ID+46),
	"Eastham Woods Chest in Pond (5,-5)": 
		CassetteBeastsLocationData("chest_overworld_5_-5", "Eastham Woods", CB_BASE_ID+47),
	"Eastham Woods Levitator Magnet Lever Chest (5,-7)": 
		CassetteBeastsLocationData("chest_overworld_5_-7", "Eastham Woods", CB_BASE_ID+48),
	"Southern Isles Chest Washed Up on Island (6,0)": 
		CassetteBeastsLocationData("overworld_6_0_chest", "Southern Isles", CB_BASE_ID+49),
	"New London Chest in House (6,-2)": 
		CassetteBeastsLocationData("overworld_6_-2_chest", "New London", CB_BASE_ID+50),
	"Deadlands Coast Gust Chest (6,-2)": 
		CassetteBeastsLocationData("overworld_6_-2_chest_2", "Deadlands Coast", CB_BASE_ID+51),
	"Autumn Hill Lever Chest in Lake (6,-3)": 
		CassetteBeastsLocationData("chest_overworld_6_-3", "Autumn Hill", CB_BASE_ID+52),
	"Autumn Hill Chest with Button in Eastham Woods (6,-5)": 
		CassetteBeastsLocationData("chest_overworld_6_-5", "Autumn Hill", CB_BASE_ID+53),
	"Southern Isles Underwater Chest (7,0)": 
		CassetteBeastsLocationData("overworld_7_0_chest", "Southern Isles", CB_BASE_ID+54),
	"Deadlands Coast Lift Rock Chest (7,-1)": 
		CassetteBeastsLocationData("overworld_7_-1_chest", "Deadlands Coast", CB_BASE_ID+55),
	"New London Statue Puzzle Chest (7,-2)": 
		CassetteBeastsLocationData("overworld_7_-2_chest_1", "New London", CB_BASE_ID+56),
	"New London 2 Button Chest (7,-2)": 
		CassetteBeastsLocationData("overworld_7_-2_chest_2", "New London", CB_BASE_ID+57),
	"Autumn Hill Shortcut Chest (7,-3)": 
		CassetteBeastsLocationData("chest_overworld_7_-3", "Autumn Hill", CB_BASE_ID+58),
	"Autumn Hill Peak Break Rock Chest (7,-4)": 
		CassetteBeastsLocationData("chest_overworld_7_-4", "Autumn Hill", CB_BASE_ID+59),
	"Deadlands Coast Chest Near Dino Quarry (8,-1)": 
		CassetteBeastsLocationData("overworld_8_-1_chest_1", "Deadlands Coast", CB_BASE_ID+60),
	"Deadlands Coast Place Two Rocks Chest (8,-1)": 
		CassetteBeastsLocationData("overworld_8_-1_chest_2", "Deadlands Coast", CB_BASE_ID+61),
	"Autumn Hill Button Chest (8,-3)": 
		CassetteBeastsLocationData("chest_overworld_8_-3", "Autumn Hill", CB_BASE_ID+62),
	"Autumn Hill Elevator Chest (8,-5)": 
		CassetteBeastsLocationData("chest_overworld_8_-5", "Autumn Hill", CB_BASE_ID+63),
	"Autumn Hill Underwater Chest (8,-6)": 
		CassetteBeastsLocationData("chest_overworld_8_-6", "Autumn Hill", CB_BASE_ID+64),
	"NE Mire Sea Chest (8,-7)": 
		CassetteBeastsLocationData("chest_overworld_8_-7", "NE Mire Sea", CB_BASE_ID+65),
	"Upper Path Chest on Wall Before Harbourtown West (-1, -2)": 
		CassetteBeastsLocationData("chest_overworld_-1_-2", "Upper Path", CB_BASE_ID+66),
	"Lakeside Chest by Waterfall (-1,-6)": 
		CassetteBeastsLocationData("overworld_-1_-6_chest_1", "Lakeside", CB_BASE_ID+67),
	"Lakeside Four Button Chest Near Ham (-1,-6)": 
		CassetteBeastsLocationData("overworld_-1_-6_chest_2", "Lakeside", CB_BASE_ID+68),
	"Ham Chest Near Mt Wirral (-1,-7)": 
		CassetteBeastsLocationData("overworld_-1_-7_chest_1", "Ham", CB_BASE_ID+69),
	"Ham Chest Fall from Mt Wirral (-1,-7)": 
		CassetteBeastsLocationData("overworld_-1_-7_chest_2", "Ham", CB_BASE_ID+70),
	"Thirstaton Lake Statue Puzzle Chest (-2,-3)": 
		CassetteBeastsLocationData("overworld_-2_-3_chest", "Thirstaton Lake", CB_BASE_ID+71),
	"Cherry Meadow Chest Over Thirstaton Lake (-2,-3)": 
		CassetteBeastsLocationData("overworld_-2_-3_chest_2", "Cherry Meadow", CB_BASE_ID+72),
	"Thirstaton Lake Chest in Wall (-2,-5)": 
		CassetteBeastsLocationData("overworld_-2_-5_chest", "Thirstaton Lake", CB_BASE_ID+73),
	"Mt Wirral Lower Platform with Button Chest (-2,-6)": 
		CassetteBeastsLocationData("overworld_-2_-6_chest", "Mt Wirral", CB_BASE_ID+74),
	"Behind Mt Wirral Chest (-2,-7)": 
		CassetteBeastsLocationData("overworld_2_-7_chest_1", "Ham", CB_BASE_ID+75),
	"East of Graveyard Lever Chest (-3,0)": 
		CassetteBeastsLocationData("chest_overworld_-3_0", "Lost Hearts Graveyard", CB_BASE_ID+76),
	"Piper Farm Chest (-3,-1)": 
		CassetteBeastsLocationData("chest_overworld_-3_-1_a", "Piper Farm", CB_BASE_ID+77),
	"Piper Farm Climb Chest (-3,-1)": 
		CassetteBeastsLocationData("chest_overworld_-3_-1_b", "Piper Farm", CB_BASE_ID+78),
	"Marshes Lift Crate in Cherry Meadow Chest (-3,-3)": 
		CassetteBeastsLocationData("chest_overworld_-3_-3", "The Marshes", CB_BASE_ID+79),
	"Cherry Meadow Chest Near Captain Buffy (-3,-5)": 
		CassetteBeastsLocationData("chest_overworld_-3_-5", "Cherry Meadow", CB_BASE_ID+80),
	"Mt Wirral Chest Above Big Entrance (-3,-6)": 
		CassetteBeastsLocationData("chest_overworld_-3_-6", "Mt Wirral", CB_BASE_ID+81),
	"Mt Wirral Chest at River Source (-3,-7)": 
		CassetteBeastsLocationData("chest_overworld_-3_-7", "Mt Wirral", CB_BASE_ID+82),
	"Graveyard Chest in Puddle (-4,0)": 
		CassetteBeastsLocationData("chest_overworld_-4_0", "Lost Hearts Graveyard", CB_BASE_ID+83),
	"Marshes 4 Rocks in a Line Chest (-4,-3)": 
		CassetteBeastsLocationData("chest_overworld_-4_-3", "The Marshes", CB_BASE_ID+84),
	"Mt Wirral Elevator Chest (-4,-6)": 
		CassetteBeastsLocationData("chest_overworld_-4_-6", "Mt Wirral", CB_BASE_ID+85),
	"Marshes Chest Near Landkeeper Office (-5,-3)": 
		CassetteBeastsLocationData("chest_overworld_-5_-3", "The Marshes", CB_BASE_ID+86),
	"Cherry Meadow Button Chest (-5,-4)": 
		CassetteBeastsLocationData("overworld_-5_-4_chest", "Cherry Meadow", CB_BASE_ID+87),
	"Mt Wirral Base Chest Near Cast Iron Shore (-5,-6)": 
		CassetteBeastsLocationData("chest_overworld_-5_-6_a", "Mt Wirral", CB_BASE_ID+88),
	"Mt Wirral Button Chest (-5,-6)": 
		CassetteBeastsLocationData("chest_overworld_-5_-6_b", "Mt Wirral", CB_BASE_ID+89),
	"Mt Wirral Chest Near Brokenhead (-5,-7)": 
		CassetteBeastsLocationData("chest_overworld_-5_-7", "Mt Wirral", CB_BASE_ID+90),
	"Marshes Coast Button Chest (-6,-1)": 
		CassetteBeastsLocationData("chest_overworld_-6_-1", "The Marshes", CB_BASE_ID+91),
	"Marshes Three Underwater Buttons Chest (-6,-2)": 
		CassetteBeastsLocationData("chest_overworld_-6_-2", "The Marshes", CB_BASE_ID+92),
	"Cast Iron Shore Magnet Button Chest (-6,-4)": 
		CassetteBeastsLocationData("chest_overworld_-6_-4", "Cast Iron Shore", CB_BASE_ID+93),
	"Cast Iron Shore Two Magnet Button Chest (-6,-5)": 
		CassetteBeastsLocationData("chest_overworld_-6_-5", "Cast Iron Shore", CB_BASE_ID+94),
	"West Mire Sea Chest Near Captain Gladiola (-7,0)": 
		CassetteBeastsLocationData("chest_overworld_-7_0", "West Mire Sea", CB_BASE_ID+95),# missing chest on titania smokestack?
	"West Mire Sea Button Chest on Pillar (-7,-3)": 
		CassetteBeastsLocationData("chest_overworld_-7_-3", "West Mire Sea", CB_BASE_ID+96),
	"Brokenhead Chest on Henge (-7,-7)": 
		CassetteBeastsLocationData("chest_overworld_-7_-7_a", "Brokenhead", CB_BASE_ID+97),
	"Brokenhead Chest Under Henge (-7,-7)": 
		CassetteBeastsLocationData("chest_overworld_-7_-7_b", "Brokenhead", CB_BASE_ID+98),
	"Autumn Gate Cave Chest (6,-4)": 
		CassetteBeastsLocationData("chest_autumn_hill_gate_autumn_cave_1", "Autumn Hill", CB_BASE_ID+99),
	"Averevoir Cave Chest (-3,-6)": 
		CassetteBeastsLocationData("chest_cave_averevoir", "Mt Wirral", CB_BASE_ID+100),
	"Deadlands Cave Chest (6,-1)": 
		CassetteBeastsLocationData("cave_deadlands_1_chest", "Deadlands Coast", CB_BASE_ID+101),
	"Deadlands Cave Break Rock Chest (6,-2)": 
		CassetteBeastsLocationData("cave_deadlands_3_chest", "Deadlands Coast", CB_BASE_ID+102),
	"Autumn Hill Gear Cave Chest (7,-6)": 
		CassetteBeastsLocationData("chest_autumn_hill_gear_cave", "Autumn Hill", CB_BASE_ID+103),
	"Lake Cave Chest (-1,-2)": 
		CassetteBeastsLocationData("cave_lake_1_chest", "Thirstaton Lake", CB_BASE_ID+104),
	"Marsh Cave Chest (-5,-1)": 
		CassetteBeastsLocationData("cave_marsh_1_chest", "The Marshes", CB_BASE_ID+105),
	"Marsh Cave Chest (-7,-1)": 
		CassetteBeastsLocationData("cave_marsh_2_chest", "The Marshes", CB_BASE_ID+106),
	"Cherry Meadow Cave Chest (-4,-6)": 
		CassetteBeastsLocationData("chest_cave_meadow_1", "Cherry Meadow", CB_BASE_ID+107),
	"Mt Wirral Waterfall Cave Chest (-2,-7)": 
		CassetteBeastsLocationData("cave_mt_wirral_1_chest", "Mt Wirral", CB_BASE_ID+108),
	"Mt Wirral Cave Bridge Chest (-3,-7)": 
		CassetteBeastsLocationData("cave_mt_wirral_2_chest", "Mt Wirral", CB_BASE_ID+109),
	"Harbourtown Outskirts Pipe Chest (1,-1)": 
		CassetteBeastsLocationData("cave_outskirts_pipe_chest", "Harbourtown Outskirts", CB_BASE_ID+110),
	"New Wirral Park Track Cave Chest(3,-5)": 
		CassetteBeastsLocationData("cave_new_wirral_park_1_chest", "New Wirral Park", CB_BASE_ID+111),
	"New Wirral Park Cave Chest (4,-3)": 
		CassetteBeastsLocationData("chest_parkcave2_1", "New Wirral Park", CB_BASE_ID+112),
	"New Wirral Park Cave Break Rock Chest (4,-3)": 
		CassetteBeastsLocationData("chest_parkcave2_2", "New Wirral Park", CB_BASE_ID+113),
	"New Wirral Park Under Ranger Station Cave Chest (2,-4)": 
		CassetteBeastsLocationData("chest_parkcave3_1", "New Wirral Park", CB_BASE_ID+114),
	"Thirsaton Lake Waterfall Cave Chest (-1,-5)": 
		CassetteBeastsLocationData("cave_lakeside_2_chest", "Thirstaton Lake", CB_BASE_ID+115),
	"Spider Cave Chest (-6,-1)": 
		CassetteBeastsLocationData("spider_cave_3_chest_1", "Spider Cave", CB_BASE_ID+116),
	"Eastham Woods Cave Chest (2,-6)": 
		CassetteBeastsLocationData("chest_woods_cave_1", "Eastham Woods", CB_BASE_ID+117),
	"Mourningtown Chest (7,-5)": 
		CassetteBeastsLocationData("chest_commune_key_rusted", "Mourningtown", CB_BASE_ID+118),
	"Glowcester Road Station Cave Chest (5,-4)": 
		CassetteBeastsLocationData("dungeon_glowshroom_cave2_chest", "Glowcester Road Station", CB_BASE_ID+119),
	"Falldown Mall Bookshop Chest (3,-7)": 
		CassetteBeastsLocationData("mall_chest_bookshop", "Falldown Mall", CB_BASE_ID+120),
	"Falldown Mall Empty Shop Chest (3,-7)": 
		CassetteBeastsLocationData("mall_empty_shop_chest", "Falldown Mall", CB_BASE_ID+121),
	"Falldown Mall Crate Room Chest (3,-7)": 
		CassetteBeastsLocationData("mall_shop_miscshop_chest", "Falldown Mall", CB_BASE_ID+122),
	"Cherry Cross Station Giant Chest (-4,-4)": 
		CassetteBeastsLocationData("chest_dungeon_meadow_garden", "Cherry Cross Station", CB_BASE_ID+123),
	"Cherry Cross Station Tiny Chest (-4,-4)": 
		CassetteBeastsLocationData("chest_dungeon_meadow_room2", "Cherry Cross Station", CB_BASE_ID+124),
	"Icelington Station Chest (-3,-7)": 
		CassetteBeastsLocationData("chest_station_mountain_entrance", "Icelington Station", CB_BASE_ID+125),
	"Titania Shipwreck Valve 1 (-6,-6)": 
		CassetteBeastsLocationData("shipwreck_valve_1", "Titania Shipwreck", CB_BASE_ID+126),
	"Titania Shipwreck Valve 2 (-6,-6)": 
		CassetteBeastsLocationData("shipwreck_valve_2", "Titania Shipwreck", CB_BASE_ID+127),
	"Titania Shipwreck Chest (-6,-6)": 
		CassetteBeastsLocationData("shipwreck_chest_1", "Titania Shipwreck", CB_BASE_ID+128),
	"Waterloop Station Break Polyhedron Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_optional_dash_reward", "Waterloop Station", CB_BASE_ID+129),
	"Waterloop Station Statues Off Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_switch_grid_off", "Waterloop Station", CB_BASE_ID+130),
	"Waterloop Station Statues On Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_switch_grid_on", "Waterloop Station", CB_BASE_ID+131),
	"Waterloop Station Lying Chest (1,-4)": 
		CassetteBeastsLocationData("chest_waterloop_lying_right", "Waterloop Station", CB_BASE_ID+132),
	"Harbourtown Apartment Chest (-1,0)": 
		CassetteBeastsLocationData("harbourtown_apartment3_chest", "Harbourtown West", CB_BASE_ID+133),
	"Harbourtown Red House Fridge (-1,0)": 
		CassetteBeastsLocationData("HouseWest3_fridge", "Harbourtown West", CB_BASE_ID+134),
	"Harbourtown Kayliegh's Home Chest (1,0)": 
		CassetteBeastsLocationData("chest_kayleigh_home", "Harbourtown East", CB_BASE_ID+135),
	"Harbourtown Town Hall Cabinet (0,0)": 
		CassetteBeastsLocationData("cabinet_town_hall", "Harbourtown East", CB_BASE_ID+136),
	"Landkeeper Office 1 Cabinet (4,-1)": 
		CassetteBeastsLocationData("chest_office1", "Harbourtown Outskirts", CB_BASE_ID+137),
	"Landkeeper Office 2 Cabinet (7,-3)": 
		CassetteBeastsLocationData("chest_office2", "Autumn Hill", CB_BASE_ID+138),
	"Landkeeper Office 3 Cabinet (7,-7)": 
		CassetteBeastsLocationData("chest_office3", "NE Mire Sea", CB_BASE_ID+139),
	"Landkeeper Office 4 Cabinet (1,-7)": 
		CassetteBeastsLocationData("chest_office4", "Eastham Woods Cliff", CB_BASE_ID+140),
	"Landkeeper Office 5 Cabinet (-6,-3)": 
		CassetteBeastsLocationData("chest_office5", "The Marshes", CB_BASE_ID+141),
	"Harbourtown Station Chest (1,-2)": 
		CassetteBeastsLocationData("harbourtown_station_chest1", "Harbourtown Station", CB_BASE_ID+142),
	"Night's Bridge Station Clockhands Chest (?,?)": 
		CassetteBeastsLocationData("room_1A_chest_1", "Night's Bridge Station", CB_BASE_ID+143),
	"Night's Bridge Station Right Azure Keystone Chest (?/?)": 
		CassetteBeastsLocationData("room_1A_chest_2", "Night's Bridge Station", CB_BASE_ID+144),
	"Night's Bridge Station Left Azure Keystone Chest (?/?)": 
		CassetteBeastsLocationData("room_2A_chest_1", "Night's Bridge Station", CB_BASE_ID+145),
	"Titania Shipwreck Chest on Chimney (-6,-6)":
		CassetteBeastsLocationData("chest_shipyard_ship_chimney", "Cast Iron Shore", CB_BASE_ID+146),
	"Ranger Handbook":
		CassetteBeastsLocationData("Ranger Handbook", "Harbourtown East", CB_BASE_ID+147),
	"Type Chart":
		CassetteBeastsLocationData("Type Chart", "Menu", CB_BASE_ID+148),
	"Harbourtown Gate Key":
		CassetteBeastsLocationData("Harbourtown Gate Key", "Harbourtown Beach", CB_BASE_ID+149),
	"Train Ticket (Glowcester)":
		CassetteBeastsLocationData("Train Ticket (Glowcester)", "Glowcester Road Station", CB_BASE_ID+150),
	"Train Ticket (Aldgrave Tomb)":
		CassetteBeastsLocationData("Train Ticket (Aldgrave Tomb)", "Aldgrave Tomb Station", CB_BASE_ID+151),
	"Captain Clee-o Coin":
		CassetteBeastsLocationData("Captain Clee-o Coin", "Eastham Woods", CB_BASE_ID+152),
	"Envelope for Meredith":
		CassetteBeastsLocationData("Envelope for Meredith", "Harbourtown East", CB_BASE_ID+153),
	"Landkeeper Key":
		CassetteBeastsLocationData("Landkeeper Key", "Harbourtown Outskirts", CB_BASE_ID+154),
	"Landkeeper Secret Hideout Button Chest (-4,-1)":
		CassetteBeastsLocationData("dungeon_landkeeper_secret_chest_1", "New Landkeeper Hideout", CB_BASE_ID+155),
	"Landkeeper Secret Hideout Pillar Chest (-4,-1)":
		CassetteBeastsLocationData("dungeon_landkeeper_secret_chest_2", "New Landkeeper Hideout", CB_BASE_ID+156),
	"Defeat Morgante": 
		CassetteBeastsLocationData("ap_encounter_aa_morgante", "Postgame", CB_BASE_ID+157),
	"Defeat Helia": 
		CassetteBeastsLocationData("ap_encounter_aa_helia", "Postgame", CB_BASE_ID+158),
	"Defeat Lenna": 
		CassetteBeastsLocationData("ap_encounter_aa_lenna", "Postgame", CB_BASE_ID+159),
}

id_off = len(base_locations)
pier_locations = {
	"Defeat Gwenivar": 
		CassetteBeastsLocationData("ap_encounter_aa_clown", "Brightside Pier", CB_BASE_ID+0),
}

id_off += len(pier_locations)
chest_loot_locations = {
	loc.replace("Chest", "Chest Loot"): CassetteBeastsLocationData("loot_"+data.cb_name, data.region, -1)\
	for loc, data in (base_locations|pier_locations).items() if "Chest" in loc
}
for i, loc in enumerate(chest_loot_locations.keys()):
	data = chest_loot_locations[loc]
	chest_loot_locations[loc] = CassetteBeastsLocationData(data.cb_name, data.region, id_off+i)

id_off += len(chest_loot_locations)
shopsanity_locations = {
	
}

id_off += len(shopsanity_locations)
trainersanity_locations = {
	"Thirstaton Lake Traveler Battle (0,-4)": 
		CassetteBeastsLocationData("encounter_overworld_0_-4_battler", "Thirstaton Lake", id_off+0),
	"Lakeside Camper Battle (0,-5)": 
		CassetteBeastsLocationData("encounter_overworld_0_-5_battler", "Lakeside", id_off+1),
	"Diogenes Battle (0,-5)": 
		CassetteBeastsLocationData("encounter_overworld_0_-5_battler_diogenes", "Lakeside", id_off+2),
	"Eastham Woods Soldier Battle Near Ham (0,-6)": 
		CassetteBeastsLocationData("encounter_overworld_0_-6_battler", "Eastham Woods", id_off+3),
	"Thirstaton Lake Researcher Battle (1,-4)": 
		CassetteBeastsLocationData("encounter_overworld_1_-4_battler", "Thirstaton Lake", id_off+4),
	"Lakeside Traveler Battle (1,-5)": 
		CassetteBeastsLocationData("encounter_overworld_1_-5_battler", "Lakeside", id_off+5),
	"Decartes Battle (1,-6)": 
		CassetteBeastsLocationData("encounter_overworld_1_-6_battler_decartes", "Eastham Woods", id_off+6),
	"Eastham Landkeeper Battle 1 (1,-7)": 
		CassetteBeastsLocationData("encounter_overworld_1_-7_landkeeper", "Eastham Woods Cliff", id_off+7),
	"Eastham Landkeeper Battle 2 (1,-7)": 
		CassetteBeastsLocationData("encounter_overworld_1_-7_landkeeper2", "Eastham Woods Cliff", id_off+8),
	"Ranger Wannabe Battle Near Ranger Station (2,-4)": 
		CassetteBeastsLocationData("encounter_nwp_ranger_wannabe_2_-4", "New Wirral Park", id_off+9),
	"Ranger Recruiter Battle Near Ranger Station (2,-4)": 
		CassetteBeastsLocationData("encounter_nwp_ranger_recruiter_2_-4", "New Wirral Park", id_off+10),
	"New Wirral Park Ranger Battle (2,-5)": 
		CassetteBeastsLocationData("encounter_overworld_2_-5_ranger", "New Wirral Park", id_off+11),
	"Eastham Landkeeper Battle 3 (2,-7)": 
		CassetteBeastsLocationData("encounter_overworld_2_-7_landkeeper", "Eastham Woods Cliff", id_off+12),
	"New Wirral Park Landkeeper Battle (3,-4)": 
		CassetteBeastsLocationData("encounter_overworld_3_-4_landkeeper", "New Wirral Park", id_off+13),
	"New Wirral Park Ranger Wannabe Duo Battle (3,-4)": 
		CassetteBeastsLocationData("encounter_overworld_3_-4_wannabe", "New Wirral Park", id_off+14),
	"New Wirral Park Madman Battle (3,-4)": 
		CassetteBeastsLocationData("encounter_overworld_3_-4_madman", "New Wirral Park", id_off+15),# has unique name? NWP_MADMAN_3_-4_NAME
	"New Wirral Park Rocker Battle (3,-5)": 
		CassetteBeastsLocationData("encounter_overworld_3_-5_battler", "New Wirral Park", id_off+16),
	"Eastham Woods Cultist Battle (3,-6)": 
		CassetteBeastsLocationData("encounter_overworld_3_-6_cultist", "Eastham Woods", id_off+17),
	"Treasure Seeker Battle Near Mall (3,-7)": 
		CassetteBeastsLocationData("encounter_overworld_3_-7_battler", "Eastham Woods Cliff", id_off+18),
	"New Wirral Park Ranger Wannabe Battle (4,-3)": 
		CassetteBeastsLocationData("encounter_overworld_4_-3_wannabe", "New Wirral Park", id_off+19),
	"New Wirral Park Cultist Battle 1 (4,-4)": 
		CassetteBeastsLocationData("encounter_nwp_4_-4_cultist", "New Wirral Park", id_off+20),
	"New Wirral Park Battle (4,-5)": 
		CassetteBeastsLocationData("encounter_overworld_4_-5_battler", "New Wirral Park", id_off+21),# has unique name? OVERWORLD_4_-5_BATTLER_NAME
	"Aristotle Battle (4,-6)": 
		CassetteBeastsLocationData("encounter_overworld_4_-6_battler_aristotle", "Eastham Woods", id_off+22),
	"Eastham Woods Landkeeper Battle 4 (4,-7)": 
		CassetteBeastsLocationData("encounter_overworld_4_-7_landkeeper", "Eastham Woods", id_off+23),
	"Southern Isles Traveler Battle (5,0)": 
		CassetteBeastsLocationData("encounter_overworld_5_0_battler", "Southern Isles", id_off+24),
	"Deadlands Coast Treasure Seeker Battle (5,-1)": 
		CassetteBeastsLocationData("encounter_overworld_5_-1_battler", "Deadlands Coast", id_off+25),
	"Deadlands Ranger Trainee Battle (5,-2)": 
		CassetteBeastsLocationData("encounter_overworld_5_-2_battler", "Deadlands", id_off+26),
	"New Wirrl Park Duo Battle (5,-3)": 
		CassetteBeastsLocationData("encounter_overworld_5_-3_battler_pair", "New Wirral Park", id_off+27),# OVERWORLD_5_-3_BATTLER_PAIR_NAME1 OVERWORLD_5_-3_BATTLER_PAIR_NAME2
	"New Wirral Park Cultist Battle 2 (5,-4)": 
		CassetteBeastsLocationData("encounter_nwp_5_-4_cultist", "New Wirral Park", id_off+28),
	"Darwin Battle (5,-5)": 
		CassetteBeastsLocationData("encounter_overworld_5_-5_battler_darwin", "New Wirral Park", id_off+29),
	"Eastham Woods Soldier Battle (5,-6)": 
		CassetteBeastsLocationData("encounter_overworld_5_-6_battler", "Eastham Woods", id_off+30),
	"Eastham Woods Duo Battle (5,-7)": 
		CassetteBeastsLocationData("encounter_overworld_5_-7_battler_pair", "Eastham Woods", id_off+31), # OVERWORLD_5_-7_BATTLER_PAIR_NAME1 OVERWORLD_5_-7_BATTLER_PAIR_NAME2
	"Southern Isles Treasure Seeker Battle (6,0)": 
		CassetteBeastsLocationData("encounter_overworld_6_0_battler", "Southern Isles", id_off+32),
	"Deadlands Coast Historian Battle 1 (6,-1)": 
		CassetteBeastsLocationData("encounter_overworld_6_-1_battler", "Deadlands Coast", id_off+33),
	"New London Landkeeper Battle (6,-2)": 
		CassetteBeastsLocationData("encounter_overworld_6_-2_landkeeper", "New London", id_off+34),
	"New London Historian Battle (6,-2)": 
		CassetteBeastsLocationData("encounter_overworld_6_-2_historian", "New London", id_off+35),
	"Autumn Hill Traveler Battle (6,-3)": 
		CassetteBeastsLocationData("encounter_overworld_6_-3_battler", "Autumn Hill", id_off+36),
	"Autumn Hill Cultist Battle Before Gate (6,-4)": 
		CassetteBeastsLocationData("encounter_overworld_6_-4_cultist", "Autumn Hill", id_off+37),
	"Autumn Hill Cultist Battle After Gate (6,-5)": 
		CassetteBeastsLocationData("encounter_overworld_6_-5_cultist", "Autumn Hill", id_off+38),
	"Autumn Hill Cultist Battle Near Sign (6,-6)": 
		CassetteBeastsLocationData("encounter_overworld_6_-6_cultist", "Autumn Hill", id_off+39),
	"Nevermort Fan Battle (7,-1)": 
		CassetteBeastsLocationData("encounter_overworld_7_-1_nevermort_fan_npc", "Deadlands Coast", id_off+40),# SD_NEVERMORT_TRAINER_NAME
	"New London Ranger Battle (7,-2)": 
		CassetteBeastsLocationData("encounter_overworld_7_-2_battler", "New London", id_off+41),
	"New Wirral Park Battle (7,-3)": 
		CassetteBeastsLocationData("encounter_overworld_7_-3_battler", "New Wirral Park", id_off+42),# OVERWORLD_7_-3_BATTLER_NAME
	"New Wirral Park Landkeeper Battle Near Office (7,-3)": 
		CassetteBeastsLocationData("encounter_overworld_7_-3_landkeeper", "New Wirral Park", id_off+43),
	"Autumn Hill Cultist Newbie Battle (7,-3)": 
		CassetteBeastsLocationData("encounter_overworld_7_-3_cultist_newbie", "Autumn Hill", id_off+44),
	"Autumn Hill Cultist Newbie Battle Near Post (7,-4)": 
		CassetteBeastsLocationData("encounter_overworld_7_-4_cultist_newbie", "Autumn Hill", id_off+45),
	"Autumn Hill Cultist Duo Battle (7,-6)": 
		CassetteBeastsLocationData("encounter_overworld_7_-6_cultist_pair", "Autumn Hill", id_off+46),
	"NE Mire Sea Landkeeper Battle (7,-7)": 
		CassetteBeastsLocationData("encounter_overworld_7_-7_landkeeper", "NE Mire Sea", id_off+47),
	"Southern Isles Ranger Wannabe Battle (8,0)": 
		CassetteBeastsLocationData("encounter_overworld_8_0_battler", "Southern Isles", id_off+48),
	"Epicurus Battle (8,-1)": 
		CassetteBeastsLocationData("encounter_overworld_8_-1_battler_epicurus", "Deadlands Coast", id_off+49),
	"Deadlands Coast Historian Battle 2 (8,-2)": 
		CassetteBeastsLocationData("encounter_overworld_8_-2_battler", "Deadlands Coast", id_off+50),
	"Autumn Hill Cultist Battle (8,-3)": 
		CassetteBeastsLocationData("encounter_overworld_8_-3_cultist", "Autumn Hill", id_off+51),
	"Autumn Hill Cultist Battle Near Zedd (8,-5)": 
		CassetteBeastsLocationData("encounter_overworld_8_-5_cultist", "Autumn Hill", id_off+52),
	"Autumn Hill Cultist Battle Near NE Mire Sea (8,-6)": 
		CassetteBeastsLocationData("encounter_overworld_8_-6_cultist", "Autumn Hill", id_off+53),
	"Thirstaton Lake Landkeeper Battle (-1,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-1_-3_landkeeper", "Thirstaton Lake", id_off+54),
	"Jackie Battle (-1,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-1_-6_battler_jackie", "Lakeside", id_off+55),# OVERWORLD_-1_-6_BATTLER_NAME
	"Lakeside Researcher Battle (-1,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-1_-6_battler2", "Lakeside", id_off+56),
	"Landkeeper Battle West of Harbourtown (-2,-1)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-1_landkeeper", "Harbourtown West", id_off+57),
	"Thirstaton Historian Battle (-2,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-3_battler", "Thirstaton Lake", id_off+58),
	"Diveana Battle (-2,-4)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-4_battler_diveal_keeper", "Thirstaton Lake", id_off+59),
	"Zhuangzi Battle (-2,-5)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-5_battler_zhuangzi", "Lakeside", id_off+60),# ZHUANGZI_NAME
	"Mt Wirral Landkeeper Battle (-2,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-6_landkeeper", "Mt Wirral", id_off+61),
	"Mt Wirral Ranger Wannabe Battle Near Ham (-2,-7,)": 
		CassetteBeastsLocationData("encounter_overworld_-2_-7_battler", "Mt Wirral", id_off+62),
	"Creep Battle Below Piper Farm (-3,0)": 
		CassetteBeastsLocationData("encounter_overworld_-3_0", "Piper Farm", id_off+63),
	"Cherry Meadow Ranger Trainee Battle (-4,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-4_-3_battler", "Cherry Meadow", id_off+64),
	"Cherry Meadow Ranger Trainee Battle Near Buffy (-4,-4)": 
		CassetteBeastsLocationData("encounter_overworld_-4_-4_battler", "Cherry Meadow", id_off+65),
	"Socrates and Plato Battle (-5,-5)": 
		CassetteBeastsLocationData("encounter_socrates_and_plato", "Cherry Meadow", id_off+66),
	"Mt Wirral Traveler Battle (-4,-7)": 
		CassetteBeastsLocationData("encounter_overworld_-4_-7_battler", "Mt Wirral", id_off+67),
	"Mt Wirral Traveler Battle Near Brokenhead (-5,-6)": 
		CassetteBeastsLocationData("encounter_overworld_-5_-6_battler", "Mt Wirral", id_off+68),
	"The Marshes Landkeeper Battle Near Spider Cave (-6,-1)": 
		CassetteBeastsLocationData("encounter_overworld_-6_-1_landkeeper1", "The Marshes", id_off+69),
	"The Marshes Landkeeper Battle Near Office (-6,-3)": 
		CassetteBeastsLocationData("encounter_overworld_-6_-3_landkeeper1", "The Marshes", id_off+70),
	"The Marshes Lankeeper Battle Near West Mire Sea (-7,-2)": 
		CassetteBeastsLocationData("encounter_overworld_-7_-2_landkeeper", "The Marshes", id_off+71),
	"Brokenhead Tamer Battle (-7,-7)": 
		CassetteBeastsLocationData("encounter_overworld_-7_-7_battler", "Brokenhead", id_off+72),
	"Mourningtown Cultist Battle 1 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_1", "Mourningtown", id_off+73),
	"Mourningtown Cultist Battle 2 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_2", "Mourningtown", id_off+74),
	"Mourningtown Cultist Battle 3 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_3", "Mourningtown", id_off+75),
	"Mourningtown Cultist Battle 4 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_4", "Mourningtown", id_off+76),
	"Mourningtown Cultist Battle 5 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_5", "Mourningtown", id_off+77),
	"Mourningtown Cultist Battle 6 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_6", "Mourningtown", id_off+78),
	"Mourningtown Cultist Battle 7 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_7", "Mourningtown", id_off+79),
	"Mourningtown Cultist Battle 8 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_8", "Mourningtown", id_off+80),
	"Mourningtown Cultist Battle 9 (7,-5)": 
		CassetteBeastsLocationData("encounter_commune_cultist_9", "Mourningtown", id_off+81),
	"Aldgrave Tomb Station Landkeeper Battle (-5,0)": 
		CassetteBeastsLocationData("encounter_dungeon_graveyard_landkeeper", "Aldgrave Tomb Station", id_off+82),
	"Landkeeper Office 1 Battle (4,-1)": 
		CassetteBeastsLocationData("encounter_office_1", "Harbourtown Outskirts", id_off+83),
	"Landkeeper Office 2 Battle (7,-3)": 
		CassetteBeastsLocationData("encounter_office_2", "Autumn Hill", id_off+84),
	"Landkeeper Office 3 Battle (7,-7)": 
		CassetteBeastsLocationData("encounter_office_3", "NE Mire Sea", id_off+85),
	"Landkeeper Office 4 Battle (1,-7)": 
		CassetteBeastsLocationData("encounter_office_4", "Eastham Woods Cliff", id_off+86),
	"Landkeeper Office 5 Battle (-6,-3)": 
		CassetteBeastsLocationData("encounter_office_5", "The Marshes", id_off+87),
}

id_off += len(trainersanity_locations)
tapesanity_locations = {
	f"Recorded {monster}":
	CassetteBeastsLocationData(f"record_{data['id']}", "Menu", id_off+i)
	for i, (monster,data) in enumerate(monsters().items())
}

id_off += len(tapesanity_locations)
tapesanity_percentage_locations = {
	f"Recorded {i+1} Monsters":
	CassetteBeastsLocationData(f"record_{i+1}", "Menu", id_off+i)
	for i in range(monsterCount(None))
}

id_off += len(tapesanity_percentage_locations)
bootlegsanity_per_tape_locations = {
	f"Recorded Bootleg {monster}":
	CassetteBeastsLocationData(f"record_bootleg_{data['id']}", "Menu", id_off+i)
	for i, (monster,data) in enumerate(monsters().items())
}

id_off += len(bootlegsanity_per_tape_locations)
bootlegsanity_specific_locations = {
	f"Recorded {_type.capitalize()} Bootleg {monster}":
	CassetteBeastsLocationData(f"record_{_type}_{data['id']}", "Menu", id_off+i*14+t)
	for i, (monster,data) in enumerate(monsters().items()) for t, _type in enumerate(types)
}

id_off += len(bootlegsanity_specific_locations)
bootlegsanity_percentage_locations = {
	f"Recorded {i+1} Bootleg Monsters":
	CassetteBeastsLocationData(f"record_bootleg_{i+1}", "Menu", id_off+i)
	for i in range(monsterCount()*14)
}

id_off += len(bootlegsanity_percentage_locations)
fusionsanity_locations = {
	f"Seen Some Fusions {i+1}":
	CassetteBeastsLocationData(f"seen_fusions_{i+1}", "Postgame", id_off+i)
	for i in range(1024)
}

event_data_table = {
	"Recruited Kayleigh": CassetteBeastsEventData("Harbourtown Station", "Recruited Kayleigh"),
	"Recruited Eugene": CassetteBeastsEventData("Harbourtown East", "Recruited Eugene"),
	"Recruited Meredith": CassetteBeastsEventData("Harbourtown East", "Recruited Meredith"),
	"Recruited Felix": CassetteBeastsEventData("Lakeside", "Recruited Felix"),
	"Recruited Viola": CassetteBeastsEventData("The Marshes", "Recruited Viola"),
	"Recruited Barkley": CassetteBeastsEventData("Mt Wirral", "Recruited Barkley"),
	"Defeated Oldgante": CassetteBeastsEventData("Harbourtown Station", "Defeated Oldgante"),
	"Defeated Poppetox": CassetteBeastsEventData("Glowcester Road Station", "Defeated Poppetox"),
	"Defeated Mourningstar": CassetteBeastsEventData("Mourningstar Crescent Station", "Defeated Mourningstar"),
	"Defeated Nowhere Monarch": CassetteBeastsEventData("Falldown Mall", "Defeated Nowhere Monarch"),
	"Defeated Heckahedron": CassetteBeastsEventData("Waterloop Station", "Defeated Heckahedron"),
	"Defeated Alice": CassetteBeastsEventData("Cherry Cross Station", "Defeated Alice"),
	"Defeated Robin Goodfellow": CassetteBeastsEventData("Bard Street Station", "Defeated Robin Goodfellow"),
	"Defeated Mammon": CassetteBeastsEventData("Landkeeper HQ", "Defeated Mammon"),
	"Defeated Lamento Mori": CassetteBeastsEventData("Aldgrave Tomb Station", "Defeated Lamento Mori"),
	"Defeated Babelith": CassetteBeastsEventData("Icelington Station", "Defeated Babelith"),
	"Defeated Shining Kuneko": CassetteBeastsEventData("Cherry Meadow", "Defeated Shining Kuneko"),
	"Defeated Morgante": CassetteBeastsEventData("Postgame", "Defeated Morgante"),
	"Defeated Helia": CassetteBeastsEventData("Postgame", "Defeated Helia"),
	"Defeated Lenna": CassetteBeastsEventData("Postgame", "Defeated Lenna"),
	"Defeated Gwenivar": CassetteBeastsEventData("Brightside Pier", "Defeated Gwenivar", "pier"),
	"Defeated Averevoir": CassetteBeastsEventData("Mt Wirral", "Defeated Averevoir"),
	"Met Ianthe": CassetteBeastsEventData("New Wirral Park", "Met Ianthe"),
	"Met Meredith": CassetteBeastsEventData("New Wirral Park", "Met Meredith"),
	"Cleared Landkeeper Offices": CassetteBeastsEventData("The Marshes", "Cleared Landkeeper Offices"),
	"Defeated Aleph": CassetteBeastsEventData("Night's Bridge Station", "Defeated Aleph"),
	"Became Captain": CassetteBeastsEventData("Harbourtown East", "Became Captain"),
	"Recruited Sunny": CassetteBeastsEventData("Mt Wirral", "Recruited Sunny"),
	"Quest People are People": CassetteBeastsEventData("New Landkeeper Hideout", "Quest People are People"),
}

location_data_table = base_locations|pier_locations|chest_loot_locations|shopsanity_locations|trainersanity_locations|tapesanity_locations|tapesanity_percentage_locations|\
						bootlegsanity_per_tape_locations|bootlegsanity_specific_locations|bootlegsanity_percentage_locations|fusionsanity_locations
location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}

def isTPL(options, name):# is Tapesanity Percentage Location
	loc_count = options.tapesanity_percentage_item_count
	last_loc  = ceil(options.tapesanity_percentage_item_count.range_end*(options.tapesanity_percentage/100))
	loc_nums = [int(i*last_loc/loc_count) for i in range(1,loc_count+1)]
	return  options.tapesanity == "percentage" and\
			name in tapesanity_percentage_locations.keys() and\
			int(name[9:-9]) in loc_nums

def isBPL(options, name):# is Bootlegsanity Percentage Location
	loc_count = options.bootlegsanity_percentage_item_count
	mon_count = monsterCount(options)
	if options.bootlegsanity == "percentage_all":
		mon_count *= 14
	last_loc  = ceil(mon_count*(options.bootlegsanity_percentage/100))
	loc_nums = [int(i*last_loc/loc_count) for i in range(1,loc_count+1)]
	return  options.bootlegsanity in ["percentage_tape", "percentage_all"] and\
			name in bootlegsanity_percentage_locations.keys() and\
			int(name[9:-17]) in loc_nums

def isFL(options, name):# is Fusionsanity Location
	return  options.fusionsanity and\
			(int(name[18:]) <= options.fusionsanity_item_count)

def isLocation(options, name):
	if not hasDLC(options, name):
		return False
	return  (name in base_locations.keys()) or\
			(name in pier_locations.keys() and options.use_pier == True) or\
			(name in chest_loot_locations.keys() and options.shuffle_chest_loot_tables == True) or\
			(name in shopsanity_locations.keys() and options.shopsanity == True) or\
			(name in trainersanity_locations.keys() and options.trainersanity == True) or\
			(name in tapesanity_locations.keys() and options.tapesanity == "specific") or\
			(name in tapesanity_percentage_locations.keys() and isTPL(options, name)) or\
			(name in bootlegsanity_per_tape_locations.keys() and options.bootlegsanity == "per_tape") or\
			(name in bootlegsanity_specific_locations.keys() and options.bootlegsanity == "specific") or\
			(name in bootlegsanity_percentage_locations.keys() and isBPL(options, name)) or\
			(name in fusionsanity_locations.keys() and isFL(options, name))

def hasDLC(options, name):
	for mon, data in monsters(None).items():
		if mon in name:
			if data['dlc'] == "pier":
				return options.use_pier
	return True

def getLocationCount(options):
	count = len(base_locations)
	if options.shuffle_chest_loot_tables:
		count += len(chest_loot_locations)

	if options.shopsanity:
		count += len(shopsanity_locations)

	if options.trainersanity:
		count += len(trainersanity_locations)

	if options.tapesanity == "specific":
		count += monsterCount(options)
	elif options.tapesanity == "percentage":
		percent = options.tapesanity_percentage/100
		if options.tapesanity_percentage_item_count > ceil(monsterCount(options)*percent):
			count += ceil(monsterCount(options)*percent)
		else:
			count += options.tapesanity_percentage_item_count

	if options.bootlegsanity == "per_tape":
		count += monsterCount(options)
	elif options.bootlegsanity == "specific":
		count += monsterCount(options)*14
	elif options.bootlegsanity in ["percentage_tape", "percentage_all"]:
		percent = (options.bootlegsanity_percentage/100)
		_max = ceil(monsterCount(options)*14*percent) if options.bootlegsanity == "percentage_all" else ceil(monsterCount(options)*percent)
		if options.bootlegsanity_percentage_item_count > _max:
			count += _max
		else:
			count += options.bootlegsanity_percentage_item_count

	if options.fusionsanity:
		count += options.fusionsanity_item_count

	return count