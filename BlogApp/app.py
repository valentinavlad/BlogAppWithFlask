from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
import json
import datetime
from posts_data import posts
import random

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        date_now = datetime.datetime.now()
 
        post = {
            "id": random.randint(1, 9),
            "title": request.form.get("title"),
            "contents": request.form.get("contents"),
            "owner": request.form.get("owner"),
            "created_at": date_now.strftime("%Y, %B, %A"),
            "modified_at":  date_now.strftime("%Y, %B, %A")
        }
        posts.append(post)
        return redirect(url_for('home'))
    return render_template('post.html')

@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        date_now = datetime.datetime.now()
 
        post = {
            "id": random.randint(1, 9),
            "title": request.form.get("title"),
            "contents": request.form.get("contents"),
            "owner": request.form.get("owner"),
            "created_at": date_now.strftime("%Y, %B, %A"),
            "modified_at":  date_now.strftime("%Y, %B, %A")
        }
        posts.append(post)
    return render_template('edit.html')

    
    
    
if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
