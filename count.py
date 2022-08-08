numList = list(map(int, input().split()))
counter = 1
for i in range(1, len(numList)):
    if numList[i - 1] != numList[i]:
        counter += 1
print(counter)
