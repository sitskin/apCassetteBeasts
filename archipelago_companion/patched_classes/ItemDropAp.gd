extends Interaction

signal obtained

const FADE_DURATION = 0.5

export (Resource) var item:Resource setget set_item
export (int) var item_amount:int = 1

onready var sprite = $SpriteContainer / Spatial / Sprite3D

var inv_full_msg_given = false

func _ready():
	set_item(item)

func set_item(value:BaseItem):
	item = value
	if sprite:
		if item == null:
			sprite.texture = preload("res://sprites/items/unknown.png")
		elif item is StickerItem:
			sprite.texture = preload("res://sprites/items/sticker.png")
		else :
			sprite.texture = item.get_icon_3d()
		var m = sprite.material_override
		while m != null:
			m.set_shader_param("texture_albedo", sprite.texture)
			m = m.next_pass

func interact(_player):
	if disabled:
		return 
	set_disabled(true)
	
	var left_over = SaveState.inventory.add_new_item(item, item_amount)
	var obtained = item_amount - left_over
	
	# PATCH: REPLACE TEXT item_amount > 0 #INTO# item_amount >= 0
	if obtained == 0 and item_amount > 0:
		if not inv_full_msg_given:
			GlobalMessageDialog.passive_message.show_message(Loc.tr("ITEM_DROP_INVENTORY_FULL"))
		inv_full_msg_given = true
	else :
		yield (MenuHelper.show_loot([{item = item, amount = obtained}]), "completed")
	
	item_amount = left_over
	
	if obtained > 0:
		emit_signal("obtained")
	
	if item_amount > 0:
		set_disabled(false)
	else :
		sprite.cast_shadow = false
		var tween = Tween.new()
		add_child(tween)
		var start = $SpriteContainer.albedo
		var end = start
		end.a = 0.0
		tween.interpolate_property($SpriteContainer, "albedo", start, end, FADE_DURATION, Tween.TRANS_CUBIC, Tween.EASE_IN_OUT)
		tween.start()
		yield (Co.wait_for_tween(tween), "completed")
		queue_free()
