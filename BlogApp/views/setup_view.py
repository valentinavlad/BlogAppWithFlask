import os.path
from flask import Blueprint, render_template, request, redirect, url_for
from setup.db_operations import DbOperations
from setup.config import Config

setup_blueprint = Blueprint('setup_blueprint', __name__, template_folder='templates',
                            static_folder='static')

@setup_blueprint.route('/', methods=['GET', 'POST'])
def setup():
    if os.path.isfile('./database.ini'):
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
