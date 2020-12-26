import os
import datetime
from injector import inject
import jwt
from dotenv import load_dotenv
from flask import session, redirect, url_for
from services.password_manager import PasswordManager
from repository.users_repo import UsersRepo

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
class Authentication():
    @inject
    def __init__(self, secure_pass: PasswordManager, repo: UsersRepo):
        self.secure_pass = secure_pass
        self.repo = repo

    def login(self, name, password):
        error = None
        user = self.repo.check_user_exists_by_name(name)
        if user is None:
            error = "This user is not registered"
            return error, user
        if user.password is None:
            return error, user
        if name != user.name or not self.secure_pass.is_correct_password(password, user):
            error = 'Invalid credentials.'
        return error, user

    @staticmethod
    def get_token(user):
        token = jwt.encode({'user_id' : user.user_id}, SECRET_KEY)
        return token.decode('UTF-8')

    @staticmethod
    def logout_user():
        session.pop('logged_in', None)
        session.clear()
        return redirect(url_for('index.posts'))

    @staticmethod
    def encode_auth_token(user):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user.user_id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'