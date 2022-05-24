from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

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

    from app.Order.order_routes import order
    app.register_blueprint(order)

    from app.Pricing.pricing_routes import provider_pricing
    app.register_blueprint(provider_pricing)

    from app.Quote.quote_routes import customer_quote
    app.register_blueprint(customer_quote)

    return app


