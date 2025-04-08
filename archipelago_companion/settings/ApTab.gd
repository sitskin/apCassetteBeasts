extends Control

const BaseArchipelagoClient = preload("res://mods/archipelago_companion/archipelago_client/BaseArchipelagoClient.gd")

onready var _hostField: LineEdit = find_node("HostEdit")
onready var _playerField: LineEdit = find_node("PlayerEdit")
onready var _passwordField: LineEdit = find_node("PasswordEdit")
onready var _connectButton: Button = find_node("ConnectButton")
onready var _disconnectButton: Button = find_node("DisconnectButton")
onready var _connectionLabel: Label = find_node("ConnectionStatusLabel")
onready var _errorLabel: Label = find_node("ErrorLabel")
onready var _isDebug: bool = OS.has_feature("editor")

onready var archipelagoConnectionManager = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager
onready var archipelagoDataManager = preload("res://mods/archipelago_companion/managers/ArchipelagoDataManager.gd").new()

func _ready():
	_errorLabel.visible = false
	archipelagoConnectionManager.connect("connectionStateChanged", self, "_onConnectionStateChanged")
	_connectButton.connect("pressed", self, "_onConnectButtonPressed")
	_disconnectButton.connect("pressed", self, "_onDisconnectButtonPressed")

# this is called when this tab is switched to
func grab_focus():
	_hostField.text = archipelagoDataManager.getServer()
	_playerField.text = archipelagoDataManager.getPlayer()
	_onEnabledToggled(archipelagoDataManager.getEnabled())
	_hostField.grab_focus()
	# Slight delay to let node tree settle before updating values in the tree
	yield(get_tree().create_timer(0.01), "timeout")
	_onConnectionStateChanged(archipelagoConnectionManager.getConnectionState())

func _onConnectionStateChanged(new_state: int, error: int = 0):
	_errorLabel.visible = false
	_updateFieldsState(new_state == BaseArchipelagoClient.ConnectState.DISCONNECTED)
	match new_state:
		BaseArchipelagoClient.ConnectState.DISCONNECTED:
			_connectionLabel.text = "Disconnected"
			_connectButton.disabled = false
			_disconnectButton.disabled = true
		BaseArchipelagoClient.ConnectState.CONNECTING:
			_connectionLabel.text = "Connecting..."
			_connectButton.disabled = true
			_disconnectButton.disabled = true
		BaseArchipelagoClient.ConnectState.DISCONNECTING:
			_connectionLabel.text = "Disconnecting..."
			_connectButton.disabled = true
			_disconnectButton.disabled = true
		BaseArchipelagoClient.ConnectState.CONNECTED_TO_SERVER:
			_connectionLabel.text = "Connected to server"
			_connectButton.disabled = true
			_disconnectButton.disabled = false
		BaseArchipelagoClient.ConnectState.CONNECTED_TO_MULTIWORLD:
			_connectionLabel.text = "Connected to multiworld"
			_connectButton.disabled = true
			_disconnectButton.disabled = false
	if error != 0:
		_setError(error)

func _updateFieldsState(isDisconnected: bool):
	_hostField.editable = isDisconnected
	_playerField.editable = isDisconnected
	_passwordField.editable = isDisconnected

func _disableAll():
	_hostField.editable = false
	_playerField.editable = false
	_passwordField.editable = false
	_connectButton.disabled = true
	_disconnectButton.disabled = true
	_connectionLabel.text = "Start a game to connect to the Archipelago Server"

func _setError(error_reason: int):
	_errorLabel.visible = true
	match error_reason:
		BaseArchipelagoClient.ConnectResult.SERVER_CONNECT_FAILURE:
			_errorLabel.text = "Failed to connect to the server"
		BaseArchipelagoClient.ConnectResult.PLAYER_NOT_SET:
			_errorLabel.text = "Need to set player name before connecting"
		BaseArchipelagoClient.ConnectResult.GAME_NOT_SET:
			_errorLabel.text = "Client needs to set game name before connecting"
		BaseArchipelagoClient.ConnectResult.INVALID_SERVER:
			_errorLabel.text = "Invalid server name"
		BaseArchipelagoClient.ConnectResult.AP_INVALID_SLOT:
			_errorLabel.text = "AP: Invalid player name"
		BaseArchipelagoClient.ConnectResult.AP_INVALID_GAME:
			_errorLabel.text = "AP: Invalid game"
		BaseArchipelagoClient.ConnectResult.AP_INCOMPATIBLE_VERSION:
			_errorLabel.text = "AP: Incompatible versions"
		BaseArchipelagoClient.ConnectResult.AP_INVALID_PASSWORD:
			_errorLabel.text = "AP: Invalid or missing password"
		BaseArchipelagoClient.ConnectResult.AP_INVALID_ITEMS_HANDLING:
			_errorLabel.text = "AP: Invalid items handling"
		BaseArchipelagoClient.ConnectResult.AP_CONNECTION_REFUSED_UNKNOWN_REASON:
			_errorLabel.text = "AP: Failed to connect (unknown error)"
		_:
			_errorLabel.text = "Unknown error"

func _onConnectButtonPressed():
	if _isDebug:
		print("Connect button pressed")
	if !(_hostField.text.length() > 0 || _playerField.text.length() > 0):
		_errorLabel.text = "Please fill out both host and player fields"
		_errorLabel.visible = true
		return
	archipelagoConnectionManager.setHost(_hostField.text)
	archipelagoConnectionManager.setPlayer(_playerField.text)
	# NOTE: Do not save the password in the save state, I know it technically doesn't
	# matter but the security part of my brain would break if we saved this
	archipelagoDataManager.setServer(_hostField.text)
	archipelagoDataManager.setPlayer(_playerField.text) 
	archipelagoConnectionManager.startConnection(_passwordField.text)

func _onDisconnectButtonPressed():
	if _isDebug:
		print("Disconnect button pressed")
	archipelagoConnectionManager.startDisconnection()

# UI Toggle was removed for now, keeping this method just in case though
func _onEnabledToggled(enabled: bool):
	if _isDebug:
		var enDis = "en" if enabled else "dis"
		print("Archipelago Client " + enDis + "abled")
	if !enabled:
		archipelagoConnectionManager.startDisconnection()
	archipelagoDataManager.setEnabled(enabled)
	_hostField.editable = enabled
	_playerField.editable = enabled
	_passwordField.editable = enabled
	_connectButton.disabled = !enabled
	# going from disabled to enabled you will be in the disconnected state
	_disconnectButton.disabled = true
	_connectionLabel.text = "Disconnected" if enabled else "Archipelago Client disabled"
