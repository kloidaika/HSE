numList = list(map(int, input().split()))
for i in range(1, len(numList)):
    if numList[i - 1] < numList[i]:
        print(numList[i])
