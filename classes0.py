class Flight:
    counter = 1
    def __init__(self, origin, destination, duration):
        self.id = Flight.counter
        Flight.counter += 1
        self.passengers = []
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.origin}")
        print(f"Flight duration: {self.duration}")
        print("Passengers: ")
        for passenger in self.passengers:
            print(passenger)

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, passenger):
        self.passengers.append(passenger.name)
        passenger.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name
        self.flight_id = None

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Flight ID: {self.flight_id}")

def main():
    f1 = Flight("New York", "Paris", 540)
    f1.delay(10)
    f1.print_info()

    p1 = Passenger("Alice")
    p2 = Passenger("Bob")
    p3 = Passenger("Cathy")

    f1.add_passenger(p1)
    f1.add_passenger(p2)
    f1.print_info()

    p1.print_info()
    p2.print_info()
    p3.print_info()

if __name__ == "__main__":
    main()
