from unittest.mock import Mock
from injector import singleton
from flask_injector import request
from repository.posts_repo import PostsRepo
from repository.users_repo import UsersRepo
from repository.database_posts_repo import DatabasePostRepo
from repository.database_users_repo import DatabaseUsersRepo
from repository.in_memory_posts_repo import InMemoryPostsRepo
from repository.in_memory_users_repo import InMemoryUsersRepo
from setup.database_config import DatabaseConfig
from setup.db_connect import DbConnect
from setup.db_operations import DbOperations
from services.authentication import Authentication
from services.password_manager import PasswordManager
from functionality.pagination import Pagination

def configure_production(binder):
    binder.bind(PostsRepo, to=DatabasePostRepo, scope=singleton)
    binder.bind(UsersRepo, to=DatabaseUsersRepo, scope=singleton)
    binder.bind(DatabaseConfig, to=DatabaseConfig, scope=singleton)
    binder.bind(Authentication, to=Authentication, scope=singleton)
    binder.bind(PasswordManager, to=PasswordManager, scope=singleton)
    binder.bind(DbConnect, to=DbConnect, scope=singleton)
    binder.bind(DbOperations, to=DbOperations, scope=singleton)
    binder.bind(Pagination, to=Pagination, scope=singleton)

def configure_test(binder):
    binder.bind(PostsRepo, to=InMemoryPostsRepo, scope=singleton)
    binder.bind(UsersRepo, to=InMemoryUsersRepo, scope=singleton)
    binder.bind(DatabaseConfig, to=Mock(DatabaseConfig), scope=request)
    binder.bind(Authentication, to=Authentication, scope=request)
    binder.bind(PasswordManager, to=PasswordManager, scope=request)
    binder.bind(DbConnect, to=Mock(DbConnect), scope=singleton)
    binder.bind(DbOperations, to=Mock(DbOperations), scope=singleton)
    binder.bind(Pagination, to=Mock(Pagination), scope=singleton)
