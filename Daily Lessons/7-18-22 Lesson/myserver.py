import pymongo
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

URL = "mongodb://localhost:27017"
my_client = pymongo.MongoClient(URL)
my_db = my_client["chess_players"]


@app.route("/")
def index():
    """Home page."""
    return "Hello World"


# Todo: select only the players with a rank of 100 or better
# Todo: return the players in ascending order by rank
@app.route("/chess-players")
def list_chess_players():
    """Return a list of the top chess players on chess.com."""
    players = my_db["top_chess_players"]
    players_list = players.find({}, {"_id": 0}).limit(100)
    return jsonify(list(players_list))


@app.route("/chess-players/list")
def list_players():
    players = my_db["top_chess_players"]
    players_list = players.find({}, {"_id": 0}).limit(100)
    return render_template("list.html", players=players_list)


@app.route("/chess-player/<key>")
def find_chess_player(key):
    """Find a player by their rank."""
    players = my_db["top_chess_players"]
    players_list = players.find({"rank": key}, {"_id": 0})
    return jsonify(list(players_list))


@app.route("/chess-player/add", methods=["GET", "POST"])
def add_chess_player():
    """Add a player to a custom collection."""
    new_player = request.get_json()
    custom_players = my_db["user_added_players"]
    custom_players.insert_one(new_player)
    return jsonify("New player added")


@app.route("/chess-player/remove/<key>")
def remove_chess_player(key):
    """
    Remove a player from the custom collection by name.
    The method replaces underscores from the URL with spaces.
    """
    custom_players = my_db["user_added_players"]
    key = key.replace("_", " ")
    custom_players.delete_one({"name": key})
    return jsonify(f"{key} removed")


@app.route("/chess-player/update/<key>", methods=["GET", "POST"])
def update_chess_player(key):
    """Update a player in the custom collection by name."""
    updated_player = request.get_json()
    custom_players = my_db["user_added_players"]
    key = key.replace("_", " ")
    custom_players.update_one({"name": key}, {"$set": updated_player})
    return jsonify(f"{key} updated")


# Only run this code if this file is being run directly
if __name__ == "__main__":
    app.run(debug=True)
