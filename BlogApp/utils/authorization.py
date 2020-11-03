from functools import wraps
from flask import url_for, redirect, session, render_template

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' in session:
            user_id = session['user_id']
            print(user_id)
        else:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def admin_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if session['name'] != 'admin':
            return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view

def admin_or_owner_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        current_user = kwargs.get("pid")
        if session['name'] != 'admin' and session['user_id'] != current_user:
            return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view

def first_loggin(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        current_user_id = kwargs.get("uid")
        repo = kwargs.get("repo")
        user = repo.find_by_id(current_user_id)
        if user.password is not None:
            return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view
