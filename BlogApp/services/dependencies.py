from injector import singleton

from repository.posts_repo import PostsRepo
from repository.database_posts_repo import DatabasePostRepo
from services.repo_service import RepoService

def configure(binder):
    binder.bind(RepoService, to=RepoService, scope=singleton)
    binder.bind(PostsRepo, to=DatabasePostRepo, scope=singleton)