from util.toJSON import SerializableObject


class KroquisItem(SerializableObject):
    def __init__(self, time: int, file_path: str):
        self.time = time
        self.file_path = file_path
