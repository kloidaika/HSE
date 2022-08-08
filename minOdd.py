numList = list(map(int, input().split()))
maxList = 0
for i in range(len(numList)):
    if numList[i] > maxList:
        maxList = numList[i]
for i in range(len(numList)):
    if numList[i] % 2 != 0 and numList[i] < maxList:
        maxList = numList[i]
print(maxList)
