# import pandas
# pandas.read_json('Angular_Projects\DashBoard\db.json').to_csv('Employe_Data.csv')

import pymongo
import json
from pymongo import MongoClient, InsertOne


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.Employee_Data
collection = db.Angular
requesting = []

with open(r"Angular_Projects\DashBoard\db.json") as file:
    for jsonObj in file:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
