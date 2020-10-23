from flask import session, redirect, url_for
from werkzeug.security import check_password_hash
class Authentication:

    @staticmethod
    def login(repo, email, password):
        error = None
        user = repo.check_user_exists(email)
        if user is None:
            error = "This user is not registered"
            return error, user
        if email != user.email or not check_password_hash(user.password, password):
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
