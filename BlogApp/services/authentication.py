from injector import inject
import jwt
from flask import session, redirect, url_for
from services.password_manager import PasswordManager
from repository.users_repo import UsersRepo

class Authentication():
    @inject
    def __init__(self, secure_pass: PasswordManager, repo: UsersRepo):
        self.secure_pass = secure_pass
        self.repo = repo

    def login(self, name, password):
        error = None
        user = self.repo.check_user_exists_by_name(name)
        if user is None:
            error = "This user is not registered"
            return error, user
        if user.password is None:
            return error, user
        if name != user.name or not self.secure_pass.is_correct_password(password, user):
            error = 'Invalid credentials.'
        token = jwt.encode({'user_id' : user.user_id}, "cucuisjdsj")
        return error, token.decode('UTF-8')

    @staticmethod
    def logout_user():
        session.pop('logged_in', None)
        session.clear()
        return redirect(url_for('index.posts'))
