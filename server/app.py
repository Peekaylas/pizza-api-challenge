from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    from server.models.restaurant import Restaurant
    from server.models.pizza import Pizza
    from server.models.restaurant_pizza import RestaurantPizza
    from server.controllers.restaurant_controller import restaurants_bp
    from server.controllers.pizza_controller import pizzas_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp

    app.register_blueprint(restaurants_bp, url_prefix='/')
    app.register_blueprint(pizzas_bp, url_prefix='/')
    app.register_blueprint(restaurant_pizzas_bp, url_prefix='/')

    @app.route("/")
    def index():
        return {"message": "Pizza API is running!"}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5555)