import pytest
from flask_injector import FlaskInjector
from app import app
from services.dependencies import configure_test
from setup.config import Config

@pytest.fixture
def client_is_config():
    app.testing = True
    FlaskInjector(app=app, 
                  modules=[configure_test]).injector.get(Config).configured = True
    return app.test_client()

@pytest.fixture
def client_is_not_config():
    app.testing = True
    FlaskInjector(app=app, 
                  modules=[configure_test]).injector.get(Config).configured = False
    return app.test_client()
