from flask import Flask, jsonify
from flask import request, g
import sqlite3 as sql

DATABASE = 'tasks_db.db'

app = Flask(__name__);

tasks = []
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    return db

@app.route('/tasks', methods=['GET'])
def get_task():
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from tasks")
    res = cur.fetchall()
    return jsonify(res)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify({'result': 'success'})

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)