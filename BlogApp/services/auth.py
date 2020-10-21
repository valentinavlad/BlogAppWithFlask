from flask import session, redirect, url_for

class Auth:

    @staticmethod
    def login(repo, email, password):
        error = None
        user = repo.check_user_exists(email)
        if user is None:
            error = "This users is not registered"
        if email is None:
            error = 'Incorrect email.'
        elif not password:
            error = 'Incorrect password.'
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
