i = int(input())
b = f"{i:032b}"
high = b[:16];low = b[16:];bi = low + high
bii = int(bi,2)
print(bii)


#有点意思，这里涉及了进制的转化。哦原来自带相关函数库
'''
十进制数据的二进制转换
①bin → binary 二进制|oct → octal 八进制|hex → hexadecimal 十六进制
    n = int(input())
    b = bin(n)
    print(b)
>>>'0b1101'

②format(对象, 格式要求)
    b = format(n, "032b")
        0   → 用 0 补
        32  → 总长度至少 32
        b   → 二进制
>>>00000000000000000000000000001101
得到固定 32 位二进制字符串

③f"{变量:格式}"
    b = f"{n:032b}"
得到固定 32 位二进制字符串

④二进制字符串 → 整数：int(字符串, 进制)
    int("1101", 2)
'''


