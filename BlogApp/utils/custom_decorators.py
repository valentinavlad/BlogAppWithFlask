from functools import wraps
from injector import inject
from flask import url_for, redirect, g
from setup.database_config import DatabaseConfig

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
        if g.user is None:
            print(g.user)
            print('*****')
            print(g.user['user_id'])
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
