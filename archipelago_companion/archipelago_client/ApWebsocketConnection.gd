extends Node

enum State {
	STATE_CONNECTING = 0
	STATE_OPEN = 1
	STATE_CLOSING = 2
	STATE_CLOSED = 3
}

const _DEFAULT_PORT = 38281
const _CONNECT_TIMEOUT_SECONDS = 5

# The client handles connecting to the server, and the peer handles sending/receiving
# data after connecting. We set the peer in the "_on_connection_established" callback,
# and clear it in the "_on_connection_closed" callback.
var _client: WebSocketClient
var _peer: WebSocketPeer
var _url: String
var _waiting_to_connect_to_server = null

var connection_state = State.STATE_CLOSED

signal connection_state_changed
signal on_connected(connection_data)
signal on_connection_refused(refused_reason)
signal on_room_info(room_info)
signal on_received_items
signal on_location_info
signal on_room_update
signal on_print_json
signal on_data_package
signal on_bounced
signal on_invalid_packet
signal on_retrieved
signal on_set_reply

signal _stop_waiting_to_connect(success)

func _ready():
	# Always process so we don't disconnect if the game is paused for too long.
	pause_mode = Node.PAUSE_MODE_PROCESS

# Public API
func connect_to_server(server: String) -> bool:
	if connection_state == State.STATE_OPEN:
		return true
	_set_connection_state(State.STATE_CONNECTING)
	
	
	#var nws = NakamaSocketAdapter.new()
	#add_child(nws)
	#nws.connect("closed", self, "_on_connection_closed")
	#nws.connect("received", self, "_on_data_received")
	#nws.connect("connected", self, "_on_connection_established")
	#nws.connect("received_error", self, "_on_connection_error")
	#nws.connect_to_host(server, 5)
	#yield(self, "_stop_waiting_to_connect")
	#return false

	# TODO: It would be nice to move a lot of this into a separate factory class so we
	# didn't have to duplicate code for the WSS and WS cases, and so we don't have
	# methods that all only called a specific times which could otherwise be discarded.
	# But, my one attempt at doing so led to weird cases where the WS client didn't
	# correctly perform the handshake with the server.

	# Use the default Archipelago port if not included in the URL
	var port_check_pattern = RegEx.new()
	port_check_pattern.compile(":(\\d+)$")
	var server_has_port = port_check_pattern.search(server)
	if not server_has_port:
		server = "%s:%d" % [server, _DEFAULT_PORT]

	# Try to connect with SSL first
	var wss_url = "wss://%s" % [server]

	# Create a timeout to trigger the done waiting signal if we take too long
	_init_client()
	_waiting_to_connect_to_server = wss_url
	_make_connection_timeout(wss_url)
	var _result = _client.connect_to_url(wss_url) # Return value is useless

	var wss_success = yield (self, "_stop_waiting_to_connect")
	_waiting_to_connect_to_server = null

	var ws_success = false
	if not wss_success:
		# We don't have any info on why the connection failed (thanks Godot), so we
		# assume it was because the server doesn't support SSL. So, try connecting using
		# "ws://" instead.
		print("Connecting with WSS failed, trying WS.")
		var ws_url = "ws://%s" % [server]
		_init_client()
		_waiting_to_connect_to_server = ws_url
		_make_connection_timeout(ws_url)
		_result = _client.connect_to_url(ws_url)

		ws_success = yield (self, "_stop_waiting_to_connect")
		_waiting_to_connect_to_server = null
		if ws_success:
			_url = ws_url
	else:
		_url = wss_url

	if wss_success or ws_success:
		_peer = _client.get_peer(1)
		_peer.set_write_mode(WebSocketPeer.WRITE_MODE_TEXT)
		_set_connection_state(State.STATE_OPEN)
		print("Connected to multiworld %s." % _url)
	
	return wss_success or ws_success

func connected_to_server() -> bool:
	return connection_state == State.STATE_OPEN
	
func disconnect_from_server():
	if connection_state == State.STATE_CLOSED:
		return
	_set_connection_state(State.STATE_CLOSING)
	# The "connection_closed" signal handler will take care of cleanup
	_client.disconnect_from_host()

func send_connect(game: String, user: String, password: String="", slot_data: bool=true):
	_send_command({
		"cmd": "Connect",
		"game": game,
		"name": user,
		"password": password,
		"uuid": "Godot %s: %s" % [game, user], # TODO: What do we need here? We can't generate an actual UUID in 3.5
		"version": {"major": 0, "minor": 5, "build": 0, "class": "Version"},
		"items_handling": 0b111, # TODO: argument
		"tags": [],
		"slot_data": slot_data
	})

func send_sync():
	_send_command({"cmd": "Sync"})

func send_location_checks(locations: Array):
	_send_command(
		{
			"cmd": "LocationChecks",
			"locations": locations,
		}
	)

# TODO: create_as_hint Enum
func send_location_scouts(locations: Array, create_as_hint: int):
	_send_command({
		"cmd": "LocationScouts",
		"locations": locations,
		"create_as_hint": create_as_hint
	})

func status_update(status: int):
	_send_command({
		"cmd": "StatusUpdate",
		"status": status,
	})

func say(text: String):
	_send_command({
		"cmd": "Say",
		"text": text,
	})

func get_data_package(games = null):
	if not games:
		_send_command({
			"cmd": "GetDataPackage",
		})
	else:
		_send_command({
			"cmd": "GetDataPackage",
			"games": games,
		})

func bounce(games: Array, slots: Array, tags: Array, data: Dictionary):
	_send_command({
		"cmd": "Bounce",
		"games": games,
		"slots": slots,
		"tags": tags,
		"data": data,
	})

# TODO: Extra custom arguments
func get_value(keys: Array):
	# This is Archipelago's "Get" command, we change the name 
	# since "get" is already taken by "Object.get".
	_send_command({
		"cmd": "Get",
		"keys": keys,
	})

# TODO: DataStorageOperation data type
func set_value(key: String, default, want_reply: bool, operations: Array):
	_send_command({
		"cmd": "Set",
		"key": key,
		"default": default,
		"want_reply": want_reply,
		"operations": operations,
	})

func set_notify(keys: Array):
	_send_command({
		"cmd": "SetNotify",
		"keys": keys,
	})

# WebSocketClient callbacks
func _on_connection_established(_proto=""):
	# We succeeded, stop waiting and tell the caller.
	emit_signal("_stop_waiting_to_connect", true)

func _on_connection_error():
	# We failed, stop waiting and tell the caller.
	emit_signal("_stop_waiting_to_connect", false)

func _on_connection_closed(was_clean=false):
	_set_connection_state(State.STATE_CLOSED)
	_peer = null

func _on_data_received():
	if self._peer == null:
		# Rare case where we have an dead connection to a server that suddenly
		# becomes active. Just ignore because we're not setup for it.
		return
	var received_data_str = _peer.get_packet().get_string_from_utf8()
	var received_data = JSON.parse(received_data_str)
	if received_data.result == null:
		print("Failed to parse JSON for %s" % received_data_str)
		return
	for command in received_data.result:
		_handle_command(command)

# Internal plumbing
func _send_command(args: Dictionary):
	print("Sending %s command" % args["cmd"])
	var command_str = JSON.print([args])
	if _peer != null:
		var _result = _peer.put_packet(command_str.to_ascii())
	else:
		print("Peer is null")

func _init_client():
	if self._client != null:
		# Disconnect signals from the old client reference
		self._client.disconnect("connection_closed", self, "_on_connection_closed")
		self._client.disconnect("data_received", self, "_on_data_received")
		self._client.disconnect("connection_established", self, "_on_connection_established")
		self._client.disconnect("connection_error", self, "_on_connection_error")
	self._client = WebSocketClient.new()
	print(self._client)
	
	# Connect base signals to get notified of connection open, close, and errors.
	var _result = self._client.connect("connection_closed", self, "_on_connection_closed")
	_result = self._client.connect("data_received", self, "_on_data_received")
	_result = self._client.connect("connection_established", self, "_on_connection_established")
	_result = self._client.connect("connection_error", self, "_on_connection_error")
	
	# Increase max buffer size to accommodate AP's larger payloads. The defaults are:
	#   - Max in/out buffer = 64 KB
	#   - Max in/out packets = 1024 
	# We increase the in buffer to 20 MB because some messages we receive are too large
	# for 64. The other defaults are fine though.
	# Figuring out how to retrofit compressed websockets would allow us to reduce the buffer significantly
	_result = _client.set_buffers(1024 * 20, 1024, 64, 1024)
	
	self._peer = null

func _make_connection_timeout(for_url: String):
	yield (GlobalMenuDialog.get_tree().create_timer(_CONNECT_TIMEOUT_SECONDS), "timeout")
	if _waiting_to_connect_to_server == for_url:
		# We took to long, stop waiting and tell the called we failed.
		_waiting_to_connect_to_server = false
		emit_signal("_stop_waiting_to_connect", false)

func _set_connection_state(state):
	var state_name = State.keys()[state]
	print("AP connection state changed to: %s." % state_name)
	connection_state = state
	emit_signal("connection_state_changed", connection_state)

func _handle_command(command: Dictionary):
	match command["cmd"]:
		"RoomInfo":
			emit_signal("on_room_info", command)
		"ConnectionRefused":
			emit_signal("on_connection_refused", command)
		"Connected":
			emit_signal("on_connected", command)
		"ReceivedItems":
			emit_signal("on_received_items", command)
		"LocationInfo":
			emit_signal("on_location_info", command)
		"RoomUpdate":
			emit_signal("on_room_update", command)
		"PrintJSON":
			emit_signal("on_print_json", command)
		"DataPackage":
			emit_signal("on_data_package", command)
		"Bounced":
			emit_signal("on_bounced", command)
		"InvalidPacket":
			emit_signal("on_invalid_packet", command)
		"Retrieved":
			emit_signal("on_retrieved", command)
		"SetReply":
			emit_signal("on_set_reply", command)
		_:
			print("Received Unknown Command %s" % command["cmd"])

func _process(_delta):
	# Only run when the connection the the server is not closed.
	if _client != null:
		_client.poll()
