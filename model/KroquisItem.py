import json
from types import SimpleNamespace
from typing import Any

from util.toJSON import SerializableObject


class KroquisItem(SerializableObject):
    def __init__(self, time: int, file_path: str):
        self.time = time
        self.file_path = file_path

    @staticmethod
    def fromJson(data: str) -> 'KroquisItem':
        obj = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        return KroquisItem.fromObj(obj)

    @staticmethod
    def fromObj(obj: Any) -> 'KroquisItem':
        return KroquisItem(time=obj.time, file_path=obj.file_path)
