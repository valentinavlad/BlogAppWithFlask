from functools import wraps
from flask import url_for, redirect
from setup.config import Config

config = Config()

def is_config_file(funct):
    @wraps(funct)
    def decorated_function(*args, **kwargs):
        if not config.is_configured():
            return redirect(url_for('setup_blueprint.setup'))
        return funct(*args, **kwargs)
    return decorated_function
