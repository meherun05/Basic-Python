class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def addToCart(self,item,price,quantity):
        product = {'item' : item,'price' : price,'quantity' : quantity}
        self.cart.append(product)

    def removeitem(self,rmvItem):
        for item in self.cart:
            if(item == rmvItem):
                self.cart.remove(item)
                print(f'{rmvItem} has been removes from your cart')
                break

    def checkOut(self,amount):
        total = 0
        for item in self.cart:
            print(f'Cart items : {item}')
            total += item['price'] * item['quantity']
        print(f'Total price is {total}')
        if amount < total :
            print(f'please give provide more money {total - amount}')
        else :
            print(f'here is your extra money {amount - total}')

shahin = Shopping('Shahin Mia')
shahin.addToCart('alu',50,2)
shahin.addToCart('fish',700,2)
shahin.addToCart('tomato',30,2)
shahin.addToCart('rice',1000,10)
print(shahin.cart)
item={'item' : 'tomato','price' : 30,'quantity' : 2}
shahin.removeitem(item)
# shahin.checkOut(600)
shahin.checkOut(1600)
