extends Node

const MonsterFormSpawnConfig = preload("res://data/spawn_config_scripts/MonsterFormSpawnConfig.gd")

var monsterWorldPath = "res://world/monsters/"
var monsterSpawnProfilesPath = "res://data/monster_spawn_profiles/"

func randomizeSpawns(data: Array):
	var monsterFormDB = Datatables.load("res://data/monster_forms/").table
	for spawnData in data:
		var habitat = spawnData.location # exact name of spawn profile file i.e. "autumn_hill_caves.tres"
		
		var spawnConfigs = []
		for spawn in spawnData.spawns:
			# exact name of monster form file without type i.e. "allseer"
			var beast = spawn.beast
			# exact name of monster world file i.e. "UndyinTentacle.tscn"
			var worldMonsterOverride = spawn.worldMonster if spawn.has("worldMonster") else null
			
			# if the beast doesn't exist, then move on
			if(!monsterFormDB.has(beast)):
				print("No file found for %s" % beast)
				continue
			var monsterForm = monsterFormDB[beast]
			
			var worldMon = worldMonsterOverride if worldMonsterOverride else "%s.tscn" % beast.capitalize()
			
			var worldMonster = load(monsterWorldPath + worldMon)
			
			var config = MonsterFormSpawnConfig.new()
			config.monster_form = monsterForm
			config.world_monster = worldMonster
			print("{monster_form: %s, world_monster: %s, weight: %s, hour_min: %s, hour_max: %s, is_valid: %s}" % 
			[config.monster_form, config.world_monster, config.weight, config.hour_min, config.hour_max, config.is_valid()])
			spawnConfigs.push_back(config)
		
		var profile:MonsterSpawnProfile = load(monsterSpawnProfilesPath + habitat)
		if(profile):
			profile.configs = spawnConfigs
