"""
@author: 北山_Besson
"""
import math
import os


def trendssphere(x, y, z, r, R):
    global count
    global i
    global fp
    if r == 0:
        y1 = R * math.sin(math.radians(i))
        fp.write(
            "particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} 0.2 0 force\n".format(x, y, z, x,
                                                                                                    y1, z))
    else:
        for j in range(0, 360, 5):
            xi = r * math.cos(math.radians(j))
            zi = r * math.sin(math.radians(j))
            yi = R * math.sin(math.radians(i))  # 去掉前面的x,y,z
            fp.write(
                "particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} 0.2 0 force\n".format(x, y, z,
                                                                                                        xi, yi,
                                                                                                        zi))


# 球心坐标
set_x = 105
set_y = 30
set_z = 175
count = 0
R = 5
dirname = "trendssphere"
if not os.path.exists(dirname):
    os.mkdir(dirname)

fp = open(dirname + "\\" + str(count) + ".mcfunction", 'w')
for i in range(-90, 90, 5):
    r = R * math.cos(math.radians(i))
    trendssphere(set_x, set_y, set_z, r, R)

fp.close()
