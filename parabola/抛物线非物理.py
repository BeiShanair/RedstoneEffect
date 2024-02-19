"""
@author: 北山_Besson
"""
import os


def parabola(x1, y1, z1, x2, y2, z2, num, tick, max_h):
    global count, fp
    d_x = (x2 - x1) / tick / num
    d_z = (z2 - z1) / tick / num
    for i in range(tick * num):
        d_t = i / num
        half_t = tick / (2 * max_h - y1 - y2) * (max_h - y1)
        xi = x1 + d_x * i
        zi = z1 + d_z * i
        if d_t <= half_t:
            yi = y1 + 2*(max_h - y1) / half_t * d_t - 0.5 * (2 * (max_h - y1) / half_t ** 2) * d_t ** 2
        else:
            yi = max_h - 0.5 * (2 * (max_h - y2) / (tick - half_t) ** 2) * (d_t - half_t) ** 2
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 0 0 0 1 force\n".format(xi, yi, zi))
        if (i + 1) % num == 0:
            count += 1
            fp.write("schedule function 5:{0} 1t\n".format(count))
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
tick = 20
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
    parabola(x1, y1, z1, x2, y2, z2, num, tick, max_h)
fp.close()
