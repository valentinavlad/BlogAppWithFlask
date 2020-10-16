from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash, session, g
from repository.users_repo import UsersRepo

users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@inject
@users_blueprint.route('/', methods=['GET', 'POST'])
def users(repo: UsersRepo):
     return render_template('list_users.html', content=repo.view_all())
