from http import client
import pymongo
from pymongo import MongoClient, UpdateOne, DeleteMany
from bson.objectid import ObjectId
from pprint import pprint
from pymongo.errors import BulkWriteError



if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client ['test_db']
    collection = db['bike']

    bulk = [
        UpdateOne({"_id": ObjectId("6305a83d19ef7bceb5ff83e0")}, 
            {"$set":{   
                        "brand" : "yamaha",
                        "model" : "Mt15",
                        "year" : 2020       
                    }}),
        
        UpdateOne({"_id": ObjectId("6305a83d19ef7bceb5ff83e3")}, 
            {"$set":{   
                        "brand" : "TVS",
                        "model" : "Apache 4V",
                        "year" : 2021       
                    }}),


    ]
    try: 
        collection.bulk_write(bulk)

    except BulkWriteError as bwe:
        pprint(bwe.details)
