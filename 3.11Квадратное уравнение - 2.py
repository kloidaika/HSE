import math

(a, b, c) = (float(input()), float(input()), float(input()))
d = b**2 - 4 * a * c
if a != 0:
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if x1 == x2:
            print(1, x1)
        elif x1 > x2:
            print(2, '{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
        elif x1 < x2:
            print(2, '{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
    else:
        print(0)
elif b != 0:
    x = -c / b
    print(1, '{0:.6f}'.format(x))
elif c == 0:
    print(3)
else:
    print(0)
