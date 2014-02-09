
import pymongo

def Destroy(collection_births, collection_deaths, iteration):
	# Calculate unit properties
	unit_die = iteration

	# Check if any units are to be destroyed
	if collection_births.find({"die" : unit_die}).count() > 0:

		# Add units to be destroyed to the deaths collection
		collection_deaths.insert(collection_births.find({"die" : unit_die}))

		# Destroy units
		collection_births.remove({"die" : unit_die})

		print("unit death may have occured - it was ment to be")
