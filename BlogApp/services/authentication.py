from injector import inject
from flask import session, redirect, url_for
from services.password_manager import PasswordManager
from repository.users_repo import UsersRepo

class Authentication():
    @inject
    def __init__(self, secure_pass: PasswordManager, repo: UsersRepo):
        self.secure_pass = secure_pass
        self.repo = repo

    def login(self, email, password):
        error = None
        user = self.repo.check_user_exists(email)
        if user is None:
            error = "This user is not registered"
            return error, user
        if email != user.email or not self.secure_pass.is_correct_password(password, user):
            error = 'Invalid credentials.'
        return error, user

    @staticmethod
    def logout_user():
        session.clear()
        return redirect(url_for('index.posts'))
