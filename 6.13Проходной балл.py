fin = open('input.txt', 'r', encoding='utf8')
marks = []
k = fin.readline()
for i in fin.readlines():
    if i != k:
        temp = i.split()
        temp = [int(temp[-3]), int(temp[-2]), int(temp[-1])]
        marks.append(temp)
t = [0] * len(marks)
marks.sort(reverse=True)
for i in range(len(t)):
    for j in range(3):
        if marks[i][j] < 40:
            t[i] += 1
# print(marks)
# print(t)
count_students = 0
sum_marks = [0] * len(marks)
for i in range(len(marks)):
    for j in range(3):
        if t[i] == 0:
            sum_marks[i] += marks[i][j]
sum_marks.sort(reverse=True)
# print(sum_marks)
min_sum_marks = sum_marks[0]
max_sum_marks = sum_marks[0]
t.sort()
print(t)
count_students /= 3
for i in range(len(sum_marks)):
    if i > int(k):
        sum_marks[i] = 0
        t[i] = -1
print(sum_marks, 'ee')
for i in range(len(t)):
    if t[i] == 0 and sum_marks[int(k)] != sum_marks[i]:
        t[i] = sum_marks[i]
        count_students += 1
        if t[i] < min_sum_marks:
            min_sum_marks = t[i]
        if t[i] > max_sum_marks:
            max_sum_marks = t[i]
    else:
        t[i] = -1
t_min = t[0]
count_top = 0
for i in range(len(sum_marks)):
    if sum_marks[i] == max_sum_marks:
        count_top += 1
for i in range(len(t)):
    if 0 < t[i] < t_min:
        t_min = t[i]
if count_top > int(k):
    print(1)
elif int(k) == count_students or t_min == -1:
    print(0)
else:
    print(t_min)
