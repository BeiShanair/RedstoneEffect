"""
@author: 北山_Besson
"""
import math
import os


def roseline(x, y, z, r, k):
    name = "roseline"
    if not os.path.exists(name):
        os.mkdir(name)
    fp = open(name + "\\" + str(count) + ".mcfunction", "w")
    for i in range(360):
        xi = r * math.sin(k * math.radians(i)) * math.cos(math.radians(i))
        yi = r * math.sin(k * math.radians(i)) * math.sin(math.radians(i))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} 0 0.2 0 force\n".format(x, y, z, xi, yi))
    fp.close()


f1 = open("point.txt", "r")  # f1存储坐标
list1 = []
for line in f1.readlines():
    line = line.strip('\n')  # \n是换行符
    list1.append(line.split(','))
f1.close()
r = 5
count = 0
k = 4         # 注意k如果是偶数，那么会显示2k个花瓣；如果k是奇数，则显示k个花瓣
for i in range(len(list1)):
    x1 = int(list1[i][0])
    y1 = int(list1[i][1])
    z1 = int(list1[i][2])
    roseline(x1, y1, z1, r, k)
    count += 1
