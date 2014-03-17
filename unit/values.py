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
	# Used in: genesis
        # Generate a family name
        name = ''.join(random.sample(string.ascii_lowercase,6))
        return(name)

def UnitsPerIteration(pop_count):
	##### KEY METRIC #####
	# Used in: create
        MIN_POPULATION_PERCENTAGE = 20
        MAX_POPULATION_PERCENTAGE = 40
        MIN_UNITS = int(((pop_count/100)*MIN_POPULATION_PERCENTAGE))
        MAX_UNITS = int(((pop_count/100)*MAX_POPULATION_PERCENTAGE))

	units_per_iteration = random.randint(MIN_UNITS, MAX_UNITS)
	return(units_per_iteration)

def ImportedUnitsPerIteration(pop_count):
	##### KEY METRIC #####
	# Used in: create
	# Generate number of 'imported' units to create - immigration
        MIN_POPULATION_PERCENTAGE = 3 
        MAX_POPULATION_PERCENTAGE = 4 
        MIN_UNITS = int(((pop_count/100)*MIN_POPULATION_PERCENTAGE))
        MAX_UNITS = int(((pop_count/100)*MAX_POPULATION_PERCENTAGE))

	imported_units_per_iteration = random.randint(MIN_UNITS, MAX_UNITS)
	return(imported_units_per_iteration)

def MatchQty(pop_count):
	##### KEY METRIC #####
	# Used in: update
	# Generate number of matches to make per iteration	
        MIN_POPULATION_PERCENTAGE = 40
        MAX_POPULATION_PERCENTAGE = 50
        MIN_MATCHES = int(((pop_count/100)*MIN_POPULATION_PERCENTAGE))
        MAX_MATCHES = int(((pop_count/100)*MAX_POPULATION_PERCENTAGE))

	matches_per_iteration = random.randint(MIN_MATCHES, MAX_MATCHES)
 	return(matches_per_iteration)

def MatchMinimumAge():
	# Used in: update
	# Generate minimum age of units to match
	match_minimum_age = 20
 	return(match_minimum_age)

def MatchGap():
	# Used in: update
	# Generate age gap between matched units
        max_age_gap = 12              
	return(int(max_age_gap/2))

def MatchMaxUnitAge():
	# Used in: update
	# Generate the maximum age of a parent unit for subunit creation
	max_unit_age = 45
	return(max_unit_age)


def MatchFirstSubunit():
	# Used in: update
	# Generate minumum age of match (iterations units have been matched) before subunits can be created
	minimum_match_duration = 1
	return(minimum_match_duration)


def MatchSubUnits():
	# Used in: update
	# Generate number of subunits resulting from match
	MIN_SUBUNITS = 0
	MAX_SUBUNITS = 6

        max_subunits = random.randint(MIN_SUBUNITS, MAX_SUBUNITS)                
	return(max_subunits)


def MatchSubUnitGap():
	# Used in: update
	# Generate gap between sub unit creation - on match creation and subunit creation
	MIN_GAP = 1
	MAX_GAP = 10

        subunit_gap = random.randint(MIN_GAP, MAX_GAP)
	return(subunit_gap)



