a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        if c > b:
            print(b)
            print(c)
            print(a)
        else:
            print(c)
            print(b)
            print(a)
    else:
        print(b)
        print(a)
        print(c)
elif b > c:
    if c > a:
        print(a)
        print(c)
        print(b)
    else:
        print(c)
        print(a)
        print(b)
else:
    print(a)
    print(b)
    print(c)
