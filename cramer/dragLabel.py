from PyQt5 import QtWidgets, QtCore
from numpy import power, sqrt

class DragLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super(DragLabel, self).__init__(parent)
        self.x = 1000
        self.y = 1000

    def setCoordinates(self, qPoint):
        self.x = qPoint.x()
        self.y = qPoint.y()

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragLabel, self).mousePressEvent(event)

    def getLen(self, x, y):
        return sqrt( power(x - self.x, 2) + power(y - self.y, 2) )

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            len = self.getLen(self.pos().x(), self.pos().y())
            if len < 40:
                currPos = self.mapToGlobal(QtCore.QPoint(self.x, self.y))
            else:
                currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragLabel, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragLabel, self).mouseReleaseEvent(event)
