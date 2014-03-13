import time

import pymongo
import random

import unit.values


def Create(collection_births, collection_matches, iteration):
	TEST_TIMER_01 = time.clock()


	TEST_TIMER_01a = time.clock()

	population_count = collection_births.count()

	imported_units_per_iteration = int(unit.values.ImportedUnitsPerIteration(population_count))
	units_per_iteration = int(unit.values.UnitsPerIteration(population_count))
	minimum_match_duration = int(unit.values.MatchFirstSubunit())
	unit_max_age = int(unit.values.MatchMaxUnitAge())
	new_subunit_gap = int(unit.values.MatchSubUnitGap())

	TEST_RESULT_01a = time.clock() - TEST_TIMER_01a


	## Generate subunits from matches
	# Find matches old enough to produce subunits
	TEST_TIMER_02 = time.clock()
	viable_matches = collection_matches.find({"matched" : {"$lte" : (iteration - minimum_match_duration)},
						  "unitA.age" : {"$lte" : unit_max_age},
						  "unitB.age" : {"$lte" : unit_max_age}})

	TEST_RESULT_02 = time.clock() - TEST_TIMER_02

	TEST_TIMER_03 = time.clock()
	subunits_created = 0
	for match in viable_matches:
		if subunits_created < units_per_iteration:
			# Check match still has subunits to create and there has been the correct duration since last subunit creation
	   	        # Add that the parent units are young enough
		

			if (match["subunits_created"] < match["max_subunits"] and 
			    match["subunit_gap"] < (iteration - match["last_subunit_created"]) and
		            match["unitA"]["age"] < unit_max_age and 
			    match["unitB"]["age"] < unit_max_age):

	
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
	


				# Increment counter
				subunits_created += 1

	TEST_RESULT_03 = time.clock() - TEST_TIMER_03

	## Generate 'imported' units - immigration
	# Only import units to healthy population - (> 10) - allow population to die

	imported_units_created = 0
	if (collection_births.count() > 10):
		TEST_TIMER_04 = time.clock()
		while (imported_units_created < imported_units_per_iteration):
			_CreateUnit(collection_births, "n_a", iteration, 1)
			imported_units_created += 1
		TEST_RESULT_04 = time.clock() - TEST_TIMER_04



	print (">>>>  GET VALUES - " + str(TEST_RESULT_01a))
	print (">>>>  INITIAL QUERY - " + str(TEST_RESULT_02))

	if (subunits_created > 0):
#		print (str(subunits_created) + " subunits created")
		print (">>>>  CREATE TASK - " + str(TEST_RESULT_03))

	
	if (imported_units_created > 0):
#		print (str(imported_units_created) + " units imported")
		print (">>>>  IMPORT TASK - " + str(TEST_RESULT_04))


	TEST_RESULT_01 = time.clock() - TEST_TIMER_01

	print (">>>>  TOTAL TASK - " + str(TEST_RESULT_01))




	



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
		
