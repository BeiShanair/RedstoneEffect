"""
@author: 北山_Besson
"""
import math
import os


def sphere(x, y, z, r, R):
    if r == 0:
        y1 = y + R * math.sin(math.radians(i))  # 各个圆的高度
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 0 0 0 1 force\n".format(x, y1, z))
    else:
        for j in range(0, 360, 10):  # 这里只有180次循环，因为粒子数太多了
            xi = x + r * math.cos(math.radians(j))
            zi = z + r * math.sin(math.radians(j))
            yi = y + R * math.sin(math.radians(i))
            fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 0 0 0 1 force\n".format(xi, yi, zi))


# 球心坐标
set_x = 105
set_y = 30
set_z = 175
count = 0
R = 5
dirname = "sphere"
if not os.path.exists(dirname):
    os.mkdir(dirname)

fp = open(dirname + "\\" + str(count) + ".mcfunction", 'w')
for i in range(-90, 90, 5):  # 意思是从底部到顶部
    r = R * math.cos(math.radians(i))  # 各层圆的半径
    sphere(set_x, set_y, set_z, r, R)
fp.close()
