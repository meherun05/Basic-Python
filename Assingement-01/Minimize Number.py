n = int(input())
arr = list(map(int, input().split()))
count = 0

while True:
    even = True
    for num in arr:
        if num % 2 != 0:
            even = False
            break
    if not even:
        break
    
    for i in range(n):
        arr[i] = arr[i] // 2
    count += 1

print(count)