balance = 5000

def itemPrice(item,price):
    global balance # if we want to use and modify gobal variable we have to use global key word
    total = balance - price
    print(f'after buying {item} i have : ',total)
    return total;
print(itemPrice('Watch',1000))