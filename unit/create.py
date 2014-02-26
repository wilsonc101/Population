import pymongo
import random

import unit.values


def Create(collection_births, collection_matches, iteration):
	population_count = collection_births.count()

	imported_units_per_iteration = int(unit.values.ImportedUnitsPerIteration(population_count))
	units_per_iteration = int(unit.values.UnitsPerIteration(population_count))
	minimum_match_duration = int(unit.values.MatchFirstSubunit())
	unit_max_age = int(unit.values.MatchMaxUnitAge())
	new_subunit_gap = int(unit.values.MatchSubUnitGap())

	## Generate subunits from matches
	# Find matches old enough to produce subunits
	viable_matches = collection_matches.find({"matched" : {"$lte" : (iteration - minimum_match_duration)},
						  "unitA.age" : {"$lte" : unit_max_age},
						  "unitB.age" : {"$lte" : unit_max_age}})

	subunits_created = 0
	for match in viable_matches:
		if subunits_created < units_per_iteration:
			# Check match still has subunits to create and there has been the correct duration since last subunit creation
	   	        # Add that the parent units are young enough
			if (match["subunits_created"] < match["max_subunits"] and 
			    match["subunit_gap"] < (iteration - match["last_subunit_created"]) and
		            match["unitA"]["age"] < unit_max_age and 
			    match["unitB"]["age"] < unit_max_age):
	
				# Create unit
				_CreateUnit(collection_births, match["unitA"]["familyname"], iteration)
	
				# Update match document:
				# - Set subunit created interation 'date'
				# - Increment subunits created
				# - Regenerate subunit gap (min of 1)
				collection_matches.update({"_id" : match["_id"]},{"$set":{"last_subunit_created" : iteration},
										  "$inc":{"subunits_created" : 1},
										  "$set":{"subunit_gap" : new_subunit_gap}},
										  upsert=False, multi=True)
				# Increment counter
				subunits_created += 1

	## Generate 'imported' units - immigration
	# Only import units to healthy population - (> 10) - allow population to die
	if (collection_births.count() > 10):
		imported_units_created = 0
		while (imported_units_created < imported_units_per_iteration):
			_CreateUnit(collection_births, "n_a", iteration, 1)
			imported_units_created += 1



def _CreateUnit(collection, familyname, iteration, imported=0):

	if (imported == 0):
		# Calculate unit properties for subunit
		unit_firstname = unit.values.FirstName()
		unit_familyname = familyname
		unit_born = int(iteration)
		unit_ttl = unit.values.LifeExpectancy()
		unit_die = unit_born + unit_ttl
		unit_age = 0
		unit_gender = unit.values.Gender()
		unit_matched = 0
		unit_imported = imported

	else:
		# Calculate unit properties for imported unit
                unit_firstname = unit.values.FirstName()
                unit_familyname = unit.values.FamilyName()
                unit_born = iteration
                unit_ttl = unit.values.LifeExpectancy(aged=1)
                unit_die = unit.values.ArtificialDeath(unit_ttl)+unit_born
                unit_age = unit_die - unit_born
                unit_gender = unit.values.Gender()
                unit_matched = 0
		unit_imported = imported



	# Create unit
	collection.insert({"firstname" : unit_firstname,
			   "familyname" : unit_familyname,
		           "born" : unit_born,
			   "ttl" : unit_ttl,
			   "die" : unit_die,
			   "age" : unit_age,
			   "gender" : unit_gender,
			   "matched" : unit_matched,
			   "imported" : unit_imported})
		
	if (imported == 0):
		print("unit " + unit_firstname + " " + unit_familyname + " was created - time to celebrate")
	else:
		print("unit " + unit_firstname + " " + unit_familyname + " moved in - make yourself at home")
		
