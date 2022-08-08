myList = list(map(int, input().split()))
mySet = set()
for n in myList:
    if n in mySet:
        print("YES")
    else:
        print("NO")
    mySet.add(n)
