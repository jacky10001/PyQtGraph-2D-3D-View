# -*- coding: utf-8 -*-
"""
Demonstrates GLVolumeItem for displaying volumetric data.

"""

## Add path to library (just for examples; you do not need this)

import time
import scipy.io
import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph import functions as fn


# data = np.load("data.npy")
data = np.zeros((444,444,444))
data[...,:80] = 1.355
data[...,80:200] = 1.365
data[...,200:] = 1.375
# print(data.max())
# print(data.min())

d2 = np.empty(data.shape + (4,), dtype=np.ubyte)
r = np.zeros(data.shape + (4,), dtype=np.ubyte)
r[..., 0] = 255
r[..., 3] = 2
g = np.zeros(data.shape + (4,), dtype=np.ubyte)
g[..., 1] = 255
g[..., 3] = 2
b = np.zeros(data.shape + (4,), dtype=np.ubyte)
b[..., 2] = 255
b[..., 3] = 2

t1 = time.time()
# data[data<1.35] = 0
data[(data<1.36) & (data>=1.35)] = 64
data[(data<1.37) & (data>=1.36)] = 128
data[(data<1.38) & (data>=1.37)] = 255

y, x, z = np.where(data==64)
d2[y, x , z, :] = r[y, x , z, :]

y, x, z = np.where(data==128)
d2[y, x , z, :] = g[y, x , z, :]

y, x, z = np.where(data==255)
d2[y, x , z, :] = b[y, x , z, :]

print("time:", time.time() - t1)

app = pg.mkQApp("GLVolumeItem Example")
w = gl.GLViewWidget()
w.opts['distance'] = 800
w.setWindowTitle('pyqtgraph example: GLVolumeItem')

v = gl.GLVolumeItem(d2)
v.translate(-50,-50,-100)
w.addItem(v)

w.show()

if __name__ == '__main__':
    pg.exec()