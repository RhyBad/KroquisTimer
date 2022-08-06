import sys

from PyQt5.QtWidgets import *

from ui.MainWindow import MainWindow


def button_add_clicked():
    QMessageBox.about(myWindow, "message", "Add Button Clicked")


def button_delete_all_clicked():
    QMessageBox.about(myWindow, "message", "Delete All Clicked")


def button_run_clicked():
    QMessageBox.about(myWindow, "message", "Run Button Clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MainWindow()

    myWindow.get_add_button().clicked.connect(button_add_clicked)
    myWindow.get_delete_all_button().clicked.connect(button_delete_all_clicked)
    myWindow.get_run_button().clicked.connect(button_run_clicked)

    myWindow.show()
    app.exec_()
