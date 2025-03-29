tool 
extends ContainerButton

signal stamp_added

export (String) var captain_id:String = ""
export (String) var captain_name:String = ""
export (String) var captain_subtitle:String = ""
export (Texture) var stamp_texture:Texture
export (bool) var suppress_auto_visible:bool = false setget set_suppress_auto_visible
export (bool) var disabled:bool = true

onready var index_label = $IndexLabel
onready var stamp = $CenterContainer / Control / Stamp
onready var animation_player = $AnimationPlayer

func _ready():
	index_label.text = str(get_index() + 1)
#>	stamp.texture = stamp_texture if stamp_texture else preload("stamp_wallace.png")
	
	set_suppress_auto_visible(suppress_auto_visible)

func set_suppress_auto_visible(value:bool):
	suppress_auto_visible = value
	if stamp:
		if suppress_auto_visible:
			stamp.visible = false
		elif Engine.editor_hint:
			stamp.visible = true
		else :
			stamp.visible = is_defeated()

func is_met()->bool:
	if is_defeated():
		return true
	var flag_name = "met_" + captain_id
	return captain_id != "" and SaveState.has_flag(flag_name)

func is_defeated()->bool:
	var flag_name = "encounter_" + captain_id
	# PATCH: ADD LINES HERE
	flag_name = "AP_" + captain_id + "_stamp"
	# PATCH: STOP
	return captain_id != "" and SaveState.has_flag(flag_name)

func add_stamp():
	stamp.visible = true
	animation_player.play("add_stamp")
	animation_player.advance(0.0)
	yield (animation_player, "animation_finished")

func emit_stamp_added():
	emit_signal("stamp_added")

func _gui_input(event):
	if Debug.dev_mode:
		if event is InputEventMouseButton and event.button_index == 1 and event.pressed:
			add_stamp()
			accept_event()
