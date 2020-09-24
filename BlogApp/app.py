from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
import json
import datetime
from posts_data import dummy_posts
import random
from post import Post


app = Flask(__name__)

@app.route('/')
@app.route('/posts', methods=['GET','POST'])
def posts():
    
    return render_template('posts.html', content=dummy_posts)

print(dummy_posts)
@app.route('/posts/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), owner= request.form.get("owner"),
                    contents=request.form.get("contents"),
                    created_at=date_now.strftime("%Y, %B, %d"),
                    modified_at=date_now.strftime("%Y, %B, %d"))

        dummy_posts.insert(0, post)
        return redirect(url_for('posts'))
    return render_template('post.html')
  

@app.route('/posts/<int:id>/edit', methods=['GET','POST'])
def edit(id):
    for post in dummy_posts:
        if post.id == id:
            found_post = post
    if request.method == 'POST':
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"), owner= request.form.get("owner"),
                    contents=request.form.get("contents"),
                    created_at=date_now.strftime("%Y, %B, %A"),
                    modified_at=date_now.strftime("%Y, %B, %A"))
        dummy_posts.remove(found_post)
        dummy_posts.append(post)
        return redirect(url_for('posts'))
    return render_template('edit.html', post=found_post)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
