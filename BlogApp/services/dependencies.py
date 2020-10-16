from unittest.mock import Mock
from injector import singleton
from flask_injector import request
from repository.posts_repo import PostsRepo
from repository.users_repo import UsersRepo
from repository.database_posts_repo import DatabasePostRepo
from repository.database_users_repo import DatabaseUsersRepo
from repository.in_memory_posts_repo import InMemoryPostsRepo
from setup.database_config import DatabaseConfig

def configure_production(binder):
    binder.bind(PostsRepo, to=DatabasePostRepo, scope=singleton)
    binder.bind(UsersRepo, to=DatabaseUsersRepo, scope=singleton)
    binder.bind(DatabaseConfig, to=DatabaseConfig, scope=singleton)

def configure_test(binder):
    binder.bind(PostsRepo, to=InMemoryPostsRepo, scope=singleton)
    #TO DO IN MEMMORY REPO USERS
    binder.bind(DatabaseConfig, to=Mock(DatabaseConfig), scope=request)
