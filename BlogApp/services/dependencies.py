from injector import singleton
from repository.posts_repo import PostsRepo
from repository.database_posts_repo import DatabasePostRepo
from repository.in_memory_posts_repo import InMemoryPostsRepo
from services.repo_service import RepoService
from setup.config import Config

def configure(binder):
    binder.bind(RepoService, to=RepoService, scope=singleton)
    binder.bind(PostsRepo, to=DatabasePostRepo, scope=singleton)
    binder.bind(Config, to=Config, scope=singleton)
