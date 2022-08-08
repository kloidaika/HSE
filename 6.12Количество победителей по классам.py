fin = open('input.txt', 'r', encoding='utf8')
pupils = []
spaceCount = 0
for now in fin.readlines():
    pupils.append(now.split())
nineMax = 0
tenMax = 0
elevenMax = 0
nineCount = 0
tenCount = 0
elevenCount = 0
for i in range(len(pupils)):
    if int(pupils[i][2]) == 9:
        if nineMax < int(pupils[i][3]):
            nineMax = int(pupils[i][3])
            nineCount = 0
        if int(pupils[i][3]) == nineMax:
            nineCount += 1
    elif int(pupils[i][2]) == 10:
        if tenMax < int(pupils[i][3]):
            tenMax = int(pupils[i][3])
            tenCount = 0
        if int(pupils[i][3]) == tenMax:
            tenCount += 1
    elif int(pupils[i][2]) == 11:
        if elevenMax < int(pupils[i][3]):
            elevenMax = int(pupils[i][3])
            elevenCount = 0
        if int(pupils[i][3]) == elevenMax:
            elevenCount += 1
print(nineCount, end=" ")
print(tenCount, end=" ")
print(elevenCount)
