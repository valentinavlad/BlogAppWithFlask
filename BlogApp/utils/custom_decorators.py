from functools import wraps
from injector import inject
from flask import url_for, redirect
from setup.database_config import DatabaseConfig

def is_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: DatabaseConfig, *args, **kwargs):
        #if not conf.is_configured():
        if not conf.configured:
            return redirect(url_for('setup_blueprint.setup'))
        return funct(*args, **kwargs)
    return decorated_function

def is_not_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: DatabaseConfig, *args, **kwargs):
        if conf.configured:
            return redirect(url_for('index.posts'))
        return funct(*args, **kwargs)
    return decorated_function
