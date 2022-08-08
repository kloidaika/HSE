def IsPointInArea(x, y):
    a = (x + y >= 0 and -2 * x - 2 + y >= 0 and (x + 1)**2 + (y - 1)**2 <= 4)
    b = (x + y <= 0 and -2 * x - 2 + y <= 0 and (x + 1)**2 + (y - 1)**2 >= 4)
    return a + b

x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print("YES")
else:
    print("NO")
