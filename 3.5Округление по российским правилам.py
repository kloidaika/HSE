import math
n = float(input())
if (n - int(n)) >= 0.5:
    print(math.ceil(n))
else:
    print(math.floor(n))
