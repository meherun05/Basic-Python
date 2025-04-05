n = int(input())
number = input()
num = [int(digit) for digit in number]
sum = 0
for v in num:
    sum += v
print(sum)