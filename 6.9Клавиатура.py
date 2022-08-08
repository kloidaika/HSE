n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))
countK = [0] * n
for i in p:
    countK[i - 1] += 1
for i in range(n):
    if c[i] < countK[i]:
        print("YES")
    else:
        print("NO")
