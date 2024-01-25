#!/usr/bin/python3
"""
0-hello_route.py - Starts a Flask web application.
"""

from flask import Flask

app = Flask(_name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route: / - Displays "Hello HBNB!"
    """
    return "Hello HBNB!"

if name == "_main_":
    app.run(host="0.0.0.0", port=5000)