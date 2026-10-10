# -*- coding: utf-8 -*-

# 实例：计算实数立方根的近似值
#      -> 通用方法 vs. 专用方法
#      -> 搭建测试平台 (黑箱测试)
#      -> Python 对模块测试的支持


## (1) 交互式测试平台
def run_cbrt():
    print("Number to test cbrt, None to stop.")
    while True:
        s = input("Next number (None to stop): ")
        
        if s == "None": return
        
        x = float(s)
        r = cbrt(x)
        if abs(r**3 - x) < 1e-3:
            print(f"Correct: cbrt({x}) = {r}")
        else:
            print(f"Wrong: {r}**3 = {r**3}")


## (2) 批量数据测试平台：用从 a 到 b 步长为 d 的一系列数做试验
def test_cbrt(a, b, d):
    x = a
    while x < b:      # 由于 a、b、d 可能是浮点数，不能用 for
        r = cbrt(x)
        if abs(r**3 - x) <= 1e-3:
            print(f"Correct: cbrt({x}) = {r}")
        else:
            print(f"Wrong: {r}**3 = {r**3}")
        x += d
    print("")         # 输出一空行


## 对于黑箱测试，更合理的方式是随机测试
## 需利用之后介绍的随机数生成函数，这里先略过


#%%

# 通用方法 (1)：枚举，作等距检查，选择最接近解的值

def cbrt(x:float) -> float:
    x = float(x)                  # 能完成转换即表示 x 是合理的参数
    sign = -1 if x < 0.0 else 1   # 用条件表达式提取 x 的符号
    x = abs(x)
    test, root = 0.0, 0.0

    while test**3 <= x:
        if abs(test**3 - x) < abs(root**3 - x):
            root = test
        test += 0.001

    return sign * root


# 具体测试
if __name__ == '__main__': # 检查本模块是否为主模块
    test_cbrt(0.0, 1.0, 0.1)
    
    test_cbrt(-1.0, 0.0, 0.2)
    
    test_cbrt(0, 200.0, 20.0)


# 枚举：遍历并检查可能解的集合，算法思想简单
# 问题：如何确保枚举出全部可能解，不发生遗漏，同时搜索空间尽可能的小？



#%%

# 通用方法 (2)：二分法 (折半法) 逼近
def cbrt(x:float) -> float:
    y = abs(x)
    if y >= 1:      # 对 y>=1，初始区间为 [1, y]
        a, b = 1.0, y
    else:           # 对 y<1，初始区间为 [0, 1]
        a, b = y, 1.0
        
    while True:
        m = (a + b)/2            # 取区间中点
        
        if abs(m**3 - y) < 1e-3: # 绝对误差
            return -m if x < 0.0 else m

        if m**3 > y:
            b = m               # 新区间 [a, m]
        else:
            a = m               # 新区间 [m, b]


if __name__ == '__main__':
    test_cbrt(0, 1000.0, 100)



#%%
# 思考：用 绝对误差 控制迭代是否合理？(考虑计算绝对值很小的数的立方根)

if __name__ == '__main__':
    x = 0.0001
    y = cbrt(x)
    print(f'cbrt({x}) = {y}, while {y}**3 = {y**3}')



#%%
# 二分法逼近 (查找) 基于分治 (分而治之) 的策略，易于理解，常用于：
#   单调区间内求方程的近似解：每次把解的查找范围缩小一半，逐步逼近符合精度要求的解
#   (有序数组的) 元素快速查找 (之后介绍)
#   ......

# 二分法逼近的要点：
#   初始区间的设置  
#   折半时，区间边界的确定
#   折半后，选择正确的区间 (左/右)
#   while 循环的控制条件 (依赖于精度要求)
#   退出循环时，确定解的正确表示形式



#%%
# 专用方法：根据牛顿迭代逼近公式，且用 相对误差 控制精度
def cbrt(x:float):
   if x == 0.0:          # 处理特殊情况
       return 0.0
   
   x1 = x
   while True:
       x2 = (2.0 * x1 + x / x1 / x1) / 3  # 递推新逼近值
       
       if abs((x2 - x1) / x1) < 1e-6:     # 相对误差
           return x2
       
       x1 = x2


if __name__ == '__main__':
    test_cbrt(-0.001, 0.001, 0.0001)
    
    test_cbrt(0.0, 20000.0, 2000)


# 一般来说，专门的方法比通用方法有更高的效率
