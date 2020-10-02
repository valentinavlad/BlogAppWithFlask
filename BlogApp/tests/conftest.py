import pytest
from app import app as flask_app

@pytest.fixture
def app_test():
    yield flask_app

@pytest.fixture
def client(app_test):
    return app_test.test_client()
