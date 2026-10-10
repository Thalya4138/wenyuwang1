# -*- coding: utf-8 -*-

# =============================================================================
# 自定义函数
# =============================================================================

#%% 最简单的自定义函数

# a function that does nothing

def func():
    pass   # pass 语句，执行时什么也不做
           # 通常用来填补语法结构 (作为语句块的占位符)
           # 即语法上需要一个语句，但程序无需执行任何动作

# Pass 语句的适用场景：
#     自顶向下分解问题时，推迟函数体、条件语句块等的具体代码实现
#     从而保持在更抽象的层次进行思考 

f = func    # 这里是函数对象 
print('f is a function object:', f)

s = func()  # 函数名加括号和参数，才是调用函数
print('call function and return:', s)    # 输出函数调用的返回值

# Note：没有 return 语句的函数 (自动地) 返回 None

# 问题：能否写 f()? 


#%% 计算三角形面积的函数 (V.1)

def triangle(a, b, c):  #函数定义
    from math import sqrt

    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area
    print(area) # 这里调用 print 有意义吗？


# 函数调用
x = triangle(6, 8, 11)
y = triangle(12, 17, 19) - triangle(4, 7, 9)
print("Area of a triangle:", x)
print("Area of a triangle with a hole:", y)



#%% 计算三角形面积的函数 (V.2)

def triangle(a, b, c):
    from math import sqrt
    
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

# Note：return 后的表达式可以任意的复杂



#%% 计算三角形面积的函数 (V.3)

## 计算之前，先检查函数的参数

def triangle(a, b, c):
    from math import sqrt
    
    if a > 0 and b > 0 and c > 0 and \
      a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return float("nan")

print(triangle(3, 3, 7))

# float("nan")：特殊的返回值
#               表示计算得到的值无法用浮点数表示 (IEEE 754 浮点数标准中定义的特殊值)
#               本身不是一个具体的数值
#               与任何值 (包括它自身) 比较是否相等时，结果均为 False
#               与任何数值 (包括自身) 比较序关系时，结果均为 False

# 类似性质的特殊浮点数：float('inf'), float('-inf')


#%%

from math import isnan

# function isnan in module math
# Return True if x is a NaN (not a number), and False otherwise.

print(isnan(float('nan')))

print(isnan(triangle(3, 3, 7)))

print(isnan(triangle(3, 4, 5)))



#%% 计算并输出三角形面积的函数 

## (定义没有 return 语句的函数)

def print_triangle(a, b, c):
    from math import sqrt
    
    if a > 0 and b > 0 and c > 0 and \
      a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print("Area of triangle:", area)
    else:
        print(a, b, c, "do not form a triangle.")

print_triangle(6, 8, 11)
print_triangle(4, 7, -9)
 

#%% 谓词 (Predicate)：实现判断的函数，返回 True / False

def isOdd(num):
    if num % 2 == 1:
        return True
    else:
        return False