numList = list(map(int, input().split()))
for i in range(len(numList) - 1, -1, -1):
    if i == len(numList) - 1:
        numList.append(0)
    numList[i + 1] = numList[i]
numList[0] = numList[len(numList) - 1]
numList.pop()
print(*numList)
