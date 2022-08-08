numList = list(map(int, input().split()))
counter = 0
for i in range(1, len(numList) - 1):
    if numList[i - 1] < numList[i] > numList[i + 1]:
        counter += 1
print(counter)
