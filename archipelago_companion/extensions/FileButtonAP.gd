extends "res://menus/title/FileButton.gd"

var ap_cm = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager
var bac = ap_cm._archipelagoClient

var ap_player_name: String = ""
var ap_seed = null
var ap_checked_location_count: int = 0
var ap_total_location_count: int = 0

# checks if the connected AP seed matches the save data
func load_file():
	release_focus()
	
	# require connection to AP to start or load a file
	if not ap_cm.isConnected():
		if not _contains_save_tags(version_dlc, DLC.save_file_format_tags) or true:
			# this currently always happens until offline play is fixed
			GlobalMessageDialog.clear_state()
			yield (GlobalMessageDialog.show_message("You are not connected to an Archipelago Server.", true), "completed")
			grab_focus()
			return
		else:
			# save data present
			print("AP file checking happens here")
	else:
		if _contains_save_tags(version_dlc, DLC.save_file_format_tags):
			if ap_cm.randSeed != ap_seed:
				var msg = "Your Archipelago game seed does not match the save seed.\nYour Seed: %s\nSave Seed: %s" % [ap_cm.randSeed, ap_seed]
				GlobalMessageDialog.clear_state()
				yield (GlobalMessageDialog.show_message(msg, true), "completed")
				grab_focus()
				return
			if bac.player != ap_player_name:
				var msg = "Your Archipelago player name does not match the save.\nYour Name: %s\nSave Name: %s" % [bac.player, ap_player_name]
				GlobalMessageDialog.clear_state()
				yield (GlobalMessageDialog.show_message(msg, true), "completed")
				grab_focus()
				return
	
	
	.load_file()


func set_state(state: int, data):
	if state == State.LOADED and data:
		if _check_path(data, ["other_data", "ap_player"]):
			ap_player_name = data.other_data.ap_player
		if _check_path(data, ["other_data", "ap_seed"]):
			ap_seed = data.other_data.ap_seed
		if _check_path(data, ["other_data", "ap_locations_checked"]):
			ap_checked_location_count = data.other_data.ap_locations_checked
		if _check_path(data, ["other_data", "ap_locations_total"]):
			ap_total_location_count = data.other_data.ap_locations_total
	
	.set_state(state, data)
