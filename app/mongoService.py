import os
from IResult import IResult
from pymongo import MongoClient
print(os.environ['DB_URL'])
client = MongoClient(os.environ['DB_URL'], 
                     username='root', 
                     password='admin',
                    authSource="admin")
results = client.LCT.results

def Save(result):
    result_id = results.insert_one(result).inserted_id
    return result_id
