from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

pathname = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'project131',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pathname, 'flight.db')
)

db = SQLAlchemy(app)

with app.app_context():
    from src.models import Flight_Booking, Passenger_Info
    db.create_all()

from src import routes