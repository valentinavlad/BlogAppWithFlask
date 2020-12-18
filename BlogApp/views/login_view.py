from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session
from repository.users_repo import UsersRepo
from services.authentication import Authentication
from utils.setup_decorators import is_config_file
from utils.authorization import token_required
from models.user import User

login_blueprint = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

def set_session(user):
    session.clear()
    session['user_id'] = user.user_id
    session['name'] = user.name
    session['email'] = user.email
    session['logged_in'] = True


@inject
@login_blueprint.route('/login', methods=['GET', 'POST'])
@is_config_file
def login(auth: Authentication):
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get("password")
        error, user = auth.login(name, password)
        if user is not None and user.password is None:
            return redirect(url_for('users.set_credentials', uid=user.user_id))
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

@inject
@login_blueprint.route('/register', methods=['GET', 'POST'])
@is_config_file
def register(repo: UsersRepo):
    if request.method == 'POST':
        error = None
        name = request.form.get('name')
        email = request.form.get("email")
        password = request.form.get("password")
        cf_password = request.form.get("cf_password")
        user = repo.check_user_exists(email)
        if user is not None:
            error = 'Üser already registered!'
        else:
            if password != cf_password:
                error = "Pass must mach"
        if error is None:
            user = User(name, email, password)
            repo.add(user)
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('register.html')
