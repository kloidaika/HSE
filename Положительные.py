numList = list(map(int, input().split()))
counter = 0
for i in range(len(numList)):
    if numList[i] > 0:
        counter += 1
print(counter)
