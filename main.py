import os
import sys

from PyQt5.QtWidgets import *

from ui.KroquisItemWidget import KroquisItemWidget
from ui.MainWindow import MainWindow


def button_add_clicked():
    QMessageBox.about(myWindow, "message", "Add Button Clicked")


def button_delete_all_clicked():
    QMessageBox.about(myWindow, "message", "Delete All Clicked")


def button_run_clicked():
    QMessageBox.about(myWindow, "message", "Run Button Clicked")


def add_kroquis_item(file_path: str):
    list_widget = myWindow.get_list_widget()

    item_widget = KroquisItemWidget()
    item_widget.load_image_from_file(file_path)

    custom_widget_item = QListWidgetItem(list_widget)
    custom_widget_item.setSizeHint(item_widget.sizeHint())

    list_widget.addItem(custom_widget_item)
    list_widget.setItemWidget(custom_widget_item, item_widget)


temp_image_file1 = os.path.dirname(os.path.abspath(__file__)) + r"\resource\sign.png"
temp_image_file2 = os.path.dirname(os.path.abspath(__file__)) + r"\resource\wink.png"
temp_image_file3 = os.path.dirname(os.path.abspath(__file__)) + r"\resource\character_sheet.jpg"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MainWindow()

    myWindow.get_add_button().clicked.connect(button_add_clicked)
    myWindow.get_delete_all_button().clicked.connect(button_delete_all_clicked)
    myWindow.get_run_button().clicked.connect(button_run_clicked)

    temp_image_files = [temp_image_file1, temp_image_file2, temp_image_file3]

    for temp_image_file in temp_image_files:
        add_kroquis_item(temp_image_file)

    myWindow.show()
    app.exec_()
