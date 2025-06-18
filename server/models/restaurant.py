from server import db
from sqlalchemy.orm import validates

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }