n = int(input())
L = -10**9
R = 10**9
for _ in range(n):
    l, r = map(int,input().split())
    L = max(L,l)
    R = min(R,r)
if L <= R:
    print(L)
else:
    print(-1)
