extends WiredChest

var apItem = preload("res://mods/archipelago_companion/items/ap_item.tres")

func get_loot()->Array:
	DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.sendChestOpened(opened_flag)
	return _getApItem()

func _getApItem():
	var itemLoot = LootRecord.new()
	itemLoot.item = ItemFactory.generate_item(apItem)
	itemLoot.item.description = "This will explain what AP item you got"
	itemLoot.amount = 1
	return [itemLoot]
