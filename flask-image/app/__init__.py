from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config, admin_password
from flask_principal import Principal, Permission, RoleNeed
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin_permission = Permission(RoleNeed('admin'))

#def create_app(config_name):
#    app = Flask(__name__, instance_path='/usr/var/src/app')
#    app.config.from_object(config.get(config_name or 'default'))
def create_app(config_name=None):
    if config_name is None:
        app = Flask(__name__, instance_path='/usr/var/src/app')
        app.config.from_object(config.get('development'))
    else:
        app = Flask(__name__, instance_path='/usr/var/src/app')
        app.config.from_object(config.get(config_name))
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.login_view='login.log_in'
    login_manager.init_app(app)
    principals = Principal(app)

    @app.before_first_request
    def create_admin():

        if not User.query.filter_by(email="admin").first(): # if this returns a user, then the email already exists in database
            # Generate default admin user account:
            new_user = User(email="admin", password=generate_password_hash(admin_password, method='sha256'), role="admin")

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()
        return True

    from app.Orders.order_routes import order
    app.register_blueprint(order)

    from app.Pricing.pricing_routes import provider_pricing
    app.register_blueprint(provider_pricing)

    from app.Quote.quote_routes import customer_quote
    app.register_blueprint(customer_quote)

    from app.Login.login_routes import login
    app.register_blueprint(login)

    from app.callback.callback_routes import callback
    app.register_blueprint(callback)

    from app.Models.association_table import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


