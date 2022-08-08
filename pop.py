numList = list(map(int, input().split()))
k = int(input())
numList.pop(k)
for i in range(len(numList)):
    print(numList[i])
