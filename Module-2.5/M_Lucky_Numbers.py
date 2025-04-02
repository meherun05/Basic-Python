num1, num2 = map(int, input().split())

def is_lucky(num):
    return all(digit in '47' for digit in str(num))

lucky_numbers = [i for i in range(num1, num2 + 1) if is_lucky(i)]

if lucky_numbers:
    print(' '.join(str(i) for i in lucky_numbers))
else:
    print(-1)