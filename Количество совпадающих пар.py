numList = list(map(int, input().split()))
counter = 0
for i in range(len(numList)):
    for j in range(len(numList)):
        if numList[i] == numList[j] and i != j:
            counter += 1
print(counter // 2)
