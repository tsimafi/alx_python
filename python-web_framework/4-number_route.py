"""
Define a route for '/hbnb'.
Returns:
    str: A simple message indicating 'HBNB'.
"""

from flask import Flask
from urllib.parse import unquote

# Create a Flask application instance
app = Flask(__name__)

# Route definitions

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Define a route for the root URL.
    Returns:
        str: A simple greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Define a route for '/hbnb'.
    Returns:
        str: A simple message indicating 'HBN
