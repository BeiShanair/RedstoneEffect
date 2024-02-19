"""
@author: 北山_Besson
"""
import cmath  # 复数数学库
import math  # 数学库
import os  # 文件系统库


# 第一部分

def medline(x1, z1, x2, z2):  # 求中垂线
    a0 = 2 * (x2 - x1)
    b0 = 2 * (z2 - z1)
    c0 = x1 ** 2 - x2 ** 2 + z1 ** 2 - z2 ** 2
    return a0, b0, c0


def lines(x1, z1, x2, z2):  # 两点法求直线
    a1 = z1 - z2
    b1 = x2 - x1
    c1 = x1 * z2 - x2 * z1
    return a1, b1, c1


def point(x0, z0, x1, z1, x2, z2):  # 求中垂线和直线交点
    a0, b0, c0 = medline(x1, z1, x2, z2)
    a1, b1, c1 = lines(x0, z0, x1, z1)
    D = a0 * b1 - a1 * b0
    if D == 0:
        return None
    x = (b0 * c1 - b1 * c0) / D
    z = (a1 * c0 - a0 * c1) / D
    return x, z


# 第二部分

def soma(x1, z1, x2, z2, y, r, way, n1):
    global n
    global list2
    global list1
    global fp
    t = abs(z1 - z2)
    Ra = cmath.polar(complex(x1, z1))[1]  # 极坐标的样式是（r,θ），所以我们取第二个参数
    Rb = cmath.polar(complex(x2, z2))[1]
    Da = int(math.degrees(Ra))
    Db = int(math.degrees(Rb))
    c = abs(Da - Db)
    if way == "1":
        if Da > Db:
            c = 360 - c
            for i in range(Da, Da + c + 1):
                rad = math.radians(i)
                xi = cmath.rect(r, rad).real + list2[n1][0]
                zi = cmath.rect(r, rad).imag + list2[n1][1]

                # 这里是有一条扩散的末地烛粒子线和一条不扩散的烟花粒子线，下同
                # schedule对应的function文件名称记得要根据你的实际情况改

                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 3 force\n".format(xi, y, zi))
                fp.write("particle firework {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force\n".format(xi, y, zi))
                if int(c) // t != 0:
                    if i != Da and (i - Da) % (int(c) // t) == 0:
                        n += 1
                        fp.write("schedule function 1:{0} 1t\n".format(n))
                        fp.close()
                        fp = open(dir_name + "\\" + str(n) + ".mcfunction", "w")


        else:
            for i in range(Da, Da + c + 1):

                rad = math.radians(i)
                xi = cmath.rect(r, rad).real + list2[n1][0]
                zi = cmath.rect(r, rad).imag + list2[n1][1]
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 3 force\n".format(xi, y, zi))
                fp.write("particle firework {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force\n".format(xi, y, zi))
                if int(c) // t != 0:
                    if i != Da and (i - Da) % (int(c) // t) == 0:
                        n += 1
                        fp.write("schedule function 1:{0} 1t\n".format(n))
                        fp.close()
                        fp = open(dir_name + "\\" + str(n) + ".mcfunction", "w")


    else:

        if Da > Db:
            for i in range(Da, Da - c - 1, -1):

                rad = math.radians(i)
                xi = cmath.rect(r, rad).real + list2[n1][0]
                zi = cmath.rect(r, rad).imag + list2[n1][1]
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 3 force\n".format(xi, y, zi))
                fp.write("particle firework {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force\n".format(xi, y, zi))
                if int(c) // t != 0:
                    if i != Da and (Da - i) % (int(c) // t) == 0:
                        n += 1
                        fp.write("schedule function 1:{0} 1t\n".format(n))
                        fp.close()
                        fp = open(dir_name + "\\" + str(n) + ".mcfunction", "w")

        else:
            c = 360 - c

            for i in range(Da, Da - c - 1, -1):

                rad = math.radians(i)
                xi = cmath.rect(r, rad).real + list2[n1][0]
                zi = cmath.rect(r, rad).imag + list2[n1][1]
                fp.write("particle end_rod {0:.10f} {1:.10f} {2:.10f} 0 0 0 0.1 3 force\n".format(xi, y, zi))
                fp.write("particle firework {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force\n".format(xi, y, zi))
                if int(c) // t != 0:
                    if i != Da and (Da - i) % (int(c) // t) == 0:
                        n += 1
                        fp.write("schedule function 1:{0} 1t\n".format(n))
                        fp.close()
                        fp = open(dir_name + "\\" + str(n) + ".mcfunction", "w")


f1 = open("point.txt", "r")  # f1存储坐标
list1 = []
for line in f1.readlines():
    line = line.strip('\n')
    list1.append(line.split(','))
f1.close()
list2 = []

x0 = float(input("Px的值："))  # 输入第一个圆心的x坐标
z0 = float(input("Pz的值："))  # 输入第一个圆心的z坐标
list2.append([x0,z0])
for i in range(1, len(list1) - 1):
    x1, z1 = float(list1[i][0]), float(list1[i][1])
    x2, z2 = float(list1[i + 1][0]), float(list1[i + 1][1])
    x0, z0 = point(x0, z0, x1, z1, x2, z2)
    list2.append([x0,z0])

y = int(input("请输入y的值："))
way = input("请输入方向（0为顺时针，1为逆时针）：")

n = 0
dir_name = "soma3.0"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
fp = open(dir_name + "\\" + str(n) + ".mcfunction", "w")
for i in range(len(list1) - 1):
    x1 = float(list1[i][0]) - list2[i][0]
    z1 = float(list1[i][1]) - list2[i][1]
    x2 = float(list1[i + 1][0]) - list2[i][0]
    z2 = float(list1[i + 1][1]) - list2[i][1]
    r1 = math.sqrt(x1 ** 2 + z1 ** 2)

    soma(x1, z1, x2, z2, y, r1, way, i)

    if i < len(list1) - 2:
        r2_x = float(list1[i + 1][0]) - list2[i + 1][0]
        r2_z = float(list1[i + 1][1]) - list2[i + 1][1]
        r2 = math.sqrt(r2_x ** 2 + r2_z ** 2)
        oo_x = list2[i][0] - list2[i + 1][0]
        oo_z = list2[i][1] - list2[i + 1][1]
        oo = math.sqrt(oo_x ** 2 + oo_z ** 2)

        if -0.5 <= oo - r1 - r2 <= 0.5:
            if way == "1":
                way = "0"
            else:
                way = "1"
