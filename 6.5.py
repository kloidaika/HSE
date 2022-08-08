vcounts = int(input())
villages = tuple(map(int, input().split()[:vcounts]))
village = []
for i in range(1, vcounts + 1):
    village.append((villages[i - 1], i))
village.sort()
bcounts = int(input())
bombshelters = tuple(map(int, input().split()[:bcounts]))
bombshelter = []
for j in range(1, bcounts + 1):
    bombshelter.append((bombshelters[j - 1], j))
bombshelter.sort()
i = 0
j = 0
VB = []
VBN = []
while i < vcounts:
    if bcounts == 1:
        VBN.append(bombshelter[j][1])
    else:
        while village[i][0] > bombshelter[j][0] and j < bcounts - 1:
            j += 1
        if abs(village[i][0] - bombshelter[j][0])\
                <= abs(village[i][0] - bombshelter[j - 1][0]):
            VB.append((village[i][1], bombshelter[j][1]))
        else:
            VB.append((village[i][1], bombshelter[j - 1][1]))
    i += 1
VB.sort()
for i in range(len(VB)):
    VBN.append(VB[i][1])
print(*VBN)
