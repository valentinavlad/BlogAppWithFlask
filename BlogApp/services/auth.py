from injector import inject
from flask import session, redirect, url_for
from werkzeug.security import check_password_hash
from repository.users_repo import UsersRepo

class Auth:

    @staticmethod
    def login(repo, email, password):
        error = None
        user = repo.check_user_exists(email)
        if user is None:
            error = "This users is not registered"
        if email is None:
            error = 'Incorrect email.'
        #elif not check_password_hash(user.password, password):
        elif not password:
            error = 'Incorrect password.'
        return error, user

    @staticmethod
    def logout_user():
        session.clear()
        return redirect(url_for('index.posts'))
