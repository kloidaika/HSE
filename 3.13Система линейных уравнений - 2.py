(a, b, c) = (float(input()), float(input()), float(input()))
(d, e, f) = (float(input()), float(input()), float(input()))
if abs(a / c) == abs(b / d) == abs(e / f):
    if a * c > 0 and b * d > 0:
        print(1, -1, 1)
    else:
        print(1, 1, 1)
    if a == 0:
        y = e / b
        x = (f - d * y) / c
    elif b == 0:
        x = e / a
        y = (f - c * x) / d
    elif c == 0:
        y = f / d
        x = (e - b * y) / a
    elif d == 0:
        x = f / c
        y = (e - a * x) / b
    #else:
        #y = (f - c * e / a) / (d - b * c / a)
        #x = (e - b * y) / a
print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
