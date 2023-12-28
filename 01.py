from christmasTree import *  
from rabbit import *  
from Starry import *


def main():
  app = QApplication(sys.argv)
  w1 = Simple_drawing_window1
  w2 = Simple_drawing_window2
  w3 = Simple_drawing_window3

  w1.show()
  w2.show()
  w3.show()

  return app.exec()

if __name__ == "__main__":
  sys.exit(main())