"""
@author: 北山_Besson
"""
import os
from PIL import Image

# 函数部分
def bw_judge(R, G, B):
    Gray_scale = int(0.299 * R + 0.587 * G + 0.114 * B)  # 求灰度值
    if Gray_scale < 132:
        color = "black"
    else:
        color = "white"
    return color


im = Image.open("test.jpg")  # 打开图片
pix = im.load()  # 加载图片
width = im.size[0]
height = im.size[1]  # 取宽度和长度

# 创建文件夹
function_dir = "picture"
if not os.path.exists(function_dir):
    os.mkdir(function_dir)

# 坐标
set_x = 105
set_y = 30
set_z = 175
count = 0
num = 15
name = str(count)
fp = open(function_dir + "\\" + name + ".mcfunction", 'w')

# 循环结构
for i in range(width):
    for j in range(height):
        R, G, B = pix[i, j]
        if bw_judge(R, G, B) == "black":
            yi = set_y - j / num
            xi = set_x - i / num
            fp.write("particle firework {0:.2f} {1:.2f} {2:.2f} 0 0.1 0 1 0 force\n".format(xi, yi, set_z))
fp.close()
