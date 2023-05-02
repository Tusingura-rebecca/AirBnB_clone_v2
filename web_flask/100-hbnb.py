#!/usr/bin/python3
"""
100-hbnb module
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the HBNB project index page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)

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
