from typing import List

from model.KroquisItem import KroquisItem
from model.SaveData import SaveData
from util.SaveManager import SaveManager


class MainViewModel:
    def __init__(self):
        self._save_manager = SaveManager()
        self._kroquis_list: List[KroquisItem] = []

    @property
    def kroquis_list(self) -> List[KroquisItem]:
        return self._kroquis_list

    @kroquis_list.setter
    def kroquis_list(self, value: List[KroquisItem]):
        self._kroquis_list = value

    def load_data(self):
        save_data = self._save_manager.load()
        self.kroquis_list = save_data.kroquis_list

    def save_data(self, kroquis_item_list: List[KroquisItem]):
        save_data = SaveData()
        save_data.kroquis_list = kroquis_item_list

        self._save_manager.save(save_data)
