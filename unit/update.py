import pymongo

def Update(collection_births, collection_marriages, iteration):
	# Increment Age
	_Aging(collection_births)

	# Marry Units
	_Marriage()



def _Aging(collection_births):
        collection_births.update({},{"$inc":{"age":1}}, upsert=False, multi=True)
        print("units have aged")


def _Marriage():
	print("no units joined yet")



