s = str(input())
print(s[:-s[::-1].find('h') - 1], s[s.find('h') + 1:], sep="")
