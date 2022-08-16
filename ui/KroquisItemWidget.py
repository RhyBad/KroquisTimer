import os

from PyQt5 import uic
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from model.KroquisItem import KroquisItem
from util.click import click

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\KroquisItemWidget.ui"
form = uic.loadUiType(ui_file_path)[0]


class KroquisItemWidget(QWidget, form):
    def __init__(self):
        self.file_path = ""
        self.pixmap = QPixmap()

        super().__init__()
        self.setupUi(self)

        click(self.get_preview_image()).connect(self.__open_image_file)

    def load_image_from_file(self, file_path: str):
        self.pixmap.load(file_path)
        self.pixmap = self.pixmap.scaled(self.get_preview_image().size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.get_preview_image().setPixmap(self.pixmap)

        self.file_path = file_path

    def convert_to_kroquis_item(self) -> KroquisItem:
        q_time = self.get_time_edit().time()
        return KroquisItem(
            time=QTime(0, 0, 0).secsTo(q_time),
            file_path=self.file_path
        )

    def __open_image_file(self):
        open_result = QFileDialog.getOpenFileName(self, 'Open image file', './', 'Images (*.png *.jpg *.jpeg *.bmp)')
        file_path = open_result[0]
        self.load_image_from_file(file_path)

    # region Components

    def get_index_text(self) -> QLabel:
        return self.indexText

    def get_preview_image(self) -> QLabel:
        return self.previewImage

    def get_time_edit(self) -> QTimeEdit:
        return self.timeEdit

    # endregion
