import pprint
from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient()

if __name__ == '__main__':
	db = client.mongo_db_lab
	definitions = db.definitions
	# print all items
	print("Print all items")
	for q in definitions.find():
		pprint.pprint(q)
	# print one item
	print("Print one item")
	pprint.pprint(definitions.find_one())
	# print specific item
	print("Print specific item")
	pprint.pprint(definitions.find_one({"word":"Flame"}))
	# print specific item by id
	print("Print specific item by id")
	pprint.pprint(definitions.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")}))
	# insert a new item
	print("Insert a new item")
	pprint.pprint(definitions.insert({"word": "crick", "definition": "n. According to many upstate New York residents, a small stream."}))
