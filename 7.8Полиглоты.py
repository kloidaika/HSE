commonLang, total = set(), set()
for i in range(int(input())):
    tmp = set()
    for j in range(int(input())):
        lang = input()
        tmp.add(lang)
    if i == 0:
        commonLang = tmp
    else:
        commonLang &= tmp
    total |= tmp
for r in (commonLang, total):
    print(len(r), *r, sep='\n')
