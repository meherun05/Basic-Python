# def double(val):
#     return val * 2;

double = lambda num : num * 2; # in lambda expretion first declare lambda then pararemters the logic
squere = lambda num : num * num;

add = lambda x,y : x + y

print(double(5))
print(squere(5))
print(add(5,5))

# lambda in map
numbers =[10,125,20,30,40,60,125,41,44,125,48]
# map_list = map(double,numbers)
map_list = map(lambda x : x *2,numbers)
print(list(map_list))

person = [
    {'name' :'Shahin','age' : 18},
    {'name' :'Meherun','age' : 17},
    {'name' :'Meherab','age' : 25},
    {'name' :'Tiana','age' : 28},
    {'name' :'Mim','age' : 29},
]

juniors = filter(lambda person : person['age'] < 20,person)
print(list(juniors))