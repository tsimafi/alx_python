"""
1-hbnb_route.py

This module implements a Flask web application with three routes.

The web application listens on 0.0.0.0, port 5000. It has three routes:
- Route: /
  Description: Displays "Hello HBNB!" when accessed.
- Route: /hbnb
  Description: Displays "HBNB" when accessed.
- Route: /c/<text>
  Description: Displays "C <text>" when accessed.

Usage:
    Run this module with Python to start the Flask web application:
        $ python3 1-hbnb_route.py

Routes:
    - /: Display "Hello HBNB!"
        - Uses the option strict_slashes=False in route definition.
    - /hbnb: Display "HBNB"
        - Uses the option strict_slashes=False in route definition.
    - /c/<text>: Display "C <text>"
        - Uses the option strict_slashes=False in route definition.

Examples:
    $ curl 0.0.0.0:5000/hbnb
    HBNB
    $ curl 0.0.0.0:5000/c/julien
    C julien
    $ curl 0.0.0.0:5000/c/is_super_fun
    C is_super_fun
    $ curl 0.0.0.0:5000/noroute
    404

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


@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """
    Defines the behavior for the route '/c/<text>'.

    Parameters:
        text (str): The custom text provided in the URL.

    Returns:
        str: The string "C <text>".
    """
    return "C {}".format(text)


@app.errorhandler(404)
def page_not_found(error):
    """
    Defines the behavior when a 404 error occurs.

    Returns:
        str: The string "404" to indicate page not found.
    """
    return "404", 404


if text == "is_super_fun":
        return "C is super fun"
    else:
        return "C {}".format(text)
