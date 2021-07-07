import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['rung']


def database_use_collection(collection):
    db_collection = db[collection]
    if not db_collection:
        db_collection.create_collection(collection)
        db_collection = db_collection
    return db_collection


def database_write_one(collection, data):
    db_collection = db[collection]
    db_collection.insert_one(data)


def database_read_one(collection, read_filter):
    data = None
    db_collection = db[collection]
    data = db_collection.find_one(read_filter)
    return data


def database_find_and_modify(collection, read_filter, update_filter, **kwargs):
    data = None
    db_collection = db[collection]
    print(kwargs)
    data = db_collection.find_one_and_update(read_filter, update_filter, **kwargs)
    return data
