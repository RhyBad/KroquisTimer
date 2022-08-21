from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class ImageLoader:
    @staticmethod
    def load_image(label: QLabel, file_path: str):
        pixmap = QPixmap(file_path)
        pixmap = ImageLoader.resize_pixmap(label.size(), pixmap)

        label.setPixmap(pixmap)

    @staticmethod
    def resize_pixmap(size: QSize, pixmap: QPixmap) -> QPixmap:
        return pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
