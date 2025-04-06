extends GiveItemAction
var apItem = preload("res://mods/archipelago_companion/items/ap_item.tres")

func _run():
	var itemName = ItemFactory.get_id(item)
	var location = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.handleGiveItemAction(itemName)
	if location != null:
		item = ItemFactory.generate_item(apItem)
		item.name = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.getItemString(location)
		item.description = "This will explain what AP item you got"
	if item.name == "Self Item":
		item = null
	if item != null and item_amount > 0:
		var co = MenuHelper.give_item(item, item_amount, passive_message)
		if co is GDScriptFunctionState:
			yield (co, "completed")
	
	return true
