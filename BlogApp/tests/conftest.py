import pytest
from app import app as flask_app
from repository.posts_repo_factory import PostsRepoFactory as repo

repo.testing = True

@pytest.fixture
def client():
    flask_app.testing = True
    return flask_app.test_client()