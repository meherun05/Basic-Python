class Calculator:
    brand = 'Casio MS343'

    def add(self,num1,num2):
        result = num1 + num2
        return result
    
    def deduct(self,num1,num2):
        result = num1 - num2
        return result
    
    def multiply(self,num1,num2):
        result = num1 * num2
        return result
    
    def devide(self,num1,num2):
        result = num1 // num2
        return result
    
myCalculator = Calculator()
print(myCalculator.add(10,20))
print(myCalculator.deduct(10,20))
print(myCalculator.multiply(10,20))
print(myCalculator.devide(10,20))