###
# Testing Flask app
###

from flask import Flask
from flask import jsonify, request


app = Flask(__name__)

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
    else:
        return 'Content-Type not supported!'


@app.route('/<file_name>.jpg')
def send_image_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

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
