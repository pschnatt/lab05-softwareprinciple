import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Star(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit = QPixmap("images/mario.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPolygon([
            QPoint( 10, 100), QPoint(80,  110),
            QPoint(100,  50), QPoint(120, 110),
            QPoint(190, 100), QPoint(140, 150),
            QPoint(170, 210), QPoint(100, 180),
            QPoint( 30, 210), QPoint( 60, 150),
        ])

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

