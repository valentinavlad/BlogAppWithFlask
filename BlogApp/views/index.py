from flask import Blueprint, render_template
from flask import url_for, request, redirect
from repository.repo_factory import RepoFactory

index_blueprint = Blueprint('index', __name__, template_folder='templates',
                            static_folder='static')
db = RepoFactory.get_repo("InMemoryDb")

@index_blueprint.route('/')
@index_blueprint.route('/posts/', methods=['GET','POST'])
def posts():
    return render_template('posts.html', content=db.view_posts())

@index_blueprint.route('/posts/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        db.add()
        return redirect(url_for('index.posts'))
    return render_template('post.html')

@index_blueprint.route('/posts/<int:pid>', methods=['GET'])
def view_post(pid):
    post = db.find_post_id(pid)
    print(post.title + " vieww")
    return render_template('view_post.html', post=post)
    
@index_blueprint.route('/posts/<int:pid>/edit', methods=['GET','POST'])
def edit(pid):
    post = db.find_post_id(pid)
    if request.method == 'POST':
        db.edit(pid)
        return redirect(url_for('index.posts'))
    return render_template('edit.html', post=post)

@index_blueprint.route('/posts/<int:pid>', methods=['POST'])
def delete(pid):
    deleted = False
    post_delete = db.find_post_id(pid)
    if post_delete is not None:
        deleted = True
        db.delete(post_delete, pid)
    if deleted:
        return redirect(url_for('index.posts'))
    return render_template('view_post.html')
