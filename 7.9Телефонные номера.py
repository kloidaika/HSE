def number(s):
    temp = []
    for i in s:
        if i.isdigit():
            temp.append(int(i))
    if len(temp) > 10:
        temp = temp[-10:]
    elif len(temp) == 7:
        temp.insert(0, 5)
        temp.insert(0, 9)
        temp.insert(0, 4)
    return temp


n = input()
telDict = dict()
for i in range(3):
    telDict[i] = number(input())
n = number(n)
check = 0
for i in range(len(telDict)):
    for j in range(len(n)):
        if n[j] == telDict[i][j]:
            check += 1
    if check == 10:
        print('YES')
    else:
        print('NO')
    check = 0
