import datetime
from injector import inject
from flask import Blueprint, render_template, url_for, request, redirect
from utils.custom_decorators import is_config_file
#from repository.posts_repo_factory import PostsRepoFactory as repo
from services.repo_service import RepoService
from models.post import Post

index_blueprint = Blueprint('index', __name__, template_folder='templates',
                            static_folder='static')

@inject
@index_blueprint.route('/', methods=['GET', 'POST'])
@is_config_file
def posts(service: RepoService):
    #return render_template('list_posts.html', content=repo.get().view_posts())
    return render_template('list_posts.html', content=service.repo.view_posts())

@inject
@index_blueprint.route('/new', methods=['GET', 'POST'])
@is_config_file
def new(service: RepoService):
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), owner=request.form.get("owner"),
                    contents=request.form.get("contents"), created_at=date_now,
                    modified_at=date_now)
        service.repo.add_post(post)
        #repo.get().add_post(post)
        return redirect(url_for('index.posts'))
    return render_template('add_post.html')

@inject
@index_blueprint.route('/<int:pid>', methods=['GET'])
@is_config_file
def view_post(service: RepoService, pid):
    post = service.repo.find_post_id(pid)
    #post = repo.get().find_post_id(pid)
    return render_template('view_post.html', post=post)

@inject
@index_blueprint.route('/<int:pid>/edit', methods=['GET', 'POST'])
@is_config_file
def edit(service: RepoService, pid):
    found_post = service.repo.find_post_id(pid)
    if request.method == 'POST':
        if found_post is not None:
            date_now = datetime.datetime.now()
            post = found_post
            post.title = request.form.get("title")
            post.owner = request.form.get("owner")
            post.contents = request.form.get("contents")
            post.created_at = found_post.created_at
            post.modified_at = date_now
            service.repo.edit_post(post)
        return redirect(url_for('index.view_post', pid=post.post_id))
    return render_template('edit_post.html', post=found_post)

@inject
@index_blueprint.route('/<int:pid>/delete', methods=['GET', 'POST'])
@is_config_file
def delete(service: RepoService, pid):
    post_delete = service.repo.find_post_id(pid)
    if post_delete is not None:
        service.repo.delete_post(pid)
        return redirect(url_for('index.posts'))
    return render_template('view_post.html')
