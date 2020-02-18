import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/api/v1/resources/users/createnew', methods=['POST'])
def api_insert():
    conn = sqlite3.connect('users.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    insert_users = cur.execute('INSERT into users (id,Name,email,password) VALUES (10,"postuser","postUser@abc.com","test");')
    con.commit();
   




@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



app.run()
