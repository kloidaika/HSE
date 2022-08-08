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
    elif int(pupils[i][2]) == 10:
        if tenMax < int(pupils[i][3]):
            tenMax = int(pupils[i][3])
    elif int(pupils[i][2]) == 11:
        if elevenMax < int(pupils[i][3]):
            elevenMax = int(pupils[i][3])
print(nineMax, end=" ")
print(tenMax, end=" ")
print(elevenMax)
