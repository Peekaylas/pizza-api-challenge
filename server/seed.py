from server import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.create_all()

    r1 = Restaurant(name="Kiki's Pizza", address="address3")
    r2 = Restaurant(name="Emma's", address="address1")
    db.session.add_all([r1, r2])
    db.session.commit()

    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=1, pizza_id=1)
    rp2 = RestaurantPizza(price=12, restaurant_id=2, pizza_id=2)
    db.session.add_all([rp1, rp2])
    db.session.commit()