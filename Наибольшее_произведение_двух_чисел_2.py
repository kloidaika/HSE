numList = list(map(int, input().split()))
maxMult = numList[0]
mult1 = 0
mult2 = 0
for i in range(len(numList)):
    for j in range(len(numList)):
        if numList[i] * numList[j] > maxMult and i != j:
            maxMult = numList[i] * numList[j]
            mult1 = numList[i]
            mult2 = numList[j]
if mult1 > mult2:
    print(mult2, mult1)
else:
    print(mult1, mult2)
