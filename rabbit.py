import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255,255,255))  
        p.drawEllipse(250, 150, 100, 150) 
        p.drawEllipse(280, 180, 20, 40)  
        p.drawEllipse(300, 180, 20, 40)  
        p.drawEllipse(270, 250, 20, 10)  
        p.drawEllipse(310, 250, 20, 10)  

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)  

        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())