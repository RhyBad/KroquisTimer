from typing import List, Callable, Optional

from PyQt5.QtGui import QPixmap

from model.KroquisItem import KroquisItem
from ui.KroquisControllerWidget import KroquisControllerWidget
from ui.KroquisViewerWidget import KroquisViewerWidget


class ControllerScreen:
    def __init__(self):
        self.widget = KroquisControllerWidget()
        self.viewer = KroquisViewerWidget()

        self.item_list: List[KroquisItem] = []
        self.current_item_index = 0

        self.close_event_listener: Optional[Callable[[], None]] = None

        super().__init__()
        self.__setup_ui()

    def show(self):
        self.change_image(0)
        self.widget.show()
        self.viewer.show()

    def __setup_ui(self):
        self.widget.close_event_listener = self.__on_widget_close_event
        self.widget.get_previous_button().clicked.connect(self.__on_previous_button_clicked)
        self.widget.get_next_button().clicked.connect(self.__on_next_button_clicked)

    def __on_widget_close_event(self):
        self.viewer.close()
        self.close_event_listener()

    def __on_previous_button_clicked(self):
        self.change_image(self.current_item_index - 1)

    def __on_next_button_clicked(self):
        self.change_image(self.current_item_index + 1)

    def set_kroquis_list(self, kroquis_list: List[KroquisItem]):
        self.item_list = kroquis_list

    def change_image(self, index: int):
        last_index = len(self.item_list) - 1
        new_index = max(0, min(index, last_index))
        self.current_item_index = new_index

        # Update Buttons
        if self.current_item_index <= 0:
            self.widget.get_previous_button().setDisabled(True)
        else:
            self.widget.get_previous_button().setEnabled(True)
        if self.current_item_index >= last_index:
            self.widget.get_next_button().setDisabled(True)
        else:
            self.widget.get_next_button().setEnabled(True)

        # Update ImageViewer
        item = self.item_list[self.current_item_index]
        self.viewer.set_pixmap(QPixmap(item.file_path))
