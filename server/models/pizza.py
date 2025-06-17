from server import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')