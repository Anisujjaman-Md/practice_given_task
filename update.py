import collections
from http import client
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

if __name__ == "__main__":

    print("Welcome to pymongo")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client ['test_db']
    collection = db['bike']

    prev= ({"_id" : ObjectId("6305a83d19ef7bceb5ff83e1")})
    
    new = {"$set":{"brand":"ferari", "model":"F430 Spider"}}

    put = collection.update_many(prev,new)
    print(put.modified_count)