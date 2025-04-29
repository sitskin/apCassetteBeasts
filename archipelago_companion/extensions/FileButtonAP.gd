extends "res://menus/title/FileButton.gd"

# checks if the connected AP seed matches the save data
func load_file():
	release_focus()
	
	# require connection to AP to start or load a file
	if not DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.isConnected():
		GlobalMessageDialog.clear_state()
		yield (GlobalMessageDialog.show_message("You are not connected to a Archipelago Server.", true), "completed")
		grab_focus()
		return
	
	if _contains_save_tags(version_dlc, DLC.save_file_format_tags):
		# save data present
		print("AP file checking happens here")
	
	.load_file()
