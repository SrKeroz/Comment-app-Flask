from flask import Flask
from flask_bootstrap import Bootstrap
from .auth import auth
from app.config import Config
from .profile import profile


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    app.register_blueprint(auth)
    app.register_blueprint(profile)


    return app