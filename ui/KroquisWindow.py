import os

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from model.KroquisItem import KroquisItem
from util.ImageLoader import ImageLoader

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\KroquisWindow.ui"
form = uic.loadUiType(ui_file_path)[0]


class KroquisWindow(QWidget, form):
    def __init__(self):
        self.pixmap = QPixmap()
        self.file_path = ""

        super().__init__()
        self.setupUi(self)

    def load_image(self, kroquis_item: KroquisItem):
        image_file_path = kroquis_item.file_path

        ImageLoader.load_image(self.get_image(), image_file_path)

        self.file_path = image_file_path

    # region Inner Callback

    def resizeEvent(self, event):
        ImageLoader.load_image(self.get_image(), self.file_path)

    # endregion

    # region Components

    def get_image(self) -> QLabel:
        return self.image

    # endregion
