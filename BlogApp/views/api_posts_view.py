from injector import inject
from flask import Blueprint, jsonify
from repository.posts_repo import PostsRepo

api_posts_blueprint = Blueprint('api_posts', __name__, template_folder='templates',
                                static_folder='static')

@inject
@api_posts_blueprint.route('/<int:pid>', methods=['GET'])
def view_post(repo: PostsRepo, pid):
    post = repo.find_by_id(pid)
    return jsonify(post.__dict__)
