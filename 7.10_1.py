# страны и города (см. latinEngDict.py)

n = int(input())
cityCount = {}
ansList = []

for i in range(n):
    line = input()
    country = line[:line.find(' ')].strip()
    cityStr = line[line.find(' ') + 1:].strip()
    cities = map(lambda s: s.strip(), cityStr.split(' '))
    for city in cities:
        if city not in cityCount:   # если города пока нет в словаре
            cityCount[city] = []    # то создаем под него ключ
        cityCount[city].append(country)     # и кладем в него страну

# print(cityCount)

m = int(input())    # кол-во городов
for j in range(m):
    line1 = input().strip()     # считываем город, обрезая по краям пробелы
    ansList.append(line1)       # добывляем в лист городов, чисто для печати

for l in ansList:
    print(*cityCount[l])    # проходя по листу городов, печ. знач. по ключу
