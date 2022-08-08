n = int(input())
m = 0
i = 1
p = 0
q = 0
l = 0
while n != 0:
    k = m
    m = n
    n = int(input())
    if k < m and m > n and i != 1 and n != 0:
        q = p
        p = i
        if q != 0 and (p - q < l or l == 0):
            l = p - q
    i += 1
    # print("k",k,"m",m,"n",n,"l",l,"i",i,"p",p,"q",q)
print(l)
