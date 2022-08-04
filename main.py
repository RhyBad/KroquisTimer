import sys

from PyQt5.QtWidgets import *

from ui.MainWindow import MainWindow


def btn_clicked():
    QMessageBox.about(myWindow, "message", "clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MainWindow()
    myWindow.get_push_button().setText("Kronii!")
    myWindow.get_push_button().clicked.connect(btn_clicked)

    myWindow.show()
    app.exec_()
