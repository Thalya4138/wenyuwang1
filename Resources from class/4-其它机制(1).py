# -*- coding: utf-8 -*-

# =============================================================================
# Python 的一些机制
# =============================================================================

#%% 条件表达式

# 自定义绝对值函数
def myAbs(x):
    # 直接 return 条件表达式的结果
    return x if x >= 0 else -x  

print(myAbs(-14.5))


#%%
## 示范：assert 语句, 类型检查，文档串

def fact(n) : # 阶乘函数
    """Function to calculate the factorial \
of the argument n, which should be a \
non-negative integer."""

    assert(isinstance(n, int) and n >= 0) 
    # 问题：能否交换两个判断？
    
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod


# 打印 fact 函数的文档串
print(fact.__doc__) 

for n in range(1, 25, 3):
    print(f'{n}! = {fact(n)}')


#%%
print(fact(-4))