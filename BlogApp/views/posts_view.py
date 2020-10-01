import datetime
from flask import Blueprint, render_template, url_for, request, redirect
from repository.posts_repo_factory import PostsRepoFactory
from models.post import Post

index_blueprint = Blueprint('index', __name__, template_folder='templates',
                            static_folder='static')
#db = PostsRepoFactory.get_repo("InMemoryPosts")
db = PostsRepoFactory.get_repo("DatabasePostRepo")
print(type(db.view_posts()))
print(db.view_posts()[0].post_id, db.view_posts()[0].title)
@index_blueprint.route('/')
@index_blueprint.route('/posts/', methods=['GET','POST'])
def posts():
    return render_template('list_posts.html', content=db.view_posts())

@index_blueprint.route('/posts/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        date_now = datetime.datetime.now().strftime("%B %d, %Y")
        post = Post(title=request.form.get("title"),owner= request.form.get("owner"),
                    contents=request.form.get("contents"), created_at =date_now, 
                    modified_at = date_now)
        db.add_post(post)
        return redirect(url_for('index.posts'))
    return render_template('add_post.html')

@index_blueprint.route('/posts/<int:pid>', methods=['GET'])
def view_post(pid):
    post = db.find_post_id(pid)
    return render_template('view_post.html', post=post)

@index_blueprint.route('/posts/<int:pid>/edit', methods=['GET','POST'])
def edit(pid):
    found_post = db.find_post_id(pid)
    if request.method == 'POST':
        if found_post is not None:
            date_now = datetime.datetime.now()
            post = found_post
            post.title = request.form.get("title")
            post.owner = request.form.get("owner")
            post.contents = request.form.get("contents")
            post.created_at = found_post.created_at
            post.modified_at = date_now.strftime("%B %d, %Y")
            db.edit_post(post)
        return redirect(url_for('index.view_post', pid=post.post_id))
    return render_template('edit_post.html', post=found_post)

@index_blueprint.route('/posts/<int:pid>', methods=['POST'])
def delete(pid):
    post_delete = db.find_post_id(pid)
    if post_delete is not None:
        db.delete_post(pid)
        return redirect(url_for('index.posts'))
    return render_template('view_post.html')
