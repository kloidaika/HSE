(N, M) = tuple(map(int, input().split()))
nSet = set()
mSet = set()
for i in range(N):
    nSet.add(int(input()))
for i in range(M):
    mSet.add(int(input()))
print(len(nSet & mSet))
print(*sorted(list(nSet & mSet)))
print(len(nSet - mSet))
print(*sorted(list((nSet - mSet))))
print(len(mSet - nSet))
print(*sorted(list(mSet - nSet)))
