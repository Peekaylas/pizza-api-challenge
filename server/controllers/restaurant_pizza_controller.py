from flask import Blueprint, jsonify, request
from server import db
from server.models import RestaurantPizza, Restaurant, Pizza
from sqlalchemy.exc import IntegrityError

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    if not data or 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    try:
        price = int(data['price'])
        if not 1 <= price <= 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
        
        restaurant = Restaurant.query.get_or_404(data['restaurant_id'])
        pizza = Pizza.query.get_or_404(data['pizza_id'])
        
        restaurant_pizza = RestaurantPizza(price=price, pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify({
            'id': restaurant_pizza.id,
            'price': restaurant_pizza.price,
            'pizza': {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            },
            'restaurant': {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
        }), 201
    
    except ValueError:
        db.session.rollback()
        return jsonify({"errors": ["Invalid price value"]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Database integrity error"]}), 400