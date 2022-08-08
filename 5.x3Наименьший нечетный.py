numList = list(map(int, input().split()))
minOdd = 0
maxList = 0
for i in range(len(numList)):
    if numList[i] > maxList:
        maxList = numList[i]
for i in range(len(numList)):
    if numList[i] <= maxList and numList[i] % 2 != 0:
        minOdd = numList[i]
print(minOdd)
