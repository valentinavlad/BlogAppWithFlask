from unittest.mock import Mock
from injector import singleton
from flask_injector import request
from repository.posts_repo import PostsRepo
from repository.users_repo import UsersRepo
from repository.image_repo import ImageRepo
from repository.db_posts_repo_sqlalchemy import DbPostsRepoSqlalchemy
from repository.db_users_repo_sqlalchemy import DbUsersRepoSqlalchemy
from repository.database_image_repo import DatabaseImageRepo
from repository.in_memory_posts_repo import InMemoryPostsRepo
from repository.in_memory_users_repo import InMemoryUsersRepo
from repository.in_memory_image_repo import InMemoryImageRepo
from setup.database_config import DatabaseConfig
from setup.db_connect import DbConnect
from setup.db_operations import DbOperations
from services.authentication import Authentication
from services.password_manager import PasswordManager
from services.user_statistic import UserStatistic
from functionality.pagination import Pagination

def configure_production(binder):
    binder.bind(UserStatistic, to=UserStatistic, scope=singleton)
    binder.bind(PostsRepo, to=DbPostsRepoSqlalchemy, scope=singleton)
    binder.bind(UsersRepo, to=DbUsersRepoSqlalchemy, scope=singleton)
    binder.bind(ImageRepo, to=DatabaseImageRepo, scope=singleton)
    binder.bind(DatabaseConfig, to=DatabaseConfig, scope=singleton)
    binder.bind(Authentication, to=Authentication, scope=singleton)
    binder.bind(PasswordManager, to=PasswordManager, scope=singleton)
    binder.bind(DbConnect, to=DbConnect, scope=singleton)
    binder.bind(DbOperations, to=DbOperations, scope=singleton)
    binder.bind(Pagination, to=Pagination, scope=singleton)

def configure_test(binder):
    binder.bind(UserStatistic, to=UserStatistic, scope=singleton)
    binder.bind(PostsRepo, to=InMemoryPostsRepo, scope=singleton)
    binder.bind(UsersRepo, to=InMemoryUsersRepo, scope=singleton)
    binder.bind(ImageRepo, to=InMemoryImageRepo, scope=singleton)
    binder.bind(DatabaseConfig, to=Mock(DatabaseConfig), scope=request)
    binder.bind(Authentication, to=Authentication, scope=request)
    binder.bind(PasswordManager, to=PasswordManager, scope=request)
    binder.bind(DbConnect, to=Mock(DbConnect), scope=singleton)
    binder.bind(DbOperations, to=Mock(DbOperations), scope=singleton)
    binder.bind(Pagination, to=Pagination, scope=singleton)
