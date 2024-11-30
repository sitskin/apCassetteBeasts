extends "res://global/save_state/SpeciesCollection.gd"

func register(tape:MonsterTape):
	var new_species:bool = false
	var species = tape.form
	var species_key = Datatables.get_db_key(tape.form)
	if not obtained.has(species_key):
		obtained[species_key] = {}
		new_species = true
	
	var type_id = tape.type_override[0].id if tape.type_override.size() > 0 else ""
	obtained[species_key][type_id] = true
	
	if tape.grade > max_tape_grades.get(species_key, 0):
		if tape.grade >= MonsterTape.MAX_TAPE_GRADE and max_tape_grades.get(species_key, 0) < MonsterTape.MAX_TAPE_GRADE:
			get_parent().stats.get_stat("maxed_tape_species").report_event(species)
		max_tape_grades[species_key] = tape.grade
		emit_signal("max_tape_grade_changed", species)
	
	if new_species:
		get_parent().stats.get_stat("observed_species").report_event(species)
		get_parent().stats.get_stat("registered_species").report_event(species)
		emit_signal("new_species_registered", species)
	
	if tape.type_override.size() > 0:
		var bootleg_type = tape.type_override[0]
		if get_parent().stats.get_stat("registered_bootleg_types").get_count(bootleg_type) == 0:
			get_parent().stats.get_stat("registered_bootleg_types").report_event(bootleg_type)
	
	if tape.form.unlock_ability != "":
		DLC.mods_by_id.archipelago_companion.archipelagoConnectionManager.sendAbilityUnlocked(tape.form.unlock_ability)

# return value is only used in UnlockDeferredAbilitiesAction, which is only used in the 
# tutorial, I guess if you happened to somehow record a mon that gives you 
# an ability before beating oldgante.  Since we are essentially removing the 
# oldgante flag blocker this is no longer needed
func unlock_abilities()->Array:
	# return if AP is enabled since we don't need this code
	if not get_parent().has_flag("encounter_aa_oldgante") or preload("res://mods/archipelago_companion/managers/ArchipelagoDataManager.gd").new().getEnabled():
		return []
	var unlocked = []
	for id in obtained.keys():
		var species = MonsterForms.get_from_key(id, false)
		if species:
			if species.unlock_ability != "" and not get_parent().has_ability(species.unlock_ability):
				# TODO: connect to AP manager got check and don't add to the unlocked array
				emit_signal("ability_unlocked", species.unlock_ability)
				unlocked.push_back(species.unlock_ability)
	return unlocked
