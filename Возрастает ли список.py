def IsAscending(A):
    i = 0
    s = 1
    while i < len(A) - 1:
        s *= A[i] < A[i + 1]
        i += 1
    return s


numList = list(map(int, input().split()))
if IsAscending(numList):
    print("YES")
else:
    print("NO")
