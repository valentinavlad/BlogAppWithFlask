from functools import wraps
from injector import inject
from flask import url_for, redirect, session, render_template
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
