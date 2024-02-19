"""
@author: 北山_Besson
"""
import os
import math


def trendscycle(x, y, z, r):
    dirname = "trendscircle"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    name = str(n)
    fp = open(dirname + "\\" + name + ".mcfunction", 'w')
    for j in range(360):
        xi = r * math.cos(math.radians(j))
        zi = r * math.sin(math.radians(j))  # 去除前面的x和z
        fp.write("particle firework {0:.2f} {1:.2f} {2:.2f} {3:.2f} 0 {4:.2f} 0.2 0 force\n".format(x, y, z, xi,
                                                                                                    zi))  # 记得改填充方式
    fp.close()


x = 90
y = 30
z = 175
r = 5
n = 0
trendscycle(x, y, z, r)
