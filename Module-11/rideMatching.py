from ride import Ride
from vehicle import Vehicle
from car import Car
from bike import Bike

class RideMatching:
    def __init__(self,driver):
        self.availableDriver = driver

    def findDriver(self,rideRequest,vehicleType):
        if len(self.availableDriver) > 0 :
            print("Looking for driver...")
            driver = self.availableDriver[0]
            if vehicleType == 'Car':
                vehicle = Car("Car","SF3532",10)
            elif vehicleType == 'Bike':
                vehicle = Bike("Bike","HJ343432",15)
            ride = Ride(rideRequest.startLocation,rideRequest.endLocation,vehicle)
            driver.acceptRideRequest(ride)
            return ride