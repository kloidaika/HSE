x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 < y2:
    if (x2 - x1 + y2 - y1) % 2 == 0:
        if y2 - y1 >= x2 - x1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
