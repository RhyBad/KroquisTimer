import os
from typing import List

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui

from common.Constants import Constants
from model.KroquisItem import KroquisItem
from ui.KroquisViewerWidget import KroquisViewerWidget

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\KroquisControllerWidget.ui"
form = uic.loadUiType(ui_file_path)[0]


class KroquisControllerWidget(QWidget, form):
    def __init__(self):
        self.viewer = KroquisViewerWidget()
        self.item_list: List[KroquisItem] = []
        self.current_item_index = 0

        super().__init__()
        self.setWindowTitle(Constants.controller_name)
        self.setupUi(self)

        self.get_previous_button().clicked.connect(self.on_previous_button_clicked)
        self.get_next_button().clicked.connect(self.on_next_button_clicked)

    def set_kroquis_list(self, kroquis_list: List[KroquisItem]):
        self.item_list = kroquis_list

    def change_image(self, index: int):
        last_index = len(self.item_list) - 1
        new_index = max(0, min(index, last_index))
        self.current_item_index = new_index

        # Update Buttons
        if self.current_item_index <= 0:
            self.get_previous_button().setDisabled(True)
        else:
            self.get_previous_button().setEnabled(True)
        if self.current_item_index >= last_index:
            self.get_next_button().setDisabled(True)
        else:
            self.get_next_button().setEnabled(True)

        # Update ImageViewer
        item = self.item_list[self.current_item_index]
        self.viewer.set_pixmap(QPixmap(item.file_path))

    def on_previous_button_clicked(self):
        self.change_image(self.current_item_index - 1)

    def on_next_button_clicked(self):
        self.change_image(self.current_item_index + 1)

    # region Inner Function Overrides

    def show(self) -> None:
        self.change_image(0)

        super().show()
        self.viewer.show()

    def hide(self) -> None:
        self.viewer.hide()
        super().hide()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.viewer.close()
        event.accept()

    # endregion

    # region Components

    def get_time_text(self) -> QLabel:
        return self.timeText

    def get_time_progress_bar(self) -> QProgressBar:
        return self.timeProgressBar

    def get_previous_button(self) -> QPushButton:
        return self.previousButton

    def get_play_button(self) -> QPushButton:
        return self.playButton

    def get_next_button(self) -> QPushButton:
        return self.nextButton

    # endregion
