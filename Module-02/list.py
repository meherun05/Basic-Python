#index  = [  0    1   2    3    4     5    6 ]
numbers = [ 10 , 20 , 6 , 89 , 789 , 48 , 58 ]
#index  = [  -7  -6   -5   -4   -3    -2  -1 ]

print(numbers[2],numbers[-3]) 

#list(start : end) 
print(numbers[2:5]) #start from start index and stop before the end index

#list(start : end : step)
print(numbers[1:4:2])
print(numbers[6:2:-1]) # print backward 
print(numbers[6:2:-2]) #print backward -2 step
print(numbers[2:]) # start from 2 index and end at the last element
print(numbers[:5]) # start from first element and end at the 5 index element
print(numbers[:]) # copy of the array
print(numbers[::-1]) # reverse the array