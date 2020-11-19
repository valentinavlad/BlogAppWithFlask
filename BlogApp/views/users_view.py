import datetime
from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session
from repository.users_repo import UsersRepo
from utils.setup_decorators import is_config_file
from utils.authorization import admin_required, admin_or_owner_required,\
   login_required, first_loggin
from models.user import User
from services.password_manager import PasswordManager

users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@inject
@users_blueprint.route('/', methods=['GET', 'POST'])
@is_config_file
@login_required
@admin_required
def users(repo: UsersRepo):
    return render_template('list_users.html', content=repo.view_all())

@inject
@users_blueprint.route('/<int:pid>', methods=['GET'])
@is_config_file
@login_required
@admin_or_owner_required
def view_user(repo: UsersRepo, pid):
    user = repo.find_by_id(pid)
    return render_template('view_user.html', user=user)

@inject
@users_blueprint.route('/new', methods=['GET', 'POST'])
@is_config_file
@login_required
@admin_required
def new(repo: UsersRepo):
    if request.method == 'POST':
        error = None
        date_now = datetime.datetime.now()
        user = User(name=request.form.get("name"), email=request.form.get("email"),
                    password=request.form.get("password"))
        if repo.check_user_exists_by_name(user.name) is True:
            repo.add(user)
            user.created_at = date_now.strftime("%B %d, %Y")
            return redirect(url_for('users.users'))
        error = "This user already exists! Use another name"
        flash(error)
    return render_template('add_user.html')

@inject
@users_blueprint.route('/<int:pid>/edit', methods=['GET', 'POST'])
@is_config_file
@login_required
@admin_or_owner_required
def edit(repo: UsersRepo, pid):
    found_user = repo.find_by_id(pid)
    if request.method == 'POST':
        if found_user is not None:
            date_now = datetime.datetime.now()
            user = found_user
            user.name = request.form.get("name")
            user.email = request.form.get("email")
            user.password = request.form.get("password")
            user.created_at = found_user.created_at
            user.modified_at = date_now.strftime("%B %d, %Y")
            session['name'] = user.name if session['name'] != 'admin' else 'admin'
            repo.edit(user)
        return redirect(url_for('users.view_user', pid=user.user_id))
    return render_template('edit_user.html', user=found_user)

@inject
@users_blueprint.route('/<int:pid>/delete', methods=['GET', 'POST'])
@is_config_file
@login_required
@admin_required
def delete(repo: UsersRepo, pid):
    user_delete = repo.find_by_id(pid)
    if user_delete is not None:
        repo.delete(pid)
        return redirect(url_for('users.users'))
    return render_template('view_user.html')

@inject
@users_blueprint.route('/<int:uid>/set_credentials', methods=['GET', 'POST'])
@first_loggin
def set_credentials(repo: UsersRepo, secure_pass: PasswordManager, uid):
    user = repo.find_by_id(uid)

    if request.method == 'POST':
        error = None
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        cf_password = request.form.get("cf_password")
        if password != cf_password:
            error = "Pass must mach"
        if error is None:
            user.name = name
            user.email = email
            user.password = secure_pass.generate_secured_pass(password)
            repo.edit(user)
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('set_credentials.html', user=user)
