class RideRequest:
    def __init__(self,rider,endLocation):
        self.rider = rider
        self.startLocation = rider.currentLocation
        self.endLocation = endLocation