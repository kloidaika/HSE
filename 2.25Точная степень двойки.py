n = int(input())
i = 1
res = 1
while res < n:
    i = i + 1
    res = res * 2
if res == n:
    print("YES")
else:
    print("NO")
