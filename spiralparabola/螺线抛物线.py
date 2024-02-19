"""
@author: 北山_Besson
"""
import os
import math
import cmath


def spiralparabola(x1, y1, z1, x2, y2, z2, num, tick, max_h, r, w):
    global count, fp
    d_x = (x2 - x1) / tick / num
    d_z = (z2 - z1) / tick / num
    t = 0.5 * math.pi - cmath.polar(complex(x2 - x1, z2 - z1))[1]
    for i in range(tick * num):
        d_t1 = i / num
        half_t = tick / (2 * max_h - y1 - y2) * (max_h - y1)
        xa = x1 + d_x * i
        za = z1 + d_z * i
        if d_t1 <= half_t:
            ya = y1 + 2 * (max_h - y1) / half_t * d_t1 - 0.5 * (2 * (max_h - y1) / half_t ** 2) * d_t1 ** 2
            v = 2 * (max_h - y1) / half_t - (2 * (max_h - y1) / half_t ** 2) * d_t1
        else:
            ya = max_h - 0.5 * (2 * (max_h - y2) / (tick - half_t) ** 2) * (d_t1 - half_t) ** 2
            v = -(2 * (max_h - y2) / (tick - half_t) ** 2) * (d_t1 - half_t)
        s = math.sqrt((d_x*num)**2+(d_z*num)**2)
        f = math.atan(v / s)
        xi = r * (-math.cos(t) * math.cos(w * d_t1) - math.sin(f) * math.sin(t) * math.sin(w * d_t1))
        yi = r * math.cos(f) * math.sin(w * d_t1)
        zi = r * (math.sin(t) * math.cos(w * d_t1) - math.cos(t) * math.sin(f) * math.sin(w * d_t1))
        xj = r * (-math.cos(t) * math.cos(w * d_t1 + math.pi) - math.sin(f) * math.sin(t) * math.sin(w * d_t1 + math.pi))
        yj = r * math.cos(f) * math.sin(w * d_t1 + math.pi)
        zj = r * (math.sin(t) * math.cos(w * d_t1 + math.pi) - math.cos(t) * math.sin(f) * math.sin(w * d_t1 + math.pi))
        fp.write(
            "particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} 0.2 0 force\n".format(xa, ya, za, xi, yi,
                                                                                                    zi))
        fp.write(
            "particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} 0.2 0 force\n".format(xa, ya, za, xj, yj,
                                                                                                    zj))
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
max_h = 25
num = 5  # 单位方块里的粒子个数
tick = 100  # 每条螺线运动时间
r = 0.5  # 运动半径
w = 1  # 角速度
name = "spiralparabola"
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
    spiralparabola(x1, y1, z1, x2, y2, z2, num, tick, max_h, r, w)
fp.close()
