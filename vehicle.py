# This module defines the Vehicle base class and Car and Bike subclasses

class Vehicle:
    def startEngine(self):
        """Starts the vehicle engine"""
        print("Vehicle engine started")

    def stopEngine(self):
        """Stops the vehicle engine"""
        print("Vehicle engine stopped")

class Car(Vehicle):
    def startEngine(self):
        """Starts the car engine"""
        print("Car engine started")

class Bike(Vehicle):
    def startEngine(self):
        """Starts the bike engine"""
        print("Bike engine started")

def startVehicleEngine(vehicle):
    """Starts the engine of any vehicle"""
    vehicle.startEngine()

# Testing
if __name__ == "__main__":
    car = Car()
    bike = Bike()

    startVehicleEngine(car)
    startVehicleEngine(bike)
