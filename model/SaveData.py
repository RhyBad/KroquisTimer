import json
from types import SimpleNamespace
from typing import List

from model.KroquisItem import KroquisItem
from util.toJSON import SerializableObject


class SaveData(SerializableObject):
    def __init__(self):
        self.kroquis_list: List[KroquisItem] = []

    @staticmethod
    def fromJSON(data: str) -> 'SaveData':
        obj = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

        result = SaveData()
        for item_obj in obj.kroquis_list:
            kroquis_item = KroquisItem.fromObj(item_obj)
            result.kroquis_list.append(kroquis_item)

        return result
