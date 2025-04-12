from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod # enforce all derived class or child class to have this method
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.category = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print('eating banana')
   
    def move(self):
        print('moving around')

    def __repr__(self):
        print(self.name)
        return super().__repr__()
    
monkey = Monkey('Monkey')
print(monkey.name)
monkey.eat()