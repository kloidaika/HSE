numList = list(map(int, input().split()))
x = int(input())
for i in range(len(numList)):
    if x > numList[i]:
        print(numList.index(numList[i]) + 1)
        break
    elif i == len(numList) - 1:
        print(len(numList) + 1)
