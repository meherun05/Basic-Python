class Person:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        print('eating rice and chicken')

class Programmer(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)

    def eat(self): # this child eat method override the parent method
        print('eating healthy food')
    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.weight * other.weight

shahin = Programmer('Shahin',21,16,68)
meherun = Programmer('Meherun',16,30,50)
shahin.eat()
print(shahin + meherun)
print(shahin * meherun)