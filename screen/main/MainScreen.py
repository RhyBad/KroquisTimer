from PyQt5.QtWidgets import QMessageBox

from screen.controller.ControllerScreen import ControllerScreen
from screen.main.KroquisListViewBinder import KroquisListViewBinder
from screen.main.MainViewModel import MainViewModel
from ui.MainWindow import MainWindow


class MainScreen:
    def __init__(self):
        self.window = MainWindow()
        self.viewBinder = KroquisListViewBinder(self.window.get_list_widget())
        self.viewModel = MainViewModel()

        self.controller = ControllerScreen()

        self.__setup_ui()

    def __setup_ui(self):
        self.window.get_add_button().clicked.connect(self.__on_button_add_clicked)
        self.window.get_delete_all_button().clicked.connect(self.__on_button_delete_all_clicked)
        self.window.get_run_button().clicked.connect(self.__on_button_run_clicked)

        self.window.observe_close_event(self.__on_window_close)

        self.controller.close_event_listener = self.__on_controller_close

    def show(self):
        self.viewModel.load_data()
        self.viewBinder.bind(self.viewModel.kroquis_list)
        self.window.show()

    def __on_button_add_clicked(self):
        self.viewBinder.add_item()

    def __on_button_delete_all_clicked(self):
        deleted_item = self.viewBinder.delete_selected_item()
        if deleted_item is None:
            QMessageBox.about(self.window, "message", "아이템 하나를 선택해 주세요.")

    def __on_button_run_clicked(self):
        item_list = self.viewBinder.get_kroquis_list()

        if len(item_list) <= 0:
            QMessageBox.about(self.window, "message", "아이템을 최소 하나 추가해주세요.")
            return

        self.controller.set_kroquis_list(item_list)
        self.controller.show()

        self.window.hide()

    def __on_window_close(self):
        kroquis_item_list = self.viewBinder.get_kroquis_list()
        self.viewModel.save_data(kroquis_item_list)

    def __on_controller_close(self):
        self.window.show()

    def __get_debug_data(self) -> str:
        result = ""
        item_list = self.viewBinder.get_kroquis_list()
        for item in item_list:
            result += "JSON: " + item.toJSON() + "\n"
        return result
