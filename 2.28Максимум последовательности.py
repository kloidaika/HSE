n = int(input())
maxInt = n
while n != 0:
    n = int(input())
    if n != 0 and n > maxInt:
        maxInt = n
print(maxInt)
