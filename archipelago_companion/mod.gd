extends ContentInfo

const ApTab: PackedScene = preload("settings/ApTab.tscn")
const REQUIRED_SINGLETON_KEYS := ["base", "class", "language", "path"]
const NEW_SINGLETON_CLASSES := [
	{
		"base": "Node",
		"class": "ArchipelagoConnectionManager",
		"language": "GDScript",
		"path": "res://mods/archipelago_companion/managers/ArchipelagoConnectionManager.gd",
	},
	{
		"base": "Node",
		"class": "ArchipelagoDataManager",
		"language": "GDScript",
		"path": "res://mods/archipelago_companion/managers/ArchipelagoDataManager.gd",
	},
]

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

# overrides parent method
func init_content() -> void:
	var apWiredChest = preload("extensions/WiredChestAP.gd")
	apWiredChest.take_over_path("res://world/objects/chests/WiredChest.gd")
	var apUnlockAblilityAction = preload("extensions/UnlockAbilityActionAP.gd")
	apUnlockAblilityAction.take_over_path("res://nodes/actions/UnlockAbilityAction.gd")
	var apSpeciesCollection = preload("extensions/SpeciesCollectionAP.gd")
	apSpeciesCollection.take_over_path("res://global/save_state/SpeciesCollection.gd")
	_addSingletonsToProject(NEW_SINGLETON_CLASSES)
	# connect to any scenes that we need modified
	DLC.mods_by_id.cat_modutils.callbacks.connect_scene_ready("res://menus/settings/SettingsMenu.tscn", self, "_onSettingsMenuReady")
	DLC.mods_by_id.cat_modutils.callbacks.connect_scene_ready("res://cutscenes/intro/OutskirtsWrongWay.tscn", self, "_onOutskirtsWrongWay")

# adds the AP Settings page to the menu
func _onSettingsMenuReady(scene: Control):
	var tab = ApTab.instance()
	scene.content_container.add_child(tab)
	tab.visible = false
	scene.tabs.push_back({
		name = "Archipelago Companion", 
		node = tab
	})

# disables tutorial railroading if AP Client is enabled
func _onOutskirtsWrongWay(scene: CheckConditionAction):
	scene.deny_flags.push_back(ArchipelagoDataManager.AP_ENABLED_KEY)

# Registers singletons to global scope, normally godot editor handles that
func _addSingletonsToProject(singletons: Array):
	var singletonClasses: Array = ProjectSettings.get_setting("_global_script_classes")
	var singletonIcons: Dictionary = ProjectSettings.get_setting("_global_script_class_icons")
	
	for newClassDict in singletons:
		if not _isValidSingletonDict(newClassDict):
			continue
		# how does GD 3.5 Array not have an any method????????
		for oldClassDict in singletonClasses:
			if oldClassDict.class == newClassDict.class:
				print("Class %s is already registered as global, skipping." % newClassDict.class)
				continue
		singletonClasses.append(newClassDict)
		singletonIcons[newClassDict.class] = "" # icon is not used, but needed for some reason
	
	ProjectSettings.set_setting("_global_script_classes", singletonClasses)
	ProjectSettings.set_setting("_global_script_class_icons", singletonIcons)

# Checks that the global script dict is formatted correctly
# { "base": "ParentClass", "class": "ClassName", "language": "GDScript", "path: "path_to_file" }
func _isValidSingletonDict(singleton_dict: Dictionary) -> bool:
	if not singleton_dict.has_all(REQUIRED_SINGLETON_KEYS):
		print("Singleton dict %s does not have all the required keys %s" % [singleton_dict, REQUIRED_SINGLETON_KEYS])
		return false
	if not File.new().file_exists(singleton_dict.path):
		print("Singleton file %s does not exist" % singleton_dict.path)
		return false
	return true
