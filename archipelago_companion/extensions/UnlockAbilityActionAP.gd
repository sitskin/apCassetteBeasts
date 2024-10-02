extends UnlockAbilityAction

func _run():
	ArchipelagoConnectionManager.sendAbilityUnlocked(ability)
	return true
