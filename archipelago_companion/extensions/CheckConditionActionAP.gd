extends "res://nodes/actions/CheckConditionAction.gd"

export (Resource) var require_item = null

static func check_conditions(conds)->bool:
	if conds.require_item != null and not SaveState.inventory.has_item(conds.require_item):
		return false
	return .check_conditions(conds)
