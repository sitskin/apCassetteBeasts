extends UnlockAbilityAction

func _run():
	DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.sendAbilityUnlocked(ability)
	return true
