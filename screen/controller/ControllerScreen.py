from typing import List, Callable, Optional

from model.KroquisItem import KroquisItem
from model.KroquisViewItem import KroquisViewItem
from ui.KroquisControllerWidget import KroquisControllerWidget
from ui.KroquisViewerWidget import KroquisViewerWidget
from util.Timer import Timer


class ControllerScreen:
    def __init__(self):
        self.widget = KroquisControllerWidget()
        self.viewer = KroquisViewerWidget()

        self.timer = Timer(self.widget)

        self.item_list: List[KroquisViewItem] = []
        self.current_item_index = 0

        self.close_event_listener: Optional[Callable[[], None]] = None

        super().__init__()
        self.__setup_ui()

    def show(self):
        self.__set_new_item_index(0)
        self.widget.show()
        self.viewer.show()
        self.timer.start()
        self.__update_ui()

    def __setup_ui(self):
        self.widget.close_event_listener = self.__on_widget_close_event
        self.widget.get_previous_button().clicked.connect(self.__on_previous_button_clicked)
        self.widget.get_next_button().clicked.connect(self.__on_next_button_clicked)
        self.widget.get_play_button().clicked.connect(self.__on_play_button_clicked)

        self.timer.on_change_listener = self.__on_timer_change

    def __on_widget_close_event(self):
        self.viewer.close()
        self.timer.stop()
        self.close_event_listener()

    def __on_previous_button_clicked(self):
        self.__set_new_item_index(self.current_item_index - 1)
        self.__update_ui()

    def __on_next_button_clicked(self):
        self.__set_new_item_index(self.current_item_index + 1)
        self.__update_ui()

    def __on_play_button_clicked(self):
        if self.timer.is_running():
            self.timer.pause()
        elif self.timer.get_progress_percentage() < 1 or (self.current_item_index < (len(self.item_list) - 1)):
            self.timer.start()

        self.__update_play_button_gui()

    def __update_play_button_gui(self):
        if self.timer.is_running():
            self.widget.get_play_button().setText("Pause")
        else:
            self.widget.get_play_button().setText("Resume")

    def __on_timer_change(self):
        if self.timer.get_elapsed_time() < self.timer.get_schedule_time():
            self.__update_time_gui()
        elif self.current_item_index < (len(self.item_list) - 1):
            self.__on_next_button_clicked()
        else:
            self.__update_time_gui()
            self.timer.pause()
            self.__update_play_button_gui()

    def set_kroquis_list(self, kroquis_list: List[KroquisItem]):
        self.item_list = list(map(lambda x: KroquisViewItem(x), kroquis_list))

    def __set_new_item_index(self, index: int):
        self.current_item_index = max(0, min(index, len(self.item_list) - 1))

    def __update_ui(self):
        self.__update_buttons()
        self.__update_image()
        self.__update_timer()
        self.__update_play_button_gui()

    def __update_buttons(self):
        # Update Buttons
        if self.current_item_index <= 0:
            self.widget.get_previous_button().setDisabled(True)
        else:
            self.widget.get_previous_button().setEnabled(True)

        if self.current_item_index >= (len(self.item_list) - 1):
            self.widget.get_next_button().setDisabled(True)
        else:
            self.widget.get_next_button().setEnabled(True)

    def __update_image(self):
        item = self.item_list[self.current_item_index]
        self.viewer.set_pixmap(item.get_pixmap())

    def __update_timer(self):
        item = self.item_list[self.current_item_index]
        self.timer.set_schedule_time(item.get_time() * 1000)
        self.__update_time_gui()

    def __update_time_gui(self):
        timer_str = self.timer.get_remaining_time()
        self.widget.get_time_text().setText(timer_str)

        progress_bar = self.widget.get_time_progress_bar()
        progress_bar_range = progress_bar.maximum() - progress_bar.minimum()
        percent = self.timer.get_progress_percentage()
        percent_int = int(percent * progress_bar_range)
        self.widget.get_time_progress_bar().setValue(percent_int)
