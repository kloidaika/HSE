import functools

print(functools.reduce(lambda a, b: a * b, map(lambda i: i**5, (map(int, input().split())))))
