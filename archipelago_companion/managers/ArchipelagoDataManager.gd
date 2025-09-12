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
	return configFile.get_value(_AP_SETTINGS_SECTION, AP_ENABLED_KEY, true)

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
	# ConfigFile truncates floats over 1*10^7
	# Saving as int is a workaround
	var dp = dataPackage.duplicate(true)
	for key in ["item_name_to_id", "location_name_to_id"]:
		for e in dp[key].keys():
			dp[key][e] = int(dp[key][e])
	configFile.set_value(_AP_DATA_PACKAGE_SECTION, gameName, dp)
	configFile.save(_CFG_FILE_PATH)

func getDataPackage(gameName: String):
	if configFile.has_section_key(_AP_DATA_PACKAGE_SECTION, gameName):
		# Reversing workaround
		var dataPackage = configFile.get_value(_AP_DATA_PACKAGE_SECTION, gameName)
		for key in ["item_name_to_id", "location_name_to_id"]:
			for e in dataPackage[key].keys():
				dataPackage[key][e] = float(dataPackage[key][e])
		return dataPackage
	return null
