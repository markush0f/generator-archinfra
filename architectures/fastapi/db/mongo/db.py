from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://root:example@db:27017/")
DB_NAME = "{{db_name}}"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

def get_collection(name: str):
    return db[name]
