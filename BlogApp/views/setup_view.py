from injector import inject
from flask import Blueprint, render_template, request, redirect, url_for
from setup.db_operations import DbOperations
from utils.custom_decorators import is_not_config_file
from setup.config import Config

setup_blueprint = Blueprint('setup_blueprint', __name__, template_folder='templates',
                            static_folder='static')
@inject
@setup_blueprint.route('/', methods=['GET', 'POST'])
def setup(db_config: Config):
    if db_config.configured:
        return redirect(url_for('index.posts'))
    db_operation = DbOperations()
    if request.method == 'POST':
        user = request.form.get('user')
        database = request.form.get('database')
        password = request.form.get('password')
        db_config.save(database, user, password)
        db_operation.connect_to_db()
        #cum pot sa schimb dinamic valoarea???
        db_config.configured = True
        return redirect(url_for('index.posts'))
    return render_template('setup.html')
