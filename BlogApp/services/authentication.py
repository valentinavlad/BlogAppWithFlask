import os
import datetime
from injector import inject
import jwt
from dotenv import load_dotenv
from flask import session, redirect, url_for, request, make_response
from services.password_manager import PasswordManager
from repository.users_repo import UsersRepo

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
class Authentication():
    @inject
    def __init__(self, secure_pass: PasswordManager, repo: UsersRepo):
        self.secure_pass = secure_pass
        self.repo = repo

    #TO DO: RENAME FUNCTION LOGIN to validate login
    def login(self, name, password):
        error = None
        user = self.repo.check_user_exists_by_name(name)
        if user is None:
            error = "This user is not registered"
            return error, user
        if name != user.name or not self.secure_pass.is_correct_password(password, user):
            error = 'Invalid credentials.'
        return error, user

    @staticmethod
    def logout_user():
        session.pop('logged_in', None)
        session.clear()
        return redirect(url_for('index.posts'))

    @staticmethod
    def encode_auth_token(user):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=1800),
                'iat': datetime.datetime.utcnow(),
                'sub': 
                {
                    "user_id" : user.user_id,
                    "name" : user.name,
                    "email" : user.email
                }
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
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'