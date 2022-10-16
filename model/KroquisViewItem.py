from PyQt5.QtGui import QPixmap

from model.KroquisItem import KroquisItem


class KroquisViewItem:
    def __init__(self, kroquis_item: KroquisItem):
        self.__data: KroquisItem = kroquis_item
        self.__pixmap: QPixmap = QPixmap(self.__data.file_path)

    def get_pixmap(self) -> QPixmap:
        return self.__pixmap

    def get_time(self) -> int:
        return self.__data.time
