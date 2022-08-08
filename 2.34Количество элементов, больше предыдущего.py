n = int(input())
i = 0
n1 = n
while n != 0:
    if n1 < n:
        i += 1
    n1 = n
    n = int(input())
print(i)
