import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["prak8"]
collection = db["MK"]
