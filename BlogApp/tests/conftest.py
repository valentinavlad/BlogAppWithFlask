import pytest
from flask_injector import FlaskInjector
from app import app
from services.dependencies import configure_test
from repository.posts_repo_factory import PostsRepoFactory as repo
from unittest import mock
from setup.config import Config
@pytest.fixture
def client():
    #FlaskInjector(app=app, modules=[configure_test])
    app.testing = True
    return app.test_client()
