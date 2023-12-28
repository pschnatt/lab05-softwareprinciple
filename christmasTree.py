import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Christmas Tree Drawing")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        # Draw Christmas tree
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.setPen(QColor(139, 69, 19))  # Brown color for tree trunk
        p.setBrush(QColor(139, 69, 19))
        p.drawRect(490, 400, 20, 40)  # Move the tree trunk even further to the right

        p.setPen(QColor(0, 128, 0))  # Green color for tree
        p.setBrush(QColor(0, 128, 0))

        p.drawPolygon([
            QPoint(450, 300), QPoint(550, 300), QPoint(500, 200),
        ])

        p.drawPolygon([
            QPoint(450, 400), QPoint(550, 400), QPoint(500, 300),
        ])

        p.end()