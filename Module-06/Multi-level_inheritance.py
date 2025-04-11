class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def move(self):
        pass

    def __repr__(self):
        return f'{self.name} {self.price}'

class Bus(Vehicle):
    def __init__(self, name, price, seat, weight):
        self.seat = seat
        self.weight = weight
        super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()

class PickupBus(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)

class AcBus(Vehicle):
    def __init__(self, name, price, seat, temperature):
        self.seat = seat
        self.temperature = temperature
        super().__init__(name, price)

    def __repr__(self):
        print(f'{self.seat}')
        return super().__repr__()

# Test
green_line = AcBus('green', 500000, 30, 16)
print(green_line)