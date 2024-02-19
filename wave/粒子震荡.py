"""
@author: 北山_Besson
"""

import librosa
import math
import os

# 音频重采样
samples, sr = librosa.load(r"test.wav", sr=16000)  # 读取音频
print(len(samples), sr)
list1 = []

for i in range(0, len(samples), 80):
    list1.append(str(samples[i]))


# for循环的步长计算：总行数/（总时长（秒）/0.05秒*10)

# 洞洞波函数（竖着的粒子圆）
def cycle_y(x, y, z, R, fp):
    for i in range(0, 360, 10):
        yi = R * math.sin(math.radians(i))
        xi = R * math.cos(math.radians(i))
        fp.write(
            "particle end_rod {0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} 0 0.4 0 force\n".format(x, y, z, xi, yi))


n = 0
x = z = 0
count = 0
num = 10
dir_name = "lzzd"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

name = str(abs(n))
fp = open(dir_name + "\\" + name + ".mcfunction", "w")
for i in range(len(list1)):
    y1 = y2 = 200
    z -= 1 / num
    R = abs(float(list1[i])) * 10
    cycle_y(x, y1, z, R, fp)
    if (i + 1) % num == 0:
        count += 1
        fp.write("schedule function 1:{0} 1t\n".format(count))
        fp.close()
        n += 1
        name = str(abs(n))
        fp = open(dir_name + "\\" + name + ".mcfunction", "w")
fp.close()
