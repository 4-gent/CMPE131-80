from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from src import db


class Flight(db.Model):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    airline = db.Column(db.String(50))
    origin = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)

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


class User_Account(db.Model):
    __tablename__ = 'user_account'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)