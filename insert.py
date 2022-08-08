numList = list(map(int, input().split()))
(k, c) = tuple(map(int, input().split()))
numList.append(c)
space = 0
i = len(numList) - 1
while i > k:
    space = numList[i - 1]
    numList[i - 1] = numList[i]
    numList[i] = space
    i -= 1
for i in range(len(numList)):
    print(numList[i], end=" ")
