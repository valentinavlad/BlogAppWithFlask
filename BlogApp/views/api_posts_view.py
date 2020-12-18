from injector import inject
from flask import Blueprint, jsonify, Response, json, make_response, request
from repository.posts_repo import PostsRepo
from services.authentication import Authentication
from utils.authorization import token_required
api_posts_blueprint = Blueprint('api_posts', __name__, template_folder='templates',
                                static_folder='static')
@inject
@api_posts_blueprint.route('/login', methods=['POST'])
def login(authentication: Authentication):
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401,\
           {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    error, user = authentication.login(auth.username, auth.password)
    if error is None:
        token = authentication.get_token(user)
        return jsonify({'token' : token})
    return make_response('Could not verify', 401,\
        {'WWW-Authenticate' : 'Basic realm="Login required!"'})

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
    if not post_delete.owner == user.user_id and not user.name == 'admin':
        return custom_response({'error': 'Forbidden'}, 403)
    repo.delete(pid)
    return jsonify({'message' : 'Post deleted!'})

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code)
