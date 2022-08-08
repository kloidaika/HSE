fin = open('input.txt')
temp = []
res = dict()
for i in fin.readlines():
    temp.append(i.split())
print(temp)
for i in range(len(temp)):
    for j in range(len(temp[i])):
        res[j] = temp[i][j]
'''for i in range(len(res)):
    for j in range(len(res)):
        if res[i] '''
print(res)