#poly = many (multiple)
#poly = shape

class Animal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        print(f'{self.name} making sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        print('meaw meaw')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        print('Gheu gheu')

don = Cat('Don')
don.makeSound()

brun = Dog('brun')
brun.makeSound()