import pymongo
import random
import string

def Create(collection, iteration):
	# Calculate unit properties
	unit_id = ''.join(random.sample(string.ascii_lowercase,6))
	unit_born = int(iteration)
	unit_ttl = _LifeExpectancy()
	unit_die = unit_born + unit_ttl
	unit_gender = _Gender()

	# Create unit
	collection.insert({"id" : unit_id,
		           "born" : unit_born,
			   "ttl" : unit_ttl,
			   "die" : unit_die,
			   "age" : int(0),
			   "gender" : unit_gender})

	print("unit " + unit_id + " was created")


def _LifeExpectancy():
	# Calculate how long a new unit will live
	MIN_AGE = 0
	MAX_AGE = 60

	# Pick a number at random
	life_expectancy = random.randint(MIN_AGE, MAX_AGE)
	return(life_expectancy)


def _Gender():
	# Pick a gender at random
	picker = random.choice("mf")

	if picker == "m":
		return("male")
	else:
		return("female")
