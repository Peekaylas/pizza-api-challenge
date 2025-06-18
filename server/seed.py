import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from server import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Italian Bistro", address="456 Oak Ave"),
            Restaurant(name="Slice of Heaven", address="789 Pine Rd")
        ]
        db.session.add_all(restaurants)
        
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
            Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
            Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms, onions")
        ]
        db.session.add_all(pizzas)
        
        db.session.commit()
        
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=15, restaurant_id=2, pizza_id=3)
        ]
        db.session.add_all(restaurant_pizzas)
        
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()