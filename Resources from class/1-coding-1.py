#%%

## 定义函数，把一个十进制正整数转换成一个二进制（字符）串
def int2bin(n:int) -> str:
    bits = ''
    
    while n != 0:
        if n % 2 == 0:
            bits = '0' + bits
        else:
            bits = '1' + bits
        n //= 2 
    
    return bits

num = 253
print("Binary string of", num, "is", int2bin(num))


#%%

# built-in function bin: Return the binary representation of an integer.

print(bin(253)) # with prefix “0b”

print(bin(-253))


#%%

# If prefix “0b” is NOT desired, 
# you can use the following ways:
    
print(bin(253)[2:])  # 简单粗暴、不适用于负整数


#%%

# built-in function format can convert a value to 
# a “formatted” representation.

print(format(253, 'b'))

print(format(-253, 'b'))


#%%

print(f'{253:b}')   # via f-string

print(f'{-253:b}')


#%%

## 定义函数，把一个内容为二进制正整数的字符串转换成一个十进制整数
def bin2int(bits:str) -> int:
    num = 0
    for i in range(len(bits)):
        num = num * 2 + int(bits[i])  # 霍纳法则（Horner's rule）/ 秦九韶算法
    
    return num

bits = '11111101'
print("Number of string", bits, "is", bin2int(bits))


#%%

## 改写函数 bin2int，for 语句直接在字符串上循环
def bin2int_v2(bits):
    num = 0
    
    # 字符串/表等对象可以直接作为 for 语句里的取值源
    for c in bits: # 变量 c 将从头起遍历 bits 中所有字符
        num = num * 2 + int(c)
    
    return num


#%%

# 当然，也可以直接用类型转换
print(int('11101', 2))

print(int('-11101', 2))
