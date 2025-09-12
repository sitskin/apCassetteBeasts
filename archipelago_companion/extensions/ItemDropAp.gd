extends "res://world/core/ItemDrop.gd"
var apItem = preload("res://mods/archipelago_companion/items/ap_item.tres")

func set_item(value:BaseItem):
	.set_item(value)
	if DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.checkItemDrop(ItemFactory.get_id(item)):
		sprite.texture = apItem.get_icon_3d()
		sprite.pixel_size = 0.02506
		sprite.offset.y = 40
		var m = sprite.material_override
		while m != null:
			m.set_shader_param("texture_albedo", sprite.texture)
			m = m.next_pass

func interact(_player):
	var itemName = ItemFactory.get_id(item)
	var location = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.handleItemDrop(itemName)
	if location != null:
		# mark item as having been picked up so it doesn't spawn again
		SaveState.flags[itemName + "_picked_up"] = true
		item = ItemFactory.generate_item(apItem)
		item.name = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.getItemString(location)
		item.description = "This will explain what AP item you got"
		if item.name == "Self Item":
			item = null
		if item != null and item_amount > 0:
			var co = MenuHelper.give_item(item, item_amount, false)
			if co is GDScriptFunctionState:
				yield (co, "completed")
		item_amount = 0
		inv_full_msg_given = true
	return .interact(_player)
