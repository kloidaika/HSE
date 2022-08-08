numList = list(map(int, input().split()))
maxList = 0
maxNum = 0
for i in range(len(numList)):
    if numList[i] >= maxList:
        maxList = numList[i]
        maxNum = i
print(maxList, maxNum)
