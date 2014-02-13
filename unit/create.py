import pymongo
import random
import string

import unit.values

def Create(collection, collection_matches, iteration):

	units_per_iteration = unit.values.UnitsPerIteration()

	created = 0
	while created < units_per_iteration:
	
	# Get matches with remaining subunits and correct gap

	# loop through to max subunits per iteration

		# set family name of subunit to familyname of unitA of match







def _CreatUnit(collection, familyname)
	# Calculate unit properties
	unit_firstname = unit.values.FirstName()
	unit_familyname = unit.values.FamilyName()

	unit_born = int(iteration)
	unit_ttl = unit.values.LifeExpectancy()
	unit_die = unit_born + unit_ttl
	unit_gender = unit.values.Gender()
	unit_matched = 0

	# Create unit
	collection.insert({"firstname" : unit_firstname,
			   "familyname" : unit_familyname,
		           "born" : unit_born,
			   "ttl" : unit_ttl,
			   "die" : unit_die,
			   "age" : int(0),
			   "gender" : unit_gender,
			   "matched" : unit_matched})
		
	print("unit " + unit_firstname + " " + unit_familyname + " was created")

