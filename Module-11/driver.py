from user import User

class Driver(User):
    def __init__(self, name, email, nid,currentLocation):
        super().__init__(name, email, nid)
        self.currentLocation = currentLocation
        self.wallet = 0

    def displayProfile(self):
        print(f'Driver name : {self.name}')

    def acceptRideRequest(self,ride):
        ride.startRide()
        ride.setDriver(self)

    def reachDestination(self,ride):
        ride.endRide()