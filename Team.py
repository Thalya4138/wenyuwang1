n = int(input())
m = 0
for i in range(0, n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        m += 1
    else:
        m += 0
print(m)
