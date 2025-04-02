def fullName(first,last):
    name = f'{first} {last}'; # f'' format string it works like first + ' ' + last in shorter way
    return name;

# name = fullName('Shahin','Mia'); # take parameters wise input
name = fullName(last='Mia',first='Shahin') # don't take parameters serial wise
print(name)

def famous_name(first,last,**additional): # use kargs
    name = f'{first} {last}'
    # print(additional['pos'])
    for key,value in additional.items():
        print(key,value);
    return name;
name = famous_name(first='Shahin',last='Mia',additional='Business',pos='Onwer')
print(name)

def sum(num1,num2): # return multiple return in function
    sum = num1 + num2
    multi = num1 * num2
    reminder = num1 - num2
    # return [sum,multi,reminder]; # return as list
    return sum,multi,reminder; # return as topolo

print(sum(10,5))