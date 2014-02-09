import pymongo
import time

import create_unit
import destroy_unit

execution_instance = str(int(time.time()))

mongo_host = 'localhost'
mongo_port = 27017

mongo_db = 'population'
mongo_collection_births = 'births_' + execution_instance
mongo_collection_deaths = 'deaths_' + execution_instance


def _mongo_connect(host, port):
	try:
		mongo_client = pymongo.MongoClient(host, port)
		print("Connected to " + mongo_host + " on port " + str(mongo_port))
		return(mongo_client)

	except:
		mongo_client = 'FALSE'
		raise SystemExit("An error occured connecting to the MongoDB Server")

	


if __name__ == '__main__':
	client = _mongo_connect(mongo_host, mongo_port)

	# Connect to Mongo database and set collection using client connection
	db = client[mongo_db]
	collection_births = db[mongo_collection_births]
	collection_deaths = db[mongo_collection_deaths]
	

iteration = 0
while 1:
	iteration += 1
	create_unit.Create(collection_births, iteration)
	destroy_unit.Destroy(collection_births, collection_deaths, iteration)
	time.sleep(.01)	






