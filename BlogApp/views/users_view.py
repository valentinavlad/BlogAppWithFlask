import datetime
from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session, g
from repository.users_repo import UsersRepo

users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@inject
@users_blueprint.route('/', methods=['GET', 'POST'])
def users(repo: UsersRepo):
     return render_template('list_users.html', content=repo.view_all())

@inject
@users_blueprint.route('/<int:pid>', methods=['GET'])
def view_user(repo: UsersRepo, pid):
    user = repo.find_by_id(pid)
    return render_template('view_user.html', user=user)

@inject
@users_blueprint.route('/<int:pid>/edit', methods=['GET', 'POST'])
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
            repo.edit(user)
        return redirect(url_for('users.view_user', pid=user.user_id))
    return render_template('edit_user.html', user=found_user)

@inject
@users_blueprint.route('/<int:pid>/delete', methods=['GET', 'POST'])
def delete(repo: UsersRepo, pid):
    user_delete = repo.find_by_id(pid)
    if user_delete is not None:
        repo.delete(pid)
        return redirect(url_for('users.users'))
    return render_template('view_user.html')
