import datetime
from flask import Blueprint, render_template
from flask import url_for, request, redirect, Response
from repository.posts_data import dummy_posts
from models.post import Post

index_blueprint = Blueprint('index', __name__, template_folder='templates',
                            static_folder='static')

@index_blueprint.route('/')
@index_blueprint.route('/posts/', methods=['GET','POST'])
def posts():
    return render_template('posts.html', content=dummy_posts)

@index_blueprint.route('/posts/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), 
                    owner= request.form.get("owner"),
                    contents=request.form.get("contents"))
        post.created_at = date_now.strftime("%B %d, %Y")
        post.modified_at = date_now.strftime("%B %d, %Y")
        dummy_posts.insert(0, post)
        return redirect(url_for('index.posts'))
    return render_template('post.html')

@index_blueprint.route('/posts/<int:id>', methods=['GET'])
def view_post(id):
    for post in dummy_posts:
        if post.post_id== id:
            found_post = post

    return render_template('view_post.html', post=found_post)

@index_blueprint.route('/posts/<int:id>/edit', methods=['GET','POST'])
def edit(id):
    for post in dummy_posts:
        if post.post_id == id:
            found_post = post
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), 
                    owner= request.form.get("owner"),
                    contents=request.form.get("contents"))
        post.created_at = date_now.strftime("%B %d, %Y")
        post.modified_at = date_now.strftime("%B %d, %Y")
        dummy_posts.remove(found_post)
        dummy_posts.insert(0, post)
        return redirect(url_for('index.posts'))
    return render_template('edit.html', post=found_post)

@index_blueprint.route('/posts/<int:id>', methods=['POST'])
def delete(id):
    deleted = False
    for post in dummy_posts:
        if post.post_id == id:
            found_post = post
            deleted = True
            dummy_posts.remove(found_post)
    if deleted:
        return redirect(url_for('index.posts'))
    return render_template('view_post.html')

