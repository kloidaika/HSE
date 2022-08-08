numList = list(map(int, input().split()))
minPositive = 0
maxList = 0
for i in range(len(numList)):
    if numList[i] > maxList:
        maxList = numList[i]
for i in range(len(numList)):
    if 0 < numList[i] <= maxList:
        minPositive = numList[i]
print(minPositive)
