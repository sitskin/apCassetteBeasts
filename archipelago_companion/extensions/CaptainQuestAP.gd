extends "res://data/quests/story/CaptainQuest.gd"

var stampsCollected: Dictionary

func update_progress():
	for id in captain_ids:
		var flag = "encounter_" + id
		if SaveState.has_flag(flag):
			defeated_captains[id] = true
		
		var stampFlag = "ap_" + id.get_slice("_", 1) + "_stamp"
		if SaveState.has_flag(stampFlag):
			stampsCollected[stampFlag] = true
		
	set_completable(stampsCollected.size() >= captain_ids.size())
	emit_signal("changed", self)

func get_description_params()->Dictionary:
	var result = .get_description_params()
	result.num = stampsCollected.size()
	return result
