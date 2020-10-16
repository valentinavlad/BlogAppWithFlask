import datetime
from injector import inject
from flask import Blueprint, render_template, url_for, request, redirect
from utils.custom_decorators import is_config_file, login_required
from repository.posts_repo import PostsRepo
from models.post import Post

index_blueprint = Blueprint('index', __name__, template_folder='templates',
                            static_folder='static')

@inject
@index_blueprint.route('/', methods=['GET', 'POST'])
@is_config_file
def posts(repo: PostsRepo):
    return render_template('list_posts.html', content=repo.view_all())

@inject
@index_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
@is_config_file
def new(repo: PostsRepo):
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), owner=request.form.get("owner"),
                    contents=request.form.get("contents"))
        repo.add(post)
        post.created_at = date_now.strftime("%B %d, %Y")
        return redirect(url_for('index.posts'))
    return render_template('add_post.html')

@inject
@index_blueprint.route('/<int:pid>', methods=['GET'])
@is_config_file
def view_post(repo: PostsRepo, pid):
    post = repo.find_by_id(pid)
    return render_template('view_post.html', post=post)

@inject
@index_blueprint.route('/<int:pid>/edit', methods=['GET', 'POST'])
@login_required
@is_config_file
def edit(repo: PostsRepo, pid):
    found_post = repo.find_by_id(pid)
    if request.method == 'POST':
        if found_post is not None:
            date_now = datetime.datetime.now()
            post = found_post
            post.title = request.form.get("title")
            post.owner = request.form.get("owner")
            post.contents = request.form.get("contents")
            post.created_at = found_post.created_at
            post.modified_at = date_now.strftime("%B %d, %Y")
            repo.edit(post)
        return redirect(url_for('index.view_post', pid=post.post_id))
    return render_template('edit_post.html', post=found_post)

@inject
@index_blueprint.route('/<int:pid>/delete', methods=['GET', 'POST'])
@is_config_file
def delete(repo: PostsRepo, pid):
    post_delete = repo.find_by_id(pid)
    if post_delete is not None:
        repo.delete(pid)
        return redirect(url_for('index.posts'))
    return render_template('view_post.html')
