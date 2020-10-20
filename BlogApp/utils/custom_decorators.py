from functools import wraps
from injector import inject
from flask import url_for, redirect, session
from setup.database_config import DatabaseConfig
from models.post import Post

def is_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: DatabaseConfig, *args, **kwargs):
        if not conf.is_configured():
            return redirect(url_for('setup_blueprint.setup'))
        return funct(*args, **kwargs)
    return decorated_function

def is_not_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: DatabaseConfig, *args, **kwargs):
        if conf.is_configured():
            return redirect(url_for('index.posts'))
        return funct(*args, **kwargs)
    return decorated_function

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' in session:
            user_id =  session['user_id']
            print(session._get_current_object)
        else:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def admin_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if session['email'] != 'admin@gmail.com':
            return redirect(url_for('index.posts'))
        return view(**kwargs)
    return wrapped_view
#nu merge asa, de schimbat, sterge postu si vezi cum altfel verifivi owneru
#cum sa determin ownerul postului
def owner_required(view):
    @wraps(view)
    def wrapped_view(post):
        if session['user_id'] != post.user_id:
            return redirect(url_for('index.posts'))
        return view(post)
    return wrapped_view