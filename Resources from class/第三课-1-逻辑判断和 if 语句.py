# -*- coding: utf-8 -*-


#%% 实例：输入三角形三边长之后，先检查数据，再计算并输出面积

from math import sqrt
edges = input('请输入三边长:').split()
a, b, c = float(edges[0]), float(edges[1]), float(edges[2])

if a > 0 and b > 0 and c > 0 and \
  a + b > c and b + c > a and a + c > b: # 利用续行符写长表达式
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))    
    print(f'area = {area:.6f}')
    # 注意：语句组要退格对齐
else:    
    print(f'{a}, {b} and {c} do not form a triangle.')



#%% 实例：利用求根公式，计算二次多项式的根

print("Program for real root(s) of quadratic equations.")
a = float(input("Coefficient of x**2: "))
b = float(input("Coefficient of x: "))
c = float(input("Constant: "))

d = b**2 - 4 * a * c  # 计算并记录判别式
if d > 0:
    tmp = sqrt(d)
    print(f"Two roots:, {(-b + tmp) / 2 / a},  {(-b - tmp) / 2 / a}")
elif d == 0:
    print(f"One root: {-b / 2 / a}")  # Note here that how to write 2a
else:
    print("No real root")

## 这里也可以改用两重 if-else 语句的嵌套