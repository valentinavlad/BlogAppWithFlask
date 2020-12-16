from injector import inject
from flask import Blueprint, jsonify, Response, json, make_response, request
from repository.posts_repo import PostsRepo
from services.authentication import Authentication

api_posts_blueprint = Blueprint('api_posts', __name__, template_folder='templates',
                                static_folder='static')
@inject
@api_posts_blueprint.route('/login')
def login(authentication: Authentication):
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401,\
           {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    token = authentication.login(auth.username, auth.password)
    return jsonify({'token' : token})

@inject
@api_posts_blueprint.route('/<int:pid>', methods=['GET'])
def view_post(repo: PostsRepo, pid):
    post = repo.find_by_id(pid)
    if post is None:
        return custom_response({'error': 'post not found'}, 404)
    return jsonify(post.__dict__)

@inject
@api_posts_blueprint.route('/<int:pid>/', methods=['DELETE'])
def delete(repo: PostsRepo, pid):
    post_delete = repo.find_by_id(pid)
    if post_delete is None:
        return jsonify({'error' : 'No post found!'})
    repo.delete(pid)
    return jsonify({'message' : 'Post deleted!'})


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code)
