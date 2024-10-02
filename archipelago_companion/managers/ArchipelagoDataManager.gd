extends Node

const _AP_EMPTY_DICT = {}
const _AP_BASE_KEY = "archipelago"
const AP_ENABLED_KEY = "archipelago_enabled"
const _AP_SERVER_KEY = "serverUrl"
const _AP_PLAYER_KEY = "player"

var enabled setget _setEnabled, _getEnabled
var server setget _setServer, _getServer
var player setget _setPlayer, _getPlayer

func _init():
	SaveSystem.connect("file_loaded", self, "_onFileLoaded")

func _setEnabled(enabled):
	SaveState.flags[AP_ENABLED_KEY] = enabled

func _getEnabled():
	return SaveState.flags[AP_ENABLED_KEY]

func _setServer(server):
	SaveState.other_data[_AP_BASE_KEY][_AP_SERVER_KEY] = server

func _getServer():
	return SaveState.other_data[_AP_BASE_KEY][_AP_SERVER_KEY]

func _setPlayer(player):
	SaveState.other_data[_AP_BASE_KEY][_AP_PLAYER_KEY] = player

func _getPlayer():
	return SaveState.other_data[_AP_BASE_KEY][_AP_PLAYER_KEY]

func _onFileLoaded():
	# in theory this should never be false but just in case
	if !SceneManager.in_game:
		return
	if !SaveState.other_data.has(_AP_BASE_KEY):
		SaveState.other_data[_AP_BASE_KEY] = _AP_EMPTY_DICT
