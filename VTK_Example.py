from PyQt5 import QtCore, QtGui, QtWidgets
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import sys


class MyVTKView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("MyVTKView")
        self.resize(800, 600)

        self.centralWidget = QtWidgets.QWidget(self)
        self.gridlayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralWidget)
        self.gridlayout.addWidget(self.vtkWidget)
        self.setCentralWidget(self.centralWidget)
        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.ren.AddActor(actor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyVTKView()
    window.show()
    window.iren.Initialize()  # Need this line to actually show the render inside Qt
    
    sys.exit(app.exec_())