import pymongo
import random
import string

import unit_values

def StartPopulation(collection_births, collections_marriages, count):
	# Initiate population
	_CreateUnits(collection_births, count)

	# Marry units
	_MarryUnits(20)



def _CreateUnits(collection, count):
	counter = 0

	while counter < count:

		counter += 1

	        # Calculate unit properties
        	unit_firstname = unit_values.FirstName()
        	unit_familyname = unit_values.FamilyName()
	        unit_born = 0
	        unit_ttl = unit_values.LifeExpectancy(aged=1)
	        unit_die = unit_values.ArtificialDeath(unit_ttl)
		unit_age = unit_ttl - unit_die
	        unit_gender = unit_values.Gender()
	
	        # Create units
	        collection.insert({"firstname" : unit_firstname,
				   "familyname" : unit_familyname,
	                           "born" : unit_born,
	                           "ttl" : unit_ttl,
	                           "die" : unit_die,
	                           "age" : unit_age,
	                           "gender" : unit_gender})
	
	        print("unit " + unit_firstname + " " + unit_familyname + " was created")
		


def _MarryUnits(pairs):
	print(pairs)
