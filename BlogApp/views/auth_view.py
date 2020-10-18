from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session, g
from repository.users_repo import UsersRepo
from utils.custom_decorators import is_config_file

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

def display_logged_user(repo: UsersRepo):
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = repo.find_by_id(user_id)
def set_session(user):
    session.clear()
    session['user_id'] = user.user_id
    session['name'] = user.name

@inject
@auth_blueprint.route('/login', methods=['GET', 'POST'])
@is_config_file
def login(repo: UsersRepo):
    if request.method == 'POST':
        error = None
        email = request.form['email']
        password = request.form['password']
        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        if error is None:
            user = repo.check_user_exists(email)
            if user is None:
                error = 'User {} is not registered.'.format(user.name)
            set_session(user)
            return redirect(url_for('index.posts'))
        flash(error)
    return render_template('login.html')

@auth_blueprint.before_app_request
def display_logged_user(repo: UsersRepo):
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = repo.find_by_id(user_id)

@auth_blueprint.route('/logout')
@is_config_file
def logout():
    session.clear()
    return redirect(url_for('index.posts'))
