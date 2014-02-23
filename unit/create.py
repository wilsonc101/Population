import pymongo
import random
import string

import unit.values

def Create(collection_births, collection_matches, iteration):

	units_per_iteration = unit.values.UnitsPerIteration()
	minimum_match_duration = unit.values.MatchFirstSubunit()

	# Find matches old enough to produce subunits
	viable_matches = collection_matches.find({"matched" : {"$lte" : iteration-minimum_match_duration})

	created = 0
	for match in viable_matches:
		# Check match still has subunits to create and there has been the correct duration since last subunit creation
		if (int(match["subunits_created"]) < int(match["max_subunits"]) and
		    int(match["subunit_gap"]) < (int(iteration)-int(match["last_subunit_created"])):

			# Create unit
			# Update match document
			# Increment counter




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

