extends Node

const _AP_EMPTY_DICT = {}
const _AP_SETTINGS_SECTION = "apSettings"
const _AP_DATA_PACKAGE_SECTION = "apDataPackage"
const AP_ENABLED_KEY = "archipelago_enabled"
const _AP_SERVER_KEY = "serverUrl"
const _AP_PLAYER_KEY = "player"

var configFile: ConfigFile
const _CFG_FILE_PATH = "user://archipelago_mod_settings.cfg"

func _init():
	configFile = ConfigFile.new()
	configFile.load(_CFG_FILE_PATH)

func setEnabled(enabled):
	configFile.set_value(_AP_SETTINGS_SECTION, AP_ENABLED_KEY, enabled)
	configFile.save(_CFG_FILE_PATH)

func getEnabled():
	return configFile.get_value(_AP_SETTINGS_SECTION, AP_ENABLED_KEY, false)

func setServer(server):
	configFile.set_value(_AP_SETTINGS_SECTION, _AP_SERVER_KEY, server)
	configFile.save(_CFG_FILE_PATH)

func getServer():
	return configFile.get_value(_AP_SETTINGS_SECTION, _AP_SERVER_KEY, "")

func setPlayer(player):
	configFile.set_value(_AP_SETTINGS_SECTION, _AP_PLAYER_KEY, player)
	configFile.save(_CFG_FILE_PATH)

func getPlayer():
	return configFile.get_value(_AP_SETTINGS_SECTION, _AP_PLAYER_KEY, "")

func setDataPackage(gameName: String, dataPackage: Dictionary):
	configFile.set_value(_AP_DATA_PACKAGE_SECTION, gameName, dataPackage)
	configFile.save(_CFG_FILE_PATH)

func getDataPackage(gameName: String):
	if configFile.has_section_key(_AP_DATA_PACKAGE_SECTION, gameName):
		return configFile.get_value(_AP_DATA_PACKAGE_SECTION, gameName)
	return null
