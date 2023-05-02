#!/usr/bin/python3
"""
10-hbnb_filters module
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the HBNB project index page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)

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
