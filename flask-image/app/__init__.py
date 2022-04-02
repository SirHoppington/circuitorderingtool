import click
from flask import Flask, current_app
from flask.cli import with_appcontext
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, instance_path='/usr/var/src/app')
    app.config.from_object(config_class)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager = LoginManager()
    login_manager.login_view = 'login.log_in'
    login_manager.init_app(app)

    from app.Provider.provider_routes import provider
    app.register_blueprint(provider)

    from app.User.user_model import User

    from app.Login.login_route import login
    app.register_blueprint(login)

    @login_manager.user_loader
    def load_user(user_id):
        return app.User.query.get(int(user_id))

    return app
