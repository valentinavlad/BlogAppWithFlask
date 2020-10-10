from injector import singleton
from repository.posts_repo import PostsRepo
from repository.database_posts_repo import DatabasePostRepo
from repository.in_memory_posts_repo import InMemoryPostsRepo
from services.repo_service import RepoService
from services.config_service import ConfigService
from setup.config_interface import ConfigInterface
from setup.config import Config


def configure(binder):
    binder.bind(RepoService, to=RepoService, scope=singleton)
    binder.bind(PostsRepo, to=DatabasePostRepo, scope=singleton)
def configure_db(binder):
    binder.bind(ConfigService, to=ConfigService, scope=singleton)
    binder.bind(ConfigInterface, to=Config, scope=singleton)