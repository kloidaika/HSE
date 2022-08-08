i = input()
parties = []
votes = []
while i != 'VOTES:':
    i = input()
    if i != 'VOTES:':
        parties.append(i)
while i != 'STOP':
    i = input()
    if i != 'STOP':
        votes.append(i)
#print(parties)
votes.sort()
#print(votes)
count_p = [0] * len(parties)
#print(count_p)
k = 0
while k < len(votes):
    for i in range(len(parties)):
        if votes[k] == parties[i]:
            count_p[i] += 1
    k += 1
#print(count_p)
res = []
for i in range(len(parties)):
    temp = [count_p[i], parties[i]]
    res.append(temp)
res.sort(reverse=True)
for i in range(len(res)):
    print(res[i][1])