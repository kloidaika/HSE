import math


def IsPrime(n):
    i = 1
    while i < math.ceil(n**0.5):
        i += 1
        if n % i == 0 and n != i:
            return "NO"
    return "YES"


n = int(input())
print(IsPrime(n))
