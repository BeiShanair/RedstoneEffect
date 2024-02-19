"""
@author: 北山_Besson
"""
import os

num = 8
t = 1 / num


def block(x, y, z):
    name = "block"
    if not os.path.exists(name):
        os.mkdir(name)
    fp = open(name + "\\" + str(count) + ".mcfunction", "w")
    xi = x - num / 2 * t
    yi = y - num / 2 * t
    zi = z - num / 2 * t
    fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi, zi))

    for j in range(8):
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi + 1, yi, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi, zi + 1))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi + 1, yi, zi + 1))
        yi += t
    for j in range(8):
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi - 1, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi, zi + 1))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi - 1, zi + 1))
        xi += t
    for j in range(8):
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi - 1, yi, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi, yi - 1, zi))
        fp.write("particle end_rod {0:.2f} {1:.2f} {2:.2f} 0 1 0 0.2 0 force\n".format(xi - 1, yi - 1, zi))
        zi += t
    fp.close()


# 坐标获取
f1 = open("point.txt", "r")  # f1存储坐标
list1 = []
for line in f1.readlines():
    line = line.strip('\n')  # \n是换行符
    list1.append(line.split(','))
f1.close()
set_y = 30
count = 0
for i in range(len(list1)):
    set_x = int(list1[i][0])
    set_z = int(list1[i][1])
    block(set_x, set_y, set_z)
    count += 1
