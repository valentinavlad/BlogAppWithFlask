import datetime
from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session
from repository.users_repo import UsersRepo
from utils.setup_decorators import is_config_file
from utils.authorization import admin_required, admin_or_owner_required,\
   login_required
from models.user import User

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
        if repo.check_user_exists_by_name(user.name) is None:
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
        if session.get("post_owner_id") is not None:
            session.pop('post_owner_id', None)
            session.pop('post_owner', None)
        return redirect(url_for('users.users'))
    return render_template('view_user.html')

@users_blueprint.route('/<int:uid>/set_credentials')
def set_credentials(uid):
    return render_template('set_credentials.html', uid=uid)
