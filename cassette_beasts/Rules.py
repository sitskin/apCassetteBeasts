from worlds.generic.Rules import set_rule, add_rule


def canGlide(state, player):
	return state.has("Progressive Glide", player)

def canDash(state, player):
	return state.has("Progressive Dash", player)

def canMagnetism(state, player):
	return state.has("Progressive Magnetism", player)

def canSwim(state, player):
	return state.has("Swim", player)

def canClimb(state, player):
	return state.has("Progressive Climb", player)

def canFly(state, player):
	return state.has("Progressive Glide", player, 2)

def hasAllStamps(state, player):
	return state.has("Captain Wallace Stamp",     player) and\
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

def clearedLandkeeperOffices(state, player):
	return state.can_reach_location("Landkeeper Office 1 Cabinet (4,-1)", player) and\
		state.can_reach_location("Landkeeper Office 2 Cabinet (7,-3)",    player) and\
		state.can_reach_location("Landkeeper Office 3 Cabinet (7,-7)",    player) and\
		state.can_reach_location("Landkeeper Office 4 Cabinet (1,-7)",    player) and\
		state.can_reach_location("Landkeeper Office 5 Cabinet (-6,-3)",   player)


def set_rules(cbworld):
	multiworld = cbworld.multiworld
	player = cbworld.player

	#---Region Rules---

	#Harbourtown Beach

	#Harbourtown East

	#Harbourtown Outskirts
	for e in multiworld.get_region("Harbourtown Outskirts", player).entrances:
		set_rule(e, lambda state: state.has("Harbourtown Gate Key", player))

	#Upper Path
	for e in multiworld.get_region("Upper Path", player).entrances:
		if e.name == "Harbourtown Outskirts":
			set_rule(e, lambda state: canGlide(state, player))
		elif e.name == "Harbourtown East":
			set_rule(e, lambda state: state.has("Defeated Oldgante", player))

	#Harbourtown West
	for e in multiworld.get_region("Harbourtown West", player).entrances:
		if e.name == "Upper Path":
			set_rule(e, lambda state: canMagnetism(state, player) or canDash(state, player))

	#New Wirral Park
	for e in multiworld.get_region("New Wirral Park", player).entrances:
		set_rule(e, lambda state: state.has("Defeated Oldgante", player))

	#Autumn Hill

	#Eastham Woods

	#Eastham Woods Cliff
	for e in multiworld.get_region("Eastham Woods Cliff", player).entrances:
		set_rule(e, lambda state: canMagnetism(state, player))

	#Deadlands

	#Deadlands Coast

	#New London
	for e in multiworld.get_region("New London", player).entrances:
		set_rule(e, lambda state: canMagnetism(state, player))

	#NE Mire Sea
	for e in multiworld.get_region("NE Mire Sea", player).entrances:
		set_rule(e, lambda state: canGlide(state, player))

	#Southern Isles

	#Lakeside

	#Thirstaton Lake
	for e in multiworld.get_region("Thirstaton Lake", player).entrances:
		set_rule(e, lambda state: canSwim(state, player))

	#Cherry Meadow

	#Ham

	#The Marshes

	#Piper Farm

	#Lost Hearts Graveyard

	#West Mire Sea
	for e in multiworld.get_region("West Mire Sea", player).entrances:
		set_rule(e, lambda state: canSwim(state, player))

	#Cast Iron Shore

	#Mt Wirral
	for e in multiworld.get_region("Mt Wirral", player).entrances:
		set_rule(e, lambda state: canGlide(state, player) and canClimb(state, player))

	#Brokenhead
	for e in multiworld.get_region("Brokenhead", player).entrances:
		set_rule(e, lambda state: canFly(state, player))

	#Harbourtown Station

	#Glowcester Road Station

	#Mourningtown
	for e in multiworld.get_region("Mourningtown", player).entrances:
		set_rule(e, lambda state: state.has("Recruited Kayleigh", player))

	#Mourningstar Crescent Street
	for e in multiworld.get_region("Mourningstar Crescent Station", player).entrances:
		set_rule(e, lambda state: state.has("Mourningtown Key", player))

	#Falldown Mall
	for e in multiworld.get_region("Falldown Mall", player).entrances:
		set_rule(e, lambda state: state.has("Recruited Meredith", player) and canMagnetism(state, player))

	#Waterloop Station

	#Cherry Cross Station
	for e in multiworld.get_region("Cherry Cross Station", player).entrances:
		set_rule(e, lambda state: canDash(state, player) or canClimb(state, player))

	#Titania Shipwreck

	#Bard Street Station
	for e in multiworld.get_region("Bard Street Station", player).entrances:
		set_rule(e, lambda state: state.has("Recruited Viola", player) and state.has("Valve Handel", player, 2))

	#Landkeeper HQ
	for e in multiworld.get_region("Landkeeper HQ", player).entrances:
		set_rule(e, lambda state: state.has("Recruited Eugene", player) and state.has("Cleared Landkeeper Offices", player))

	#Aldgrave Tomb Station

	#Icelington Station

	#Night's Bridge Station
	for e in multiworld.get_region("Night's Bridge Station", player).entrances:
		set_rule(e, lambda state: state.has("Song Fragment", player, 8))

	#Postgame
	for e in multiworld.get_region("Postgame", player).entrances:
		set_rule(e, lambda state: state.has("Azure Keystone", player, 2))


	#---Location Rules---
	#set_rule(multiworld.get_location("", player),
	#	lambda state: state.has("", player))
	set_rule(multiworld.get_location("Defeat Poppetox", player),
		lambda state: state.has("Train Ticket (Glowcester)", player))
	set_rule(multiworld.get_location("Defeat Alice", player),
		lambda state: state.has("White Rabbit Key", player))
	set_rule(multiworld.get_location("Defeat Lamento Mori", player),
		lambda state: state.has("Train Ticket (Aldgrave Tomb)", player))
	set_rule(multiworld.get_location("Beat Clee-o", player),
		lambda state: state.has("Coin", player))
	set_rule(multiworld.get_location("Beat Buffy", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Beat Iantha", player),
		lambda state: hasAllStamps(state, player))
	set_rule(multiworld.get_location("Harbourtown Chest under Crate on Flour Mill (0,-1)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Upper Path Magnet Platform Chest (0,-2)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Thirstaton Lake Underwater Chest (0,-3)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Harbourtown Chest on Top of House (1,-1)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("Eastham Woods Three Lights Chest (1,-6)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Harbourtown Outskirts Break Rock Chest (2,-2)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Eastham Woods Magnet Button Chest (2,-6)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Eastham Woods Chest on Cliff Below Mall (3,-7)", player),
		lambda state: canMagnetism(state, player) or canClimb(state, player))
	#set_rule(multiworld.get_location("Eastham Woods Chest on Mall Roof (3,-7)", player),
	#	lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("New Wirral Park Break Rock Chest in Wall (4,-5)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Eastham Woods Levitator Magnet Chest (4,-6)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Eastham Woods Four Button Chest (4,-7)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Deadlands Coast Button Chest (5,-1)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("New Wirral Park Lower Platform Chest (5,-3)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Eastham Woods Levitator Magnet Lever Chest (5,-7)", player),
		lambda state: canGlide(state, player) and canMagnetism(state, player))
	set_rule(multiworld.get_location("Southern Isles Chest Washed Up on Island (6,0)", player),
		lambda state: canSwim(state, player))
	set_rule(multiworld.get_location("New London Chest in House (6,-2)", player),
		lambda state: canClimb(state, player))
	set_rule(multiworld.get_location("Deadlands Coast Gust Chest (6,-2)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Autumn Hill Lever Chest in Lake (6,-3)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("Southern Isles Underwater Chest (7,0)", player),
		lambda state: canSwim(state, player) and canDash(state, player))
	set_rule(multiworld.get_location("Autumn Hill Peak Break Rock Chest (7,-4)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Autumn Hill Underwater Chest (8,-6)", player),
		lambda state: canGlide(state, player) or canSwim(state, player))
	set_rule(multiworld.get_location("NE Mire Sea Chest (8,-7)", player),
		lambda state: canGlide(state, player) and canMagnetism(state, player))
	set_rule(multiworld.get_location("Upper Path Chest on Wall Before Harbortown West (-1, -2)", player),
		lambda state: canGlide(state, player) and canMagnetism(state, player))
	set_rule(multiworld.get_location("Ham Chest Near Mt Wirral (-1,-7)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("Ham Chest Fall from Mt Wirral (-1,-7)", player),
		lambda state: state.can_reach_region("Mt Wirral", player))
	set_rule(multiworld.get_location("Piper Farm Climb Chest (-3,-1)", player),
		lambda state: canClimb(state, player))
	set_rule(multiworld.get_location("Cherry Meadow Chest Near Captain Buffy (-3,-5)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Cherry Meadow Button Chest (-5,-4)", player),
		lambda state: canDash(state, player) or canClimb(state, player))
	set_rule(multiworld.get_location("Cast Iron Shore Magnet Button Chest (-6,-4)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Cast Iron Shore Two Magnet Button Chest (-6,-5)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("West Mire Sea Chest Near Captain Gladiola (-7,0)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("West Mire Sea Button Chest on Pillar (-7,-3)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("Deadlands Cave Break Rock Chest (6,-2)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Autumn Hill Gear Cave Chest (7,-6)", player),
		lambda state: canGlide(state, player) and canDash(state, player))
	set_rule(multiworld.get_location("Marsh Cave Chest (-7,-1)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Harbourtown Outskirts Pipe Chest (1,-1)", player),
		lambda state: canGlide(state, player) and canDash(state, player))
	set_rule(multiworld.get_location("New Wirral Park Cave Chest (4,-3)", player),
		lambda state: canGlide(state, player) or canClimb(state, player))
	set_rule(multiworld.get_location("New Wirral Park Under Ranger Station Cave Chest (2,-4)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("Thirsaton Lake Waterfall Cave Chest (-1,-5)", player),
		lambda state: canGlide(state, player))
	set_rule(multiworld.get_location("Eastham Woods Cave Chest (2,-6)", player),
		lambda state: canMagnetism(state, player))
	set_rule(multiworld.get_location("Falldown Mall Empty Shop Chest (3,-7)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Falldown Mall Crate Room Chest (3,-7)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Waterloop Station Break Polyhedron Chest (1,-4)", player),
		lambda state: canDash(state, player))
	set_rule(multiworld.get_location("Landkeeper Office 1 Cabinet (4,-1)", player),
		lambda state: canGlide(state, player) and state.has("Landkeeper Window Key", player))
	set_rule(multiworld.get_location("Landkeeper Office 2 Cabinet (7,-3)", player),
		lambda state: canGlide(state, player) and state.has("Landkeeper Window Key", player))
	set_rule(multiworld.get_location("Landkeeper Office 3 Cabinet (7,-7)", player),
		lambda state: canGlide(state, player) and canMagnetism(state, player) and state.has("Landkeeper Window Key", player))
	set_rule(multiworld.get_location("Landkeeper Office 4 Cabinet (1,-7)", player),
		lambda state: canGlide(state, player) and canMagnetism(state, player) and state.has("Landkeeper Window Key", player))
	set_rule(multiworld.get_location("Landkeeper Office 5 Cabinet (-6,-3)", player),
		lambda state: canGlide(state, player) and state.has("Landkeeper Window Key", player))

	#--Trainersanity---
	if cbworld.options.trainersanity:
		set_rule(multiworld.get_location("Cherry Meadow Ranger Trainee Battle Near Buffy (-4,-4)", player),
			lambda state: canDash(state, player))
		set_rule(multiworld.get_location("Landkeeper Office 1 Battle (4,-1)", player),
			lambda state: canGlide(state, player) and state.has("Landkeeper Window Key", player))
		set_rule(multiworld.get_location("Landkeeper Office 2 Battle (7,-3)", player),
			lambda state: canGlide(state, player) and state.has("Landkeeper Window Key", player))
		set_rule(multiworld.get_location("Landkeeper Office 3 Battle (7,-7)", player),
			lambda state: canGlide(state, player) and canMagnetism(state, player) and state.has("Landkeeper Window Key", player))
		set_rule(multiworld.get_location("Landkeeper Office 4 Battle (1,-7)", player),
			lambda state: canGlide(state, player) and canMagnetism(state, player) and state.has("Landkeeper Window Key", player))
		set_rule(multiworld.get_location("Landkeeper Office 5 Battle (-6,-3)", player),
			lambda state: canGlide(state, player) and state.has("Landkeeper Window Key", player))

	#---Events---
	set_rule(multiworld.get_location("Recruited Kayleigh", player),
		lambda state: state.has("Defeated Oldgante", player))
	set_rule(multiworld.get_location("Recruited Eugene", player),
		lambda state: state.has("Defeated Oldgante", player))
	set_rule(multiworld.get_location("Recruited Meredith", player),
		lambda state: state.has("Envelope for Meredith", player))
	set_rule(multiworld.get_location("Recruited Barkley", player),
		lambda state: state.has("Progressive Climb", player))
	set_rule(multiworld.get_location("Cleared Landkeeper Offices", player),
		lambda state: clearedLandkeeperOffices(state, player))