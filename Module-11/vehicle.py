from abc import ABC

class Vehicle(ABC):
    speed={
        'Car':50,
        'Bike':60,
        'CNG':15
    }
    def __init__(self,vehicleType,licencePlate,rate):
        self.vehicleType = vehicleType
        self.licencePlate = licencePlate
        self.rate = rate