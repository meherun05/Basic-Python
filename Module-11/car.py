from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicleType, licencePlate, rate):
        super().__init__(vehicleType, licencePlate, rate)