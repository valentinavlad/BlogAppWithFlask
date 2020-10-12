import pytest
from flask_injector import FlaskInjector
from app import app
from services.dependencies import configure_test

@pytest.fixture
def client():
    FlaskInjector(app=app, modules=[configure_test])
    app.testing = True
    return app.test_client()
