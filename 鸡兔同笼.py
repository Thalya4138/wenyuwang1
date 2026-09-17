a = int(input())
if a % 2 == 0:
    x = a // 2
    if a % 4 == 0:
        y = a // 4
    else:
        y = (a - 2) // 4 + 1
else:
    x = y = 0
print(y, x)
