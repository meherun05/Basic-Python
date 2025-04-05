class Shop:
    shoppingMall = 'calooo'

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

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