extends "res://data/item_scripts/TutorialItem.gd"

func custom_use_menu(_node, _context_kind:int, _context, _arg = null):
	yield (show_tutorials(), "completed")
	
	if ! ("hasReceivedTypeChart" in SaveState.other_data.archipelago):
		GlobalMessageDialog.clear_state()
		var itemName = ItemFactory.get_id(TypeChart)
		DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.handleGiveItemAction(itemName)
		SaveState.other_data.archipelago["hasReceivedTypeChart"] = true
