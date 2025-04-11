class Laptop:
    def __init__(self,brand,price,color,memory):
        self.brand = brand
        self.price   = price
        self.color = color
        self.memory = memory
        
        def run(self):
            return f'Running laptop: {self.brand}'
        
        def coding(self):
            return f'learing python and practicing'
        
class Phone:
    def __init__(self,brand,price,color,dual_sim):
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def call(self,number,txt):
        return f'sending sms to {number} with {txt}'
    
    def run(self):
        return f'opening...'

class Camera:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
                