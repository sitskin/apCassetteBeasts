extends WiredSpawner

func spawn():
	var spawn_configs = spawn_profile.spawn_configs
	# double check that it is an item spawn
	if spawn_configs.size() == 1 && spawn_configs.front().item is BaseItem:
		var itemName = ItemFactory.get_id(spawn_configs.front().item)
		var isItemPickedUp = SaveState.flags.has(itemName + "_picked_up")
		var isApItem = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.checkItemDrop(itemName)
		# if the item has been picked up already, and it is an AP item then do not spawn again
		if isItemPickedUp && isApItem:
			return
	.spawn()
