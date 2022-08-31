import os.path

from PyQt5.QtWidgets import QWidget, QFileDialog


class ImageBrowser:
    recent_open_path = ""

    @staticmethod
    def open(widget: QWidget) -> str:
        if not os.path.exists(ImageBrowser.recent_open_path):
            ImageBrowser.recent_open_path = "./"

        open_result = QFileDialog.getOpenFileName(widget, 'Open image file', ImageBrowser.recent_open_path,
                                                  'Images (*.png *.jpg *.jpeg *.bmp)')

        image_path = open_result[0]
        ImageBrowser.recent_open_path = os.path.dirname(image_path)

        return image_path
