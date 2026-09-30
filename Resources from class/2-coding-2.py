
#%%
# ord(c): 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
#         例如 ord('0') 返回整数 48，ord('a') 返回整数 97
#              ord('€') （欧元符号）返回 8364


# chr(i): 返回 Unicode 码位为整数 i 的字符的字符串格式。是 ord() 的逆函数。
#         例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。
#         实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。
#         如果 i 超过这个范围，会触发 ValueError 异常。

#%%

print(chr(0x07))  # 字符 0x07：BEL，响铃


#%%

print(chr(10) == '\n')   # 字符 0x0A：new line


#%% print printable characters in ASCII

count = 1
for i in range(32, 127):
    if count < 10:
        print(chr(i), end='\t')
        count += 1
    else:
        print(chr(i))
        count = 1



#%% pillow 模块简介

# 全称：Python Imaging Library
# Python 在图像处理领域广泛使用的第三方库（其它的图像处理模块还有 OpenCV、SimpleCV 等）
# Ref: https://pillow.readthedocs.io/en/stable/index.html

# 导入 pillow 库中的核心模块 Image
from PIL import Image

# 打开图片
# Lenna 是一幅早期广泛应用于图像处理和视频处理研究的测试图
img = Image.open('lenna.png')

# 利用外部图片查看器显示图片
img.show()


#%% 查看图片的各种属性

print(img.format, img.mode, img.size, sep='\n')

#%% 旋转图像并显示

rotated_img = img.rotate(90)
rotated_img.show()
