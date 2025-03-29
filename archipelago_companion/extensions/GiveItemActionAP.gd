extends GiveItemAction

func _run():
	var itemName = ItemFactory.get_id(item)
	var isHandled = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.handleGiveItemAction(itemName)
	if item != null and item_amount > 0 and !isHandled:
		var co = MenuHelper.give_item(item, item_amount, passive_message)
		if co is GDScriptFunctionState:
			yield (co, "completed")
	
	return true
