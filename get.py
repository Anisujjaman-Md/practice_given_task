import collections
from http import client
import pymongo
from pymongo import MongoClient

if __name__ == "__main__":


    # print("Welcome to pymongo")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client ['test_db']
    collection = db['car']
  
    allInfo= collection.find({"brand":"audi"})
    
    for i in allInfo:
        print(i)