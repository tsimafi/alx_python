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
        str: A simple message indicating 'HBNB'.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Define a route for '/c/<text>' where <text> is a variable.
    Args:
        text (str): The text provided in the URL.
    Returns:
        str: A message with 'C' followed by the unquoted and underscore-replaced text.
    """
    text = unquote(text).replace("_", " ")  # Decode URL and replace underscores
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Define routes for '/python/' and '/python/<text>'.
    Args:
        text (str): Optional text provided in the URL.
    Returns:
        str: A message with 'Python' followed by the unquoted and underscore-replaced text (or default if not provided).
    """
    text = unquote(text).replace("_", " ") if text else "is cool"  # Decode URL and replace underscores
    return 'Python {}'.format(text)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
