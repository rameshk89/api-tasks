from flask import Flask, jsonify
from flask import request

app = Flask(__name__);

tasks = []

@app.route('/tasks', methods=['GET'])
def get_task():
    if tasks:
        return jsonify(tasks)
    else:
        return jsonify([{'id': 1, 'body': 'This is dummy body'}])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify({'result': 'success'})

app.run()