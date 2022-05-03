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


# data = scipy.io.loadmat("Tomo.mat")["RI"]
# data = scipy.io.loadmat("phantom.mat")["RI"]
# data[data<1.38] = 0
# np.save("data.npy", data)
data = np.load("data.npy")
print(data.max())
print(data.min())

data[data<1.37] = 0
# data[(data<1.39) & (data>=1.37)] = 128
# data[data>=1.39] = 255

app = pg.mkQApp("GLVolumeItem Example")
w = gl.GLViewWidget()
w.opts['distance'] = 800
w.setWindowTitle('pyqtgraph example: GLVolumeItem')

d2 = np.empty(data.shape + (4,), dtype=np.ubyte)
d2[..., 0] = data
d2[d2>=1.37] = np.array([255,255,255,128])
d2[..., 1] = d2[..., 0]
d2[..., 2] = d2[..., 0]
# d2[..., 3] = d2[..., 0]*0.2
d2[..., 3] = (d2[..., 3].astype(float) / 255.) **2 * 255

v = gl.GLVolumeItem(d2)
v.translate(-50,-50,-100)
w.addItem(v)

w.show()

if __name__ == '__main__':
    pg.exec()