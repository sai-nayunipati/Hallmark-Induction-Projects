"""Build an API using Python Flask."""

from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my API!"


@app.route("/hello")
def hello():
    return "Hello World!"


db = mysql.connector.connect(host="localhost", user="root",
                             password="", database="test")
cursor = db.cursor()


@app.route("/todo/all", methods=["GET"])
def get_all_todos():
    sql = "SELECT * FROM todos"
    cursor.execute(sql)
    res = cursor.fetchall()
    return jsonify(res)


@app.route("/todo/<int:id>")
def get_todo_by_id(id):
    sql = "SELECT * FROM todos WHERE id = %s"
    cursor.execute(sql, (id,))
    res = cursor.fetchall()
    return jsonify(res)


@app.route("/todo/add", methods=['GET', 'POST'])
def add_todo():
    todo = request.get_json()
    sql = f"INSERT INTO todos (todo, userid) VALUES (%s, %s)"
    val = (todo['todo'], todo['userid'])
    cursor.execute(sql, val)
    db.commit()

    return jsonify(cursor.lastrowid)


@app.route("/todo/remove/<int:id>", methods=['GET', 'DELETE'])
def remove_todo(id):
    sql = f"DELETE FROM todos WHERE id=%s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    return jsonify("Todo removed.")


# Make sure we can only run the module explicitly.
if __name__ == '__main__':
    app.run(debug=True)
