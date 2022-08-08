(a, b, c, d) = (int(input()), int(input()), int(input()), int(input()))
if c == 0:
    if a == 0:
        print("INF")
    else:
        print(-b // a)
elif a == 0:
    if b == 0 and c == 0:
        print("INF")
    else:
        print("NO")
elif d // c != b // a:
    print(-b // a)
else:
    print("NO")
