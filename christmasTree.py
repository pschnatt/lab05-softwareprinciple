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
        p.drawRect(190, 400, 20, 40)  # Tree trunk

        p.setPen(QColor(0, 128, 0))  # Green color for tree
        p.setBrush(QColor(0, 128, 0))


        p.drawPolygon([
            QPoint(150, 300), QPoint(250, 300), QPoint(200, 200),
        ])

        # p.drawPolygon([
        #     QPoint(50, 100), QPoint(350, 100), QPoint(200, 0),
        # ])

        # p.drawPolygon([
        #     QPoint(100, 200), QPoint(300, 200), QPoint(200, 100),
        # ])

        p.drawPolygon([
            QPoint(150, 400), QPoint(250, 400), QPoint(200, 300),
        ])

        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
