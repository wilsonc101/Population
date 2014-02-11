import pymongo
import random
import string


def LifeExpectancy(aged=0):
        # Calculate how long a new unit will live

	if aged == 0:
	        MIN_AGE = 0
	else:
		MIN_AGE = 1

        MAX_AGE = 60

        # Pick a number at random
        life_expectancy = random.randint(MIN_AGE, MAX_AGE)
        return(life_expectancy)


def Gender():
        # Pick a gender at random
        picker = random.choice("mf")
	return(picker)
	

def FirstName():
        # Generate a fisrt name
        name = ''.join(random.sample(string.ascii_lowercase,6))
        return(name)

def FamilyName():
        # Generate a family name
        name = ''.join(random.sample(string.ascii_lowercase,6))
        return(name)


def ArtificialDeath(ttl):
	# Used in genesis to create aged units
        # Calculate how long a new unit will live
        MIN_AGE = 1
        MAX_AGE = int(ttl)

        # Pick a number at random
        age = random.randint(MIN_AGE, MAX_AGE)
        return(age)



