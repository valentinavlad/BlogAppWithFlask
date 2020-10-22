from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session
from repository.users_repo import UsersRepo
from services.authentication import Authentication
from utils.setup_decorators import is_config_file

login_blueprint = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

def set_session(user):
    session.clear()
    session['user_id'] = user.user_id
    session['name'] = user.name
    session['email'] = user.email

@inject
@login_blueprint.route('/login', methods=['GET', 'POST'])
@is_config_file
def login(repo: UsersRepo, auth: Authentication):
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        error, user = auth.login(repo, email, password)
        if error is None:
            set_session(user)
            return redirect(url_for('index.posts'))
        flash(error)
    return render_template('login.html')

@inject
@login_blueprint.route('/logout')
@is_config_file
def logout(auth: Authentication):
    return auth.logout_user()
