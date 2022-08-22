import collections
from http import client
import pymongo
from pymongo import MongoClient

if __name__ == "__main__":

    print("Welcome to pymongo")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client ['test_db']
    collection = db['car information']

    prev = {"_id" : "6303434d9cb36b0511f91ee0"}
    new = {"$set":{"brand":"ferari", "model":"F430 Spider"}}

    put = collection.update_many(prev,new)
    print(put.modified_count)