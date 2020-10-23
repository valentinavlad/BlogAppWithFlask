from flask import session, redirect, url_for
from services.password_manager import PasswordManager
class Authentication:
    @staticmethod
    def login(repo, email, password):
        error = None
        user = repo.check_user_exists(email)
        if user is None:
            error = "This user is not registered"
            return error, user
        if email != user.email or not PasswordManager.is_correct_password(password, user):
            error = 'Invalid credentials.'
        return error, user

    @staticmethod
    def logout_user():
        session.clear()
        return redirect(url_for('index.posts'))

    @staticmethod
    def is_admin():
        return session['email'] == 'admin@gmail.com'
    @staticmethod
    def is_current_user():
        return session['user_id']
