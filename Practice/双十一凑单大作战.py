n = int(input())
P = list(map(int,input().split()))
P.sort()
l = len(P)
k = len(P) // 3
count = 0
for i in range(1,k+1):
    P.pop(l-3*i)
for i in P:
    count += i
print(count)
