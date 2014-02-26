import pymongo

import unit.values

def Update(collection_births, collection_matches, iteration):
	# Increment Age
	_Aging(collection_births)

	# Match Units
	_Match(collection_births, collection_matches, iteration)



def _Aging(collection):
	# Age all units by 1 iteration
        collection.update({},{"$inc":{"age":1}}, upsert=False, multi=True)


def _Match(collection_births, collection_matches, iteration):
	# Match units 
	# Only match male to female (for now)

        population_count = collection_births.count()

	# Match values
	matches_per_iteration = unit.values.MatchQty(population_count)		# number of matches to make per iteration
	age_gap = unit.values.MatchGap()					# age gap between matched units
	max_subunits = unit.values.MatchSubUnits()				# offspring generated from match
	subunit_gap = unit.values.MatchSubUnitGap()				# minimum interations between subunit creation
	minimum_age = unit.values.MatchMinimumAge()

	matched = 0
	matches = 0
	while matches < matches_per_iteration:
		matches += 1

		# Select first partner in match
		unitA = collection_births.find_one({"matched" : 0, 
						    "gender" : "m", 
						    "age" : {"$gte" : minimum_age}}) 


		# Select second partner in match if fisrt is present
		if (unitA != None):
			unitB = collection_births.find_one({"matched" : 0, 
							    "gender" : "f", 
	   						    "age" : {"$gte" : minimum_age, 
								     "$gte" : unitA["age"]-age_gap, 
								     "$lte" : unitA["age"]+age_gap}})

		
		# If both units are present, mark as matched and record match
		if (unitA != None and unitB != None):		
			matched += 1
			collection_births.update({"_id" : unitA["_id"]},{"$set":{"matched" : 1}}, upsert=False, multi=True)
			collection_births.update({"_id" : unitB["_id"]},{"$set":{"matched" : 1}}, upsert=False, multi=True)

			collection_matches.insert({"matched" : iteration,
						   "unitA" : unitA,
				   		   "unitB" : unitB,
						   "max_subunits" : max_subunits,
						   "subunit_gap" : subunit_gap,
						   "subunits_created" : 0,
						   "last_subunit_created" : 0})

	if (matched > 0):
		print(str(matched) + " units matched - good for them")
	
					






