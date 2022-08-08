numList = list(map(int, input().split()))
space = 0
for i in range(1, len(numList), 2):
    space = numList[i]
    numList[i] = numList[i - 1]
    numList[i - 1] = space
for i in range(len(numList)):
    print(numList[i], end=" ")
