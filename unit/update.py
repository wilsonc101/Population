import pymongo

def Update(collection_births, collection_matches, iteration):
	# Increment Age
	_Aging(collection_births)

	# Match Units
	_Match(collection_births, collection_matches)



def _Aging(collection):
	# Age all units by 1 iteration
        collection.update({},{"$inc":{"age":1}}, upsert=False, multi=True)
        print("units have aged")


def _Match(collection_births, collection_matches):
	# Match units 
	# Only match male to female (for now)


	# Match values
	matches_per_iteration = 5	# number of matches to make per iteration
	max_age_gap = 5			# age gap between matched units
	max_subunits = 0		# offspring generated from match


	matches = 0
	while matches < matches_per_iteration:
		matches += 1

		# Select first partner in match
		unitA = collection_births.find_one({"matched" : 0, "gender" : "m", "age" : {"$gte" : 20}}) 


		# Select second partner in match if fisrt is present
		if (unitA != None):
			unitB = collection_births.find_one({"matched" : 0, "gender" : "f", "age" : {"$gte" : 20, "$gte" : unitA["age"]-5, "$lte" : unitA["age"]+5}})

		
		# If both units are present, mark as matched and record match
		if (unitA != None and unitB != None):		
			collection_births.update({"_id" : unitA["_id"]},{"$set":{"matched" : 1}}, upsert=False, multi=True)
			collection_births.update({"_id" : unitB["_id"]},{"$set":{"matched" : 1}}, upsert=False, multi=True)

			collection_matches.insert({"unitA" : unitA,
				   		   "unitB" : unitB,
						   "max_subunits" : max_subunits,
						   "subunits_created" : 0,
						   "last_subunit_created" : 0})
			print("units matched")
		else:
			print("no units to match")
	
					






