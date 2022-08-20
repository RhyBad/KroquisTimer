import os
import sys

from model.SaveData import SaveData

save_file_name = "SaveData.json"


class SaveManager:
    def __init__(self):
        self.save_file_path = os.path.join(self.__get_executable_path(), save_file_name)

    def save(self, data: SaveData):
        json_data = data.toJSON()
        with open(self.save_file_path, 'w') as f:
            f.write(json_data)

    def load(self) -> SaveData:
        with open(self.save_file_path, 'r') as f:
            raw_data = f.read()

        save_data = SaveData.fromJSON(raw_data)
        return save_data

    @staticmethod
    def __get_executable_path() -> str:
        application_path = ""
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        return application_path
