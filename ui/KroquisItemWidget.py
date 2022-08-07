import os

from PyQt5 import uic
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\KroquisItemWidget.ui"
form = uic.loadUiType(ui_file_path)[0]


class KroquisItemWidget(QWidget, form):
    def __init__(self):
        self.pixmap = QPixmap()

        super().__init__()
        self.setupUi(self)

    def load_image_from_file(self, file_path: str):
        self.pixmap.load(file_path)
        self.pixmap = self.pixmap.scaled(self.get_preview_image().size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.get_preview_image().setPixmap(self.pixmap)

    # region Components

    def get_index_text(self) -> QLabel:
        return self.indexText

    def get_preview_image(self) -> QLabel:
        return self.previewImage

    def get_time_edit(self) -> QTimeEdit:
        return self.timeEdit

    # endregion
