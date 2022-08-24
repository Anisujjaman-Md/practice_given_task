import collections
from http import client
import pymongo
from pymongo import MongoClient

if __name__ == "__main__":

    print("Welcome to pymongo")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client ['test_db']
    collection = db['car']
    five_list = [
        {"brand": "ford","model": "Mustang", "year": 1964, "Class":"First Class"},
        {"brand": "audi","model": "A8", "year": 2015},
        {"brand": "audi","model": "Q3", "year": 2020},
        {"brand": "marcedese ","model": "G Class", "year": 2015},
        {"brand": "toyota","model": "Harier", "year": 2020},
        ]
    collection.insert_many(five_list)

    collection2 = db['bike']
    five_list = [
        {"brand": "yamaha","model": "R15", "year": 2022, "Class":"First Class"},
        {"brand": "honda","model": "CBR", "year": 2015},
        {"brand": "suzuki","model": "XSR", "year": 2020},
        {"brand": "TVS ","model": "Apache 4v", "year": 2015},
        {"brand": "Bajaj","model": "Pulser NS 160", "year": 2020},
        ]
    collection2.insert_many(five_list)