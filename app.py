"""
Testing Flask app
"""

import os
from flask import Flask, request, jsonify
from flask import flash, redirect
from analyze import analyze

UPLOAD_FOLDER = './cached/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users = []
files = []

@app.route('/')
def home():
    """Render website's home page."""
    return jsonify("<h1> Welcome to TU.AI! </h1>")


@app.route('/users')
def get_users():
    """ Get users """
    return jsonify(users)

@app.route('/users', methods = ['POST'])
def create_user():
    """ Create users """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        users.append(json)
        return json
    return 'Content-Type not supported!'

@app.route('/files')
def get_files():
    """ Get filles """
    path = "resources/family.png"
    result = analyze(path)
    return jsonify(result)

@app.route('/upload', methods = ['POST'])
def upload_file():
    """ Uploading image for analysis """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            files.append(filepath)
            return jsonify(analyze(filepath))

###
# The functions below should be applicable to all Flask apps.
###
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

###
# The functions below should be applicable to all Flask apps.
###
@app.errorhandler(404)
def page_not_found():
    """Custom 404 page."""
    return jsonify("<h1> Not Found </h1>")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
