"""The backend of the PickUp application."""

from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(host="localhost", user="root",
                             password="", database="pickup_db")
cursor = db.cursor()


current_user_id = 1


@app.route('/browse')
@app.route('/')
def browse_page():
    """Return the browse page displaying all the products."""
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    res = cursor.fetchall()
    return render_template('browse.html', items=res)


@app.route('/cart')
def cart_page():
    """Return the cart page displaying all the products in the cart."""
    sql = "SELECT cart_item_id, item_id FROM cart_items WHERE buyer_id = %s"
    val = (current_user_id,)
    cursor.execute(sql, val)
    res = cursor.fetchall()
    to_pass = []
    for e in res:
        sql = "SELECT name, dollars FROM items WHERE item_id = %s"
        val = (e[1],)
        cursor.execute(sql, val)
        item = cursor.fetchone()

        # (cart_item_id , item_name, dollars)
        to_pass.append((e[0], item[0], item[1]))

    print(to_pass)

    return render_template('cart.html', cart_items=to_pass)


@app.route('/add/<int:item_id>')
def add_item_to_cart(item_id):
    """Add an item to the cart."""
    sql = "INSERT INTO cart_items (item_id, buyer_id) VALUES (%s, %s)"
    cursor.execute(sql, (item_id, current_user_id))
    db.commit()
    return jsonify({"success": True})


@app.route('/clear')
def clear_cart():
    """Clear all items in the cart of the logged in user."""
    sql = "DELETE FROM cart_items WHERE buyer_id = %s"
    val = (current_user_id,)
    cursor.execute(sql, val)
    db.commit()
    return jsonify({"success": True})


# Make sure we can only run the module explicitly.
if __name__ == '__main__':
    app.run(debug=True)
