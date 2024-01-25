#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask

app = Flask(name)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the root route."""
    return 'Hello HBNB!'


if name == "main":
    app.run(host="0.0.0.0", port=5000)
