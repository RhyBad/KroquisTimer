import sys

from PyQt5.QtWidgets import *

from screen.main.MainScreen import MainScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainScreen = MainScreen()

    # Debug

    mainScreen.show()
    app.exec_()
