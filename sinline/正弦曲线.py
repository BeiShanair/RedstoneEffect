"""
@author: 北山_Besson
"""
import random
import math
import os


def sinline(x1, y1, z1, x2, y2, z2, num, tick, A, w, f):
    global count, fp
    d_x = (x2 - x1) / tick / num
    d_y = (y2 - y1) / tick / num
    d_z = (z2 - z1) / tick / num
    for i in range(tick * num):
        xi = x1 + d_x * i
        yi = y1 + d_y * i + A * math.sin(w * math.radians(i) + f)
        zi = z1 + d_z * i
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 0 0 0 1 force\n".format(xi, yi, zi))
        if (i + 1) % num == 0:
            count += 1
            fp.write("schedule function 6:{0} 1t\n".format(count))
            fp.close()
            fp = open(name + "\\" + str(count) + ".mcfunction", "w")


A = random.randint(2, 5)
w = random.randint(1, 4)
f = math.pi * random.random()
f1 = open("point.txt", "r")  # f1存储坐标
list1 = []
for line in f1.readlines():
    line = line.strip('\n')  # \n是换行符
    list1.append(line.split(','))
f1.close()
count = 0
num = 10
tick = 20  # 这个tick是每条直线运动的时间！是每条！不是全部！！！
name = "sinline"
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
    sinline(x1, y1, z1, x2, y2, z2, num, tick, A, w, f)
fp.close()
