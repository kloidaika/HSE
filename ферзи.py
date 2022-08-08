queens = []
i = 0
while i < 8:
    queens.append(list(map(int, input().split())))
    i += 1
# print(queens)
i = 0
j = 0
t = 0
for i in range(len(queens)):
    for j in range(len(queens)):
        if (queens[i][0] == queens[j][0] or queens[i][1] ==  queens[j][1]) and i != j:
            print("NO")
            t = 1
        # if queens[i][0]
    if t != 0:
        break
    else:
        print("YES")
        break