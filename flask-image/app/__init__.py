from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, instance_path='/usr/var/src/app')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)

    from app.Order.order_routes import order
    app.register_blueprint(order)

    from app.Pricing.pricing_routes import provider_pricing
    app.register_blueprint(provider_pricing)

    return app


