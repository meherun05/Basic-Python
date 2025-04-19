from rider import Rider
from driver import Driver
from ride import Ride
from car import Car
from bike import Bike
from rideRequest import RideRequest
from rideMatching import RideMatching
from rideSharing import RideSharing

niyeJao = RideSharing("Niye Jao")

rohim = Driver("Rohim Uddin","abc@gmail.com",41546464,"Mohakhali")
niyeJao.addDriver(rohim)

kolim = Rider("Kolim Udin","abr@gmail.com",45545656,"Banani",400)
niyeJao.addRider(kolim)
print(niyeJao)
kolim.requestRide(niyeJao,"Mirpur","Car")
rohim.reachDestination(kolim.currentRide)
kolim.showCurrentRide()