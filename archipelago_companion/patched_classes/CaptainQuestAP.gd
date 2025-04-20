extends Quest

export (Array, String) var captain_ids: Array

var defeated_captains: Dictionary

func _ready():
	SaveState.connect("flag_changed", self, "_on_flag_changed")
	update_progress()

func get_num_defeated()->int:
	return defeated_captains.size()

func _start_quest(params):
	._start_quest(params)
	update_progress()

func update_progress():
	for id in captain_ids:
		var flag = "encounter_" + id
		# PATCH: ADD LINES HERE
		flag = "ap_" + id + "_stamp"
		# PATCH: STOP
		if SaveState.has_flag(flag):
			defeated_captains[id] = true
	set_completable(defeated_captains.size() >= captain_ids.size())
	emit_signal("changed", self)

func get_description_params()->Dictionary:
	var result = .get_description_params()
	result.num = defeated_captains.size()
	result.max = captain_ids.size()
	return result

func _on_flag_changed(_flag, _value):
	update_progress()

func set_snapshot(snap, version: int)->bool:
	if .set_snapshot(snap, version):
		update_progress()
		return true
	return false
