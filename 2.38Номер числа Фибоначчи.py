n = int(input())
i = 1
f0 = 0
f1 = 1
f = f0 + f1
while n > f:
    f = f0 + f1
    f0 = f1
    f1 = f
    i += 1
if n == f:
    print(i)
else:
    print(-1)
