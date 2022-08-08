numList = list(map(int, input().split()))
maxNum1 = numList[0]
maxNum2 = numList[0]
maxIndex = 0
minNum1 = numList[0]
minNum2 = numList[0]
minIndex = 0
for i in range(len(numList)):
    if numList[i] > maxNum1:
        maxNum1 = numList[i]
        maxIndex = i
maxMult1 = numList[0] * maxNum1
numList.pop(maxIndex)
for i in range(len(numList)):
    if numList[i] * maxNum1 >= maxMult1:
        maxMult1 = numList[i] * maxNum1
        maxNum2 = numList[i]
for i in range(len(numList)):
    if numList[i] < minNum1:
        minNum1 = numList[i]
        minIndex = i
maxMult2 = numList[0] * minNum1
numList.pop(minIndex)
for i in range(len(numList)):
    if numList[i] * minNum1 >= maxMult2:
        maxMult2 = numList[i] * minNum1
if maxMult1 > maxMult2:
    print(maxNum2, maxNum1)
else:
    print(minNum1, minNum2)
