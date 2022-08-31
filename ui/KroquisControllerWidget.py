from typing import Callable, Optional

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

from common.Constants import Constants
from ui.get_ui_file_path import get_ui_file_path

ui_file_path = get_ui_file_path("KroquisControllerWidget.ui")
form = uic.loadUiType(ui_file_path)[0]


class KroquisControllerWidget(QWidget, form):
    def __init__(self):
        self.close_event_listener: Optional[Callable[[], None]] = None

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(Constants.controller_window_name)
        self.__set_dark_theme()

        time_text_font = self.get_time_text().font()
        time_text_font.setPointSize(100)
        time_text_font.setBold(True)
        self.get_time_text().setFont(time_text_font)

    def __set_dark_theme(self):
        self.__set_text_color_white()
        self.__set_background_color_black()

        self.__set_button_color_dark(self.get_previous_button())
        self.__set_button_color_dark(self.get_play_button())
        self.__set_button_color_dark(self.get_next_button())

    @staticmethod
    def __set_button_color_dark(button: QPushButton):
        new_font = button.font()
        new_font.setBold(True)
        button.setFont(new_font)

        button.setStyleSheet("background-color : rgb(73, 69, 79); color : white")

    def __set_text_color_white(self):
        self.get_time_text().setStyleSheet("color : white")

    def __set_background_color_black(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)

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
