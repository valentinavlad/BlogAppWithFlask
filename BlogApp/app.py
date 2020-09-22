from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h1>Hello world!!</h1>'

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
