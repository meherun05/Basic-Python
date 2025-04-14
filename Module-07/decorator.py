import math
import time

def timer(fn):
    def inner(*args,**kargs):
        print('time stated..')
        start = time.time()
        fn(*args,**kargs)
        end = time.time() - start
        print(f'total time taken {end}')
    return inner

# timer()()

@timer
def getFactorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is {result}')

# timer(getFactorial)() # worst way to decorate

getFactorial(n = 5)