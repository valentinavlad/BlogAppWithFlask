import os.path
from injector import inject
from flask import Blueprint, render_template, request, redirect, url_for
from setup.db_operations import DbOperations
from setup.config import Config
from setup.config_interface import ConfigInterface
from services.config_service import ConfigService
setup_blueprint = Blueprint('setup_blueprint', __name__, template_folder='templates',
                            static_folder='static')

@inject
@setup_blueprint.route('/', methods=['GET', 'POST'])
def setup(config_db: ConfigService):
    if os.path.isfile('./database.ini'):
    #if config_db.config.is_configured:
        return redirect(url_for('index.posts'))
    db_operation = DbOperations()
    if request.method == 'POST':
        user = request.form.get('user')
        database = request.form.get('database')
        password = request.form.get('password')
        db_operation.config.load(database, user, password)
        db_operation.connect_to_db()
        return redirect(url_for('index.posts'))
    return render_template('setup.html')
