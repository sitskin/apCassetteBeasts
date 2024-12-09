extends Quest

const ACTION_CLUES = [
	"CLUE_ACTION_ROCK", 
	"CLUE_ACTION_CRATE", 
	"CLUE_ACTION_DASH", 
	"CLUE_ACTION_MAGNETISM", 
	"CLUE_ACTION_JUMP_3", 
	"CLUE_ACTION_FACE_4_DIRECTIONS", 
	"CLUE_ACTION_NIGHT", 
	"CLUE_ACTION_MAP_3", 
	"CLUE_ACTION_ITEM_3", 
]

export (Array, String) var archangel_ids:Array
export (Array, String) var marker_flags:Array
export (int) var num_clues:int = 8
export (int) var min_required_clues:int = 4

var archangels_defeated:int
var clues_obtained:int
var story_end_location:Resource
var clue_action:String = "CLUE_ACTION_JUMP_3"

func _ready():
	SaveState.connect("flag_changed", self, "_on_flag_changed")
	update_clue_count()

func generate(params:Dictionary = {})->bool:
	var locations = Datatables.load("res://data/story_end_locations").table.values()
	story_end_location = create_random("story_end_location").choice(locations)
	
	clue_action = create_random("clue_action").choice(ACTION_CLUES)
	
	var result = .generate(params)
	
	update_clue_count()
	return result

func _is_end_mirror_visible()->bool:
	return story_end_location and ((SaveState.has_flag("intermission_done") and SaveState.has_flag("end_mirror_found")) or archangels_defeated >= archangel_ids.size())

func generate_map_markers():
	var num_markers = int(min(map_marker_chunks.size(), min(archangel_ids.size(), marker_flags.size())))
	var result = []
	
	if _is_end_mirror_visible():
		result.push_back(story_end_location.chunk_meta)
	else :
		for i in range(num_markers):
			if SaveState.has_flag(marker_flags[i]) and not SaveState.has_flag("encounter_" + archangel_ids[i]):
				result.push_back(map_marker_chunks[i])
	
	set_generated_map_marker_chunks(result)

func _fast_traveling_to_dungeon_final():
	if SaveState.party.partner.relationship_level < 1:
		SaveState.party.current_partner_id = "kayleigh"

func create_random(key:String)->Random:
	return Random.new(Random.child_seed(SaveState.random_seed, key))

func update_clue_count():
	archangels_defeated = 0
	for id in archangel_ids:
		var flag = "encounter_" + id
		# PATCH: ADD LINES HERE
		flag = "ap_" + flag
		# PATCH: STOP
		if SaveState.has_flag(flag):
			archangels_defeated += 1
	clues_obtained = int(min(archangels_defeated, num_clues))
	generate_map_markers()
	set_completable(clues_obtained >= min_required_clues)
	SaveState.stats.get_stat("song_parts").set_count(null, clues_obtained)
	emit_signal("changed", self)

func debug_obtain_all_clues():
	for id in archangel_ids:
		var flag = "encounter_" + id
		SaveState.set_flag(flag, true)
	update_clue_count()

func get_description_params()->Dictionary:
	var result = .get_description_params()
	result.num = clues_obtained
	result.max = num_clues
	return result

func _on_flag_changed(_flag, _value):
	update_clue_count()

func set_snapshot(snap, version:int)->bool:
	if .set_snapshot(snap, version):
		return generate()
	return false

func get_all_clues()->Array:
	var clues = [
		"CLUE_SONG_PROLOGUE1", 
		"CLUE_SONG_PROLOGUE2"
	]
	if story_end_location:
		clues.push_back(story_end_location.clue_ew)
	clues.push_back("CLUE_FLUFF")
	if story_end_location:
		clues.push_back(story_end_location.clue_ns)
		clues.push_back(story_end_location.clue_biome)
		clues.push_back(story_end_location.clue_location)
	clues.push_back(clue_action)
	clues.push_back("CLUE_SONG_EPILOGUE1")
	clues.push_back("CLUE_SONG_EPILOGUE2")
	return clues

func get_obtained_clues()->Array:
	var clues = get_all_clues()
	if clues_obtained + 2 < clues.size():
		clues = clues.slice(0, clues_obtained + 1)
		clues.push_back("CLUE_UNKNOWN")
	return clues
