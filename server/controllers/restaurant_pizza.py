from flask import jsonify, request
from server import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)

    if not restaurant or not pizza:
        return jsonify({'error': 'Restaurant or Pizza not found'}), 404

    new_rp = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(new_rp)
    db.session.commit()

    return jsonify({
        'id': new_rp.id,
        'price': new_rp.price,
        'pizza': {'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients},
        'restaurant': {'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address}
    })