from flask import Flask, url_for, request, render_template
from markupsafe import escape
import json
import datetime

app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': 'Python',
        'contents': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
        'owner': 'D.B.Higgins',
        'created_at': 'September 20, 2020',
        'modified_at': 'September 21, 2020'
    },
    {
        'id': 2,
        'title': 'Php',
        'contents': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
        'owner': 'D.B.Higgins',
        'created_at': 'September 19, 2020',
        'modified_at': 'September 21, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        req = request.form

        toDict = dict(req)
        posts.append(toDict)
        
        

    return render_template('post.html')


if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
