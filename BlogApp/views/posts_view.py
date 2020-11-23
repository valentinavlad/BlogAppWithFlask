import datetime
import os
from injector import inject
from flask import Blueprint, render_template, url_for, request,\
   redirect, session, send_from_directory
from utils.setup_decorators import is_config_file
from utils.authorization import login_required
from repository.posts_repo import PostsRepo
from repository.users_repo import UsersRepo
from models.post import Post
from functionality.pagination import Pagination
from encoding_file import encode_file, decode_file

index_blueprint = Blueprint('index', __name__, template_folder='templates',
                            static_folder='static')
IMG_FOLDER = 'static/img/'
def session_add(select_form_get_user_id, user_repo):
    session['post_owner_id'] = select_form_get_user_id
    session['post_owner'] = user_repo.find_by_id(int(select_form_get_user_id)).name

@index_blueprint.route('/reset', methods=['GET', 'POST'])
@is_config_file
def reset():
    session.pop('post_owner_id', None)
    session.pop('post_owner', None)
    return redirect(url_for('index.posts'))

@inject
@index_blueprint.route('/', methods=['GET', 'POST'])
@is_config_file
def posts(repo: PostsRepo, user_repo: UsersRepo):
    owner_id = 0 if session.get("post_owner_id") is None else int(session['post_owner_id'])
    current_owner = '' if session.get("post_owner") is None else session['post_owner']
    if request.method == 'POST':
        select_form_get_user_id = request.form.get('users')
        if select_form_get_user_id is not None:
            session_add(select_form_get_user_id, user_repo)
            current_owner = request.args.get('user', session['post_owner'], type=str)
            owner_id = int(session['post_owner_id'])
    page = request.args.get('page', 1, type=int)

    pagination = Pagination(page, repo.get_count(owner_id))

    users = user_repo.view_all()
    all_posts = repo.get_all(owner_id, \
                pagination.records_per_page, pagination.offset)
    next_url = url_for('index.posts', page=str(pagination.next_page), user=current_owner) \
                   if pagination.has_next() else None
    prev_url = url_for('index.posts', page=str(pagination.prev_page)) \
                   if pagination.has_prev() else None

    return render_template('list_posts.html', content=all_posts,\
            next_url=next_url, prev_url=prev_url, users=users)

def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join('static/img/', uploaded_file.filename))
    return uploaded_file

@inject
@index_blueprint.route('/new', methods=['GET', 'POST'])
@is_config_file
@login_required
def new(repo: PostsRepo):
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        uploaded_file = request.files['file']

        post = Post(title=request.form.get("title"), owner=int(session['user_id']),
                    contents=request.form.get("contents"), img=uploaded_file)
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
@is_config_file
@login_required
def edit(repo: PostsRepo, pid):
    found_post = repo.find_by_id(pid)
    if session['name'] != 'admin' and not found_post.is_owner():
        return render_template('403error.html'), 403
    if request.method == 'POST':
        if found_post is not None:
            date_now = datetime.datetime.now()
            post = found_post
            post.title = request.form.get("title")
            post.contents = request.form.get("contents")
            post.created_at = found_post.created_at
            post.modified_at = date_now.strftime("%B %d, %Y")
            post.img = request.files['file']
            repo.edit(post)
        return redirect(url_for('index.view_post', pid=post.post_id))
    return render_template('edit_post.html', post=found_post)

@inject
@index_blueprint.route('/<int:pid>/delete', methods=['GET', 'POST'])
@is_config_file
@login_required
def delete(repo: PostsRepo, pid):
    post_delete = repo.find_by_id(pid)
    if post_delete is not None:
        if not post_delete.is_owner() and not session['email'] == 'admin@gmail.com':
            return render_template('403error.html'), 403
        repo.delete(pid)
        return redirect(url_for('index.posts'))
    return render_template('view_post.html')

@index_blueprint.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(IMG_FOLDER, filename)
