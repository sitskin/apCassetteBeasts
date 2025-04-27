extends "res://world/quest_scenes/LostAndFoundItem.gd"

func _enter_tree():
	var quest = get_parent().quest
	if quest == null:
		queue_free()
		return 
	
	var itemName = ItemFactory.get_id(quest.required_item)
	var isApItem = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.checkItemDrop(itemName)
	# this value is set as a part of the ItemDropAp code
	var hasPickedUpItem = SaveState.flags.has(itemName + "_picked_up")
	
	if has_node("ItemDrop"):
		$ItemDrop / QuestMarker.quests = [quest.get_resource()]
		var item_drop = $ItemDrop
		# if it is not an ap item, go with quest.completable
		# if it is an ap item, go with hasPickedUpItem
		if (quest.completable && !isApItem) || hasPickedUpItem:
			remove_child(item_drop)
			item_drop.queue_free()
		else :
			item_drop.item = quest.required_item
			item_drop.item_amount = quest.required_item_amount
