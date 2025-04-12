# Encapsulation : hide details
# access modifier : public,protected,private
class Bank:
    def __init__(self,holder,initial_deposit):
        self.holder = holder # public attribute 
        self._branch = "Mirpur" # protected attribute
        self.__balance = initial_deposit # private attribute
        
    def getBalance(self):
        print (self.__balance)

    def deposit(self,amount):
         self.__balance += amount

    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return f'No money have in your account'

accountHolder = Bank('Shahin',150000)
print(accountHolder.holder)
print(accountHolder._branch)
accountHolder.getBalance()
# print(accountHolder.__balance) # it will trowe error like this AttributeError: 'Bank' object has no attribute '__balance' beacasuse balance is private
# print(dir(accountHolder))
print(accountHolder._Bank__balance) # this is how can we access the private attributes
        