# -*- coding: utf-8 -*-
"""
Demonstrates a variety of uses for ROI. This class provides a user-adjustable
region of interest marker. It is possible to customize the layout and 
function of the scale/rotate handles in very flexible ways. 
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import scipy.io
import cv2

pg.setConfigOptions(imageAxisOrder='row-major')


arr = scipy.io.loadmat("D:\\GitHub\\DHT-Software\\data\\Data\\PhaseUnwrapping\\291.mat")["PU"][:1081,:1081]
arr = cv2.resize(arr, (500,500))

## create GUI
app = pg.mkQApp("ROI Examples")
w = pg.GraphicsLayoutWidget(show=True, size=(1000,800), border=True)
w.setWindowTitle('pyqtgraph example: ROI Examples')

w1 = w.addLayout(row=0, col=0)
v1a = w1.addViewBox(row=0, col=1, lockAspect=True)
v1b = w1.addViewBox(row=0, col=2, lockAspect=True)
img1a = pg.ImageItem(arr)
v1a.addItem(img1a)

img1b = pg.ImageItem()
# v1b.addItem(img1b)
v1a.disableAutoRange('xy')
v1b.disableAutoRange('xy')
v1a.autoRange()
v1b.autoRange()

g = pg.GridItem()
r4 = pg.ROI([0,0], [1,1], resizable=False, removable=True)
r4.addRotateHandle([1,0], [0.5, 0.5])
r4.addRotateHandle([0,1], [0.5, 0.5])
v1b.addItem(g)
v1b.addItem(r4)
img1b.setParentItem(r4)



# # rois.append(pg.RectROI([20, 20], [20, 20], pen=(0,9)))
# r1 = pg.LineROI([0, 60], [20, 80], width=5, pen=(1,9), removable=True)
# # rois.append(pg.TriangleROI([80, 75], 20, pen=(5, 9)))
# # rois.append(pg.MultiRectROI([[20, 90], [50, 60], [60, 90]], width=5, pen=(2,9)))
# # rois.append(pg.EllipseROI([60, 10], [30, 20], pen=(3,9)))
# # rois.append(pg.CircleROI([80, 50], [20, 20], pen=(4,9)))
# # rois.append(pg.LineSegmentROI([[110, 50], [20, 20]], pen=(5,9)))
# r2 = pg.PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=(6,9), closed=True, removable=True)

# def update(roi):
#     img1b.setImage(roi.getArrayRegion(arr, img1a), levels=(arr.min(), arr.max()))
#     r4.setSize((img1b.width(),img1b.height()))
#     v1b.autoRange()

# r1.sigRegionChanged.connect(update)
# r1.sigRemoveRequested.connect(lambda: v1a.removeItem(r1))
# r2.sigRegionChanged.connect(update)
# r2.sigRemoveRequested.connect(lambda: v1a.removeItem(r2))
# v1a.addItem(r1)
# v1a.addItem(r2)




rois = []
# rois.append(pg.RectROI([20, 20], [20, 20], pen=(0,9)))
rois.append(pg.LineROI([0, 60], [20, 80], width=5, pen=(1,9), removable=True))
# rois.append(pg.TriangleROI([80, 75], 20, pen=(5, 9)))
# rois.append(pg.MultiRectROI([[20, 90], [50, 60], [60, 90]], width=5, pen=(2,9)))
# rois.append(pg.EllipseROI([60, 10], [30, 20], pen=(3,9)))
# rois.append(pg.CircleROI([80, 50], [20, 20], pen=(4,9)))
# rois.append(pg.LineSegmentROI([[110, 50], [20, 20]], pen=(5,9)))
rois.append(pg.PolyLineROI([[80, 60], [90, 30], [60, 40]], pen=(6,9), closed=True, removable=True))

def update(roi):
    img1b.setImage(roi.getArrayRegion(arr, img1a), levels=(arr.min(), arr.max()))
    r4.setSize((img1b.width(),img1b.height()))
    v1b.autoRange()
    
for roi in rois:
    roi.sigRegionChanged.connect(update)
    v1a.addItem(roi)

update(rois[-1])

def remove(roi):
    v1a.removeItem(roi)
for roi in rois:
    roi.sigRemoveRequested.connect(remove)
r4.sigRemoveRequested.connect(lambda: v1b.removeItem(r4))


if __name__ == '__main__':
    pg.exec()
