extends WiredChest

var apItem = preload("res://mods/archipelago_companion/items/ap_item.tres")

func get_loot()->Array:
	if opened_flag == "":
		return .get_loot()
	DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.sendChestOpened(opened_flag)
	return _getApItem()

func _getApItem():
	var itemLoot = LootRecord.new()
	itemLoot.item = ItemFactory.generate_item(apItem)
	itemLoot.item.name = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.getItemString(opened_flag)
	itemLoot.item.description = "This will explain what AP item you got"
	itemLoot.amount = 1
	return [itemLoot]

func interact(_player):
	if not state or opened:
		return 
	
	WorldSystem.push_flags(WorldSystem.WorldFlags.PHYSICS_ENABLED)
	
	for child in get_children():
		if child is Action:
			var result = child.run()
			if result is GDScriptFunctionState:
				result = yield (result, "completed")
			if not result:
				WorldSystem.pop_flags()
				return 
	
	animation_player.play("open")
	yield (animation_player, "animation_finished")
	
	if has_node(NodePath("EncounterConfig")):
		var winner = yield (_run_battle(), "completed")
		if winner != 0:
			animation_player.play_backwards("open")
			yield (animation_player, "animation_finished")
			WorldSystem.pop_flags()
			return 
		yield (Co.wait(0.5), "completed")
	
	opened = true
	interaction.disabled = true
	set_opened_flag(true)
	
	GlobalMessageDialog.clear_state()
	
	var loot:Array = get_loot()
	if loot.size() == 0:
		yield (GlobalMessageDialog.show_message("ITEM_CHEST_EMPTY"), "completed")
	else :
		if loot[0].item.name != "Self Item":
			yield (MenuHelper.give_items(loot), "completed")
	
	if always_close_after_opening:
		animation_player.play_backwards("open")
		yield (animation_player, "animation_finished")
	
	WorldSystem.pop_flags()
