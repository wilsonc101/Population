
import pymongo

def Destroy(collection_births, collection_deaths, iteration):
	# Check if any units are to be destroyed
	if collection_births.find({"die" : iteration}).count() > 0:

		# Add units to be destroyed to the deaths collection
		collection_deaths.insert(collection_births.find({"die" : iteration}))

		# Destroy units
		collection_births.remove({"die" : iteration})

		print("a unit has died - it was ment to be")
