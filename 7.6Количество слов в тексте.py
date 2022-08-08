import sys


wordsSet = set()
for line in sys.stdin:
    for word in line.split():
        wordsSet.add(word)
print(len(wordsSet))
