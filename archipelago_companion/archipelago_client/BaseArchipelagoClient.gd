## Base Godot Archipelago Client
## Mostly copied from Rampaging Hippy's Brotato godot_ap_client implementation
##
## Manages the connection to the server, raises signals when Server-Client packets are
## received, and stores information about the connect multiworld room and slot.
##
## In addition, provides methods for sending Client-Server commands, and high-level API
## for common workflows such as establishing the connection.

class_name BaseArchipelagoClient
extends Node

const _AP_TYPES = preload("./ApTypes.gd")

enum ConnectState {
	DISCONNECTED = 0
	CONNECTING = 1
	DISCONNECTING = 2
	CONNECTED_TO_SERVER = 3
	CONNECTED_TO_MULTIWORLD = 4
}

enum ConnectResult {
	SUCCESS = 0
	SERVER_CONNECT_FAILURE = 1
	PLAYER_NOT_SET = 2
	GAME_NOT_SET = 3
	INVALID_SERVER = 4
	# The following correspond to the errors the AP ConnectionRefused message can send.
	AP_INVALID_SLOT = 5
	AP_INVALID_GAME = 6
	AP_INCOMPATIBLE_VERSION = 7
	AP_INVALID_PASSWORD = 8
	AP_INVALID_ITEMS_HANDLING = 9
	# Fallback in case a new error is added that we don't support yet
	AP_CONNECTION_REFUSED_UNKNOWN_REASON = 10
	ALREADY_CONNECTED = 11
}

class ApDataPackage:
	var item_name_to_id: Dictionary
	var location_name_to_id: Dictionary
	var item_id_to_name: Dictionary
	var location_id_to_name: Dictionary
	var version: int
	var checksum: String

	func _init(data_package_object: Dictionary):
		checksum = data_package_object["checksum"]
		item_name_to_id = data_package_object["item_name_to_id"]
		location_name_to_id = data_package_object["location_name_to_id"]

		item_id_to_name = Dictionary()
		for item_name in item_name_to_id:
			var item_id = item_name_to_id[item_name]
			item_id_to_name[item_id] = item_name
			
		location_id_to_name = Dictionary()
		for location_name in location_name_to_id:
			var location_id = location_name_to_id[location_name]
			location_id_to_name[location_id] = location_name

const ArchipelagoDataManager = preload("res://mods/archipelago_companion/managers/ArchipelagoDataManager.gd")

var websocket_client
var dataManager: ArchipelagoDataManager
var connect_state = ConnectState.DISCONNECTED
var player: String = ""
var server: String = "archipelago.gg"
var game: String = ""

var team: int
var slot: int
var players: Array
var missing_locations: Array
var checked_locations: Array
var slot_data: Dictionary
var slot_info: Dictionary
var hint_points: int

var room_info: Dictionary
var data_package: ApDataPackage
var gameToDataPackage: Dictionary
var locationId_itemInfo: Dictionary

signal _received_connect_response(message)
## Sent when the connection status to the server changes.
##
## Includes the new server state (one of `GodotApClient.ConnectResult`), and an error
## code if the connection encountered an error.
signal connection_state_changed(state, error)
signal item_received(item_data, network_item)
## Sent when a `SetReply` packet is received. Contains the key and new and old values.
signal data_storage_updated(key, new_value, original_value)
## Emitted when a `RoomUpdate` packet is received. Contains the new room information.
signal room_updated(updated_room_info)

func _init(websocket_client_):
	self.websocket_client = websocket_client_
	self.dataManager = ArchipelagoDataManager.new()

func _ready():
	websocket_client.connect("on_received_items", self, "_on_received_items")
	websocket_client.connect("on_set_reply", self, "_on_set_reply")
	websocket_client.connect("on_retrieved", self, "_on_retrieved")
	websocket_client.connect("on_room_update", self, "_on_room_update")

func _connected_or_connection_refused_received(message: Dictionary):
	emit_signal("_received_connect_response", message)

func connect_to_multiworld(password: String="", get_data_pacakge: bool=true) -> int:
	## Connect to the multiworld using the host/port/player/password provided.
	##
	## NOTE: The game, server, and player fields for the class MUST be set before
	## calling this. Otherwise, this will not attempt to connect will return an error
	## code.
	##
	## This follows the Archipelago Connection Handshake as closely as possible to
	## connect to the server. Depending on the current connection state, this behaves
	## differently:
	##	- If the client is not connected, establishes the connection to the server, then
	##	  sends a `Connect` packet to connect to a slot in the room using the provided
	##	  player name and password.
	##	- If the client is connected to a server, but hasn't connected to a slot in the
	##	  room yet, it uses the existing server connection and skips to sending the
	##	  `Connect` packet.
	##		- This allows the client to be connected in steps, in case the player name
	##		  or password was invalid. It also matches the AP Text Client behavior.
	##	- If the client is already connected to a server, does nothing and returns 
	##	  ALREADY_CONNECTED. 
	##		- The client must be explicitly disconnected with `disconnect` to change 
	##		  servers.
	##
	## Returns a status code, whichis one of `GodotApClient.ConnectResult`, indicating
	## the connection result.
	if websocket_client.connected_to_server() and self.connect_state == ConnectState.CONNECTED_TO_MULTIWORLD:
		return ConnectResult.ALREADY_CONNECTED
	elif player.strip_edges().empty():
		return ConnectResult.PLAYER_NOT_SET
	elif server.strip_edges().empty():
		return ConnectResult.INVALID_SERVER
	elif game.strip_edges().empty():
		return ConnectResult.GAME_NOT_SET

	_set_connection_state(ConnectState.CONNECTING)

	# Go through the handshake at below in order:
	# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/network%20protocol.md#archipelago-connection-handshake

	# 1. Client establishes WebSocket connection to the Archipelago server.
	# Skip if we're already connected to a server
	if not websocket_client.connected_to_server():
		var funcstate = websocket_client.connect_to_server(server)
		var server_connect_result = yield (funcstate, "completed")

		if server_connect_result == false:
			_set_connection_state(ConnectState.DISCONNECTED, ConnectResult.SERVER_CONNECT_FAILURE)
			return ConnectResult.SERVER_CONNECT_FAILURE
		else:
			_set_connection_state(ConnectState.CONNECTED_TO_SERVER)
			connect_state = ConnectState.CONNECTED_TO_SERVER
	
		# 2. Server accepts connection and responds with a RoomInfo packet.
		room_info = yield (websocket_client, "on_room_info")

		# 3. Get all games' data package
		var games = []
	
		for game in room_info.games:
			if !(game in games):
				games.append(game)
				# check to see if we have this game's data package already
				var cachedDataPackage = dataManager.getDataPackage(game)
				var remoteCheck = room_info.datapackage_checksums[game]
				if cachedDataPackage != null && remoteCheck == cachedDataPackage.checksum:
					self.gameToDataPackage[game] = ApDataPackage.new(cachedDataPackage)
				else:
					websocket_client.get_data_package([game])
					var data_package_message = yield (websocket_client, "on_data_package")
					for gameName in data_package_message["data"]["games"].keys():
						dataManager.setDataPackage(gameName, data_package_message["data"]["games"][gameName])
						self.gameToDataPackage[gameName] = ApDataPackage.new(data_package_message["data"]["games"][gameName])
		
		# 4. Grab our data package for easier reference
		if get_data_pacakge:
			data_package = self.gameToDataPackage[self.game]

	# 5. Client sends Connect packet in order to authenticate with the server.
	# 6. Server validates the client's packet and responds with Connected or
	#    ConnectionRefused.

	# Wait for the first response the server sends back
	var _result = websocket_client.connect(
		"on_connected",
		self,
		"_connected_or_connection_refused_received"
	)
	_result = websocket_client.connect(
		"on_connection_refused",
		self,
		"_connected_or_connection_refused_received"
	)
	if room_info.password:
		websocket_client.send_connect(game, player, password)
	else:
		websocket_client.send_connect(game, player)
	var connect_response = yield (self, "_received_connect_response")

	if connect_response["cmd"] == "ConnectionRefused":
		# There may be multiple errors, but there isn't a clean way in Godot to return
		# them all. Just return the first error the multiworld server sent us.
		var ap_error: int
		match connect_response["errors"][0]:
			"InvalidSlot":
				ap_error = ConnectResult.AP_INVALID_SLOT
			"InvalidGame":
				ap_error = ConnectResult.AP_INVALID_GAME
			"IncompatibleVersion":
				ap_error = ConnectResult.AP_INCOMPATIBLE_VERSION
			"InvalidPassword":
				ap_error = ConnectResult.AP_INVALID_PASSWORD
			"InvalidItemsHandling":
				ap_error = ConnectResult.AP_INVALID_ITEMS_HANDLING
			_:
				ap_error = ConnectResult.AP_CONNECTION_REFUSED_UNKNOWN_REASON
		self._set_connection_state(self.connect_state, ap_error)
		return ap_error

	self.team = connect_response["team"]
	self.slot = connect_response["slot"]
	self.players = connect_response["players"]
	self.missing_locations = connect_response["missing_locations"].duplicate()
	self.checked_locations = connect_response["checked_locations"].duplicate()
	self.slot_data = connect_response["slot_data"]
	self.slot_info = connect_response["slot_info"]
	self.hint_points = connect_response["hint_points"]

	# The last two steps are handled by signal handlers and other classes.
	# 7. Server may send ReceivedItems to the client, in the case that the client is
	#    missing items that are queued up for it.
	# 8. Server sends PrintJSON to all players to notify them of the new client
	#    connection.

	_set_connection_state(ConnectState.CONNECTED_TO_MULTIWORLD)
	
	# We scout all of our missing locations in order to setup sent item text
	websocket_client.send_location_scouts(missing_locations, 0)
	var locationInfo = yield (websocket_client, "on_location_info")
	var slotId_playerName:Dictionary
	for player in self.players:
		slotId_playerName[player.slot] = player.alias
	for networkItem in locationInfo.locations:
		var locationId = networkItem.location
		if networkItem.player == self.slot:
			continue
		var playerName = slotId_playerName[networkItem.player]
		var gameName = self.slot_info[str(networkItem.player)].game
		var itemId_name = self.gameToDataPackage[gameName].item_id_to_name
		var itemName = itemId_name[networkItem.item]
		self.locationId_itemInfo[locationId] = {"playerName": playerName, "itemName": itemName}
	
	return ConnectResult.SUCCESS

func disconnect_from_multiworld():
	## Disconnect from the server. Can be called even when not connected.
	_set_connection_state(ConnectState.DISCONNECTING)
	self.websocket_client.disconnect_from_server()
	_set_connection_state(ConnectState.DISCONNECTED)

func _set_connection_state(state: int, error: int=0):
	print("Setting connection state to %s." % ConnectState.keys()[state])
	self.connect_state = state
	emit_signal("connection_state_changed", self.connect_state, error)

func set_status(status: int):
	## Send a `StatusUpdate` packet with the new client status.
	# TODO: bounds checking
	websocket_client.status_update(status)

func check_locations(location_strings: PoolStringArray):
	## Send a `LocationChecks` packet with the provided location(s).
	## locations will be converted to ids prior to being sent
	## if an id is not found that location will not be sent
	## A single integer/location ID will be wrapped in an array berfore sending.
	if not self.slot_data:
		return
	for location in location_strings:
		if not self.slot_data["location_cbName_to_apName"].has(location):
			print("Location id is not in the location_cbName_to_apName Dict.  Location id: " + location)
			continue
		var apLocationName = self.slot_data["location_cbName_to_apName"][location]
		var location_id = self.data_package.location_name_to_id[apLocationName]
		if not location_id:
			print("Location id could not be found for: " + location)
			continue
		print("Sending location check for " + location + " with id " + str(location_id))
		websocket_client.send_location_checks([location_id])

func scout_locations(location_strings: PoolStringArray):
	if not self.data_package:
		return
	for location in location_strings:
		var apLocationName = self.slot_data["location_cbName_to_apName"][location]
		var location_id = data_package.location_name_to_id[apLocationName]
		if not location_id:
			print("Location id could not be found for: " + location)
			continue
		print("Sending location scout for " + location + " with id " + location_id)
		websocket_client.send_location_scouts([location_id], false)

func get_value(keys: Array):
	## Send a `Get` packet to query the server's data storage.
	##
	## Note that the name does not match the sent packet, since `get` is a predefined
	## method on Godot Objects.
	websocket_client.get_value(keys)

func set_notify(keys: Array):
	## Send a `SetNotify` packet to the server with the provided keys.
	websocket_client.set_notify(keys)

func set_value(key: String, operations, values, default=null, want_reply: bool=false):
	## Send a `Set` packet to the server to update the server's data storage.
	##
	## Note that the name does not match the sent packet, because `set` is a predefined
	## method on Godot Objects.
	var ap_ops = Array()
	# Shorthand to allow more concise single operation argument
	if not (operations is Array):
		# TODO: Check values as well? Hard because update operation takes a dict value.
		operations = [operations]
		values = [values]
	for i in range(operations.size()):
		var operation_obj = {"operation": operations[i],"value": values[i]}
		ap_ops.append(operation_obj)
	websocket_client.set_value(key, default, want_reply, ap_ops)

func _on_received_items(command):
	# TODO: update missing and checked locations?
	# TODO: Since we have a manager we can send the full array
	var network_items = command["items"]
	for network_item in network_items:
		var item_data = null
		if self.slot_data:
			var ap_item_name = self.data_package.item_id_to_name[network_item["item"]]
			item_data = self.slot_data["item_apName_to_cbItemData"][ap_item_name]
		emit_signal("item_received", item_data, network_item)

func _on_retrieved(command):
	# TODO: Custom additional args
	for key in command["keys"]:
		emit_signal(
			"data_storage_updated",
			key,
			command["keys"][key]
		)

func _on_room_update(command: Dictionary):
	if command.has("checked_locations"):
		for location in command["checked_locations"]:
			checked_locations.append(location)
			var missing_idx = missing_locations.find(location)
			missing_locations.remove(missing_idx)
	emit_signal("room_updated", command)

func _on_set_reply(command):
	emit_signal(
		"data_storage_updated",
		command["key"],
		command["value"],
		command["original_value"]
	)
