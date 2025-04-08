extends ContentInfo

const ApTab: PackedScene = preload("settings/ApTab.tscn")

const MODUTILS: Dictionary = {
	"class_patch": [
		{
			"patch": "res://mods/archipelago_companion/patched_classes/StampSlotAP.gd",
			"target": "res://menus/ranger_stamp_card/StampSlot.gd",
		},
		{
			"patch": "res://mods/archipelago_companion/patched_classes/ArchangelQuestAP.gd",
			"target": "res://data/quests/story/ArchangelQuest.gd",
		},
	],
}

# faking singletons cause godot doesn't let mods add to autoloader
const ArchipelagoConnectionManager = preload("managers/ArchipelagoConnectionManager.gd")
var archipelagoConnectionManager: ArchipelagoConnectionManager

func init_content() -> void:
	archipelagoConnectionManager = ArchipelagoConnectionManager.new()
	SaveSystem.add_child(archipelagoConnectionManager)
	var apWiredChest = preload("extensions/WiredChestAP.gd")
	apWiredChest.take_over_path("res://world/objects/chests/WiredChest.gd")
	var apUnlockAblilityAction = preload("extensions/UnlockAbilityActionAP.gd")
	apUnlockAblilityAction.take_over_path("res://nodes/actions/UnlockAbilityAction.gd")
	var apSpeciesCollection = preload("extensions/SpeciesCollectionAP.gd")
	apSpeciesCollection.take_over_path("res://global/save_state/SpeciesCollection.gd")
	var apGiveItemAction = preload("extensions/GiveItemActionAP.gd")
	apGiveItemAction.take_over_path("res://nodes/actions/GiveItemAction.gd")
	var apShowStampCardAction = preload("extensions/ShowStampCardActionAP.gd")
	apShowStampCardAction.take_over_path("res://nodes/actions/ShowStampCardAction.gd")
	# connect to any scenes that we need modified
	DLC.mods_by_id.cat_modutils.callbacks.connect_scene_ready("res://menus/settings/SettingsMenu.tscn", self, "_onSettingsMenuReady")
	DLC.mods_by_id.cat_modutils.callbacks.connect_scene_ready("res://cutscenes/intro/OutskirtsWrongWay.tscn", self, "_onOutskirtsWrongWay")

# adds the AP Settings page to the menu
func _onSettingsMenuReady(scene: Control):
	if scene.tabs[scene.tabs.size() - 1].name == "Archipelago Companion":
		return
	var tab = ApTab.instance()
	scene.content_container.add_child(tab)
	tab.visible = false
	scene.tabs.push_back({
		name = "Archipelago Companion", 
		node = tab
	})

# disables tutorial railroading if AP Client is enabled
func _onOutskirtsWrongWay(scene: CheckConditionAction):
	scene.deny_flags.push_back(preload("managers/ArchipelagoDataManager.gd").new().AP_ENABLED_KEY)
