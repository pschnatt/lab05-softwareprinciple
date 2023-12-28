from rabbit import *
from christmasTree import *


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w.show()
    w2.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())