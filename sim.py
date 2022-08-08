n = int(input())
numList = list(map(int, input().split()))
x = int(input())
dif = 1000
mem = 0
for i in range(len(numList)):
    if abs(x - numList[i]) <= 2 * dif:
        dif = abs(x - numList[i]) / 2
        mem = numList[i]
print(mem)
