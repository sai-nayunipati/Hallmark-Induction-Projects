"""
This module can identify the college from the email address. It does this using 
the Hipo university domains list API. Most universities in the world are supported.
The data is first stored in a MySQL database if needed, and is then read.

This program has trouble with email addresses like john@cs.usc.edu because the department
domain is not ignored by the SQL query logic.
"""

import mysql.connector
import requests


def populate_database():
    """
    This function populates the MySQL databse with university information from the API.
    It ignores duplicates upon insertion.
    """
    # Establish the database connection.
    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="test")
    cursor = db.cursor()

    # Make an API call and store the response. (pylint: disable=invalid-name)
    URL = 'http://universities.hipolabs.com/search'
    r = requests.get(URL)
    # print("Status code:", r.status_code)
    list_of_dicts = r.json()

    # Add each university to the database
    for university in list_of_dicts:
        # I'm including unused variables to make the query more readable. (pylint: disable=unused-variable)
        domains, web_pages, state_province, name, country, alpha_two_code = university.values()

        # pylint: disable=line-too-long
        sql = "INSERT IGNORE into universities (name, country, web_pages, domains) VALUES (%s, %s, %s, %s)"
        vals = (name, country, str(web_pages), str(domains))
        cursor.execute(sql, vals)

    db.commit()
    db.close()


def get_name_from_address(address):
    """
    This function takes an email address and returns the university name.
    It assumes that the SQL database has already been populated.
    """
    # Establish the database connection. (pylint: disable=invalid-name)
    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="test")
    cursor = db.cursor()

    # Get the university name from the database.
    sql = "SELECT name FROM universities WHERE domains LIKE %s"
    # The wildcards are crucial because the domains are stored in a list in SQL
    vals = ("%" + address.split("@")[1] + "%",)
    cursor.execute(sql, vals)

    result = cursor.fetchone()
    if result is None:
        db.close()
        return "Could not determine the university name."
    else:
        db.close()
        return result[0]


# populate_database()
university_name = get_name_from_address("johns@uconn.edu")
print(university_name)  # Will print "University of Connecticut"
