numbers = [ 10 , 20 , 6 , 89 , 789 , 48 , 58 ]
numbers.append(100); # insert element at last index
numbers.insert(1,12) # insert the value at i index in array
if 89 in numbers:
    numbers.remove(89);
last = numbers.pop();
print(numbers)
index = numbers.index(10) # find value in array return index number
print(index)
print(last)
numbers.sort()#sort the list
print(numbers)