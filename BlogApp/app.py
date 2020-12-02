from flask import Flask, redirect
from injector import inject
from flask_injector import FlaskInjector
from utils.setup_decorators import is_config_file
from services.dependencies import configure_production
from setup.db_operations import DbOperations
from views.posts_view import index_blueprint
from views.setup_view import setup_blueprint
from views.login_view import login_blueprint
from views.users_view import users_blueprint
from views.user_statistic_view import user_statistic_blueprint

app = Flask(__name__)

app.secret_key = 'any random string'

app.register_blueprint(index_blueprint, url_prefix="/posts")
app.register_blueprint(setup_blueprint, url_prefix="/setup")
app.register_blueprint(login_blueprint, url_prefix="/auth")
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(user_statistic_blueprint, url_prefix="/statistics")

@app.route('/')
@is_config_file
def index():
    return redirect('/posts/')

@inject
@app.before_first_request
@is_config_file
def db_version_checking(db_operation: DbOperations):
    if not db_operation.is_db_updated():
        db_operation.update_version()

FlaskInjector(app=app, modules=[configure_production])

if __name__ == '__main__':
    #app.run(debug=True)
    app.run('localhost', 4449)
    