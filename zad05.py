import math
import sys

n = int(input("n: "))

if n < 2:
    print("Error: number must be at least 2")
    sys.exit()

def is_prime(n:int):

    for i in range(2,math.isqrt(n)):
        if n / i == n // i:
            return(False)
    return(True)

if is_prime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')
