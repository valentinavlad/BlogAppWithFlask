import pytest
from app import app as flask_app
from repository.posts_repo_factory import PostsRepoFactory

@pytest.fixture
def app_test():
    yield flask_app

@pytest.fixture
def client(app_test):
    return app_test.test_client()

@pytest.fixture
def db_inmemmory(app_test):
    return PostsRepoFactory.get_repo("InMemoryPosts")
