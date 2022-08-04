import os

from PyQt5 import uic
from PyQt5.QtWidgets import *

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\MainWindow.ui"
form = uic.loadUiType(ui_file_path)[0]


class MainWindow(QMainWindow, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_push_button(self) -> QPushButton:
        return self.pushButton
