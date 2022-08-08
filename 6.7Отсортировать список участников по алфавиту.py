fin = open('input.txt', 'r', encoding='utf8')
pupils = []
for now in fin.readlines():
    pupils.append(now.split())
pupils.sort(key=lambda p: p[0])
for i in range(len(pupils)):
    del pupils[i][2]
for i in range(len(pupils)):
    print(*pupils[i])
