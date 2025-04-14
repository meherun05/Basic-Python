class Shoping :
    cart = [] #class attribute or static attribute
    origin = 'China'

    def __init__(self,name,location):
        self.name = "Jamu na city" #instance attribute
        self.location = 'Jam er majh khane'

    def purchace(self,item,price,amount):
        remaining = amount - price
        print(f'buying {item} for price {price} and remaining : {remaining}')

    @classmethod # this is use for class method 
    def hudaiDekhi(self,item):
        print(f'Ac er batas khete aschi ar hudai time pass korte kisu {item} dekhtechi')

    @staticmethod # for decalare static method in class
    def multi(a,b):
        print(a*b)
    

# when i will try to access the method from class without using @classmethod it throw error that need one requirment it mean it need the self also in parameter
# Shoping.purchace('Dress',600,1000) 

mirpur = Shoping('Mirpur super market','Mirpur-1') # but when we use shoping varible we can access the purchace with 3 parameters
# mirpur.purchace('eges',50,200)

Shoping.hudaiDekhi('Dolls') # this is class method so its just need 1 parameters or as many i declared in method

Shoping.multi(10,2) # this is a static method it can't access the class attribute init