def xor(x, y):
    return (x + y) % 2 != 0


x = int(input())
y = int(input())
if xor(x, y):
    print(1)
else:
    print(0)
