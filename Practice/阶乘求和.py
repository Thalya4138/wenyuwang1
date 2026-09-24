n = int(input())
k = 0
for i in range(1,n+1):
    m = 1
    for s in range(1,1+i):
        m *= s
    k += m
print(k)