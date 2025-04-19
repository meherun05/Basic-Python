class RideSharing:
    def __init__(self,companyName):
        self.companyName = companyName
        self.riders = []
        self.drivers = []
        self.rides = []

    def addRider(self,rider):
        self.riders.append(rider)
    
    def addDriver(self,driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"Company name {self.companyName} with Riders : {len(self.riders)} with Drivers : {len(self.drivers)}"