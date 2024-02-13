from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)

# Route definitions
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = unquote(text).replace("_", " ")
    return 'C {}'.format(text)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
