import os
import sys

from PyQt5.QtWidgets import *

from model.KroquisItem import KroquisItem
from ui.MainWindow import MainWindow


def button_add_clicked():
    QMessageBox.about(myWindow, "message", "Add Button Clicked")


def button_delete_all_clicked():
    QMessageBox.about(myWindow, "message", "Delete All Clicked")


def button_run_clicked():
    QMessageBox.about(myWindow, "message", "Run Button Clicked")


temp_image_file1 = os.path.dirname(os.path.abspath(__file__)) + r"\resource\sign.png"
temp_image_file2 = os.path.dirname(os.path.abspath(__file__)) + r"\resource\wink.png"
temp_image_file3 = os.path.dirname(os.path.abspath(__file__)) + r"\resource\character_sheet.jpg"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MainWindow()

    myWindow.get_add_button().clicked.connect(button_add_clicked)
    myWindow.get_delete_all_button().clicked.connect(button_delete_all_clicked)
    myWindow.get_run_button().clicked.connect(button_run_clicked)

    kroquis_items = [
        KroquisItem(0, temp_image_file1),
        KroquisItem(0, temp_image_file2),
        KroquisItem(0, temp_image_file3)
    ]

    for kroquis_item in kroquis_items:
        myWindow.add_kroquis_item(kroquis_item)

    myWindow.show()
    app.exec_()
