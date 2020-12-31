import os
from functools import wraps
from injector import inject
from flask import url_for, redirect, session, render_template, request, jsonify
import jwt
from dotenv import load_dotenv
from repository.users_repo import UsersRepo

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' in session:
            user_id = session['user_id']
            print(user_id)
        else:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def admin_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if session['name'] != 'admin':
            return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view

def admin_or_owner_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        current_user = kwargs.get("pid")
        if session['name'] != 'admin' and session['user_id'] != current_user:
            return render_template('403error.html'), 403
        return view(**kwargs)
    return wrapped_view

def token_required(func):
    @wraps(func)
    @inject
    def decorated(user_repo: UsersRepo, *args, **kwargs):
        pid = kwargs.get("pid")
        repo = kwargs.get("repo")
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if not auth_token:
            return jsonify({'message' : 'Token is missing'}), 401
        try:
            data = jwt.decode(auth_token, SECRET_KEY)
            user = user_repo.find_by_id(data['sub']['user_id'])
            post = repo.find_by_id(pid)
            if post is None:
                return jsonify({'error': 'Post not found'}), 404
            if not int(post.owner) == user.user_id and not user.name == 'admin':
                return jsonify({'error': 'Forbidden'}), 403
        except jwt.DecodeError:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return func(*args, **kwargs)
    return decorated
