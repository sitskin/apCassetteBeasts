extends "res://menus/gain_exp/GainExpMenu.gd"

func apply_exp():
	var loot_exp_yield = exp_yield
	var percent = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.getSetting("experience_multiplier")
	if percent != null:
		exp_yield *= percent/100
		
	var leveling = []
	var unlocked_stickers = []
	
	GlobalMessageDialog.clear_state()
	
	if whitelist.size() == 0:
		exp_label.visible = true
		exp_label.text = Loc.trf("BATTLE_EXP_POINTS", [exp_yield])
	else:
		exp_label.visible = false
	
	reset_pitch()
	
	var points = {}
	for member in party:
		if member[0] == null:
			continue
		if member[0].relationship_level > 0 and whitelist.size() == 0:
			member[0].relationship_points += exp_yield
		
		if whitelist.size() == 0 or whitelist.has(member[0]):
			points[member[0]] = exp_yield
		else:
			points[member[0]] = 0
		
		if whitelist.size() == 0:
			var p = member[0].get_total_exp() + exp_yield
			if p < highest_total_exp:
				points[member[0]] += int(min(exp_yield * 2, highest_total_exp - p))
	
	for partner in bg_partners:
		if whitelist.size() == 0 or whitelist.has(partner):
			points[partner] = exp_yield / 2
		else:
			points[partner] = 0
	
	for tape in active_tapes:
		if whitelist.size() == 0 or whitelist.has(tape):
			points[tape] = exp_yield
		else:
			points[tape] = 0
	for tape in inactive_tapes:
		if whitelist.size() == 0 or whitelist.has(tape):
			points[tape] = exp_yield
		else:
			points[tape] = 0
	
	queue_levels(leveling, points)
	yield (animate_exp_bars(leveling), "completed")
	level_up_all(leveling, unlocked_stickers)
	while leveling.size() > 0:
		speed_up()
		queue_levels(leveling, points)
		yield (animate_exp_bars(leveling), "completed")
		level_up_all(leveling, unlocked_stickers)
	
	yield (Co.wait(1.0), "completed")
	exp_label.visible = false
	
	var rewards = []
	if loot_table != null:
		rewards = loot_table.generate_rewards(loot_rand, loot_exp_yield)
	rewards += extra_loot
	if rewards.size() > 0 or unlocked_stickers.size() > 0:
		yield (MenuHelper.give_items(rewards, unlocked_stickers), "completed")
	
	SaveState.party.notify_tapes_changed()
	
	yield (Co.wait(1.0), "completed")
	cancelable = true
	cancel()
