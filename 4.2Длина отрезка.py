def distance(x1, y1, x2, y2):
    x = max(x1, x2) - min(x1, x2)
    y = max(y1, y2) - min(y1, y2)
    return (x**2 + y**2)**(0.5)
(x1, y1) = (float(input()), float(input()))
(x2, y2) = (float(input()), float(input()))
print('{0:.5f}'.format(distance(x1, y1, x2, y2)))
