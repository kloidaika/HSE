fin = open('input.txt', 'r', encoding='utf8')
nineSum = 0
nineCount = 0
tenSum = 0
tenCount = 0
elevenSum = 0
elevenCount = 0
pupils = []
spaceCount = 0
for now in fin.readlines():
    pupils.append(now.split())
for i in range(len(pupils)):
    if int(pupils[i][2]) == 9:
        nineSum += int(pupils[i][3])
        nineCount += 1
    elif int(pupils[i][2]) == 10:
        tenSum += int(pupils[i][3])
        tenCount += 1
    elif int(pupils[i][2]) == 11:
        elevenSum += int(pupils[i][3])
        elevenCount += 1
print('{0:.10f}'.format(nineSum / nineCount), end=" ")
print('{0:.10f}'.format(tenSum / tenCount), end=" ")
print('{0:.10f}'.format(elevenSum / elevenCount))
