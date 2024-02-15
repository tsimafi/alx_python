"""
1-hbnb_route.py

This module implements a Flask web application with two routes.

The web application listens on 0.0.0.0, port 5000. It has two routes:
- Route: /
  Description: Displays "Hello HBNB!" when accessed.
- Route: /hbnb
  Description: Displays "HBNB" when accessed.

Usage:
    Run this module with Python to start the Flask web application:
        $ python3 1-hbnb_route.py

Routes:
    - /: Display "Hello HBNB!"
        - Uses the option strict_slashes=False in route definition.
    - /hbnb: Display "HBNB"
        - Uses the option strict_slashes=False in route definition.

Example:
    $ curl 0.0.0.0:5000/hbnb
    HBNB

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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Defines the behavior for the route '/hbnb'.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
