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
const _ITEM_GIVE_DELAY = 1.0

var _tempReceivedItems = []

var locationId_ItemDescription: Dictionary

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
	SaveSystem.connect("file_loaded", self, "_onFileLoaded")
	SaveState.connect("flag_changed", self, "_onFlagChanged")
	Console.register("getApItem", {
		"description":"Triggers the receive AP item method", 
		"args":[TYPE_STRING, TYPE_INT], 
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

func _process(delta):
	if WorldSystem.is_in_world() and WorldSystem.is_player_control_enabled():
		_itemGiveTimer -= delta
		if _itemGiveTimer < 0.0:
			_itemGiveTimer = _ITEM_GIVE_DELAY
			_giveReceivedItems(_itemsReceivedFromServer)
			_itemsReceivedFromServer.clear()

func _onFileLoaded():
	SaveState.set_flag(ArchipelagoDataManager.AP_ENABLED_KEY, archipelagoDataManager.getEnabled())
	# if it doesn't exist create it
	if !SaveState.other_data.has("archipelago") or !SaveState.other_data["archipelago"].has("receivedItems"):
		SaveState.other_data["archipelago"] = {"receivedItems": []}
	for data in _tempReceivedItems:
		_onApItemReceived(data.itemData, data.networkItem)
	
	# we now have the full list of items this game has received
	# cross reference that with the list of items in other_data
	# add all missing items to _itemsReceivedFromServer

func _getApItemConsole(itemName: String, itemAmount: int):
	_giveReceivedItems([GivenApItem.new([itemName, itemAmount])])

# recieving items from server
# itemData is [itemName, itemAmount]
# networkItem is {item: int, location: int, ...}
func _onApItemReceived(itemData: Array, networkItem: Dictionary):
	if !SaveState.other_data.has("archipelago"):
		_tempReceivedItems.append({"itemData": itemData, "networkItem": networkItem})
		return
	if networkItem.location in SaveState.other_data.archipelago.receivedItems:
		print("The location %d already exists" % networkItem.location)
		return
	SaveState.other_data.archipelago.receivedItems.push_back(networkItem.location)
	_itemsReceivedFromServer.append(GivenApItem.new(itemData))

func _giveReceivedItems(givenItems: Array):
	var cbItemsToGive = []
	for givenItem in givenItems:
		var itemName: String = givenItem.itemName
		var itemAmount: int = givenItem.itemAmount
		var cbItem = ItemFactory.create_from_id(itemName)
		if cbItem != null:
			cbItemsToGive.append({"item": cbItem, "amount": itemAmount})
			continue
		
		if SaveState.abilities.has(itemName):
			_onAbilityReceived(itemName)
		
		if "progressive" in itemName:
			if "glide" in itemName:
				_onAbilityReceived("flight" if SaveState.has_ability("glide") else "glide")
			if "magnetism" in itemName:
				if SaveState.has_ability("magnetism"):
					pass #TODO ability advantage
				else:
					_onAbilityReceived("magnetism")
			if "dash" in itemName:
				if SaveState.has_ability("dash"):
					pass #TODO ability advantage
				else:
					_onAbilityReceived("dash")
			if "climb" in itemName:
				if SaveState.has_ability("climb"):
					pass #TODO ability advantage
				else:
					_onAbilityReceived("climb")
		
		if "aa_" in itemName:
			_onSongReceived(itemName)
		
		if "_stamp" in itemName:
			_onStampReceived(itemName)
		
	if !cbItemsToGive.empty():
		MenuHelper.give_items(cbItemsToGive)

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

func _onStampReceived(stampFlag: String):
	SaveState.set_flag(stampFlag, true)
	print("Stamp for captain %s given to player" % stampFlag)

func _onFlagChanged(flag: String, value: bool):
	if "captain" in flag and value:
		return sendCaptainDefeated(flag)
	if "aa" in flag and !("encounter" in flag) and value:
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
	#_sendCheckLocation(abilityName)

func sendCaptainDefeated(captainFlag: String):
	print("Captain Defeated: %s" % captainFlag)
	# there may be some additional information added
	_sendCheckLocation(captainFlag)

func handleGiveItemAction(itemName: String):
	if !(itemName in _archipelagoClient.slot_data["giveItemAction_to_location"]):
		return null
	var location = _archipelagoClient.slot_data["giveItemAction_to_location"][itemName]
	_archipelagoClient.check_locations([location])
	return location

func getItemString(locationString: String):
	var apName = _archipelagoClient.slot_data["location_cbName_to_apName"][locationString]
	var locationId = _archipelagoClient.data_package.location_name_to_id[apName]
	if !_archipelagoClient.locationId_itemInfo.has(locationId):
		return "Self Item"
	var itemInfo = _archipelagoClient.locationId_itemInfo[locationId]
	return "Sent %s to %s" % [itemInfo.itemName, itemInfo.playerName]
