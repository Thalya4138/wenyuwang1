n = int(input())
events = map(int, input().split())
m = 0
t = 0
for i in events:
    m += i
    if m >= 0:
        continue
    else:
        m = 0
        t += 1
print(t)
