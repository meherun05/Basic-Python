class Shop :
    cart = [] # cart is an class attribute
    def __init__(self,buyer):
        self.buyer = buyer
    
    def addToCart(self,item):
        self.cart.append(item)

shahin = Shop('Shahin')
shahin.addToCart('shoes')
shahin.addToCart('shirt')
shahin.addToCart('panjabi')
print (shahin.cart)
meherun = Shop('Meherun')
meherun.addToCart('bag')
meherun.addToCart('make-up')
meherun.addToCart('dress')
print (meherun.cart)