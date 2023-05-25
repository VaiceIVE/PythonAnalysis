import os
from IResult import IResult
from pymongo import MongoClient
from bson.objectid import ObjectId
print(os.environ['DB_URL'])
client = MongoClient(os.environ['DB_URL'], 
                     username='root', 
                     password='admin',
                    authSource="admin")
results = client.LCT.results

def Save(result):
    result_id = results.insert_one(result).inserted_id
    return str(result_id)

def Get(id):
    result = results.find_one({'_id': ObjectId(id)})

    return result

def Getall():
    result = results.find()

    return result
