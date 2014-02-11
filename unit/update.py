import pymongo

def Update(collection_births, collection_marriages, iteration):
	# Increment Age
	_Aging(collection_births)

	# Match Units
	_Match()



def _Aging(collection_births):
        collection_births.update({},{"$inc":{"age":1}}, upsert=False, multi=True)
        print("units have aged")


def _Match():
	print("no units joined yet")



