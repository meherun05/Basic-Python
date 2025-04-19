from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, vehicleType, licencePlate, rate):
        super().__init__(vehicleType, licencePlate, rate)