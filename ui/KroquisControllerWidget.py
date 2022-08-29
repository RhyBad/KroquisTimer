import os
from typing import Callable, Optional

from PyQt5 import uic
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

from common.Constants import Constants

ui_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "KroquisControllerWidget.ui")
form = uic.loadUiType(ui_file_path)[0]


class KroquisControllerWidget(QWidget, form):
    def __init__(self):
        self.close_event_listener: Optional[Callable[[], None]] = None

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(Constants.controller_window_name)

        time_text_font = self.get_time_text().font()
        time_text_font.setPointSize(100)
        time_text_font.setBold(True)
        self.get_time_text().setFont(time_text_font)

    # region Inner Function Overrides

    def closeEvent(self, event: QCloseEvent):
        self.close_event_listener()
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
