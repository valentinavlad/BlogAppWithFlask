from injector import inject
import psycopg2
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc
from models.user import User
from repository.users_repo import UsersRepo
from services.password_manager import PasswordManager
from setup.db_connect import DbConnect
from repository.models.post import Post
from repository.models.user import User
from repository.posts_repo import PostsRepo
from models.user import User as ModelUser


class DbUsersRepoSqlalchemy(UsersRepo):

    @inject
    def __init__(self, secure_pass: PasswordManager, db_connect: DbConnect):
        self.secure_pass = secure_pass
        self.db_connect = db_connect
        self.session = Session(bind=self.db_connect.get_engine())

    def find_by_id(self, pid):
        query = self.session.query(User).filter(User.user_id == pid).first()
        user = ModelUser.unmapp_user(query)
        return user

    def check_user_exists_by_name(self, name):
        query = self.session.query(User).filter(User.name == name).first()
        return query is None

    def edit(self, user):
        user_update = {User.name: user.name, User.email: user.email,
                       User.password: user.password, User.created_at: user.created_at,
                       User.modified_at: User.modified_at}
        get_user = self.session.query(User).filter(User.user_id == user.user_id)
        get_user.update(user_update)
        self.session.commit()

    def delete(self, pid):
        user = self.session.query(User).filter(User.user_id == pid).first()
        self.session.delete(user)
        self.session.commit()

    @inject
    def add(self, user):
        user_to_add = User(
            name=user.name,
            email=user.email,
            password=self.secure_pass.generate_secured_pass(user.password),
            created_at=user.created_at,
            modified_at=user.modified_at)
        self.session.add(user_to_add)
        self.session.commit()

    def view_all(self):
        users = []
        query = self.session.query(User)
       
        for row in query:
            user = ModelUser.unmapp_user(row)
            users.append(user)
        return users
