#!/usr/bin/python3
"""Starts a Flask web application.
listens on 0.0.0.0:5000.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"
