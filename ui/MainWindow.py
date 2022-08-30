from typing import Callable, List

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *

from common.Constants import Constants
from ui.get_ui_file_path import get_ui_file_path

ui_file_path = get_ui_file_path("MainWindow.ui")
form = uic.loadUiType(ui_file_path)[0]


class MainWindow(QMainWindow, form):
    def __init__(self):
        self._close_event_observers: List[Callable[[], None]] = []

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(Constants.main_window_name)

    def observe_close_event(self, callback: Callable[[], None]):
        self._close_event_observers.append(callback)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        for callback in self._close_event_observers:
            callback()
        event.accept()

    # region Components

    def get_add_button(self) -> QPushButton:
        return self.addButton

    def get_delete_all_button(self) -> QPushButton:
        return self.deleteAllButton

    def get_run_button(self) -> QPushButton:
        return self.runButton

    def get_list_widget(self) -> QListWidget:
        return self.listWidget

    # endregion
