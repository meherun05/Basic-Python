numbers = [ 10 , 25 , 6 , 89 , 79 , 48 , 58,23,95 ]

odds = []
for num in numbers :
    if num % 2 == 1 and num % 5 == 0: 
        odds.append(num)

print(odds)

odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0];
print(odd_nums)

age_combo = []
names = ['Shahin','Meherab','Meherun']
ages = [17,12,15]

for name in names :
    print('name : ',name)
    for age in ages : 
        print(age)
        age_combo.append([name,age]);

print(age_combo)


numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])