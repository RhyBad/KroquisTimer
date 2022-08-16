from PyQt5.QtWidgets import QMessageBox

from screen.main.KroquisListViewBinder import KroquisListViewBinder
from screen.main.MainViewModel import MainViewModel
from ui.MainWindow import MainWindow


class MainScreen:
    def __init__(self):
        self.window = MainWindow()
        self.viewBinder = KroquisListViewBinder(self.window.get_list_widget())
        self.viewModel = MainViewModel()

        self.__setup_ui()

    def __setup_ui(self):
        self.window.get_add_button().clicked.connect(self.button_add_clicked)
        self.window.get_delete_all_button().clicked.connect(self.button_delete_all_clicked)
        self.window.get_run_button().clicked.connect(self.button_run_clicked)

        self.window.observe_close_event(self.save_data)

    def show(self):
        self.viewModel.load_data()
        self.viewBinder.bind(self.viewModel.kroquis_list)
        self.window.show()

    def button_add_clicked(self):
        self.viewBinder.add_item()

    def button_delete_all_clicked(self):
        deleted_item = self.viewBinder.delete_selected_item()
        if deleted_item is None:
            QMessageBox.about(self.window, "message", "Please select an item.")

    def button_run_clicked(self):
        QMessageBox.about(self.window, "message", self.__get_debug_data())

    def save_data(self):
        print("Save data!")
        print(self.__get_debug_data())

    def __get_debug_data(self) -> str:
        result = ""
        item_list = self.viewBinder.get_kroquis_list()
        for item in item_list:
            result += "Path: " + item.file_path + "\n"
        return result
