from datetime import datetime

class Ride:
    def __init__(self,startLocation,endLocation,vehicle):
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.driver = None
        self.rider = None
        self.startTime = None
        self.endTime = None
        self.estimatedFare = self.calculateFare(vehicle.vehicleType)
        self.vehicle = vehicle
    
    def setDriver(self,driver):
        self.driver = driver
    
    def startRide(self):
        self.startTime = datetime.now()

    def endRide(self):
        self.endTime = datetime.now()
        self.rider.wallet -= self.estimatedFare
        self.driver.wallet += self.estimatedFare

    def calculateFare(self,vehicleType):
        print(vehicleType)
        distance = 10
        farePerKM = {
            'Car':50,
            'Bike':40,
            'cng':10
        }
        return distance * farePerKM.get(vehicleType)

    def __repr__(self):
        return f"Ride details. started location : {self.startLocation} ended location : {self.endLocation}\n"

