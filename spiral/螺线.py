"""
@author: 北山_Besson
"""
import os
import math
import cmath


def spiral(x1, y1, z1, x2, y2, z2, tick, num, r, w):
    global count, fp
    d_x = (x2 - x1) / tick / num
    d_y = (y2 - y1) / tick / num
    d_z = (z2 - z1) / tick / num
    s = math.sqrt((x1 - x2) ** 2 + (z1 - z2) ** 2)
    t = 0.5 * math.pi - cmath.polar(complex(x2 - x1, z2 - z1))[1]
    f = math.atan((y2 - y1) / s)
    for i in range(tick * num):
        d_t = i / num
        x = x1 + d_x * i
        y = y1 + d_y * i
        z = z1 + d_z * i
        xi = r * (-math.cos(t) * math.cos(w * d_t) - math.sin(f) * math.sin(t) * math.sin(w * d_t))
        yi = r * math.cos(f) * math.sin(w * d_t)
        zi = r * (math.sin(t) * math.cos(w * d_t) - math.cos(t) * math.sin(f) * math.sin(w * d_t))
        fp.write(
            "particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} 0.2 0 force\n".format(x, y, z, xi, yi,
                                                                                                    zi))
        if (i + 1) % num == 0:
            count += 1
            fp.write("schedule function 8:{0} 1t\n".format(count))
            fp.close()
            fp = open(name + "\\" + str(count) + ".mcfunction", "w")


f1 = open("point.txt", "r")  # f1存储坐标
list1 = []
for line in f1.readlines():
    line = line.strip('\n')  # \n是换行符
    list1.append(line.split(','))
f1.close()
count = 0
num = 5  # 单位方块里的粒子个数
tick = 30  # 每条螺线运动时间
r = 0.5  # 运动半径
w = 1  # 角速度
name = "spiral"
if not os.path.exists(name):
    os.mkdir(name)
fp = open(name + "\\" + str(count) + ".mcfunction", "w")
for i in range(len(list1) - 1):
    x1 = int(list1[i][0])
    y1 = int(list1[i][1])
    z1 = int(list1[i][2])
    x2 = int(list1[i + 1][0])
    y2 = int(list1[i + 1][1])
    z2 = int(list1[i + 1][2])
    spiral(x1, y1, z1, x2, y2, z2, tick, num, r, w)
fp.close()
