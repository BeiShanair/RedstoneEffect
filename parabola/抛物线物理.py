"""
@author: 北山_Besson
"""
import math
import os

g = 10


# 注意！！！！！这里的方法是纯物理法，在基于重力加速度为10的背景下，第二个坐标点的y2基本上是没用的（就是它是一般达不到那个点）
def parabola(x1, y1, z1, x2, y2, z2, num, max_h):
    global count, fp
    tick = int(math.sqrt(2 * (max_h - y1) / g) + math.sqrt(2 * (max_h - y2) / g)) * 20
    d_x = (x2 - x1) / tick / num
    d_z = (z2 - z1) / tick / num
    for i in range(tick * num):
        d_t = i / num / 20
        xi = x1 + d_x * i
        zi = z1 + d_z * i
        if d_t <= math.sqrt(2 * (max_h - y1) / g):
            yi = y1 + math.sqrt(2 * (max_h - y1) * g) * d_t - 0.5 * g * d_t ** 2
        else:
            yi = max_h - 0.5 * g * (d_t - math.sqrt(2 * (max_h - y1) / g)) ** 2
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 0 0 0 1 force\n".format(xi, yi, zi))
        if (i + 1) % num == 0:
            count += 1
            fp.write("schedule function 1:{0} 1t\n".format(count))
            fp.close()
            fp = open(name + "\\" + str(count) + ".mcfunction", "w")


f1 = open("point.txt", "r")  # f1存储坐标
list1 = []
for line in f1.readlines():
    line = line.strip('\n')  # \n是换行符
    list1.append(line.split(','))
f1.close()
count = 0
num = 5
max_h = 25
name = "parabola"
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
    parabola(x1, y1, z1, x2, y2, z2, num, max_h)
fp.close()
