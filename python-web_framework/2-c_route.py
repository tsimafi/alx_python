#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(_name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display “Hello HBNB!” """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display “HBNB” """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Display “C ” followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)