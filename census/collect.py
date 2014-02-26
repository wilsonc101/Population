import pymongo
import random


def Collect(collection_census, collection_births, collection_deaths, collection_matches, iteration):
	living_pop = _Record_Living_Population(collection_births)
	living_pop_m = _Record_Living_Population(collection_births, gender="m")
	living_pop_f = _Record_Living_Population(collection_births, gender="f")

	living_import_pop = _Record_Living_Imported_Population(collection_births)
	living_import_pop_m = _Record_Living_Imported_Population(collection_births, gender="m")
	living_import_pop_f = _Record_Living_Imported_Population(collection_births, gender="f")

	total_pop = _Record_Total_Population(collection_births, collection_deaths)
	total_pop_m = _Record_Total_Population(collection_births, collection_deaths, gender="m")
	total_pop_f = _Record_Total_Population(collection_births, collection_deaths, gender="f")
	

	# Enter into stats collections
	collection_census.insert({"iteration" : iteration,
				  "living_population" : living_pop,
				  "living_male_population" : living_pop_m,
				  "living_female_population" : living_pop_f,
				  "living_imported_population" : living_import_pop,
				  "living_imported_male_population" : living_import_pop_m,
				  "living_imported_female_population" : living_import_pop_f,
				  "total_population" : total_pop,
				  "total_male_population" : total_pop_m,
				  "total_female_population" : total_pop_m})
				  


def _Record_Living_Population(collection_births, gender="all"):

	if (gender == "all"):
		# total
		count = collection_births.count()
	else:
		# gender specific
		count = collection_births.find({"gender" : gender}).count()

	return(count)


def _Record_Living_Imported_Population(collection_births, gender="all"):

	if (gender == "all"):
		# total
		count = collection_births.find({"imported" : 1}).count()
	else:
		# gender specific
		count = collection_births.find({"gender" : gender, "imported" : 1}).count()

	return(count)


def _Record_Total_Population(collection_births, collection_deaths, gender="all"):

	if (gender == "all"):
		# total
		count = int(collection_births.count()) + int(collection_deaths.count())
	else:
		# gender specific
		count = int(collection_births.find({"gender" : gender}).count()) + int(collection_deaths.find({"gender" : gender}).count())

	return(count)




	
