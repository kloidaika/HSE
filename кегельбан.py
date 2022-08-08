n, k = tuple(map(int, input().split()))
i = 0
lr = []
res = []
while i < k:
    lr.append(list(map(int, input().split())))
    i += 1
i = 0
while i < n:
    res.append("I")
    i += 1
i = 0
j = 0
while i < n:
    while j < k:
        p = lr[j][0]
        q = lr[j][1]
        while p <= q:
            res[p - 1] = "."
            p += 1
        j += 1
    i += 1
for i in range(len(res)):
    print(res[i], end="")
