extends Node

const ApWebSocketConnection = preload("res://mods/archipelago_companion/archipelago_client/ApWebsocketConnection.gd")
const BaseArchipelagoClient = preload("res://mods/archipelago_companion/archipelago_client/BaseArchipelagoClient.gd")
const ArchipelagoDataManager = preload("res://mods/archipelago_companion/managers/ArchipelagoDataManager.gd")

var archipelagoDataManager: ArchipelagoDataManager

var _apWebSocketConnection: ApWebSocketConnection
var _archipelagoClient: BaseArchipelagoClient

var _itemsReceivedWhileNotInWorld = []

const _ITEM_DIR_PATH = "res://data/items/"

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
	_apWebSocketConnection.connect("on_location_info", self, "_locationInfoReceived")
	SceneManager.connect("scene_changed", self, "_onSceneChanged")
	SaveSystem.connect("file_loaded", self, "_onFileLoaded")
	SaveState.connect("flag_changed", self, "_onFlagChanged")
	Console.register("getApItem", {
		"description":"Triggers the receive AP item method", 
		"args":[TYPE_STRING], 
		"target":[self, "_getApItemConsole"],
	})

func isConnected():
	return _archipelagoClient.connect_state == BaseArchipelagoClient.ConnectState.CONNECTED_TO_MULTIWORLD

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

func getConnectionState() -> int:
	return _archipelagoClient.connect_state

func _locationInfoReceived(locationInfo: Dictionary):
	pass

func _onConnectionChanged(newState: int, error: int = 0):
	emit_signal("connectionStateChanged", newState, error)

func _onSceneChanged():
	if WorldSystem.is_in_world():
		while _itemsReceivedWhileNotInWorld.size() > 0:
			var dict = _itemsReceivedWhileNotInWorld.pop_back()
			_givePlayerItem(dict.itemName, dict.item)

func _onFileLoaded():
	SaveState.set_flag(ArchipelagoDataManager.AP_ENABLED_KEY, archipelagoDataManager.getEnabled())
	# if it doesn't exist create it
	if !SaveState.other_data.has("archipelago") or !SaveState.other_data["archipelago"].has("receivedItems"):
		SaveState.other_data["archipelago"] = {"receivedItems": []}
	# if we are connected then (following is probably in a method as it will
	# also need to happen if the user starts the game and then connects to server)
	# call sync await the packet 
	
	# we now have the full list of items this game has received
	# cross reference that with the list of items in other_data
	# add all missing items to _itemsReceivedWhileNotInWorld

func _getApItemConsole(itemName: String):
	pass
	#_onApItemReceived(itemName, {item = 1, location = 2, player = 3, flags = 0})

# recieving items from server
# item is {item: int, location: int, player: int, flags: int}
# flags are 0b001: logic, 0b010: important, 0b100: trap
func _onApItemReceived(item_data: Array, network_item: Dictionary):
	# assuming that I cannot get an item via item_received more than once
	SaveState.other_data.archipelago.receivedItems.push_back(network_item)
	if !WorldSystem.is_in_world():
		_itemsReceivedWhileNotInWorld.append({"itemName": item_data[0], "itemAmount": item_data[1]})
		return
	_givePlayerItem(item_data[0], item_data[1])

func _givePlayerItem(itemName: String, itemAmount: int):
	# "wood*100"
	if _tryGiveItem(itemName, itemAmount):
		return
	if SaveState.abilities.has(itemName):
		return _onAbilityReceived(itemName)
	if "aa" in itemName:
		return _onSongReceived(itemName)
	if "captain" in itemName:
		return _onStampReceived(itemName)
	print("Unknown AP item received, name: %s" % itemName)

func _isItemResourceName(itemName: String):
	var dir = Directory.new()
	if dir.open(_ITEM_DIR_PATH) == OK:
		dir.list_dir_begin()
		var fileName = dir.get_next()
		while fileName != "":
			if itemName in fileName:
				return true
			fileName = dir.get_next()
	return false

func _tryGiveItem(itemName: String, itemAmount: int):
	var item = ItemFactory.create_from_id(itemName)
	if item == null:
		return false
	MenuHelper.give_item(item, itemAmount, false)
	print("Item %s given to player" % itemName)
	return true

func _onAbilityReceived(abilityName: String):
	SaveState.set_ability(abilityName, true)
	print("Ability %s given to player" % abilityName)

func _onSongReceived(aaName: String):
	SaveState.set_flag("ap_encounter_" + aaName, true)
	print("Song for archangel %s given to player" % aaName)

func _onStampReceived(captainName: String):
	SaveState.set_flag("ap_encounter_" + captainName, true)
	print("Stamp for captain %s given to player" % captainName)

func _onFlagChanged(flag: String, value: bool):
	if "captain" in flag and value:
		return sendCaptainDefeated(flag)
	if "aa" in flag and value:
		return sendArchAngelDefeated(flag)

# sending checks to server
func _sendCheckLocation(location: String):
	_archipelagoClient.check_locations([location])

func sendChestOpened(chestFlag: String):
	print("Opened chest: %s" % chestFlag)
	# there may be some additional information added
	_sendCheckLocation(chestFlag)

func sendArchAngelDefeated(aaFlag: String):
	print("Archangel defeated: %s" % aaFlag)
	# there may be some additional information added
	_sendCheckLocation(aaFlag)

func sendAbilityUnlocked(abilityName: String):
	print("Ability Unlocked: %s" % abilityName)
	# there may be some additional information added
	_sendCheckLocation(abilityName)

func sendCaptainDefeated(captainFlag: String):
	print("Captain Defeated: %s" % captainFlag)
	# there may be some additional information added
	_sendCheckLocation(captainFlag)
