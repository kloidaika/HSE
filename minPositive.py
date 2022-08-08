numList = list(map(int, input().split()))
maxNum = 1000
for i in range(len(numList)):
    if maxNum > numList[i] > 0:
        maxNum = numList[i]
print(maxNum)
