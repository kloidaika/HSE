a = int(input())
b = int(input())
c = int(input())
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("impossible")
else:
    if a > b:
        if a > c:
            if a ** 2 == b ** 2 + c ** 2:
                print("rectangular")
            elif a ** 2 < b ** 2 + c ** 2:
                print("acute")
            elif a ** 2 > b ** 2 + c ** 2:
                print("obtuse")
        else:
            if c ** 2 == b ** 2 + a ** 2:
                print("rectangular")
            elif c ** 2 < b ** 2 + a ** 2:
                print("acute")
            elif c ** 2 > b ** 2 + a ** 2:
                print("obtuse")
    elif b > c:
        if b ** 2 == c ** 2 + a ** 2:
            print("rectangular")
        elif b ** 2 < c ** 2 + a ** 2:
            print("acute")
        elif b ** 2 > c ** 2 + a ** 2:
            print("obtuse")
    else:
        if c ** 2 == b ** 2 + a ** 2:
            print("rectangular")
        elif c ** 2 < b ** 2 + a ** 2:
            print("acute")
        elif c ** 2 > b ** 2 + a ** 2:
            print("obtuse")
