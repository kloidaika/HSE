n = int(input())
i = 0
m = n
while n != 0:
    if n > m:
        m = n
        i = 0
    if m == n:
        i += 1
    n = int(input())
print(i)
