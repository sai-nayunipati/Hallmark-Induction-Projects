"""Task seven of the induction program."""

import csv
# The error is thrown because pylint fails to see the venv modules.
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = db.cursor()

# Add all the entries in the csv.
with open("data.csv", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        # pylint: disable=line-too-long
        SQL = "INSERT INTO accounts(username, first_name, last_name, email, age) VALUES (%s, %s, %s, %s, %s)"
        values = (f"{row[0]}", f"{row[1]}",
                  f"{row[2]}", f"{row[3]}", f"{row[4]}")
        cursor.execute(SQL, values)

        print("Added: " + str(row))

# Save changes.
db.commit()
