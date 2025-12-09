# %%

from utils import load_advent_of_code

data = load_advent_of_code(202509)

print(data)
# %%
import numpy as np

dd = np.zeros((len(data), len(data[0])))
# %%dd.sh

rsize = 0
for ii in range(len(data)):
    for jj in range(ii + 1, len(data)):
        xii, yii = [int(q) for q in data[ii].split(",")]
        xjj, yjj = [int(q) for q in data[jj].split(",")]
        newsize = (np.abs(xjj - xii) + 1) * (np.abs(yjj - yii) + 1)
        if newsize > rsize:
            rsize = newsize

print(rsize)
# %%
import matplotlib.pyplot as plt

xcoords = [int(line.split(",")[0]) for line in data]
ycoords = [int(line.split(",")[1]) for line in data]
plt.plot(xcoords, ycoords, marker=".")
plt.xlim(3500, 6200)
plt.ylim(60000, 70000)
plt.show()
# %%
xdiffs = np.array([xx2 - xx1 for xx2, xx1 in zip(xcoords[1:], xcoords[0:-1])])

# %%
yline_bottom = 48246
yline_top = 50331
xjj = 94803
rsize = 0
maxtop = 0
maxbot = 10000000
for ii in range(len(data)):
    xii, yii = [int(q) for q in data[ii].split(",")]
    if yii > yline_top and xii >= xjj:
        if yii > maxtop:
            maxtop = yii
        # print(xii, yii, "top")
    if yii < yline_bottom and xii >= xjj:
        if yii < maxbot:
            maxbot = yii
        # print(xii, yii, "bottom")
print(maxtop, maxbot)
for ii in range(len(data)):
    xii, yii = [int(q) for q in data[-ii].split(",")]
    if xii < 50000:
        yay = False
        if yii > yline_top and yii <= maxtop:
            yjj = yline_top
            newsize = (np.abs(xjj - xii) + 1) * (np.abs(yjj - yii) + 1)
            yay = True
        if yii < yline_bottom and yii >= maxbot:
            yjj = yline_bottom
            newsize = (np.abs(xjj - xii) + 1) * (np.abs(yjj - yii) + 1)
            yay = True
        if yay and newsize > rsize:
            bigx = xii
            bigy = yii
            print(bigx, bigy, newsize)
            rsize = newsize
        # print(xii, yii, "bottom")
print(rsize)

# %%
