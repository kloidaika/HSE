n = int(input())
m = 0
i = 1
j = 1
l = 0
while n != 0:
    m = n
    n = int(input())
    if n == m:
        i += 1
    else:
        if i > l:
            l = i
        i = 1
print(l)
