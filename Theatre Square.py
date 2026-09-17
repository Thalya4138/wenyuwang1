n, m, a = map(int, input().split())
if n % a == 0:
    if m % a == 0:
        print(n * m // (a**2))
    else:
        b = (m // a) * a
        print(n * (b + a) // (a**2))
else:
    if m % a == 0:
        b = (n // a) * a
        print(m * (b + a) // (a**2))
    else:
        b = (m // a) * a
        c = (n // a) * a
        print(((b + a) * (c + a)) // (a**2))
