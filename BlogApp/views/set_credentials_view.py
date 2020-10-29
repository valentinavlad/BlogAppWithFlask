from injector import inject
from flask import Blueprint, render_template, url_for, \
    request, redirect, flash
from repository.users_repo import UsersRepo
from services.password_manager import PasswordManager

credentials_blueprint = Blueprint('credentials_blueprint', __name__, template_folder='templates',
                                  static_folder='static')
@inject
@credentials_blueprint.route('/', methods=['GET', 'POST'])
def set_credentials(repo: UsersRepo, secure_pass: PasswordManager):
    if request.method == 'POST':
        error = None
        name = request.form.get('name')
        email = request.form.get("email")
        password = request.form.get("password")
        cf_password = request.form.get("cf_password")
        user = repo.check_user_exists_by_name(name)
        if user is None:
            error = 'Üser does not exist!'
        else:
            if password != cf_password:
                error = "Pass must mach"
        if error is None:
            user.email = email
            user.password = secure_pass.generate_secured_pass(password)
            repo.edit(user)
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('set_credentials.html')
