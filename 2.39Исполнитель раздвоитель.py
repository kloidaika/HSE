a = int(input())
b = int(input())
while a != b:
    if b * 2 <= a and a % 2 == 0:
        a //= 2
        print(":2")
    else:
        a -= 1
        print("-1")
