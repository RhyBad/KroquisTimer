import os
from typing import List, Callable

from model.KroquisItem import KroquisItem

temp_image_file1 = os.path.dirname(os.path.abspath(__file__)) + r"\..\..\resource\sign.png"
temp_image_file2 = os.path.dirname(os.path.abspath(__file__)) + r"\..\..\resource\wink.png"
temp_image_file3 = os.path.dirname(os.path.abspath(__file__)) + r"\..\..\resource\character_sheet.jpg"


class MainViewModel:
    def __init__(self):
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
        kroquis_items = [
            KroquisItem(0, temp_image_file1),
            KroquisItem(0, temp_image_file2),
            KroquisItem(0, temp_image_file3)
        ]
        self.kroquis_list = kroquis_items

    def observe_kroquis_list(self, callback: Callable[[List[KroquisItem]], None]):
        self._kroquis_list_observers.append(callback)
