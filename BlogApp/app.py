from flask import Flask, redirect
from flask_injector import FlaskInjector

from services.dependencies import configure, configure_db
from views.posts_view import index_blueprint
from views.setup_view import setup_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint, url_prefix="/posts")
app.register_blueprint(setup_blueprint, url_prefix="/setup")

@app.route('/')
def index():
    return redirect('/posts/')

FlaskInjector(app=app, modules=[configure, configure_db])

if __name__ == '__main__':
    # Run the app server on localhost:4449
    #app.run(debug=True)
    app.run('localhost', 4449)
