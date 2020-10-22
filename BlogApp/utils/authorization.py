from functools import wraps
from injector import inject
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
        if session['email'] != 'admin@gmail.com':
             return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view

def admin_or_owner_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        current_user = kwargs.get("pid")
        if session['email'] != 'admin@gmail.com' and session['user_id'] != current_user:
            return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view
