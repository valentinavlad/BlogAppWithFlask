from injector import inject
from flask import Blueprint, jsonify, Response, json, make_response,\
   request, session, flash
from repository.posts_repo import PostsRepo
from services.authentication import Authentication
from utils.authorization import token_required
from services.password_manager import PasswordManager
from repository.users_repo import UsersRepo

api_posts_blueprint = Blueprint('api_posts', __name__, template_folder='templates',
                                static_folder='static')

@inject
@api_posts_blueprint.route('/login', methods=['POST'])
def login(user_repo: UsersRepo, authentication: Authentication):
    auth = request.get_json()
    user = user_repo.check_user_exists_by_name(auth['username'])
    if user is not None and user.password is None:
        return custom_response({'message': 'Accepted', 'user_id': user.user_id}, 202)

    error, user = authentication.login(auth['username'], auth['password'])
    if error is None:
        token = authentication.encode_auth_token(user)
        if token:
            responseObject = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': token.decode()
            }
            set_session_token(authentication, token)
            return make_response(jsonify(responseObject)), 200
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Credentials invalid!'
        }
        return make_response(jsonify(responseObject)), 404
    return make_response('Could not verify', 401)


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
def delete(user, repo: PostsRepo, pid):
    post_delete = repo.find_by_id(pid)
    if post_delete is None:
        return custom_response({'error': 'post not found'}, 404)
    if not int(post_delete.owner) == user.user_id and not user.name == 'admin':
        return custom_response({'error': 'Forbidden'}, 403)
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
    if user is None:
        return jsonify({'message' : 'Token is invalid!'}), 401
    session['user_id'] = user["user_id"]
    session['name'] = user["name"]
    session['email'] = user["email"]
    session['logged_in'] = True

@inject
@api_posts_blueprint.route('/<int:uid>/set_credentials',  methods=['POST'])
def set_credentials(repo: UsersRepo, secure_pass: PasswordManager, uid):
    user = repo.find_by_id(uid)
    error = None
    #TO DO VALIDATE FORM
    if user.password is not None:
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
        #return redirect(url_for('auth.login'))
