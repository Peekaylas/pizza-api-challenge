from server import db
from sqlalchemy.orm import validates

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name

    def __repr__(self):
        return f'<Pizza {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }