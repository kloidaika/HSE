p = int(input())
x = int(input())
y = int(input())
s = x * 100 + y
s = int(s + s * p / 100)
print(int(s) // 100, int(s) % 100)
