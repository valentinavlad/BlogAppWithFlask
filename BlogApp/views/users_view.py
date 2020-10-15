from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session, g
from repository.database_users_repo import DatabaseUsersRepo
from models.user import User

users_blueprint = Blueprint('users', __name__, template_folder='templates',
                            static_folder='static')


@inject
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login(repo: DatabaseUsersRepo):
    if request.method == 'POST':
        error = None
        user = User(name=request.form.get("name"), email=request.form.get("email"),
                    password=request.form.get("password"))
        user_exists = repo.check_user_exists(user)
        if not user_exists:
            error = 'User {} is not registered.'.format(user.name)
        if not user.name:
            error = 'Name is required.'
        elif not user.email:
            error = 'Email is required.'
        elif not user.password:
            error = 'Password is required.'

        if error is None:
            session.clear()
            session['user_id'] = user.user_id
            return redirect(url_for('index.posts'))
        flash(error)
    return render_template('login.html')

@users_blueprint.before_app_request
def display_logged_user(repo: DatabaseUsersRepo):
    user_id = session['user_id']
    if user_id is None:
        g.user = None
    else:
        g.user = repo.find_by_id(user_id)

@users_blueprint.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index.posts'))