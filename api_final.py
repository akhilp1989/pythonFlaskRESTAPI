import flask
from flask import request, jsonify,render_template,redirect, url_for,flash
import random


import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d




@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/home', methods=['GET'])
def welcome():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('users.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM users;').fetchall()

    return jsonify(all_users)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST', 'GET'])
def api_insert():
    # msg = "Record successfully added"
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    email = request.form.get('email')
    password = request.form.get('password')
    name=request.form.get('name');
    id = random.randint(300, 1000)
    request_body=(id,name,email,password)
    
    insert_users = cur.execute('INSERT into users VALUES (?,?,?,?);',request_body)
    conn.commit();
    return redirect('/home')

@app.route('/login', methods=['POST'])
def login_post():
    conn = sqlite3.connect('users.db')   
    cur = conn.cursor()
    email = request.form.get('email')
    password = request.form.get('password')
    e=(email,)
    user = cur.execute("SELECT * FROM users WHERE email=?",e).fetchone()
    
    # flash(email)


    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user:
        flash('Please check your login details and try again.')
        return redirect('/login') # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return redirect('/home')

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# @app.route('/api/v1/resources/users', methods=['GET'])
# def api_filter():
#     query_parameters = request.args

#     id = query_parameters.get('id')
   

#     query = "SELECT * FROM users WHERE"
#     to_filter = []

#     if id:
#         query += ' id=? AND'
#         to_filter.append(id)
#     if email:
#         query += ' email=? AND'
#         to_filter.append(email)
    
#     if not (id ):
#         return page_not_found(404)

#     query = query[:-4] + ';'

#     conn = sqlite3.connect('users.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()

#     results = cur.execute(query, to_filter).fetchall()

#     return jsonify(results)

app.run()