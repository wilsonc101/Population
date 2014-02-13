import pymongo
import random
import string



def ArtificialDeath(ttl):
	# Used in: genesis
        # Calculate how long a new unit will live
        MIN_AGE = 1
        MAX_AGE = int(ttl)

        # Pick a number at random
        age = random.randint(MIN_AGE, MAX_AGE)
        return(age)

def LifeExpectancy(aged=0):
	# Used in: genesis, create
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
	# Used in: genesis, create
        # Pick a gender at random
        picker = random.choice("mf")
	return(picker)

def FirstName():
	# Used in: genesis, create
        # Generate a first name
        name = ''.join(random.sample(string.ascii_lowercase,6))
        return(name)

def FamilyName():
	# Used in: genesis, create
        # Generate a family name
        name = ''.join(random.sample(string.ascii_lowercase,6))
        return(name)

def UnitsPerIteration()
	# Used in: create
	units_per_iteration = 5
	return(units_per_iteration)

def MatchMinimumAge():
	# Used in: update
	# Generate minimum age of matches	
	match_minimum_age = 20
 	return(match_minimum_age)

def MatchQty():
	# Used in: update
	# Generate number of matches to make per iteration	
	matches_per_iteration = 5
 	return(matches_per_iteration)

def MatchGap():
	# Used in: update
	# Generate age gap between matched units
        max_age_gap = 6               
	return(int(max_age_gap/2))


def MatchSubUnits():
	# Used in: update
	# Generate number of subunits resulting from match
        max_subunits = 2                
	return(max_subunits)


def MatchSubUnitGap():
	# Used in: update
	# Generate gap between sub unit creation
        subunit_gap = 2
	return(subunit_gap)



