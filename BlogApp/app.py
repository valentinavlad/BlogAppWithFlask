from flask import Flask, redirect
from views.posts_view import index_blueprint
from views.setup_view import setup_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint, url_prefix="/posts")
app.register_blueprint(setup_blueprint, url_prefix="/setup")

@app.route('/')
def index():
    return redirect('/posts/')
if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
