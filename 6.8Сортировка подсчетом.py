def CountSort(A):
    countA = [0] * 101
    for i in A:
        countA[i] += 1
    k = 0
    for i in range(len(countA)):
        while countA[i] > 0:
            A[k] = i
            k += 1
            countA[i] -= 1


n = list(map(int, input().split()))
CountSort(n)
print(*n)
