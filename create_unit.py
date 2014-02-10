import pymongo
import random
import string

import unit_values

def Create(collection, iteration):
	# Calculate unit properties
	unit_firstname = unit_values.FirstName()
	unit_familyname = unit_values.FamilyName()
	unit_born = int(iteration)
	unit_ttl = unit_values.LifeExpectancy()
	unit_die = unit_born + unit_ttl
	unit_gender = unit_values.Gender()

	# Create unit
	collection.insert({"firstname" : unit_firstname,
			   "familyname" : unit_familyname,
		           "born" : unit_born,
			   "ttl" : unit_ttl,
			   "die" : unit_die,
			   "age" : int(0),
			   "gender" : unit_gender})

	print("unit " + unit_firstname + " " + unit_familyname + " was created")

