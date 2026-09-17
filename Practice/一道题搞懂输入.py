mode = int(input())
if mode == 1:
    s = input()
    print(s)
elif mode == 2:
    x = int(input())
    print(x**2)
elif mode == 3:
    m, n, p = input().split()
    print(p, n, m)
elif mode == 4:
    a, b = map(int, input().split())
    q = a + b
    p = a * b
    print(q, p)
elif mode == 5:
    a = list(map(int, input().split()))
    s1 = len(a)
    s2 = sum(a)
    s3 = max(a)
    print(s1, s2, s3)
elif mode == 6:
    t = input()
    k = 0
    while t != "END":
        m = int(t)
        k += m
        t = input()
    print(k)
elif mode == 7:
    n = int(input())
    m = []
    for i in range(0, n):
        a, b = map(int, input().split())
        c = a + b
        m.append(c)
    print(*m)
elif mode == 8:
    m, n, p = input().split(",")
    print(p, n, m)
