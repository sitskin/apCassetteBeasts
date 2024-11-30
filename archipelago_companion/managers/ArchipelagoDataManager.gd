extends Node

const _AP_EMPTY_DICT = {}
const _AP_BASE_KEY = "archipelago"
const AP_ENABLED_KEY = "archipelago_enabled"
const _AP_SERVER_KEY = "serverUrl"
const _AP_PLAYER_KEY = "player"

var configFile
const _CFG_FILE_PATH = "user://archipelago_mod_settings.cfg"

func _init():
	configFile = ConfigFile.new()
	configFile.load(_CFG_FILE_PATH)

func setEnabled(enabled):
	configFile.set_value(_AP_BASE_KEY, AP_ENABLED_KEY, enabled)
	configFile.save(_CFG_FILE_PATH)

func getEnabled():
	return configFile.get_value(_AP_BASE_KEY, AP_ENABLED_KEY, false)

func setServer(server):
	configFile.set_value(_AP_BASE_KEY, _AP_SERVER_KEY, server)
	configFile.save(_CFG_FILE_PATH)

func getServer():
	return configFile.get_value(_AP_BASE_KEY, _AP_SERVER_KEY, "")

func setPlayer(player):
	configFile.set_value(_AP_BASE_KEY, _AP_PLAYER_KEY, player)
	configFile.save(_CFG_FILE_PATH)

func getPlayer():
	return configFile.get_value(_AP_BASE_KEY, _AP_PLAYER_KEY, "")
