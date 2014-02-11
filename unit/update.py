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
	offspring = 0			# offspring generated from match
			


	matches = 0
	while matches < matches_per_iteration:
		matches += 1
		
		



		# Select first partner in match
		unitA = collection_births.find_one({"matched" : 0, "gender" : "m", "age" : {"$gte" : 20}})

		# Select second partner in match
		unitB = collection_births.find_one({"matched" : 0, "gender" : "f", "age" : {"$gte" : 20, "$gte" : unitA["age"]-5, "$lte" : unitA["age"]+5}})
		
		try:
			print(unitA["age"])
			print(unitB["age"])
			print("units joined - test")
		except:
			print("nothing to join")
	
					




#		collection.insert({"unitA_id" : "test",
#				   "unitA_firstname" : "test",
#				   "unitA_familyname" : "test",
#				   "b_firstname" : "test"})



