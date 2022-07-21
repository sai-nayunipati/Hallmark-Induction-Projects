import pymongo
import logging

logging.basicConfig(filename="logs.txt", filemode="a")

URL = "mongodb://localhost:27017"
mongoClient = pymongo.MongoClient(URL)
mydb = mongoClient["test_db"]
mycollection = mydb["test_collection"]

print("Hello! This is your simplified MongoDB shell. Enter a command:\n")

command = input("mycollection.")
try:
    eval("mycollection." + command)
except Exception as e:
    print("An error has occurred: " + str(e))