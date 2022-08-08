s = str(input())
print(s[:s.find('h')], s[len(s) - s[::-1].find('h'):], sep="")
