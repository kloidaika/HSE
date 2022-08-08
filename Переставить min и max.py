numList = list(map(int, input().split()))
maxNum = numList[0]
indexMax = 0
for i in range(len(numList)):
    if numList[i] > maxNum:
        maxNum = numList[i]
        indexMax = i
minNum = maxNum
indexMin = 0
for i in range(len(numList)):
    if numList[i] < minNum:
        minNum = numList[i]
        indexMin = i
numList.pop(indexMax)
numList.insert(indexMax, minNum)
numList.pop(indexMin)
numList.insert(indexMin, maxNum)
print(*numList)
