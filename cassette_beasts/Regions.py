from typing import NamedTuple

class CassetteBeastsRegionData(NamedTuple):
	name: str
	exit_rules: dict[str, callable] = {}

region_data = [
	CassetteBeastsRegionData("Menu",
		{
			"Harbourtown Beach": lambda state, player: True,
			"Harbourtown East": lambda state, player: True,
			"Night's Bridge Station": lambda state, player: songPartCount(state, player) >= 8 and \
				state.has("Progressive Glide", player) and state.has("Swim", player) and \
				state.has("Progressive Magnetism", player) and state.has("Progressive Dash", player),
		}),
	CassetteBeastsRegionData("Harbourtown Beach",
		{
			"Harbourtown East": lambda state, player: True,
			"Harbourtown Outskirts": lambda state, player: state.has("Harbourtown Gate Key", player),
			"Brightside Pier": lambda state, player: state.has("Song Part", player, 4),
		}),
	CassetteBeastsRegionData("Harbourtown East",
		{
			"Harbourtown Beach": lambda state, player: True,
			"Upper Path": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Harbourtown Outskirts",
		{
			"Upper Path": lambda state, player: state.has("Progressive Glide", player, 1),
			"New Wirral Park": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Upper Path",
		{
			"Harbourtown West": lambda state, player:
				state.has("Progressive Dash", player, 1) or (state.has("Progressive Glide", player, 1) and state.has("Progressive Magnetism", player, 1)),
			"Thirstaton Lake": lambda state, player: state.has("Swim", player),
			"Harbourtown Station": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Harbourtown West",
		{

		}),
	CassetteBeastsRegionData("New Wirral Park",
		{
			"Autumn Hill": lambda state, player: True,
			"Eastham Woods": lambda state, player: True,
			"Deadlands": lambda state, player: True,
			"Lakeside": lambda state, player: True,
			"Glowcester Road Station": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Autumn Hill",
		{
			"Mourningtown": lambda state, player: True,
			"Dino Quarry": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Eastham Woods",
		{
			"NE Mire Sea": lambda state, player: state.has("Progressive Glide", player, 1) and state.has("Progressive Magnetism", player, 1),
			"Ham": lambda state, player: True,
			"Eastham Woods Cliff": lambda state, player: state.has("Progressive Magnetism", player, 1),
		}),
	CassetteBeastsRegionData("Eastham Woods Cliff",
		{
			"Falldown Mall": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Deadlands",
		{
			"Deadlands Coast": lambda state, player: True,
			"New London": lambda state, player: state.has("Progressive Magnetism", player, 1) or state.has("Progressive Dash", player, 1),
		}),
	CassetteBeastsRegionData("Deadlands Coast",
		{
			"Southern Isles": lambda state, player: True,
			"Dino Quarry": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Dino Quarry",
		{

		}),
	CassetteBeastsRegionData("New London",
		{

		}),
	CassetteBeastsRegionData("NE Mire Sea",
		{

		}),
	CassetteBeastsRegionData("Southern Isles",
		{

		}),
	CassetteBeastsRegionData("Lakeside",
		{
			"Thirstaton Lake": lambda state, player: state.has("Swim", player),
			"Cherry Meadow": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Thirstaton Lake",
		{
			"Waterloop Station": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Cherry Meadow",
		{
			"The Marshes": lambda state, player: True,
			"Cast Iron Shore": lambda state, player: True,
			"Mt Wirral": lambda state, player: state.has("Progressive Climb", player, 1),
			"Cherry Cross Station": lambda state, player: state.has("Progressive Dash", player, 1) or state.has("Progressive Climb", player, 1),
			"Glaistainbury Abbey": lambda state, player: state.has("Progressive Magnetism", player, 1),
		}),
	CassetteBeastsRegionData("Ham",
		{
			"Mt Wirral": lambda state, player: state.has("Progressive Climb", player, 1),
		}),
	CassetteBeastsRegionData("The Marshes",
		{
			"Piper Farm": lambda state, player: True,
			"Lost Hearts Graveyard": lambda state, player: True,
			"West Mire Sea": lambda state, player: True,
			"Spider Cave": lambda state, player: True,
			"Landkeeper HQ": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Spider Cave",
		{

		}),
	CassetteBeastsRegionData("Piper Farm",
		{
			"Harbourtown West": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Lost Hearts Graveyard",
		{
			"Aldgrave Tomb Station": lambda state, player: True,
			"New Landkeeper Hideout": lambda state, player: state.has("Recruited Sunny", player),
		}),
	CassetteBeastsRegionData("West Mire Sea",
		{

		}),
	CassetteBeastsRegionData("Cast Iron Shore",
		{
			"Titania Shipwreck": lambda state, player: state.has("Recruited Viola", player),
		}),
	CassetteBeastsRegionData("Mt Wirral",
		{
			"Brokenhead": lambda state, player: state.has("Progressive Glide", player, 2),
			"Icelington Station": lambda state, player: True,
		}),
	CassetteBeastsRegionData("Brokenhead",
		{

		}),
	CassetteBeastsRegionData("Harbourtown Station",
		{

		}),
	CassetteBeastsRegionData("Glowcester Road Station",
		{

		}),
	CassetteBeastsRegionData("Mourningtown",
		{
			"Mourningstar Crescent Station": lambda state, player: state.has("Mourningtown Key", player),
		}),
	CassetteBeastsRegionData("Mourningstar Crescent Station",
		{

		}),
	CassetteBeastsRegionData("Falldown Mall",
		{

		}),
	CassetteBeastsRegionData("Waterloop Station",
		{

		}),
	CassetteBeastsRegionData("Cherry Cross Station",
		{

		}),
	CassetteBeastsRegionData("Glaistainbury Abbey",
		{

		}),
	CassetteBeastsRegionData("Titania Shipwreck",
		{
			"Bard Street Station": lambda state, player: state.has("Valve Handle", player, 2),
		}),
	CassetteBeastsRegionData("Bard Street Station",
		{

		}),
	CassetteBeastsRegionData("Landkeeper HQ",
		{

		}),
	CassetteBeastsRegionData("Aldgrave Tomb Station",
		{

		}),
	CassetteBeastsRegionData("Icelington Station",
		{

		}),
	CassetteBeastsRegionData("Night's Bridge Station",
		{
			"Postgame": lambda state, player: state.has("Defeated Aleph", player),
		}),
	CassetteBeastsRegionData("Postgame",
		{

		}),
	CassetteBeastsRegionData("Brightside Pier",
		{
			"The Witch House": lambda state, player: state.has("The Witch House Pass", player),
			"Funworld": lambda state, player: state.has("Funworld Pass", player),
			"Cosmic Zone": lambda state, player: state.has("Cosmic Zone Pass", player),
		}),
	CassetteBeastsRegionData("The Witch House",
		{

		}),
	CassetteBeastsRegionData("Funworld",
		{

		}),
	CassetteBeastsRegionData("Cosmic Zone",
		{

		}),
	CassetteBeastsRegionData("New Landkeeper Hideout",
		{

		}),
]

region_data_table = {region.name: region for region in region_data}


def songPartCount(state, player) -> int:
	return sum([
		state.has("Song Part (Oldgante)", player),
		state.has("Song Part (Puppetox)", player),
		state.has("Song Part (Mourningstar)", player),
		state.has("Song Part (Nowhere Monarch)", player),
		state.has("Song Part (Heckahedron)", player),
		state.has("Song Part (Alice)", player),
		state.has("Song Part (Robin Goodfellow)", player),
		state.has("Song Part (Mammon)", player),
		state.has("Song Part (Lamento Mori)", player),
		state.has("Song Part (Babelith)", player),
		state.has("Song Part (Kuneko)", player),
		state.has("Song Part (Averevoir)", player),
		state.has("Song Part (Helia)", player),
		state.has("Song Part (Lenna)", player),
		state.has("Song Part (Finalgante)", player),
		state.has("Song Part (Gwenivar)", player)
		])