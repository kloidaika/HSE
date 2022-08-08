n = int(input())
m = 0
i = 1
j = 1
l = 0
k = 0
while n != 0:
    m = n
    n = int(input())
    if n > m:
        i += 1
    else:
        if i > l:
            l = i
        i = 1
    if n < m and n != 0:
        j += 1
    else:
        if j > k:
            k = j
        j = 1
if l > k:
    print(l)
else:
    print(k)
