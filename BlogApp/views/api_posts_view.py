from injector import inject
from flask import Blueprint, jsonify, Response, json, make_response,\
   request, session
from repository.posts_repo import PostsRepo
from repository.users_repo import UsersRepo
from services.password_manager import PasswordManager
from services.authentication import Authentication
from utils.authorization import token_required

api_posts_blueprint = Blueprint('api_posts', __name__, template_folder='templates',
                                static_folder='static')

@inject
@api_posts_blueprint.route('/login', methods=['POST'])
def login(user_repo: UsersRepo, authentication: Authentication):
    auth = request.get_json()
    user = user_repo.check_user_exists_by_name(auth['username'])
    if user is not None and (user.password is None or user.password == ''):
        return custom_response({'message': 'Accepted', 'user_id': user.user_id}, 202)
    error, user = authentication.login(auth['username'], auth['password'])
    if error is None:
        token = authentication.encode_auth_token(user)
        if token:
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': token.decode()
            }
            set_session_token(authentication, token)
            return make_response(jsonify(response_object)), 200
    response_object = {
        'status': 'fail',
        'message': 'Credentials invalid!'
    }
    return make_response(jsonify(response_object)), 401

@inject
@api_posts_blueprint.route('/<int:pid>', methods=['GET'])
def view_post(repo: PostsRepo, pid):
    post = repo.find_by_id(pid)
    if post is None:
        return custom_response({'error': 'post not found'}, 404)
    return jsonify(post.__dict__)

@inject
@api_posts_blueprint.route('/<int:pid>/', methods=['DELETE'])
@token_required
def delete(repo: PostsRepo, pid):
    post_delete = repo.find_by_id(pid)
    if post_delete is None:
        return custom_response({'error': 'post not found'}, 404)
    repo.delete(pid)
    return jsonify({'message' : 'Post deleted!'})

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code)

@inject
def set_session_token(auth: Authentication, token):
    session.clear()
    user = auth.decode_auth_token(token)
    session['user_id'] = user["user_id"]
    session['name'] = user["name"]
    session['email'] = user["email"]
    session['logged_in'] = True

@inject
@api_posts_blueprint.route('/<int:uid>/set_credentials', methods=['POST'])
def set_credentials(repo: UsersRepo, secure_pass: PasswordManager, uid):
    user = repo.find_by_id(uid)
    error = None
    if user.password != '':
        return custom_response({'error': 'Forbidden!'}, 403)
    post_data = request.get_json()
    email = post_data["email"]
    password = post_data["password"]
    cf_password = post_data["cf_password"]
    if password != cf_password:
        error = "Pass must mach"
    if error is None:
        user.email = email
        user.password = secure_pass.generate_secured_pass(password)
        repo.edit(user)
        return jsonify(user.__dict__)
    return custom_response({'error': 'Forbidden!'}, 403)

@inject
@api_posts_blueprint.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    session.clear()
    return custom_response({'message': 'Successfully logged out.'}, 200)
