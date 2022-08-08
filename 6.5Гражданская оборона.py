n = int(input())
settles = []
temp = tuple(map(int, input().split()))
for i in range(n):
    settles.append((temp[i], i + 1))
m = int(input())
shelters = []
temp = tuple(map(int, input().split()))
for i in range(m):
    shelters.append((temp[i], i + 1))
settles.sort()
shelters.sort()
minDist = abs(settles[0][0] - shelters[0][0])
t = 0
k = shelters[t][1]
res = []
if len(shelters) > 1:
    for i in range(len(settles)):
        minDist = abs(settles[i][0] - shelters[t][0])
        for j in range(len(shelters) - 1):
            if minDist >= abs(settles[i][0] - shelters[j + 1][0]):
                minDist = abs(settles[i][0] - shelters[j + 1][0])
                k = shelters[j + 1][1]
                t = j + 1
        res.append((settles[i][1], k))
else:
    print(shelters[0][1])
res.sort()
for i in range(len(res)):
    print(res[i][1], end=" ")
