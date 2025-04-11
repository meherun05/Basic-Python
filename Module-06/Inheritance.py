#base class
class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'running gadget: {self.brand}'

class Laptop:
    def __init__(self,memory):
        self.memory = memory
        
        def coding(self):
            return f'learing python and practicing'
        
class Phone(Gadget):
    def __init__(self,dual_sim,brand,price,color,origin):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)

    def __repr__(self):
        return f'phone : {self.dual_sim} brand {self.brand}'

    def call(self,number,txt):
        return f'sending sms to {number} with {txt}'
    
    def run(self):
        return f'opening...'

class Camera:
    def __init__(self,pixel):
        self.pixel = pixel
    
    def run(self):
        pass

    def change_lens(self):
        pass
                

myPhone = Phone(True,'iPhone',100022555,'gray','Bangladesh')
myPhone.call(1021,'nothing')
print(myPhone)