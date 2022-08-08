import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 0
x *= 100
s = x + y
while i < k:
    i += 1
    s = int(s + s * p / 100)
print(s // 100, s % 100)
