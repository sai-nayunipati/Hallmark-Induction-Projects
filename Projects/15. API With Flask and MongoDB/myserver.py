"""
This API queries the MongoDB database created in the last
exercise and returns the data in JSON format.
"""

import pymongo
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

URL = "mongodb://localhost:27017"
my_client = pymongo.MongoClient(URL)
my_db = my_client["chess_players"]


@app.route("/chess-player/all")
def fetch_top_players():
    """Return a list of all the top chess players in my database sorted by rank."""
    players = my_db["top_chess_players"]
    players_list = players.find({}, {"_id": 0})
    players_list = sorted(players_list, key=lambda k: k['rank'])
    return jsonify(list(players_list))


@app.route("/chess-player/top/<int:key>")
def fetch_top_players_limited(key):
    """Return a limited list of the top chess players on chess.com sorted by rank."""
    players = my_db["top_chess_players"]
    players_list = players.find({'rank': {'$lte': key}}, {"_id": 0})
    players_list = sorted(players_list, key=lambda k: k['rank'])
    return jsonify(list(players_list))


@app.route("/chess-player/rank/<int:key>")
def fetch_top_player_by_rank(key):
    """Find a player by their rank."""
    players = my_db["top_chess_players"]
    players_list = players.find({"rank": key}, {"_id": 0})
    return jsonify(list(players_list)[0])


@app.route("/chess-player/name/<string:name>")
def fetch_top_player_by_name(name):
    """
    Find a player by their name.
    May return multiple players with the same name.
    """
    name = name.replace("_", " ").title()
    players = my_db["top_chess_players"]
    players_list = list(players.find({"name": name}, {"_id": 0}))
    if len(players_list) == 0:
        return jsonify({"error": "Player not found."})
    return jsonify(list(players_list))


@app.route("/chess-player/random")
def fetch_top_player_random():
    """Query the database for a random top player."""
    players = my_db["top_chess_players"]
    players_cursor = list(players.aggregate(
        [{'$sample': {'size': 1}}, {'$project': {'_id': 0}}]))
    return jsonify(players_cursor[0])


@app.route("/chess-player/custom/all")
def fetch_custom_players():
    """Return a list of all the custom chess players in my database sorted by rank."""
    players = my_db["user_added_players"]
    players_list = players.find({}, {"_id": 0})
    return jsonify(list(players_list))


@app.route("/chess-player/add", methods=["GET", "POST"])
def add_custom_player():
    """Add a player to a custom collection."""
    new_player = request.get_json()
    custom_players = my_db["user_added_players"]
    custom_players.insert_one(new_player)
    return jsonify("New player added")


@app.route("/chess-player/remove/<key>")
def remove_custom_player(key):
    """
    Remove a player from the custom collection by name.
    The method replaces underscores from the URL with spaces.
    """
    custom_players = my_db["user_added_players"]
    key = key.replace("_", " ").title()
    custom_players.delete_one({"name": key})
    return jsonify(f"{key} removed")


@app.route("/chess-player/update/<key>", methods=["GET", "POST"])
def update_custom_player(key):
    """Update a player in the custom collection by name."""
    updated_player = request.get_json()
    custom_players = my_db["user_added_players"]
    key = key.replace("_", " ").title()
    custom_players.update_one({"name": key}, {"$set": updated_player})
    return jsonify(f"{key} updated")


@app.route("/")
def index():
    """Return an HTML page with a list of the top chess players on chess.com."""
    players = my_db["top_chess_players"]
    players_list = players.find({}, {"_id": 0}).limit(100)
    return render_template("index.html", players=players_list)


@app.route("/faq")
def faq():
    """Return an HTML page displaying the FAQs."""
    return render_template("faq.html")


@app.route("/pricing")
def pricing():
    """Return an HTML page displaying the pricing."""
    return render_template("pricing.html")


@app.route("/about")
def about():
    """Return an HTML page displaying the about page."""
    return render_template("about.html")


@app.route("/features")
def features():
    """Return an HTML page displaying the features page."""
    return render_template("features.html")


# Only run this code if this file is being run directly
if __name__ == "__main__":
    app.run(debug=True)
