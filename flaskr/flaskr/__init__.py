import os

from flask import Flask
from . import db, auth, blog


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists and when not testing.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
    
    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/hello')
    def hello():
        return 'Hello, World'
    
    db.init_app(app)

    app.register_blueprint(auth.bp)

    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app
