m,k = map(int,input().split())
a = (m % 19 == 0)
count = {}
for x in str(m):
    x = int(x)
    count[x] = count.get(x, 0) + 1
b = (count[3] == k )
if a and b:
    print("YES")
else:
    print("NO")