import mysql.connector

# the default mysql credentials are "root" and a blank password
db = mysql.connector.connect(
    host="localhost", user="root", password="", database="test")

cursor = db.cursor()

search = input("Enter Keyword : ")

# A SQL command like we would type in the command line
sql = f"SELECT * FROM todos WHERE todo like '%{search}%' LIMIT 10"

cursor.execute(sql)

# db.commit is used to save changes if we actually modify the database

res = cursor.fetchall()

for todo in res:
    print(todo)
