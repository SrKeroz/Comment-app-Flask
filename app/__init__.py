from flask import Flask
# flask
from flask_bootstrap import Bootstrap

# directory
from .auth import auth
from .profile import profile
from .models import UserModel

# config
from app.config import Config

# login manager
from flask_login import LoginManager

login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = f"Necesitas iniciar sesion para acceder a esta pagina"

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query(user_id)




def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(profile)


    return app