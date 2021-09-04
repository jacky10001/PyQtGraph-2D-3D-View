import glob
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import scipy.io
import cv2
import sys
import time
import matplotlib.pyplot as plt


## Create a GL View widget to display data
app = pg.mkQApp("GLSurfacePlot Example")
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=100)

x = np.linspace(-50, 50, 500)
y = np.linspace(-50, 50, 500)
d = (x.reshape(500,1)**2 + y.reshape(1,500)**2) * 0.1
d2 = d ** 0.5 + 0.5
## precompute height values for all frames
phi = np.arange(0, np.pi*2, np.pi/20.)
z = np.sin(d[np.newaxis,...] + phi.reshape(phi.shape[0], 1, 1)) / d2[np.newaxis,...]
print(x.shape)
print(y.shape)

cmap = plt.get_cmap('jet')

t1 = time.time()
minZ=np.min(z)
maxZ=np.max(z)
print(minZ, maxZ, z.shape)
rgba_img = cmap((z[0]*5-minZ)/(maxZ -minZ))
print(rgba_img.shape)
print(z.shape)

p4 = gl.GLSurfacePlotItem(x=x, y=y, colors=rgba_img, computeNormals=False)
w.addItem(p4)
t2 = time.time()
print(t2-t1)

index = 0
def update():
    global p4, z, index
    p4.setData(z=z[index%z.shape[0]]*5)
    index += 1
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

if __name__ == '__main__':
    pg.exec()
