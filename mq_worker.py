#!/usr/bin/python

import pymongo
import pika

import unit.values


mongo_host = '10.224.36.180'
mongo_port = 27017

broker_host = '10.224.36.180'
queue_name = "create"

def _mongo_connect(host, port):
        try:
                mongo_client = pymongo.MongoClient(host, port)
                print("Connected to " + mongo_host + " on port " + str(mongo_port))
                return(mongo_client)

        except:
                mongo_client = 'FALSE'
                raise SystemExit("An error occured connecting to the MongoDB Server")



def poll_queue(ch, method, properties, body):

    db, collection, action, att1, att2, att3, att4 = body.split(",")

    if client.alive() == True:
      db = client[db]

      if action == "create":
        collection_births = db[collection]

	_CreateUnit(collection_births, att1, att2, att3, att4)

    else:
      raise SystemExit("Not connected to server MongoDB Server")


    ch.basic_ack(delivery_tag = method.delivery_tag)
	



def _CreateUnit(collection, familyname, iteration, imported=0, generation=0):

        # Common unit properties
        unit_firstname = unit.values.FirstName()
        unit_born = int(iteration)
        unit_matched = 0
        unit_imported = imported
        unit_generation = generation


        if (imported == 0):
                # Calculate unit properties for subunit
                unit_familyname = familyname
                unit_ttl = unit.values.LifeExpectancy()
                unit_die = unit_born + unit_ttl
                unit_age = 0
                unit_gender = unit.values.Gender()

        else:
                # Calculate unit properties for imported unit
                unit_familyname = unit.values.FamilyName()
                unit_ttl = unit.values.LifeExpectancy(aged=1)
                unit_die = unit.values.ArtificialDeath(unit_ttl)+unit_born
                unit_age = unit_die - unit_born
                unit_gender = unit.values.Gender()

       # Create unit
        collection.insert({"firstname" : unit_firstname,
                           "familyname" : unit_familyname,
                           "born" : unit_born,
                           "ttl" : unit_ttl,
                           "die" : unit_die,
                           "age" : unit_age,
                           "gender" : unit_gender,
                           "matched" : unit_matched,
                           "imported" : unit_imported,
                           "generation" : unit_generation})

	print("Created: " + unit_firstname + " " + unit_familyname)
				
				
				
if __name__ == '__main__':

    client = _mongo_connect(mongo_host, mongo_port)

    connection = pika.BlockingConnection(pika.ConnectionParameters(broker_host))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(poll_queue, queue=queue_name)

    channel.start_consuming()



