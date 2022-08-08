a, b, c = (float(input()), float(input()), float(input()))
p = (a + b + c) / 2
print('{0:.6f}'.format((p * (p - a) * (p - b) * (p - c))**0.5))
