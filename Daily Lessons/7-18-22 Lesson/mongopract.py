import pymongo

URL = "mongodb://localhost:27017"
mongoClient = pymongo.MongoClient(URL)
mydb = mongoClient["mydb"]
mycollection = mydb["users"]

documents = mycollection.find().limit(15)
print(list(documents))

# for document in documents:
#     print(document[' "City"'], document[' "State"'])

# find(query, projection)
documents = mycollection.find(
    {
        "name": {"$eq": "prasad"}
    },
    # 0 = don't display, 1 = display
    {"_id": 0, "name": 1, "email": 1}
)

# print(list(documents))

# mycollection.update_one({"name": "prasad"}, {"$set": {"password": "12345678"}})

# mycollection.insert_one({"name": "prasad", "email": ""})
