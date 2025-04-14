class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money

    @property # for this decaretor we can use age as class attribute and this is a getter without setter is readonly
    def age(self):
        return self._age
    
    @property # getter
    def salary(self):
        return self.__money
    
    @salary.setter # setter
    def salary(self,incrementSalary):
        if(incrementSalary < 0):
            return "incremented salary can't be negetive"
        self.__money += incrementSalary
    
shahin = User('Shhain',17,120000)
# print(shahin.age()) # if we don't use @property decaretor we call age like method
print(shahin.age)

print(shahin.salary)
shahin.salary = 15000
print(shahin.salary)

        