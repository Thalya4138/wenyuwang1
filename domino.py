M,N = map(int,input().split())
if M % 2 == 0:
    if N % 2 == 0:
        a = M * N // 2
    if N % 2 != 0:
        a = M * N // 2
else:
    if N % 2 == 0:
        a = M * N // 2
    else:
        a = (M * N -1) // 2
print(a)