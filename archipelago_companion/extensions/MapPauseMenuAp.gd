extends "res://menus/map_pause/MapPauseMenu.gd"

func _ready():
	# add return to entrance
	var level = WorldSystem.get_level_map()
	# if there is a level, and fast travel is not enabled, add warp to entrance
	if level != null && !level.enable_fast_travel:
		var warpToEntranceButton = party_button.duplicate()
		warpToEntranceButton.text = "Warp to Entrance"
		warpToEntranceButton.focus_mode = Control.FOCUS_ALL
		if warpToEntranceButton.is_connected("pressed", self, "_on_PartyButton_pressed"):
			warpToEntranceButton.disconnect("pressed", self, "_on_PartyButton_pressed")
		warpToEntranceButton.connect("pressed", self, "_warpToEntrance")
		buttons.add_child_below_node(party_button, warpToEntranceButton)
		buttons.setup_focus()
	._ready()

func _warpToEntrance():
	WorldSystem.warp(SaveState.last_warp_scene, SaveState.last_warp_chunk, 
		SaveState.last_warp_target, { autosave = false })
	cancel()
