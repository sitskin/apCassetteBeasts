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
		{
			"patch": "res://mods/archipelago_companion/patched_classes/MonsterSpawnConfigAP.gd",
			"target": "res://data/spawn_config_scripts/MonsterSpawnConfig.gd",
		},
		{
			"patch": "res://mods/archipelago_companion/patched_classes/ItemDropAp.gd",
			"target": "res://world/core/ItemDrop.gd",
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
	var apCaptainQuest = preload("extensions/CaptainQuestAP.gd")
	apCaptainQuest.take_over_path("res://data/quests/story/CaptainQuest.gd")
	var apGainExpMenu = preload("extensions/GainExpMenuAP.gd")
	apGainExpMenu.take_over_path("res://menus/gain_exp/GainExpMenu.gd")
	var apBattle = preload("res://mods/archipelago_companion/extensions/BattleAP.gd")
	apBattle.take_over_path("res://battle/Battle.gd")
	var apWiredSpawner = preload("extensions/WiredSpawnerAp.gd")
	apWiredSpawner.take_over_path("res://world/objects/spawner/WiredSpawner.gd")
	var apLostAndFoundItem = preload("extensions/LostAndFoundItemAp.gd")
	apLostAndFoundItem.take_over_path("res://world/quest_scenes/LostAndFoundItem.gd")
	var apFileButton = preload("res://mods/archipelago_companion/extensions/FileButtonAP.gd")
	apFileButton.take_over_path("res://menus/title/FileButton.gd")
	var apSaveDataContainer = preload("res://mods/archipelago_companion/extensions/FileMenu_SaveDataContainerAP.gd")
	apSaveDataContainer.take_over_path("res://menus/title/FileMenu_SaveDataContainer.gd")
	
	
	# connect to any scenes that we need modified
	var callbacks = DLC.mods_by_id.cat_modutils.callbacks
	callbacks.connect_scene_ready("res://menus/settings/SettingsMenu.tscn", self, "_onSettingsMenuReady")
	callbacks.connect_scene_ready("res://menus/title/FileMenu.tscn", self, "_onFileMenu")
	callbacks.connect_scene_ready("res://cutscenes/intro/OutskirtsWrongWay.tscn", self, "_onOutskirtsWrongWay")
	callbacks.connect_class_ready("res://world/core/ConditionalLayer.gd", self, "_removeInvisWalls")
	callbacks.connect_scene_ready("res://cutscenes/intro/PensbyIntro.tscn", self, "_giveKayleighEarly")
	callbacks.connect_scene_ready("res://cutscenes/merchants/Clemence_Exchange.tscn", self, "_unlockTapes")
	callbacks.connect_scene_ready("res://cutscenes/merchants/RangerTrader_Exchange.tscn", self, "_removeAbilityAdvantages")
	callbacks.connect_scene_ready("res://world/core/ItemDrop.tscn", self, "_onItemDrop")

func _onItemDrop(scene: Interaction):
	var item = scene.item
	var sprite = scene.sprite
	# need to use resource loading in order to grab the correct taken over class
	scene.set_script(preload("res://mods/archipelago_companion/extensions/ItemDropAp.gd"))
	scene.sprite = sprite
	scene.item = item

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

func _onFileMenu(scene: SlidingControl):
	var path = "VBoxContainer/HBoxContainer/PanelContainer/ScrollContainer/ScrollInterior/FileButtonContainer"
	for file_button in scene.get_node(path).get_children():
		if not "file" in file_button.file_path:
			continue
		file_button.file_path = file_button.file_path.replace("file", "ap_save")
		var ap_sticker = TextureRect.new()
		ap_sticker.texture = preload("res://mods/archipelago_companion/sprites/ap_save_file_sticker.png")
		ap_sticker.anchor_left = 0.75
		ap_sticker.anchor_top = 0.6
		ap_sticker.anchor_bottom = 1
		ap_sticker.anchor_right = 1
		file_button.add_child(ap_sticker)
		file_button.refresh()

# disables tutorial railroading if AP Client is enabled
func _onOutskirtsWrongWay(scene: CheckConditionAction):
	scene.deny_flags.push_back(preload("managers/ArchipelagoDataManager.gd").new().AP_ENABLED_KEY)

func _removeInvisWalls(scene: Node):
	if scene.name == "ConditionalLayer_Tutorial":
		scene.queue_free()

func _giveKayleighEarly(scene: Cutscene):
	scene.get_node("QuestStartAction").queue_free()
	var unlockKayleighAction = UnlockPartnerAction.new()
	unlockKayleighAction.partner_id = "kayleigh"
	scene.add_child(unlockKayleighAction)
	# need to use resource loading in order to grab the correct taken over class
	var giveHarbourtownKeyAction = load("res://nodes/actions/GiveItemAction.gd").new()
	giveHarbourtownKeyAction.item = ItemFactory.generate_item(load("res://data/items/key_harbourtown.tres"))
	scene.add_child(giveHarbourtownKeyAction)
	var give5TapesAction = load("res://nodes/actions/GiveItemAction.gd").new()
	give5TapesAction.item = ItemFactory.generate_item(load("res://data/items/tape_basic.tres"))
	give5TapesAction.item_amount = 5
	scene.add_child(give5TapesAction)
	var setEncounterAction = CheckConditionAction.new()
	setEncounterAction.set_flags = ["encounter_aa_oldgante"]
	scene.add_child(setEncounterAction)
	var unlockTrainAction = UnlockAbilityAction.new()
	unlockTrainAction.ability = "train_travel"
	scene.add_child(unlockTrainAction)
	scene.add_child(WaitAction.new())
	var warpToCafeAction = WarpAction.new()
	warpToCafeAction.warp_target_scene = "res://world/maps/interiors/GramophoneInterior.tscn"
	warpToCafeAction.warp_target_name = "CafeTable"
	scene.add_child(warpToCafeAction)

func _unlockTapes(scene: Cutscene):
	var exchange = scene.get_node("ExchangeMenuAction")
	var basicTapeIndex = exchange.exchanges.find(load("res://data/exchanges/clemence/tape_basic.tres"))
	var chromeTapeIndex = exchange.exchanges.find(load("res://data/exchanges/clemence/tape_chrome.tres"))
	if basicTapeIndex >= 0:
		exchange.exchanges[basicTapeIndex].conditional = null
	if chromeTapeIndex >= 0:
		exchange.exchanges[chromeTapeIndex].conditional = null

func _removeAbilityAdvantages(scene: Cutscene):
	var exchange = scene.get_node("ExchangeMenuAction")
	var climbIndex = exchange.exchanges.find(load("res://data/exchanges/ranger_trader/ability_advantage_climb.tres"))
	var dashIndex = exchange.exchanges.find(load("res://data/exchanges/ranger_trader/ability_advantage_dash.tres"))
	var magIndex = exchange.exchanges.find(load("res://data/exchanges/ranger_trader/ability_advantage_magnetism.tres"))
	if climbIndex >= 0:
		exchange.exchanges.remove(climbIndex)
	if dashIndex >= 0:
		exchange.exchanges.remove(dashIndex)
	if magIndex >= 0:
		exchange.exchanges.remove(magIndex)
