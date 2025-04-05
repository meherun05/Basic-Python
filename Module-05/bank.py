class Bank :
    def __init__(self,balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        print(self.balance)

brac = Bank(150000)
brac.withdraw(15000)
brac.deposit(10000)

        