
import pymongo

def Destroy(collection_births, collection_deaths, iteration):
	# Check if any units are to be destroyed
	if collection_births.find({"die" : iteration}).count() > 0:

		# Add units to be destroyed to the deaths collection
		collection_deaths.insert(collection_births.find({"die" : iteration}))

		# Count units before destruction
		pre_destroy = collection_births.count()

		# Destroy units
		collection_births.remove({"die" : iteration})

		post_destroy = collection_births.count()


		print(str(pre_destroy - post_destroy) + " unit(s) has/have destroyed")
