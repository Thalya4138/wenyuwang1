n = int(input())
money = list(map(int, input().split()))
five = 0
ten = 0
for x in money:
    if x == 5:
        five += 1
    elif x == 10:
        if five == 0:
            print("NO")
            break
        five -= 1
        ten += 1
    elif x == 20:
        if ten > 0 and five > 0:
            ten -= 1
            five -= 1
        elif five >= 3:
            five -= 3
        else:
            print("NO")
            break
else:
    print("YES")