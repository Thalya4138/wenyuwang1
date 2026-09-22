r1 = list(map(int,input().split()))
r2 = list(map(int,input().split()))
r3 = list(map(int,input().split()))
r4 = list(map(int,input().split()))
r5 = list(map(int,input().split()))
matrix = [r1, r2, r3, r4, r5]
for number,row in enumerate(matrix,start=1):
    for num,i in enumerate(row,start=1):
        if i == 1:
            x = num
            y = number
            found=True
            break
    if found:
        break
sum = abs(3-x)+abs(3-y)
print(sum)