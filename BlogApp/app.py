from flask import Flask,url_for
from views.index import index_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint, url_prefix="")

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
