from rabbit import *


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())