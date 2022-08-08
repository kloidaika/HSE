n = int(input())
i = 0
f0 = 0
f1 = 1
while i < n:
    f = f0 + f1
    f0 = f1
    f1 = f
    i += 1
print(f0)
