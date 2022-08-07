import os

from PyQt5 import uic
from PyQt5.QtWidgets import *

from model.KroquisItem import KroquisItem
from ui.KroquisItemWidget import KroquisItemWidget

ui_file_path = os.path.dirname(os.path.abspath(__file__)) + r"\MainWindow.ui"
form = uic.loadUiType(ui_file_path)[0]


class MainWindow(QMainWindow, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def add_kroquis_item(self, item: KroquisItem):
        list_widget = self.get_list_widget()

        item_widget = KroquisItemWidget()
        item_widget.load_image_from_file(item.file_path)

        custom_widget_item = QListWidgetItem(list_widget)
        custom_widget_item.setSizeHint(item_widget.sizeHint())

        list_widget.addItem(custom_widget_item)
        list_widget.setItemWidget(custom_widget_item, item_widget)

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
