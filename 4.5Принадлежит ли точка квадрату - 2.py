def IsPointInSquare(x, y):
    return -1 <= abs(x) + abs(y) <= 1

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
