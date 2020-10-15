from flask import Flask, redirect
from flask_injector import FlaskInjector

from services.dependencies import configure_production
from views.posts_view import index_blueprint
from views.setup_view import setup_blueprint
from views.users_view import users_blueprint

app = Flask(__name__)
app.secret_key = 'any random string'

app.register_blueprint(index_blueprint, url_prefix="/posts")
app.register_blueprint(setup_blueprint, url_prefix="/setup")
app.register_blueprint(users_blueprint, url_prefix="/user")

@app.route('/')
def index():
    return redirect('/posts/')

FlaskInjector(app=app, modules=[configure_production])

if __name__ == '__main__':
    app.run(debug=True)
    #app.run('localhost', 4449)
