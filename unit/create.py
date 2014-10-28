import time

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

	viable_matches = []
	loop_protect = 0

	all_matches = collection_matches.find({"matched" : {"$lte" : (iteration - minimum_match_duration)},
		                               "unitA.age" : {"$lte" : unit_max_age},
               		                       "unitB.age" : {"$lte" : unit_max_age}})


	## Build list of viable matches for subunit creation
	while len(viable_matches) < units_per_iteration:

		loop_protect += 1
		if loop_protect >= collection_matches.count(): break

		if (all_matches != None):
			for one_match in all_matches:
				if (one_match["subunits_created"] < one_match["max_subunits"] and 
			  	    one_match["subunit_gap"] < (iteration - one_match["last_subunit_created"])):
				
					viable_matches.append(one_match)


	for match in viable_matches:

			# Check match still has subunits to create and there has been the correct duration since last subunit creation
	   	        # Add that the parent units are young enough
		


#			if (match["subunits_created"] < match["max_subunits"] and 
#			    match["subunit_gap"] < (iteration - match["last_subunit_created"])):

#			if (match["subunits_created"] < match["max_subunits"] and 
#			    match["subunit_gap"] < (iteration - match["last_subunit_created"]) and
#		            match["unitA"]["age"] < unit_max_age and 
#			    match["unitB"]["age"] < unit_max_age):

	
				# Update match document:
				# - Set subunit created interation 'date'
				# - Increment subunits created
				# - Regenerate subunit gap (min of 1)
				collection_matches.update({"_id" : match["_id"]},{"$set":{"last_subunit_created" : iteration},
										  "$inc":{"subunits_created" : 1},
										  "$set":{"subunit_gap" : new_subunit_gap}},
										  upsert=False, multi=True)

				# Inherited properties
				subunit_familyname = match["unitA"]["familyname"]
				subunit_generation = int(match["unitA"]["generation"])+1
				
				# Create unit
				_CreateUnit(collection_births, subunit_familyname, iteration, 0, subunit_generation)
	


	## Generate 'imported' units - immigration
	# Only import units to healthy population - (> 10) - allow population to die

	imported_units_created = 0
	if (collection_births.count() > 10):
		while (imported_units_created < imported_units_per_iteration):
			_CreateUnit(collection_births, "n_a", iteration, 1)
			imported_units_created += 1



def _CreateUnit(collection, familyname, iteration, imported=0, generation=0):

	# Common unit properties
        unit_firstname = unit.values.FirstName()
	unit_born = int(iteration)
	unit_matched = 0
	unit_imported = imported
	unit_generation = generation


	if (imported == 0):
		# Calculate unit properties for subunit
		unit_familyname = familyname
		unit_ttl = unit.values.LifeExpectancy()
		unit_die = unit_born + unit_ttl
		unit_age = 0
		unit_gender = unit.values.Gender()

	else:
		# Calculate unit properties for imported unit
                unit_familyname = unit.values.FamilyName()
                unit_ttl = unit.values.LifeExpectancy(aged=1)
                unit_die = unit.values.ArtificialDeath(unit_ttl)+unit_born
                unit_age = unit_die - unit_born
                unit_gender = unit.values.Gender()



	# Create unit
	collection.insert({"firstname" : unit_firstname,
			   "familyname" : unit_familyname,
		           "born" : unit_born,
			   "ttl" : unit_ttl,
			   "die" : unit_die,
			   "age" : unit_age,
			   "gender" : unit_gender,
			   "matched" : unit_matched,
			   "imported" : unit_imported,
			   "generation" : unit_generation})
		
#	if (imported == 0):
#		print("unit " + unit_firstname + " " + unit_familyname + " was created - time to celebrate")
#	else:
#		print("unit " + unit_firstname + " " + unit_familyname + " moved in - make yourself at home")
		
