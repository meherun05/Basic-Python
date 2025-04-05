# n = int(input());
# arr = list(map(int, input().split()))

# for i in range(n):
#     val = int(input())
#     arr.append(val)

# print(arr)
n = int(input())
arr = list(map(int, input().split()))
if(arr == arr[::-1]):
    print('YES')
else :
    print('NO')