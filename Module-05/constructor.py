class Phone :
    manufactured = 'China'

    def __init__(self,owner,brand,price):
            self.owner = owner
            self.brand = brand
            self.price = price

    def sendSMS(self,phone,sms):
        text = f'sending to : {phone} {sms}'
        return text
    
HisPhone = Phone('Shain','OPPO',15000)
print(HisPhone.owner,HisPhone.brand, HisPhone.price)
myPhone = Phone('Meherun','Readme',230000)
print(myPhone.owner,myPhone.brand, myPhone.price)