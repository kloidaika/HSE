(s, n) = tuple(map(int, input().split()))
users_mem = []
for i in range(n):
    users_mem.append(int(input()))
users_mem.sort()
counter = 0
while s > 0 and counter < len(users_mem):
    s -= users_mem[counter]
    counter += 1
if s >= 0:
    counter += 1
print(counter - 1)
