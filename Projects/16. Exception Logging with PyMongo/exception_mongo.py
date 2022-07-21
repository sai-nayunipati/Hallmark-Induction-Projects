import logging
import pymongo

logging.basicConfig(filename="logs.txt", filemode="w", level=logging.INFO,
                    format="%(asctime)s : %(message)s")
logger = logging.getLogger()

URL = "mongodb://localhost:27017"
mongoClient = pymongo.MongoClient(URL)
mydb = mongoClient["test_db"]
mycollection = mydb["test_collection"]

print("Hello! This is your simplified MongoDB shell. Enter a command:\n")

method = input("(Omit parentheses and args): mycollection.")
args = input("\n(Omit the closing parenthesis): mycollection." + method + "(")
try:
    eval("mycollection." + method + "(" + args + ")")  # pylint: disable=eval-used
except TypeError as te:
    logger.info("%s() is not a valid method.", method)
    logger.exception(te)
    print("An error occurred. Check the log for more information.")
except NameError as ne:
    logger.info("Invalid args: %s(%s)", method, args)
    logger.exception(ne)
    print("An error occurred. Check the log for more information.")
except Exception as e:  # pylint: disable=broad-except
    logger.info("Some unknown error occurred.")
    logger.exception(e)
    print("An error occurred. Check the log for more information.")
finally:
    print("\nThe shell has closed.")
