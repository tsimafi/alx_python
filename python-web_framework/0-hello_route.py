"""
0-hello_route.py

This module implements a simple Flask web application with a single route.

The web application listens on 0.0.0.0, port 5000. It has one route:
- Route: /
  Description: Displays "Hello HBNB!" when accessed.

Usage:
    Run this module with Python to start the Flask web application:
        $ python3 0-hello_route.py

Routes:
    - /: Display "Hello HBNB!"
        - Uses the option strict_slashes=False in route definition.

Example:
    $ curl 0.0.0.0:5000
    Hello HBNB!

Author:
    [Your Name]
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Defines the behavior for the route '/'.

    Returns:
        str: The string "Hello HBNB!".
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
