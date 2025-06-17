import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pizza_restaurant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False