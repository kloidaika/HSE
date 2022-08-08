state = open('input.txt', 'r', encoding='utf-8')
report = open('output.txt', 'w', encoding='utf-8')

pupils = []
k = int(state.readline())
for line in state:
    pupil = list(map(int, line.split()[-1:-4:-1]))
    if len([1 for i in range(0, 3) if pupil[i] >= 40]) == 3:
        pupils.append(sum(pupil))

pupils.sort()  # обязательная сортировка
if len(pupils) <= k:
    print(0, file=report)
elif pupils.count(max(pupils)) > k:
    print(1, file=report)
else:
    achieve = pupils[-k]
    index_achieve = pupils.index(achieve)
    if len(pupils) - k != index_achieve:
        while pupils[index_achieve] == achieve:
            index_achieve += 1
    print(pupils[index_achieve], file=report)
report.close()
