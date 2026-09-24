n,a=map(int,input().split())
t = 0
s = 0
for i in range(1,n+1):
    for j in range(i):
        t += a*(10**j)
    s += t
    t = 0
print(s)