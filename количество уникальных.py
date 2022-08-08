numList = list(map(int, input().split()))
check = 0
for i in range(len(numList)):
    for j in range(len(numList)):
        if numList[i] == numList[j] and i != j:
            check += 1
            continue
    if check == 0:
        print(numList[i], end=" ")
    check = 0
