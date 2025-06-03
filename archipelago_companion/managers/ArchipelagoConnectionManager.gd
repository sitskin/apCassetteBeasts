extends Node

const ApWebSocketConnection = preload("res://mods/archipelago_companion/archipelago_client/ApWebsocketConnection.gd")
const BaseArchipelagoClient = preload("res://mods/archipelago_companion/archipelago_client/BaseArchipelagoClient.gd")
const ArchipelagoDataManager = preload("res://mods/archipelago_companion/managers/ArchipelagoDataManager.gd")

class GivenApItem:
	var itemName: String
	var itemAmount: int
	func _init(apItemObject: Array):
		itemName = apItemObject[0]
		itemAmount = apItemObject[1]

var archipelagoDataManager: ArchipelagoDataManager

var _apWebSocketConnection: ApWebSocketConnection
var _archipelagoClient: BaseArchipelagoClient

var _itemsReceivedFromServer = []
var _itemGiveTimer = 0.0
const _ITEM_GIVE_DELAY = 0.5

var _trapsReceivedFromServer = []

const _AP_AA_DEFEATED_KEY = "ap_aa_defeated"
const _AP_EVENT_FLAGS_TO_AP = {
	"ap_event_recruited_kayleigh": "Recruited Kayleigh",
	"ap_event_recruited_eugine": "Recruited Eugene",
	"ap_event_recruited_meredith": "Recruited Meredith",
	"ap_event_recruited_felix": "Recruited Felix",
	"ap_event_recruited_viola": "Recruited Viola",
	"ap_event_recruited_dog": "Recruited Barkley",
	"ap_event_recruited_sunny": "Recruited Sunny",
	"encounter_aa_oldgante": "Defeated Oldgante",
	"encounter_aa_puppet": "Defeated Poppetox",
	"encounter_aa_mourningstar": "Defeated Mourningstar",
	"encounter_aa_monarch": "Defeated Nowhere Monarch",
	"encounter_aa_cube": "Defeated Heckahedron",
	"encounter_aa_alice": "Defeated Alice",
	"encounter_aa_robin": "Defeated Robin Goodfellow",
	"encounter_aa_mammon": "Defeated Mammon",
	"encounter_aa_lamento_mori": "Defeated Lamento Mori",
	"encounter_aa_tower": "Defeated Babelith",
	"encounter_aa_kuneko": "Defeated Shining Kuneko",
	"encounter_aa_averevoir": "Defeated Averevoir",
	"encounter_aa_finalgante": "Defeated Morgante",
	"encounter_aa_helia": "Defeated Helia",
	"encounter_aa_lenna": "Defeated Lenna",
	"encounter_aa_clown": "Defeated Gwenivar",
	"encounter_aa_aleph_null": "Defeated Aleph",
	"met_ianthe": "Met Ianthe",
	"met_meredith": "Met Meredith",
	"met_felix": "Met Felix",
	"encounter_ianthe": "Bacame Captain"
}

var _tempReceivedItems = []
var randSeed: int
var _locationsCheckedWithoutConnection = []

signal connectionStateChanged(state, error)

func _init():
	archipelagoDataManager = ArchipelagoDataManager.new()
	_apWebSocketConnection = ApWebSocketConnection.new()
	_archipelagoClient = BaseArchipelagoClient.new(_apWebSocketConnection)
	self.add_child(_apWebSocketConnection)
	self.add_child(_archipelagoClient)
	_archipelagoClient.game = "Cassette Beasts"
	_archipelagoClient.connect("_received_connect_response", self, "_receivedConnectPacket")
	_archipelagoClient.connect("connection_state_changed", self, "_onConnectionChanged")
	_archipelagoClient.connect("item_received", self, "_onApItemReceived")
	_apWebSocketConnection.connect("on_room_info", self, "_roomInfoReceived")
	SaveSystem.connect("file_loaded", self, "_onFileLoaded")
	SaveState.connect("flag_changed", self, "_onFlagChanged")
	SceneManager.preloader.connect("singleton_setup_completed", self, "_onSingleSetupComplete")
	Console.register("getApItem", {
		"description":"Triggers the receive AP item method", 
		"args":[TYPE_STRING, TYPE_INT], 
		"target":[self, "_getApItemConsole"],
	})
	Console.register("getApTapes", {
		"description":"Gives one of each AP bootleg tape", 
		"args":[], 
		"target":[self, "_getApTapesConsole"],
	})

func isConnected():
	return _archipelagoClient.connect_state == BaseArchipelagoClient.ConnectState.CONNECTED_TO_MULTIWORLD

func isInGame():
	return SaveSystem.save_path != "user://unknown.json"

func setHost(host: String):
	_archipelagoClient.server = host

func setPlayer(player: String):
	_archipelagoClient.player = player

func startConnection(password: String = ""):
	if not archipelagoDataManager.getEnabled():
		return
	# intentional fire and forget, all information passed to signal handlers
	_archipelagoClient.connect_to_multiworld(password)

func startDisconnection():
	_archipelagoClient.disconnect_from_multiworld()
	_tempReceivedItems.clear()

func getConnectionState() -> int:
	return _archipelagoClient.connect_state

func _roomInfoReceived(roomInfo: Dictionary):
	randSeed = roomInfo.seed_name.hash()

func _onConnectionChanged(newState: int, error: int = 0):
	emit_signal("connectionStateChanged", newState, error)
	if isConnected() && _locationsCheckedWithoutConnection.size() > 0:
		_archipelagoClient.check_locations(_locationsCheckedWithoutConnection)

# preload has finished, quests now exists
func _onSingleSetupComplete():
	SaveState.quests.connect("quest_completed", self, "_onQuestCompleted")

func _process(delta):
	if WorldSystem.is_in_world() and WorldSystem.is_player_control_enabled():
		_itemGiveTimer -= delta
		if _itemGiveTimer < 0.0:
			_itemGiveTimer = _ITEM_GIVE_DELAY
			if len(_itemsReceivedFromServer) > 0:
				_giveReceivedItems(_itemsReceivedFromServer)
				_itemsReceivedFromServer.clear()
			elif len(_trapsReceivedFromServer) > 0:
				_giveReceivedTraps(_trapsReceivedFromServer)
				_trapsReceivedFromServer.clear()

func _onFileLoaded():
	if !isInGame():
		return 
	SaveState.set_random_seed(randSeed)
	SaveState.achievements.connect("achievement_unlocked", self, "_checkForVictory")
	SaveState.set_flag(ArchipelagoDataManager.AP_ENABLED_KEY, archipelagoDataManager.getEnabled())
	# if it doesn't exist create it
	if !SaveState.other_data.has("archipelago") or !SaveState.other_data["archipelago"].has("receivedItems"):
		SaveState.other_data["archipelago"] = {"receivedItems": []}
	if !SaveState.other_data.has("ap_seed"):
		SaveState.other_data["ap_seed"] = randSeed
	if !SaveState.other_data.has("ap_player"):
		SaveState.other_data["ap_player"] = _archipelagoClient.player
	SaveState.other_data["ap_locations_checked"] = getCheckedLocationCount()
	SaveState.other_data["ap_locations_total"] = getTotalLocationCount()
	for data in _tempReceivedItems:
		_onApItemReceived(data.itemData, data.networkItem)
	_tempReceivedItems.clear()

func _onQuestCompleted(quest_res: Resource):
	var quest = quest_res.instance()
	if "required_item" in quest:
		var questItem = quest.required_item
		if questItem && checkItemDrop(ItemFactory.get_id(questItem)):
			handleItemDrop(ItemFactory.get_id(questItem))

func _getApItemConsole(itemName: String, itemAmount: int):
	_giveReceivedItems([GivenApItem.new([itemName, itemAmount])])

func _getApTapesConsole():
	var items_to_give = []
	var items = ["blizzard", "contagion", "damascus", "deluge", "earthquake", "ferocious", "glitter_bomb", "inferno", "maelstrom", "overgrowth", "plastic", "stained_glass", "tornado"]
	for item in items:
		var cbItem = ItemFactory.create_from_id("res://mods/archipelago_companion/items/ap_tape_%s.tres" % item)
		items_to_give.append({"item": cbItem, "amount": 1})
	MenuHelper.give_items(items_to_give)

# recieving items from server
# itemData is [itemName, itemAmount]
# networkItem is {item: int, location: int, ...}
func _onApItemReceived(itemData: Array, networkItem: Dictionary):
	if !isInGame() || !SaveState.other_data.has("archipelago"):
		_tempReceivedItems.append({"itemData": itemData, "networkItem": networkItem})
		return
	if networkItem.location in SaveState.other_data.archipelago.receivedItems:
		print("The location %d already exists" % networkItem.location)
		return
	if networkItem.location > 0:
		SaveState.other_data.archipelago.receivedItems.push_back(networkItem.location)
	_itemsReceivedFromServer.append(GivenApItem.new(itemData))

func _giveReceivedItems(givenItems: Array):
	var cbItemsToGive = []
	for givenItem in givenItems:
		var itemName: String = givenItem.itemName
		if "ap_tape" in itemName:
			itemName = "res://mods/archipelago_companion/items/%s.tres" % itemName
		var itemAmount: int = givenItem.itemAmount
		var cbItem = ItemFactory.create_from_id(itemName)
		if cbItem != null:
			cbItemsToGive.append({"item": cbItem, "amount": itemAmount})
			continue
		
		if "ap_trap" in itemName:
			_trapsReceivedFromServer.append(itemName)
		
		if SaveState.abilities.has(itemName):
			_onAbilityReceived(itemName)
		
		if "progressive" in itemName:
			if "glide" in itemName:
				_onAbilityReceived("flight" if SaveState.has_ability("glide") else "glide")
			if "magnetism" in itemName:
				if SaveState.has_ability("magnetism"):
					SaveState.stats.get_stat("exchange_purchased").report_event("ability_advantage_magnetism")
				else:
					_onAbilityReceived("magnetism")
			if "dash" in itemName:
				if SaveState.has_ability("dash"):
					SaveState.stats.get_stat("exchange_purchased").report_event("ability_advantage_dash")
				else:
					_onAbilityReceived("dash")
			if "climb" in itemName:
				if SaveState.has_ability("climb"):
					SaveState.stats.get_stat("exchange_purchased").report_event("ability_advantage_climb")
				else:
					_onAbilityReceived("climb")
		
		if "aa_" in itemName:
			_onSongReceived(itemName)
		
		if "_stamp" in itemName:
			_onStampReceived(itemName)
		
		if itemName == "ap_stamina":
			_increaseStamina()
		
	if !cbItemsToGive.empty():
		MenuHelper.give_items(cbItemsToGive)

func _giveReceivedTraps(givenTraps: Array):
	var encounter = EncounterConfig.new()
	for givenTrap in givenTraps:
		if "solo" in givenTrap:
			var character = CharacterConfig.new()
			character.base_character = preload("res://data/characters/blank_monster.tres")
			character.pronouns = randi() % 3
			character.level_override = WorldSystem.get_player().character.level
			var tape = TapeConfig.new()
			tape.set("form", load("res://data/monster_forms/%s.tres" % givenTrap.replace("ap_trap_solo_", "")))
			tape.set("tape_seed_value", randi())
			encounter.add_child(character)
			character.add_child(tape)
		elif "swarm" in givenTrap:
			for i in range(5):
				var character = CharacterConfig.new()
				character.base_character = preload("res://data/characters/blank_monster.tres")
				character.pronouns = randi() % 3
				character.level_override = int(WorldSystem.get_player().character.level / 2)
				var tape = TapeConfig.new()
				tape.set("form", load("res://data/monster_forms/%s.tres" % givenTrap.replace("ap_trap_swarm_", "")))
				tape.set("tape_seed_value", randi())
				encounter.add_child(character)
				character.add_child(tape)
		elif "special" in givenTrap:
			match givenTrap.replace("ap_trap_special_", ""):
				"starters":
					specialTrapStarters(encounter)
				"partners":
					specialTrapPartners(encounter)
				"fused":
					specialTrapFused(encounter)
	if encounter.get_child_count() > 0:
		encounter.run_encounter(encounter.get_config())
	if len(givenTraps) > 1:
		showPassiveMessage("Recieved %s Traps" % len(givenTraps))
	else:
		showPassiveMessage("Recieved Trap")
	print("Traps given to player: ", givenTraps)

func _onAbilityReceived(abilityName: String):
	SaveState.set_ability(abilityName, true)
	showPassiveMessage("Recieved %s" % abilityName)
	print("Ability %s given to player" % abilityName)

func _onSongReceived(aaName: String):
	SaveState.set_flag("ap_song_part_" + aaName, true)
	showPassiveMessage("Recieved Song Part")
	print("Song for archangel %s given to player" % aaName)

func _onStampReceived(stampFlag: String):
	SaveState.set_flag(stampFlag, true)
	var msg_words = stampFlag.replace("ap_", "").split("_")
	msg_words[1].replace("cleeo", "Clee-o").replace("dreadful", "Penny Dreadful")
	for i in range(len(msg_words)):
		msg_words[i] = msg_words[i].capitalize()
	showPassiveMessage("Recieved %s" % " ".join(msg_words))
	print("Stamp for captain %s given to player" % msg_words[1])

func _increaseStamina():
	SaveState.max_stamina += 0.5
	showPassiveMessage("Stamina increased to %s" % SaveState.max_stamina)
	print("Stamina increased to %s" % SaveState.max_stamina)

func _onFlagChanged(flag: String, value: bool):
	if "encounter_captain" in flag and value:
		sendCaptainDefeated(flag)
	if "encounter_aa" in flag and value:
		sendArchAngelDefeated(flag)
	if flag in _AP_EVENT_FLAGS_TO_AP.keys() and value:
		print("%s flag changed, Sending set message: %s" % [flag, _AP_EVENT_FLAGS_TO_AP[flag]])
		_archipelagoClient.set_value(_AP_EVENT_FLAGS_TO_AP[flag],
			"replace", 1)
	_checkForVictory()

# sending checks to server
func _sendCheckLocation(location: String):
	if !isConnected():
		_locationsCheckedWithoutConnection.append(location)
		return
	_archipelagoClient.check_locations([location])
	SaveState.other_data.ap_locations_checked += 1

func sendChestOpened(chestFlag: String):
	print("Opened chest: %s" % chestFlag)
	# there may be some additional information added
	_sendCheckLocation(chestFlag)

func sendArchAngelDefeated(aaFlag: String):
	var locationString = "ap_" + aaFlag
	print("Archangel defeated: %s" % locationString)
	SaveState.stats.get_stat(_AP_AA_DEFEATED_KEY).set_count(locationString, 1)
	_sendCheckLocation(locationString)

func sendAbilityUnlocked(abilityName: String):
	print("Ability Unlocked: %s" % abilityName)
	# there may be some additional information added
	#_sendCheckLocation(abilityName)

func sendCaptainDefeated(captainFlag: String):
	print("Captain Defeated: %s" % captainFlag)
	# there may be some additional information added
	_sendCheckLocation(captainFlag)

func sendSpecies(species_key: String):
	print("Recorded species: %s" % species_key)
	if getSetting("tapesanity") == 1:# specific
		_sendCheckLocation("record_%s" % species_key)

func sendBootlegSpecies(species_key: String, type: String):
	print("Recorded bootleg: %s %s" % [type, species_key])
	if getSetting("bootlegsanity") == 1:# per tape
		_sendCheckLocation("record_bootleg_%s" % species_key)
	elif getSetting("bootlegsanity") == 2:# specific
		_sendCheckLocation("record_%s_%s" % [type, species_key])

func checkRecorded(obtained: Dictionary):
	for species_key in obtained.keys():
		sendSpecies(species_key)
		for type in obtained[species_key]:
			if type != "":
				sendBootlegSpecies(species_key, type)

func checkItemDrop(itemName: String):
	return itemName in _archipelagoClient.slot_data["itemDrop_to_location"]

func handleItemDrop(itemName: String):
	if !(itemName in _archipelagoClient.slot_data["itemDrop_to_location"]):
		return null
	var location = _archipelagoClient.slot_data["itemDrop_to_location"][itemName]
	_sendCheckLocation(location)
	return location

func handleGiveItemAction(itemName: String):
	if !(itemName in _archipelagoClient.slot_data["giveItemAction_to_location"]):
		return null
	var location = _archipelagoClient.slot_data["giveItemAction_to_location"][itemName]
	_sendCheckLocation(location)
	return location

func specialTrapStarters(encounter: EncounterConfig):
	for mon in ["bansheep", "candevil"]:
		var character = CharacterConfig.new()
		character.base_character = preload("res://data/characters/blank_monster.tres")
		character.pronouns = randi() % 3
		character.level_override = WorldSystem.get_player().character.level
		var tape = TapeConfig.new()
		tape.set("form", load("res://data/monster_forms/%s.tres" % mon))
		tape.set("tape_seed_value", randi())
		encounter.add_child(character)
		character.add_child(tape)

func specialTrapPartners(encounter: EncounterConfig):
	for mon in ["sirenade", "kittelly", "clocksley", "brushroom", "spirouette", "pombomb", "bear1"]:
		var character = CharacterConfig.new()
		character.base_character = preload("res://data/characters/blank_monster.tres")
		character.pronouns = randi() % 3
		character.level_override = int(WorldSystem.get_player().character.level / 3)
		var tape = TapeConfig.new()
		tape.set("form", load("res://data/monster_forms/%s.tres" % mon))
		tape.set("tape_seed_value", randi())
		encounter.add_child(character)
		character.add_child(tape)

func specialTrapFused(encounter: EncounterConfig):
	var character = FusedCharacterConfig.new()
	character.base_character = preload("res://data/characters/blank_monster.tres")
	character.pronouns = randi() % 3
	character.level_override = int(WorldSystem.get_player().character.level)
	var tape1 = TapeConfig.new()
	tape1.set("form", load("res://data/monster_forms/traffikrab.tres"))
	tape1.set("tape_seed_value", randi())
	var tape2 = TapeConfig.new()
	tape2.set("form", load("res://data/monster_forms/traffikrab.tres"))
	tape2.set("tape_seed_value", randi())
	encounter.add_child(character)
	character.add_child(tape1)
	character.add_child(tape2)

func showPassiveMessage(message: String, speaker: String = "Archipelago"):
	var msg = PassiveMessageAction.new()
	msg.speaker_name = speaker
	msg.message = message
	msg.use_pawn_npc_name = false
	WorldSystem.add_child(msg)
	msg._run()
	msg.queue_free()

# refactor to getItem that will return either the apItem if remote
# or the acutal item if local, and figure out the location id and add it to the
# array of received locations
func getItemString(locationString: String):
	var apName = _archipelagoClient.slot_data["location_cbName_to_apName"][locationString]
	var locationId = _archipelagoClient.data_package.location_name_to_id[apName]
	if !_archipelagoClient.locationId_itemInfo.has(locationId):
		#var itemData = _archipelagoClient.slot_data["item_apName_to_cbItemData"][apName]
		return "Self Item"
	var itemInfo = _archipelagoClient.locationId_itemInfo[locationId]
	return "Sent %s to %s" % [itemInfo.itemName, itemInfo.playerName]

func getSetting(setting: String):
	if _apWebSocketConnection.connection_state != 1:
		return null
	return _archipelagoClient.slot_data.settings[setting]

func getTotalLocationCount() -> int:
	return _archipelagoClient.missing_locations.size() + _archipelagoClient.checked_locations.size()

func getCheckedLocationCount() -> int:
	return _archipelagoClient.checked_locations.size()

func _checkForVictory():
	if !isConnected():
		return
	# victory logic:
	# Escape - Complete Land of Confusion
	# Captain - Beat Ianthe and become a Captain
	# Sunny - Complete People are People
	# Pier - Complete Pier of the Unknown (Requires DLC)
	# Archangel Hunt - Defeat a selection of Archangels
	var passingChecks = 0
	var victoryConditions = _archipelagoClient.slot_data.settings.goal
	if victoryConditions.has("Escape") && SaveState.has_flag("encounter_aa_aleph_null"):
		passingChecks += 1
	if victoryConditions.has("Captain") && SaveState.has_flag("encounter_ianthe"):
		passingChecks += 1
	if victoryConditions.has("Sunny") && SaveState.achievements.is_unlocked("quest_sunny"):
		passingChecks += 1
	if victoryConditions.has("Pier") && false: # not sure what flag this is
		passingChecks += 1
	if victoryConditions.has("Archangel Hunt") && false: # need number required
		SaveState.stats.get_stat(_AP_AA_DEFEATED_KEY).total
		passingChecks += 1
	if passingChecks >= victoryConditions.size():
		print("VICTORY!")
		_archipelagoClient.set_status(30)
