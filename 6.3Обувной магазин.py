leg = int(input())
shop = list(map(int, input().split()))
shop.sort()
if shop[0]
counter = 0
for i in range(len(shop)):
    if shop[i] - leg >= 3:
        counter += 1
        leg = shop[i]
print(counter)
