numList = list(map(int, input().split()))
maxList = numList[0]
maxIndex = 0
for i in range(len(numList)):
    if numList[i] > maxList:
        maxList = numList[i]
        maxIndex = i
print(maxList, maxIndex)
