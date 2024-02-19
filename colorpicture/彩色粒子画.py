"""
@author: 北山_Besson
"""
import os
from PIL import Image

im = Image.open("test.jpg")  # 打开图片
pix = im.load()  # 加载图片
width = im.size[0]
height = im.size[1]  # 取宽度和长度

# 创建文件夹
function_dir = "colorpicture"
if not os.path.exists(function_dir):
    os.mkdir(function_dir)

# 坐标
set_x = 115
set_y = 30
set_z = 175
count = 0
num = 15
name = str(count)
fp = open(function_dir + "\\" + name + ".mcfunction", 'w')

# 循环结构
for i in range(width):
    for j in range(height):
        xi = set_x + i / num
        yi = set_y - j / num
        R, G, B = pix[i, j]
        R /= 255
        G /= 255
        B /= 255
        fp.write(
            "particle dust {0:.2f} {1:.2f} {2:.2f} 1.0 {3:.2f} {4:.2f} {5:.2f} 0 0 0 0 1 force\n".format(R, G, B, xi,
                                                                                                         yi, set_z))
fp.close()
