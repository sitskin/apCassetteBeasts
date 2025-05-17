extends "res://menus/title/FileMenu_SaveDataContainer.gd"


#onready var ap_player_label = self.get_node("PanelContainer2/VBoxContainer2/SaveDataFilledContainer/APPlayerLabel")
#onready var ap_locs_label = self.get_node("PanelContainer2/VBoxContainer2/SaveDataFilledContainer/APLocsLabel")
#onready var ap_player_label = get_node("APPlayerLabel")
#onready var ap_locs_label = get_node("APLocsLabel")

var ap_player_label
var ap_locs_label

func _ready():
	setup_ap_labels()
	
func setup_ap_labels():
	var path = "PanelContainer2/VBoxContainer2/SaveDataFilledContainer"
	ap_player_label = Label.new()
	ap_player_label.set_name("APPlayerLabel")
	ap_player_label.margin_top = 186
	ap_player_label.margin_bottom = 246
	ap_player_label.margin_right = 640
	ap_player_label.rect_position = Vector2(0, 186)
	ap_player_label.rect_size = Vector2(640, 60)
	ap_player_label.add_color_override("font_color", Color(0,0,0))
	ap_player_label.text = "Archipelago Player: "
	self.get_node(path).add_child(ap_player_label)
	ap_locs_label = Label.new()
	ap_locs_label.set_name("APLocsLabel")
	ap_locs_label.margin_top = 246
	ap_locs_label.margin_bottom = 300
	ap_locs_label.margin_right = 640
	ap_locs_label.text = "   Locations: "
	ap_locs_label.add_color_override("font_color", Color(0,0,0))
	self.get_node(path).add_child(ap_locs_label)

func set_current_button(value: FileButton):
	.set_current_button(value)
	var loc_count = [current_button.ap_checked_location_count, current_button.ap_total_location_count]
	if current_button and current_button.state == FileButton.State.LOADED and ap_locs_label != null:
		ap_player_label.text = "Archipelago Player: %s" % current_button.ap_player_name
		ap_locs_label.text = "  Locations: %s / %s" % loc_count
	
	
