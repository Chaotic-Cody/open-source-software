import pprint
from bson.objectid import ObjectId
import datetime
from pymongo import MongoClient
client = MongoClient()

# "date": datetime.datetime.utcnow()

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client.mongo_db_lab
    definitions = db.definitions

    # grab random item
    rand_doc = definitions.aggregate([{"$sample": { "size": 1}}]).next()
    #pprint.pprint(rand_doc)
    # push timestamp
    print("before update")
    definitions.update(rand_doc, {"$push": {"dates": datetime.datetime.utcnow()}})
    pprint.pprint(rand_doc)

    return None


if __name__ == '__main__':
    print random_word_requester()
