a = int(input())
if a % 4 != 0:
    print("N")
else:
    if a % 100 == 0 and a % 400 != 0:
        print("N")
    elif a % 3200 == 0:
        print("N")
    else:
        print("Y")
