fin = open('input.txt', 'r', encoding='utf8')
all_text = []
parties = []
votes = []
for i in fin.readlines():
    all_text.append(i.strip())
all_text.pop(0)
for i in range(len(all_text)):
    if all_text[i] != 'VOTES:':
        parties.append(all_text[i])
    else:
        t = i + 1
        break
for i in range(t, len(all_text)):
    votes.append(all_text[i])
votes.sort()
count_p = [0] * len(parties)
k = 0
while k < len(votes):
    for i in range(len(parties)):
        if votes[k] == parties[i]:
            count_p[i] += 1
    k += 1
sum_p = 0
for i in range(len(count_p)):
    sum_p += count_p[i]
for i in range(len(count_p)):
    if count_p[i] / sum_p > 0.07:
        print(parties[i])
