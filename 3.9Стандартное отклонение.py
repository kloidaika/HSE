import math

x = int(input())
s = 0
s2 = 0
counter = 0
while x != 0:
    s += x
    s2 += x**2
    x = int(input())
    counter += 1
    print(s)
    print(s2)
    print(counter, x)
s = s**2 / (counter)
res = math.sqrt((s2 - s)/(counter - 1))
print(res)