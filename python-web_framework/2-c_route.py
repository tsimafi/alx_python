from flask import Flask

app = Flask(name)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    result = 'C ' + text.replace('_', ' ')
    return result

if name == 'main':
    app.run(host='0.0.0.0', port=5000)