from flask import Flask, render_template, request, jsonify
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    #flights=db.execute("select * from flights").fetchall()
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    flight_id = int(request.form.get("flight_id"))
    #db.execute("insert into passengers (name, flight_id) values (:name, :flight_id)",
    #{"name": name, "flight_id": flight_id})
    #db.commit()
    flight = Flight.query.get(flight_id)
    passenger = Passenger(name = name, flight_id = flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    #flights = db.execute("select * from flights").fetchall()
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/passengers/<int:flight_id>")
def passengers(flight_id):
    #passengers = db.execute("select name from passengers where flight_id=:flight_id",
    #{"flight_id": flight_id}).fetchall()
    flight = Flight.query.get(flight_id)
    passengers = Passenger.query.filter_by(flight_id = flight_id).all()
    return render_template("passengers.html", passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "Invalid flight_id"}), 422

    names = []
    for passenger in flight.passengers:
        names.append(passenger.name)
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
    })
