#!/usr/bin/python3
"""
8-cities_by_states module
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Fetchs data from the storage engine
    """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def do_teardown_appcontext(exc):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """
    Custom 404 response
    """
    return "404: Page not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
