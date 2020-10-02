import pytest
from app import app as flask_app
from repository.posts_repo_factory import PostsRepoFactory as repo

repo.testing = True
@pytest.fixture
def client(app_test):
    return app_test.test_client()
