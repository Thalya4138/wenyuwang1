# -*- coding: utf-8 -*-

#%% for 语句的嵌套

for k in range(3): # 外层 for 循环
         
    n = int(input('Factorial for: '))
    
    prod = 1       # 累积变量，需设置合适的初值
    for i in range(2, n + 1): # 内层 for 循环
        prod *= i  # 原地更新，执行效率可能更高
    
    print(f"The factorial of {n} is {prod}.")



#%% 字符串的循环 1

## 用下标进行循环 (对于表的循环，写法类似)

s = '0123456789'

for i in range(len(s)):
    print(s[i], end=' ')  # 关键字实参 end=' ' 可以用来设置行式输出时的结束符
print()



#%% 字符串的循环 2

## 直接在字符串上循环 (类似的，也有直接在表上循环)
## 字符串、表等对象可以直接作为 for 语句中循环变量的取值源

for c in s: 
    print(c, end=',') # 变量 c 将从头起遍历串 s 中所有字符
print()



#%% 测试 for 语句的执行方式

n = 4
for i in range(n):
    print("itn: #", i)
    n = n + 1

print(f'After iteration, {i = }')

# =============================================================================
# Note 1: for 的循环方式在进入循环时即确定；
# 
# Note 2: for 循环结束后，循环变量继续存在，并且保持最后的值。
# =============================================================================


#%% 交互式阶乘计算器

print("This is a factorial calculator. Negative to stop.")

n = int(input("Factorial for (Negative to stop): "))
while n >= 0: # 问题：这里能用 for 语句替代吗？
    prod = 1
    for i in range(2, n + 1):
        prod *= i

    print(f"The factorial of {n} is {prod}.")    
    n = int(input("Factorial for (Negative to stop): "))

print("Thanks for using. Bye!")



#%%
## 牛顿迭代法求平方根 (!!!)

s = float(input("Square root for: "))

guess = 1.0

while guess * guess != s:
    guess = (guess + s / guess) / 2

print(f"Square root for {s} is {guess}")


# while 可能发生无穷循环 / 死循环
# 在 console 中可以用 ctrl-c 中断计算


#%%
## 牛顿迭代法求平方根，带简单的显示过程 (XXX!)

s = float(input("Square root for: "))

guess, n = 1.0, 0

while guess * guess != s:
    guess, n = (guess + s / guess) / 2, n + 1
    print(f"#{n}: {guess} {guess * guess}")

print(f"Square root for {s} is {guess}")



#%%
## 牛顿迭代法求平方根 (近似值)，带显示过程
## 内置函数 abs：计算参数的绝对值
s = float(input("Square root for: "))

guess, n = 1.0, 0

while abs(guess * guess - s) > 1e-12:
    guess, n = (guess + s / guess) / 2, n + 1
    print(f"#{n}: {guess} {guess * guess}")

print(f"Square root for {s} is {guess}")

# =============================================================================
# Note-1：浮点数的内部实现可能存在表示误差
# Note-2：浮点数计算有误差，而且误差会积累
# Note-3：绝对不能用浮点数的相等关系来控制循环
# =============================================================================


#%% 写循环计算 0.1 + 0.2 + ... + 2.0

num, s = 0.0, 0
while num <= 2.0:  # 实际循环执行了多少次？ 
    print(f'{num = }')
    s += num   
    num += 0.1
    
print(f'\n{s = : .6f}')

## Note-4：尽可能不用浮点数运算来控制有准确执行次数的循环