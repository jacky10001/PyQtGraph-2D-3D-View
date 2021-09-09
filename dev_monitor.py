
import scipy.io
import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui


data3d = np.load("data3d.npy")

app = pg.mkQApp("GLVolumeItem Example")
w = gl.GLViewWidget()
w.opts['distance'] = 800
w.show()
w.setWindowTitle('pyqtgraph example: GLVolumeItem')
v = gl.GLVolumeItem(data3d)
v.translate(-50,-50,-100)
w.addItem(v)

def update():
    global v, data3d
    data3d = np.load("data3d.npy")
    v.setData(data3d)

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(500)

if __name__ == '__main__':
    pg.exec()