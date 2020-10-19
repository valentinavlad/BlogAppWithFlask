from injector import inject
from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session, g
from repository.users_repo import UsersRepo
from services.auth import Auth
from utils.custom_decorators import is_config_file

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

def set_session(user):
    session.clear()
    session['user_id'] = user.user_id
    session['name'] = user.name
    session['email'] = user.email

@inject
@auth_blueprint.route('/login', methods=['GET', 'POST'])
@is_config_file
def login(repo: UsersRepo, auth: Auth):
    if request.method == 'POST':
        email = request.form.get("email")
        password =  request.form.get("password")
        error, user = auth.login(repo, email, password)
        if error is None:
            set_session(user)
            return redirect(url_for('index.posts'))
        flash(error)
    return render_template('login.html')

@inject
@auth_blueprint.route('/logout')
def logout(auth: Auth):
    return auth.logout_user()
