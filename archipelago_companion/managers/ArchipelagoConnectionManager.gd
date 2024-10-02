#class_name ArchipelagoConnectionManager 
extends Node

const ApWebSocketConnection = preload("res://mods/archipelago_companion/archipelago_client/ApWebsocketConnection.gd")
const BaseArchipelagoClient = preload("res://mods/archipelago_companion/archipelago_client/BaseArchipelagoClient.gd")

var _apWebSocketConnection: ApWebSocketConnection
var _archipelagoClient: BaseArchipelagoClient

signal connectionStateChanged(state, error)

func _init():
	_apWebSocketConnection = ApWebSocketConnection.new()
	_archipelagoClient = BaseArchipelagoClient.new(_apWebSocketConnection)
	self.add_child(_apWebSocketConnection)
	self.add_child(_archipelagoClient)
	_archipelagoClient.game = "Cassette Beasts"
	_archipelagoClient.connect("connection_state_changed", self, "_onConnectionChanged")
	_archipelagoClient.connect("item_received", self, "_onApItemReceived")

func isConnected():
	return _archipelagoClient.connect_state == BaseArchipelagoClient.ConnectState.CONNECTED_TO_MULTIWORLD

func setHost(host: String):
	_archipelagoClient.server = host

func setPlayer(player: String):
	_archipelagoClient.player = player

func startConnection(password: String = ""):
	if not ArchipelagoDataManager.enabled:
		return
	# intentional fire and forget, all information passed to signal handlers
	_archipelagoClient.connect_to_multiworld(password)

func startDisconnection():
	_archipelagoClient.disconnect_from_multiworld()

func getConnectionState() -> int:
	return _archipelagoClient.connect_state

func _onConnectionChanged(newState: int, error: int = 0):
	emit_signal("connectionStateChanged", newState, error)

# recieving items from server
func _onApItemReceived(itemName: String, item: Dictionary):
	pass

func _onItemReceived(item: BaseItem):
	pass

func _onAbilityReceived(abilityName: String):
	pass

func _onSongReceived(aaFlag: String):
	pass

func _onStampReceived(captainName: String):
	pass

# sending checks to server
func _sendCheckLocation(locationId: int):
	_archipelagoClient.check_location(locationId)

func sendChestOpened(chestFlag: String):
	print("Opened chest " + chestFlag)

func sendArchAngelDefeated(aaName: String):
	pass

func sendAbilityUnlocked(abilityName: String):
	pass

func sendCaptainDefeated(captainName: String):
	pass
