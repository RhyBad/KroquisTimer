import os
from typing import List, Callable

from model.KroquisItem import KroquisItem
from model.SaveData import SaveData
from util.SaveManager import SaveManager

temp_image_file1 = os.path.dirname(os.path.abspath(__file__)) + r"\..\..\resource\sign.png"
temp_image_file2 = os.path.dirname(os.path.abspath(__file__)) + r"\..\..\resource\wink.png"
temp_image_file3 = os.path.dirname(os.path.abspath(__file__)) + r"\..\..\resource\character_sheet.jpg"


class MainViewModel:
    def __init__(self):
        self._save_manager = SaveManager()
        self._kroquis_list: List[KroquisItem] = []
        self._kroquis_list_observers: List[Callable[[List[KroquisItem]], None]] = []

    @property
    def kroquis_list(self) -> List[KroquisItem]:
        return self._kroquis_list

    @kroquis_list.setter
    def kroquis_list(self, value: List[KroquisItem]):
        self._kroquis_list = value
        for callback in self._kroquis_list_observers:
            callback(self._kroquis_list)

    def load_data(self):
        save_data = self._save_manager.load()
        self.kroquis_list = save_data.kroquis_list

    def save_data(self, kroquis_item_list: List[KroquisItem]):
        save_data = SaveData()
        save_data.kroquis_list = kroquis_item_list

        self._save_manager.save(save_data)

    def observe_kroquis_list(self, callback: Callable[[List[KroquisItem]], None]):
        self._kroquis_list_observers.append(callback)
