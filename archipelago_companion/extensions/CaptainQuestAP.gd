extends "res://data/quests/story/CaptainQuest.gd"

var stampsCollected: Dictionary

func update_progress():
	for id in captain_ids:
		var flag = "encounter_" + id
		if SaveState.has_flag(flag):
			defeated_captains[id] = true
		
		var stampFlag = "ap_" + id + "_stamp"
		if SaveState.has_flag(stampFlag):
			stampsCollected[stampFlag] = true
		
	set_completable(stampsCollected.size() >= captain_ids.size())
	emit_signal("changed", self)
