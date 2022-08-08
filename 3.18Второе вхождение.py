s = str(input())
if s.find('f') != -1:
    if s.find('f', s.find('f') + 1) != -1:
        print(s.find('f', s.find('f') + 1))
    else:
        print(-1)
else:
    print(-2)
