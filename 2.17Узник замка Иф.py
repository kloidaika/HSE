a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
s = d * e
if d > e:
    d, e = e, d
if a * b > s and a * c > s and b * c > s or d < min(a, b, c):
    print("NO")
else:
    print("YES")
