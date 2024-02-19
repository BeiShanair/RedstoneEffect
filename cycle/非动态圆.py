"""
@author: 北山_Besson
"""
import os
import math  # 数学库


def cycle(x, y, z, r):
    dirname = "circle"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    name = str(i)
    fp = open(dirname + "\\" + name + ".mcfunction", 'w')
    for j in range(360):  # 360次循环
        xi = x + r * math.cos(math.radians(j))
        zi = z + r * math.sin(math.radians(j))
        fp.write("particle firework {0:.2f} {1:.2f} {2:.2f} 0 0 0 0 1 force\n".format(xi, y, zi))
    fp.close()


x = 90
y = 30
z = 175  # 坐标获取可以按照小方块的方式来，这里犯懒了...
r = 5  # 半径
i = 0  # 这里没有用for循环，所以指定了i值
cycle(x, y, z, r)
