from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Index Page</p>'


@app.route('/hello')
def hello_world():
    return '<p>Hello, World</p>'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/login')
def login():
    return 'login'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='John Doe'))