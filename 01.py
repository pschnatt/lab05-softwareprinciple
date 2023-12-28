import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QPixmap
from PySide6.QtCore import QPoint

from christmasTree import *  
from rabbit import *  
from Starry import *

class MainDrawingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        w1 = Simple_drawing_window1() 
        w2 = Simple_drawing_window2()
        w3 = Simple_drawing_window3() 

        layout.addWidget(w1)
        layout.addWidget(w2)
        layout.addWidget(w3)

        self.setWindowTitle('Main Drawing Window')
        self.show()

def main():
    app = QApplication(sys.argv)
    main_window = MainDrawingWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
