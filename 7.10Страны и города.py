def makeDict(line):
    temp = line.split()
    d = dict()
    for i in range(1, len(temp)):
        d[temp[i]] = temp[0]
    return d


countries = list()
res = dict()
for i in range(int(input())):
    temp = input()
    countries.append(makeDict(temp))
for i in countries:
    res = res | i
for i in range(int(input())):
    city = input()
    print(res.get(city))