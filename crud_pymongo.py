import pymongo


client = pymongo.MongoClient("mongodb://localhost:0000/")
db = client["ur_database"]
collection = db["ur_collection"]
