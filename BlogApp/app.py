import datetime
from flask import Flask, url_for, request, render_template, redirect, Response
from repository.posts_data import dummy_posts
from models.post import Post

app = Flask(__name__)


@app.route('/')
@app.route('/posts/', methods=['GET','POST'])
def posts():
    return render_template('posts.html', content=dummy_posts)

@app.route('/posts/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), 
                    owner= request.form.get("owner"),
                    contents=request.form.get("contents"))
        post.created_at = date_now.strftime("%B %d, %Y")
        post.modified_at = date_now.strftime("%B %d, %Y")
        dummy_posts.insert(0, post)
        return redirect(url_for('posts'))
    return render_template('post.html')

@app.route('/posts/<int:id>', methods=['GET'])
def view_post(id):
    for post in dummy_posts:
        if post.post_id== id:
            found_post = post

    return render_template('view_post.html', post=found_post)

@app.route('/posts/<int:id>/edit', methods=['GET','POST'])
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
        return redirect(url_for('posts'))
    return render_template('edit.html', post=found_post)

@app.route('/posts/<int:id>', methods=['POST'])
def delete(id):
    deleted = False
    for post in dummy_posts:
        if post.post_id == id:
            found_post = post
            deleted = True
            dummy_posts.remove(found_post)
    if deleted:
        return redirect(url_for('posts'))
    return Response("", status=400)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
