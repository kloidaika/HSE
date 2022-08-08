numList = list(map(int, input().split()))
space = 0
for i in range(len(numList) // 2):
    space = numList[i]
    numList[i] = numList[len(numList) - i - 1]
    numList[len(numList) - i - 1] = space
for i in range(len(numList)):
    print(numList[i], end=" ")
