from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from src import db

class Flight_Booking(db.Model):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True)
    origin = Column(String(50))
    destination = Column(String(50))
    passenger_count = Column(Integer)
    departure = Column(String(50))
    arrival = Column(String(50))
    trip_type = Column(Integer)

class Passenger_Info(db.Model):
    __tablename__ = 'passenger_Info'

    #Personal Info
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(64))
    address = db.Column(db.String(100))

    #Payment Info
    card_name = db.Column(db.String(50))
    card_number = db.Column(db.Integer)
    expiration_date = db.Column(db.Integer)
    cvv_number = db.Column(db.Integer)

    #Payment After Calculation
    airefare_cost = db.Column(db.Float)
    baggage_cost = db.Column(db.Float)
    security_cost = db.Column(db.Float)
    tax_cost = db.Column(db.Float)
    total_cost = db.Column(db.Float)

    #Trip Information
    trip = db.Column(db.String(50))
    trip_int = db.Column(db.Integer)
    passengers = db.Column(db.Integer)

class Flight(db.Model):
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True)
    airline = Column(String(50))