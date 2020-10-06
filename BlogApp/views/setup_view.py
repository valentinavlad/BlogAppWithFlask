import os.path
from flask import Blueprint, render_template, request, redirect, url_for
from setup.db_operations import DbOperations

setup_blueprint = Blueprint('setup_blueprint', __name__, template_folder='templates',
                            static_folder='static')

class Setup:
    @setup_blueprint.route('/', methods=['GET', 'POST'])
    def setup():
        db_operation = DbOperations()
        if request.method == 'POST':
            user = request.form.get('user')
            database = request.form.get('database')
            password = request.form.get('password')
            # create database.ini        
            db_operation.config.write_config_data(database, user, password)
            
            if os.path.isfile('./database.ini'):
                db_operation.create_database()
                print("INSIDE SETUP IS FILE")
                #config.get_connection_by_config('database.ini', 'postgresql')
                return redirect(url_for('index.posts'))
            else:
                print('Database.ini does not exist!!')
            return redirect(url_for('index.posts'))
        return render_template('setup.html')