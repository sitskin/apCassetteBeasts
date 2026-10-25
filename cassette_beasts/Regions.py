from typing import NamedTuple
from .Strings import ALDGRAVE_TOMB_STATION, AUTUMN_HILL, BARD_STREET_STATION, BRIGHTSIDE_PIER, BROKENHEAD, CAST_IRON_SHORE, CHERRY_CROSS_STATION, CHERRY_MEADOW, COSMIC_ZONE, COSMIC_ZONE_PASS, DEADLANDS, DEADLANDS_COAST, DEFEATED_ALEPH, DINO_QUARRY, EASTHAM_WOODS, EASTHAM_WOODS_CLIFF, FALLDOWN_MALL, FUNWORLD, FUNWORLD_PASS, GLAISTAINBURY_ABBEY, GLOWCESTER_ROAD_STATION, HAM, HARBOURTOWN_BEACH, HARBOURTOWN_EAST, HARBOURTOWN_GATE_KEY, HARBOURTOWN_OUTSKIRTS, HARBOURTOWN_STATION, HARBOURTOWN_WEST, ICELINGTON_STATION, LAKESIDE, LANDKEEPER_HQ, LOST_HEARTS_GRAVEYARD, MENU, MOURNINGSTAR_CRESCENT_STATION, MOURNINGTOWN, MOURNINGTOWN_KEY, MT_WIRRAL, NEW_LANDKEEPER_HIDEOUT, NEW_LONDON, NEW_WIRRAL_PARK, NE_MIRE_SEA, NIGHT_S_BRIDGE_STATION, PIPER_FARM, POSTGAME, PROGRESSIVE_CLIMB, PROGRESSIVE_DASH, PROGRESSIVE_GLIDE, PROGRESSIVE_MAGNETISM, RECRUITED_SUNNY, RECRUITED_VIOLA, SONG_PART, SONG_PART_ALICE, SONG_PART_AVEREVOIR, SONG_PART_BABELITH, SONG_PART_FINALGANTE, SONG_PART_GWENIVAR, SONG_PART_HECKAHEDRON, SONG_PART_HELIA, SONG_PART_KUNEKO, SONG_PART_LAMENTO_MORI, SONG_PART_LENNA, SONG_PART_MAMMON, SONG_PART_MOURNINGSTAR, SONG_PART_NOWHERE_MONARCH, SONG_PART_OLDGANTE, SONG_PART_PUPPETOX, SONG_PART_ROBIN_GOODFELLOW, SOUTHERN_ISLES, SPIDER_CAVE, SWIM, THE_MARSHES, THE_WITCH_HOUSE, THE_WITCH_HOUSE_PASS, THIRSTATON_LAKE, TITANIA_SHIPWRECK, UPPER_PATH, VALVE_HANDLE, WATERLOOP_STATION, WEST_MIRE_SEA

class CassetteBeastsRegionData(NamedTuple):
	name: str
	exit_rules: dict[str, callable] = {}

region_data = [
	CassetteBeastsRegionData(MENU,
		{
			HARBOURTOWN_BEACH: lambda state, player: True,
			HARBOURTOWN_EAST: lambda state, player: True,
			NIGHT_S_BRIDGE_STATION: lambda state, player: songPartCount(state, player) >= 8 and \
				state.has(PROGRESSIVE_GLIDE, player) and state.has(SWIM, player) and \
				state.has(PROGRESSIVE_MAGNETISM, player) and state.has(PROGRESSIVE_DASH, player),
		}),
	CassetteBeastsRegionData(HARBOURTOWN_BEACH,
		{
			HARBOURTOWN_EAST: lambda state, player: True,
			HARBOURTOWN_OUTSKIRTS: lambda state, player: state.has(HARBOURTOWN_GATE_KEY, player),
			BRIGHTSIDE_PIER: lambda state, player: state.has(SONG_PART, player, 4),
		}),
	CassetteBeastsRegionData(HARBOURTOWN_EAST,
		{
			HARBOURTOWN_BEACH: lambda state, player: True,
			UPPER_PATH: lambda state, player: True,
		}),
	CassetteBeastsRegionData(HARBOURTOWN_OUTSKIRTS,
		{
			UPPER_PATH: lambda state, player: state.has(PROGRESSIVE_GLIDE, player, 1),
			NEW_WIRRAL_PARK: lambda state, player: True,
		}),
	CassetteBeastsRegionData(UPPER_PATH,
		{
			HARBOURTOWN_WEST: lambda state, player:
				state.has(PROGRESSIVE_DASH, player, 1) or (state.has(PROGRESSIVE_GLIDE, player, 1) and state.has(PROGRESSIVE_MAGNETISM, player, 1)),
			THIRSTATON_LAKE: lambda state, player: state.has(SWIM, player),
			HARBOURTOWN_STATION: lambda state, player: True,
		}),
	CassetteBeastsRegionData(HARBOURTOWN_WEST,
		{

		}),
	CassetteBeastsRegionData(NEW_WIRRAL_PARK,
		{
			AUTUMN_HILL: lambda state, player: True,
			EASTHAM_WOODS: lambda state, player: True,
			DEADLANDS: lambda state, player: True,
			LAKESIDE: lambda state, player: True,
			GLOWCESTER_ROAD_STATION: lambda state, player: True,
		}),
	CassetteBeastsRegionData(AUTUMN_HILL,
		{
			MOURNINGTOWN: lambda state, player: True,
			DINO_QUARRY: lambda state, player: True,
		}),
	CassetteBeastsRegionData(EASTHAM_WOODS,
		{
			NE_MIRE_SEA: lambda state, player: state.has(PROGRESSIVE_GLIDE, player, 1) and state.has(PROGRESSIVE_MAGNETISM, player, 1),
			HAM: lambda state, player: True,
			EASTHAM_WOODS_CLIFF: lambda state, player: state.has(PROGRESSIVE_MAGNETISM, player, 1),
		}),
	CassetteBeastsRegionData(EASTHAM_WOODS_CLIFF,
		{
			FALLDOWN_MALL: lambda state, player: True,
		}),
	CassetteBeastsRegionData(DEADLANDS,
		{
			DEADLANDS_COAST: lambda state, player: True,
			NEW_LONDON: lambda state, player: state.has(PROGRESSIVE_MAGNETISM, player, 1) or state.has(PROGRESSIVE_DASH, player, 1),
		}),
	CassetteBeastsRegionData(DEADLANDS_COAST,
		{
			SOUTHERN_ISLES: lambda state, player: True,
			DINO_QUARRY: lambda state, player: True,
		}),
	CassetteBeastsRegionData(DINO_QUARRY,
		{

		}),
	CassetteBeastsRegionData(NEW_LONDON,
		{

		}),
	CassetteBeastsRegionData(NE_MIRE_SEA,
		{

		}),
	CassetteBeastsRegionData(SOUTHERN_ISLES,
		{

		}),
	CassetteBeastsRegionData(LAKESIDE,
		{
			THIRSTATON_LAKE: lambda state, player: state.has(SWIM, player),
			CHERRY_MEADOW: lambda state, player: True,
		}),
	CassetteBeastsRegionData(THIRSTATON_LAKE,
		{
			WATERLOOP_STATION: lambda state, player: True,
		}),
	CassetteBeastsRegionData(CHERRY_MEADOW,
		{
			THE_MARSHES: lambda state, player: True,
			CAST_IRON_SHORE: lambda state, player: True,
			MT_WIRRAL: lambda state, player: state.has(PROGRESSIVE_CLIMB, player, 1),
			CHERRY_CROSS_STATION: lambda state, player: state.has(PROGRESSIVE_DASH, player, 1) or state.has(PROGRESSIVE_CLIMB, player, 1),
			GLAISTAINBURY_ABBEY: lambda state, player: state.has(PROGRESSIVE_MAGNETISM, player, 1),
		}),
	CassetteBeastsRegionData(HAM,
		{
			MT_WIRRAL: lambda state, player: state.has(PROGRESSIVE_CLIMB, player, 1),
		}),
	CassetteBeastsRegionData(THE_MARSHES,
		{
			PIPER_FARM: lambda state, player: True,
			LOST_HEARTS_GRAVEYARD: lambda state, player: True,
			WEST_MIRE_SEA: lambda state, player: True,
			SPIDER_CAVE: lambda state, player: state.has(PROGRESSIVE_DASH, player),
			LANDKEEPER_HQ: lambda state, player: True,
		}),
	CassetteBeastsRegionData(SPIDER_CAVE,
		{

		}),
	CassetteBeastsRegionData(PIPER_FARM,
		{
			HARBOURTOWN_WEST: lambda state, player: True,
		}),
	CassetteBeastsRegionData(LOST_HEARTS_GRAVEYARD,
		{
			ALDGRAVE_TOMB_STATION: lambda state, player: True,
			NEW_LANDKEEPER_HIDEOUT: lambda state, player: state.has(RECRUITED_SUNNY, player),
		}),
	CassetteBeastsRegionData(WEST_MIRE_SEA,
		{

		}),
	CassetteBeastsRegionData(CAST_IRON_SHORE,
		{
			TITANIA_SHIPWRECK: lambda state, player: state.has(RECRUITED_VIOLA, player),
		}),
	CassetteBeastsRegionData(MT_WIRRAL,
		{
			BROKENHEAD: lambda state, player: state.has(PROGRESSIVE_GLIDE, player, 2),
			ICELINGTON_STATION: lambda state, player: True,
		}),
	CassetteBeastsRegionData(BROKENHEAD,
		{

		}),
	CassetteBeastsRegionData(HARBOURTOWN_STATION,
		{

		}),
	CassetteBeastsRegionData(GLOWCESTER_ROAD_STATION,
		{

		}),
	CassetteBeastsRegionData(MOURNINGTOWN,
		{
			MOURNINGSTAR_CRESCENT_STATION: lambda state, player: state.has(MOURNINGTOWN_KEY, player),
		}),
	CassetteBeastsRegionData(MOURNINGSTAR_CRESCENT_STATION,
		{

		}),
	CassetteBeastsRegionData(FALLDOWN_MALL,
		{

		}),
	CassetteBeastsRegionData(WATERLOOP_STATION,
		{

		}),
	CassetteBeastsRegionData(CHERRY_CROSS_STATION,
		{

		}),
	CassetteBeastsRegionData(GLAISTAINBURY_ABBEY,
		{

		}),
	CassetteBeastsRegionData(TITANIA_SHIPWRECK,
		{
			BARD_STREET_STATION: lambda state, player: state.has(VALVE_HANDLE, player, 2),
		}),
	CassetteBeastsRegionData(BARD_STREET_STATION,
		{

		}),
	CassetteBeastsRegionData(LANDKEEPER_HQ,
		{

		}),
	CassetteBeastsRegionData(ALDGRAVE_TOMB_STATION,
		{

		}),
	CassetteBeastsRegionData(ICELINGTON_STATION,
		{

		}),
	CassetteBeastsRegionData(NIGHT_S_BRIDGE_STATION,
		{
			POSTGAME: lambda state, player: state.has(DEFEATED_ALEPH, player),
		}),
	CassetteBeastsRegionData(POSTGAME,
		{

		}),
	CassetteBeastsRegionData(BRIGHTSIDE_PIER,
		{
			THE_WITCH_HOUSE: lambda state, player: state.has(THE_WITCH_HOUSE_PASS, player),
			FUNWORLD: lambda state, player: state.has(FUNWORLD_PASS, player),
			COSMIC_ZONE: lambda state, player: state.has(COSMIC_ZONE_PASS, player),
		}),
	CassetteBeastsRegionData(THE_WITCH_HOUSE,
		{

		}),
	CassetteBeastsRegionData(FUNWORLD,
		{

		}),
	CassetteBeastsRegionData(COSMIC_ZONE,
		{

		}),
	CassetteBeastsRegionData(NEW_LANDKEEPER_HIDEOUT,
		{

		}),
]

region_data_table = {region.name: region for region in region_data}


def songPartCount(state, player) -> int:
	return sum([
		state.has(SONG_PART_OLDGANTE, player),
		state.has(SONG_PART_PUPPETOX, player),
		state.has(SONG_PART_MOURNINGSTAR, player),
		state.has(SONG_PART_NOWHERE_MONARCH, player),
		state.has(SONG_PART_HECKAHEDRON, player),
		state.has(SONG_PART_ALICE, player),
		state.has(SONG_PART_ROBIN_GOODFELLOW, player),
		state.has(SONG_PART_MAMMON, player),
		state.has(SONG_PART_LAMENTO_MORI, player),
		state.has(SONG_PART_BABELITH, player),
		state.has(SONG_PART_KUNEKO, player),
		state.has(SONG_PART_AVEREVOIR, player),
		state.has(SONG_PART_HELIA, player),
		state.has(SONG_PART_LENNA, player),
		state.has(SONG_PART_FINALGANTE, player),
		state.has(SONG_PART_GWENIVAR, player)
		])
