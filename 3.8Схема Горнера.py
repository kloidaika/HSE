n = int(input())
x = float(input())
i = 0
res = 0
while i < n + 1:
    i += 1
    s = float(input())
    if i == 1:
        res += s
    else:
        res = x * res + s
print('{0:.6f}'.format(res))
