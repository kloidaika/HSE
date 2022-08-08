n = int(input())
i = 0
pupils = []
temp = []
while i < n:
    (name, mark) = tuple(input().split())
    mark = int(mark)
    pupils.append((name, mark))
    i += 1
pupils.sort(key=lambda pupils: pupils[1], reverse=True)
for i in range(len(pupils)):
    print(pupils[i][0])
