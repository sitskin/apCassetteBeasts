extends SpawnConfig
#> class_name MonsterSpawnConfig

const BOOTLEG_CHANCE = 0.001
const LEVEL_BOOST = 0
const LEVEL_BOOST_FRAC = - 0.1
const LEVEL_BOOST_RANDOMNESS = 1.0
const NIGHT_LEVEL_BOOST_FRAC = 0.1

const BlankMonster = preload("res://data/characters/blank_monster.tres")

export (Array, Resource) var monster_forms: Array = []
export (PackedScene) var world_monster: PackedScene
export (Character.CharacterKind) var character_kind: int = Character.CharacterKind.MONSTER
export (bool) var disable_fleeing: bool = false
export (String, "", "monster", "monster_dlc") var level_scale_override_key: String = ""

func spawn()->Node:
	assert (world_monster != null)
	var node = world_monster.instance()
	return _configure_world_mon(node)

func spawn_async()->Node:
	assert (world_monster != null)
	var node = yield (InstanceQueue.instance_async(world_monster), "completed")
	return _configure_world_mon(node)

func _configure_world_mon(node: Node)->Node:
	var encounter = EncounterConfig.new()
	encounter.name = "EncounterConfig"
	node.add_child(encounter)
	
	var first = true
	
	for mon in monster_forms:
		var c = CharacterConfig.new()
		c.base_character = BlankMonster
		c.pronouns = randi() % 3
		c.character_kind = character_kind
		
		c.level_boost = LEVEL_BOOST
		c.level_boost_frac = LEVEL_BOOST_FRAC
		c.level_boost_randomness = LEVEL_BOOST_RANDOMNESS
		c.night_level_boost_frac = NIGHT_LEVEL_BOOST_FRAC
		
		c.level_scale_override_key = level_scale_override_key
		
		encounter.add_child(c)
		encounter.move_child(c, randi() % encounter.get_child_count())
		var tape = TapeConfig.new()
		tape.form = mon
		# PATCH: ADD LINES HERE
		var ap_chance = DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.getSetting("bootleg_multiplier")
		if ap_chance == null:
			ap_chance = 1
		# PATCH: STOP
		# PATCH: REPLACE TEXT BOOTLEG_CHANCE #INTO# BOOTLEG_CHANCE * ap_chance
		if character_kind == Character.CharacterKind.MONSTER and randf() < BOOTLEG_CHANCE:
			tape.type_override = [BattleSetupUtil.random_type(Random.new())]
		c.add_child(tape)
		
		if first and node.has_node(@"MonsterPalette"):
			
			var palette = node.get_node(@"MonsterPalette")
			palette.tape_path = palette.get_path_to(tape)
			assert ( not palette.tape_path.is_empty())
			first = false
	
	encounter.can_flee = not disable_fleeing
	
	return node
