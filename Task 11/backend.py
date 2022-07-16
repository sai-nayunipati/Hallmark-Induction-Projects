"""The backend of the LISTR application."""

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(host="localhost", user="root",
                             password="", database="test")
cursor = db.cursor()


@app.route("/tasks/all", methods=["GET"])
def get_all_tasks():
    """Get all tasks."""
    sql = "SELECT * FROM listr_tasks"
    cursor.execute(sql)
    res = cursor.fetchall()
    return jsonify(res)


# Not used anymore.
# @app.route("/tasks/<int:id>")
# def get_task_by_id(id):
#     """Get task by id."""
#     sql = "SELECT * FROM listr_tasks WHERE id = %s"
#     cursor.execute(sql, (id,))
#     res = cursor.fetchall()
#     return jsonify(res)


@app.route("/tasks/add", methods=['GET', 'POST'])
def add_task():
    """Add a task. All fields EXCEPT id are required."""
    todo = request.get_json()
    sql = "INSERT INTO listr_tasks (content, is_completed, place_in_order, added_by) VALUES (%s, %s, %s, %s)"
    val = (todo['content'], todo['is_completed'],
           todo['place_in_order'], todo['added_by'],)
    cursor.execute(sql, val)
    db.commit()

    return jsonify(cursor.lastrowid)


# Not used anymore.
# @app.route("/tasks/remove/<int:id>", methods=['GET', 'DELETE'])
# def remove_task(id):
#     """Remove a task by id. The task must exist."""
#     sql = "DELETE FROM listr_tasks WHERE id=%s"
#     val = (id,)
#     cursor.execute(sql, val)
#     db.commit()
#     return jsonify("Todo removed.")


@app.route("/tasks/clear", methods=['GET'])
def remove_all_tasks():
    """Remove all tasks."""
    sql = "DELETE FROM listr_tasks"
    cursor.execute(sql)
    db.commit()

    return jsonify("All todos removed.")


@app.route("/tasks/update/<int:id>", methods=['GET', 'POST'])
def update_task(id):
    """Change the completion status of a task by id. The task must exist."""
    sql = "UPDATE listr_tasks SET is_completed = NOT is_completed WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()

    return jsonify("Todo updated.")


@app.route("/tasks/move-up/<int:id>", methods=['GET'])
def move_task_up(id):
    """
    Swap the position of a task with the one before it in place_in_order.
    Precondition: the task must have a place_in_order > 1.
    """
    sql = "SELECT place_in_order FROM listr_tasks WHERE id = %s"
    cursor.execute(sql, (id,))
    task_place = cursor.fetchone()[0]

    sql = f"""UPDATE listr_tasks
             SET place_in_order = CASE place_in_order
                                       WHEN {task_place - 1} THEN {task_place}
                                       WHEN {task_place} THEN {task_place - 1}
                                       ELSE place_in_order
                                  END;"""

    cursor.execute(sql)
    db.commit()

    return jsonify("Task moved up.")


@app.route("/tasks/move-down/<int:id>", methods=['GET'])
def move_task_down(id):
    """
    Swap the position of a task with the one after it in place_in_order.
    Precondition: the task must have a place_in_order < the number of tasks.
    """
    sql = "SELECT place_in_order FROM listr_tasks WHERE id = %s"
    cursor.execute(sql, (id,))
    task_place = cursor.fetchone()[0]

    sql = f"""UPDATE listr_tasks
             SET place_in_order = CASE place_in_order
                                       WHEN {task_place + 1} THEN {task_place}
                                       WHEN {task_place} THEN {task_place + 1}
                                       ELSE place_in_order
                                  END;"""
    cursor.execute(sql)
    db.commit()

    return jsonify("Task moved down.")


@app.route("/about")
def about_page():
    """About page."""
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    """Contact page."""
    return render_template("contact.html")


@app.route("/")
def home():
    sql = "SELECT * FROM listr_tasks"
    cursor.execute(sql)
    res = cursor.fetchall()
    return render_template('home.html', todos=res)


# Make sure we can only run the module explicitly.
if __name__ == '__main__':
    app.run(debug=True)
