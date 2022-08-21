from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import *

from common.Constants import Constants


class KroquisViewerWidget(QWidget):
    _sizeHint = QSize()

    pixmap: QPixmap = None
    scaled: QPixmap = None
    ratio = Qt.KeepAspectRatio
    transformation = Qt.SmoothTransformation

    def __init__(self, pixmap=None):
        super().__init__()
        self.setWindowTitle(Constants.app_name)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.set_pixmap(pixmap)

    def update_scaled(self):
        if self.pixmap:
            self.scaled = self.pixmap.scaled(self.size(), self.ratio, self.transformation)
        self.update()

    def set_pixmap(self, pixmap):
        if self.pixmap != pixmap:
            self.pixmap = pixmap
            if isinstance(pixmap, QPixmap):
                self._sizeHint = pixmap.size()
            else:
                self._sizeHint = QSize()
            self.updateGeometry()
            self.update_scaled()

    def set_aspect_ratio(self, ratio):
        if self.ratio != ratio:
            self.ratio = ratio
            self.update_scaled()

    def set_transformation(self, transformation):
        if self.transformation != transformation:
            self.transformation = transformation
            self.update_scaled()

    # region Inner Function Overrides

    def sizeHint(self):
        return self._sizeHint

    def resizeEvent(self, event):
        self.update_scaled()

    def paintEvent(self, event):
        if not self.pixmap:
            return
        qp = QPainter(self)
        r = self.scaled.rect()
        r.moveCenter(self.rect().center())
        qp.drawPixmap(r, self.scaled)

    # endregion
