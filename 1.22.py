n = int(input())
n1 = n // 1000
n2 = n // 100 % 10
n3 = n % 100 // 10
n4 = n % 10
print(((n1 - n4)**2 + (n2 - n3)**2) + 1)
