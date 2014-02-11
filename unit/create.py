import pymongo
import random
import string

import unit.values

def Create(collection, iteration):
	# Calculate unit properties
	unit_firstname = unit.values.FirstName()
	unit_familyname = unit.values.FamilyName()
	unit_born = int(iteration)
	unit_ttl = unit.values.LifeExpectancy()
	unit_die = unit_born + unit_ttl
	unit_gender = unit.values.Gender()

	# Create unit
	collection.insert({"firstname" : unit_firstname,
			   "familyname" : unit_familyname,
		           "born" : unit_born,
			   "ttl" : unit_ttl,
			   "die" : unit_die,
			   "age" : int(0),
			   "gender" : unit_gender})

	print("unit " + unit_firstname + " " + unit_familyname + " was created")

