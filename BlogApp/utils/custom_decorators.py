from functools import wraps
from injector import inject
from flask import url_for, redirect
from setup.config import Config

def is_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: Config, *args, **kwargs):
        configured = conf.is_configured()
        
        #if not conf.is_configured():
        if not conf.configured:
            return redirect(url_for('setup_blueprint.setup')) 
        return funct(*args, **kwargs)
    return decorated_function
#aici e buba
def is_not_config_file(funct):
    @wraps(funct)
    @inject
    def decorated_function(conf: Config, *args, **kwargs):
        configured = conf.is_configured()
        #if conf.is_configured():
        if conf.configured:
            return redirect(url_for('index.posts'))
        return funct(*args, **kwargs)
    return decorated_function
