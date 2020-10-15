from flask import Blueprint, render_template, url_for, request, redirect

users_blueprint = Blueprint('users', __name__, template_folder='templates',
                            static_folder='static')

@users_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')