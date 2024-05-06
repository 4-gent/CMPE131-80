from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from src import db

class Flight(db.Model):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    airline = Column(String(50))
    origin = Column(String(50))
    destination = Column(String(50))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)