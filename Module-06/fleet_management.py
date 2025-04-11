# Ena Poribohon

class Company:
    def __init__(self,name,address):
        self.name = name
        self.bus = []
        self.route = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors =[]

class Driver:
    def __init__(self,name,license,age):
        self.name = name
        self.license = license
        self.age = age

class Passenger:
    def __init__(self):
        pass
        
class Supervisors:
    def __init__(self):
        pass
        