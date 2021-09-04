# -*- coding: utf-8 -*-
"""
    Animated 3D sinc function
"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys

## Define a scalar field from which we will generate an isosurface
def psi(i, j, k, offset=(25, 25, 50)):
    x = i-offset[0]
    y = j-offset[1]
    z = k-offset[2]
    th = np.arctan2(z, np.hypot(x, y))
    r = np.sqrt(x**2 + y**2 + z **2)
    a0 = 1
    ps = (1./81.) * 1./(6.*np.pi)**0.5 * (1./a0)**(3/2) * (r/a0)**2 * np.exp(-r/(3*a0)) * (3 * np.cos(th)**2 - 1)
    return ps


class Visualizer(object):
    def __init__(self):
        self.traces = dict()
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        # self.w.opts['distance'] = 40
        self.w.setCameraPosition(distance=40)
        self.w.setWindowTitle('pyqtgraph example: GLLinePlotItem')
        self.w.setGeometry(0, 110, 720, 600)
        self.w.show()

        # create the background grids
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.w.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.w.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.w.addItem(gz)


        print("Generating scalar field..")
        data = np.abs(np.fromfunction(psi, (50,50,100)))


        print("Generating isosurface..")
        verts, faces = pg.isosurface(data, data.max()/4.)

        md = gl.MeshData(vertexes=verts, faces=faces)

        colors = np.ones((md.faceCount(), 4), dtype=float)
        colors[:,3] = 0.2
        colors[:,2] = np.linspace(0, 1, colors.shape[0])
        md.setFaceColors(colors)
        m1 = gl.GLMeshItem(meshdata=md, smooth=False, shader='balloon')
        m1.setGLOptions('additive')

        # self.w.addItem(m1)
        m1.translate(-25, -25, -20)

        m2 = gl.GLMeshItem(meshdata=md, smooth=True, shader='balloon')
        m2.setGLOptions('additive')

        self.w.addItem(m2)
        m2.translate(-25, -25, -50)



# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    v = Visualizer()
    pg.exec()

