import pymongo

url = "mongodb://localhost:27017"

mongoClient = pymongo.MongoClient(url)

mydb = mongoClient["mydb"]

mycollection = mydb["users"]

# find(query, projection)
# documents = mycollection.find().limit(15)

# print(list(documents))

# for document in documents:
#     print(document[' "City"'], document[' "State"'])

documents = mycollection.find(
    {
        "name": {"$eq": "prasad"}
    },
    {"_id": 0, "name": 1, "email": 1}
)

print(list(documents))

mycollection.update_one({"name": "prasad"}, {"$set": {"password": "12345678"}})

# Insert a new item in mongodb


mycollection.insert_one({"name": "prasad", "email": ""})
