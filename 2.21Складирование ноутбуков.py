a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())
s1 = (a // x) * (c // y) * (b // z)
s2 = (a // y) * (c // x) * (b // z)
s3 = (a // z) * (c // x) * (b // y)
s4 = (a // x) * (c // z) * (b // y)
s5 = (a // z) * (c // y) * (b // x)
s6 = (a // y) * (c // z) * (b // x)
if s1 < s2:
    s1 = s2
if s3 < s4:
    s3 = s4
if s5 < s6:
    s5 = s6
if s1 < s3:
    s1 = s3
if s1 < s5:
    s1 = s5
print(s1)
