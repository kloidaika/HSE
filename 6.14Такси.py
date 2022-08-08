km = list(map(int, input().split()))
fare = list(map(int, input().split()))
km.sort()
fare.sort(reverse=True)
sum = 0
for i in range(len(km)):
    sum += km[i] * fare[i]
print(sum)
