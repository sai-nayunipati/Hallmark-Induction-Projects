import requests
import mysql.connector
from datetime import datetime
from tqdm import tqdm

# Make an API call and store the response.
db = mysql.connector.connect(host="localhost", user="root",
                             password="", database="test")
cursor = db.cursor()

url = 'https://inshorts.deta.dev/news'
params = {"category": "all"}
r = requests.get(url, params)
# print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()

# Process results.
for item in tqdm(response_dict['data']):
    author, content, date, id, image, resource, time, title, url = item.values()
    sql = "INSERT IGNORE into news (id, title, content, author, date, time, url, image, resource) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Make the date into a SQL date format
    dt = datetime.strptime(date, "%d %b %Y,%A").strftime("%Y-%m-%d")

    vals = (id, title, content, author, dt, time, url, image, resource)
    cursor.execute(sql, vals)
    print(author, title)

db.commit()
db.close()
