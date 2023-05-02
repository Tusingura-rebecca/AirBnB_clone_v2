#!/usr/bin/python3
"""
9-states module
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(state_id=None):
    """
    Fetchs data from the storage engine
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


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
