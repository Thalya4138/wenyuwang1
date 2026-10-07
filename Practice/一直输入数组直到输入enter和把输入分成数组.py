'''输入数组直到输入enter
import math
x = 0
y = 0
while True:
    s = input()
    if s == "":
        break
    a, b = map(float, s.split())
    x += a
    y += b
print(f"{math.sqrt(x**2+y**2):.4}")'''

#把输入分组
import math
x = 0
y = 0
s = list(map(float, input().split()))
for i in range(0, len(s), 2):
    x += s[i]
    y += s[i + 1]
print(f"{math.sqrt(x**2 + y**2):.4f}")