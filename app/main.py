
"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from flask import Flask
from flask import jsonify, request

###
# Routing for your application.
###

app = Flask(__name__)


users = []
files = []

@app.route('/')
def home():
    """Render website's home page."""
    return jsonify("<h1> Welcome to TU.AI! </h1>")


@app.route('/users')
def get_users():
    return jsonify(users)

@app.route('/users', methods = ['POST'])
def create_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        users.append(json)
        return json
    else:
        return 'Content-Type not supported!'

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.jpg')
def send_image_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify("<h1> Not Found </h1>")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")