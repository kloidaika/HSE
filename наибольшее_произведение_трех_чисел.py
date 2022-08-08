numList = list(map(int, input().split()))
maxMult = numList[0]
mult1 = numList[0]
mult2 = numList[0]
mult3 = numList[0]
index1 = 0
index2 = 0
maxMult1 = numList[0] * numList[1] * numList[2]
for i in range(len(numList)):
    for j in range(len(numList)):
        if numList[i] * numList[j] > maxMult and i != j:
            maxMult = numList[i] * numList[j]
            mult1 = numList[i]
            index1 = i
            mult2 = numList[j]
            index2 = j
for i in range(len(numList)):
    if numList[i] * maxMult >= maxMult1 and i != index1 and i!= index2:
         maxMult1 = numList[i] * maxMult
         mult3 = numList[i]
print(mult1, mult2, mult3)
