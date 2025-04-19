from user import User
from rideRequest import RideRequest
from rideMatching import RideMatching
from ride import Ride
from car import Car
from bike import Bike

class Rider(User):
    def __init__(self, name, email, nid,currentLocation,initialAmount):
        super().__init__(name, email, nid)
        self.currentRide = None
        self.currentLocation = currentLocation
        self.wallet = initialAmount

    def displayProfile(self):
        print(f'Rider name : {self.name} and email : {self.email}')

    def loadCash(self,amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount is less than 0")
            
    def updateLocation(self,location):
        self.currentLocation = location

    def requestRide(self,rideSharing,destination,vehicleType):
        rideRequest = RideRequest(self,destination)
        rideMatching = RideMatching(rideSharing.drivers)
        ride = rideMatching.findDriver(rideRequest,vehicleType)
        ride.rider = self
        self.currentRide = ride
        print("YAY! We got a ride!!")

    def showCurrentRide(self):
        print("Ride Details")
        print(f"Rider : {self.name} ")
        print(f"Driver : {self.currentRide.driver.name} ")
        print(f"Start Location : {self.currentRide.startLocation} ")
        print(f"End Location : {self.currentRide.endLocation} ")
        print(f"Total Cost : {self.currentRide.estimatedFare} ")
