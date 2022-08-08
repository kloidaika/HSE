s = str(input())
if (s.find('f')) != -1:
    print(s.find('f'), end=" ")
    if s.find('f', s.find('f') + 1) != -1:
        print(len(s) - s[::-1].find('f') - 1)
