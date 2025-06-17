from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .controllers.restaurant_controller import restaurants_bp
from .controllers.pizza_controller import pizzas_bp
from .controllers.restaurant_pizza_controller import restaurant_pizzas_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(restaurant_pizzas_bp)
    
    return app