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

    def show(self):
        self.viewModel.load_data()
        self.viewBinder.bind(self.viewModel.kroquis_list)
        self.window.show()

    def button_add_clicked(self):
        QMessageBox.about(self.window, "message", "Add Button Clicked")

    def button_delete_all_clicked(self):
        QMessageBox.about(self.window, "message", "Delete All Clicked")

    def button_run_clicked(self):
        QMessageBox.about(self.window, "message", "Run Button Clicked")
