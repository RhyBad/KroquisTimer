import sys

from PyQt5.QtWidgets import *


def __show_window():
    app = QApplication(sys.argv)

    window = QWidget()
    window.show()

    app.exec_()


if __name__ == '__main__':
    __show_window()
