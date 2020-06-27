import os
import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def create_table():
    db.create_all()

def add_flight():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        f1 = Flight(origin = origin, destination = destination, duration = duration)
        #__init__
        db.session.add(f1)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

def read_flight():
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")

def main():
    read_flight()

if __name__ == '__main__':
    with app.app_context():
        main()
