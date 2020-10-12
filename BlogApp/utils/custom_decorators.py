from functools import wraps
from injector import inject
from flask import url_for, redirect
from services.config_service import ConfigService

def is_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: ConfigService, *args, **kwargs):
        if not conf.config.is_configured():
            return redirect(url_for('setup_blueprint.setup'))
        return funct(*args, **kwargs)
    return decorated_function

def is_not_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: ConfigService, *args, **kwargs):
        if conf.config.is_configured():
            return redirect(url_for('index.posts'))
        return funct(*args, **kwargs)
    return decorated_function
