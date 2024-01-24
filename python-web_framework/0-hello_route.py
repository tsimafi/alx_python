from flask import Flask

app = Flask(name)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if name == 'main':
    app.run(host='0.0.0.0', port=5000)