from typing import List

from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from model.KroquisItem import KroquisItem
from ui.KroquisItemWidget import KroquisItemWidget


class KroquisListViewBinder:
    def __init__(self, list_widget: QListWidget):
        self.__list_widget = list_widget

    def bind(self, kroquis_list: List[KroquisItem]):
        self.__list_widget.clear()
        for item in kroquis_list:
            self.add_kroquis_item(item)

    def add_kroquis_item(self, item: KroquisItem):
        item_widget = KroquisItemWidget()
        item_widget.load_image_from_file(item.file_path)

        custom_widget_item = QListWidgetItem(self.__list_widget)
        custom_widget_item.setSizeHint(item_widget.sizeHint())

        self.__list_widget.addItem(custom_widget_item)
        self.__list_widget.setItemWidget(custom_widget_item, item_widget)

    def get_kroquis_list(self) -> List[KroquisItem]:
        result: List[KroquisItem] = []
        for i in range(self.__list_widget.count()):
            widget_item = self.__list_widget.item(i)
            item: KroquisItemWidget = self.__list_widget.itemWidget(widget_item)
            result.append(item.convert_to_kroquis_item())
        return result
