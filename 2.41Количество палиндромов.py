k = int(input())
i = 0
while k > 0:
    n = k
    p = 0
    while n > 0:
        p = p * 10 + n % 10
        n //= 10
    if p == k:
        i += 1
    k -= 1
print(i)
