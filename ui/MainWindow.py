import os

from PyQt5 import uic
from PyQt5.QtWidgets import *

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\MainWindow.ui"
form = uic.loadUiType(ui_file_path)[0]


class MainWindow(QMainWindow, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # region Components

    def get_add_button(self) -> QPushButton:
        return self.addButton

    def get_delete_all_button(self) -> QPushButton:
        return self.deleteAllButton

    def get_run_button(self) -> QPushButton:
        return self.runButton

    def get_list_widget(self) -> QListWidget:
        return self.listWidget

    # endregion
