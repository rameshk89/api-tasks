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

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)