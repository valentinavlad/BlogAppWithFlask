from injector import inject
from flask import Blueprint, jsonify, Response, json
from repository.posts_repo import PostsRepo

api_posts_blueprint = Blueprint('api_posts', __name__, template_folder='templates',
                                static_folder='static')

@inject
@api_posts_blueprint.route('/<int:pid>', methods=['GET'])
def view_post(repo: PostsRepo, pid):
    post = repo.find_by_id(pid)
    if post is None:
        return custom_response({'error': 'post not found'}, 404)
    return jsonify(post.__dict__)

def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code)
