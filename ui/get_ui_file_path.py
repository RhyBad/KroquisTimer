import os
import sys


def get_ui_file_path(file_name: str) -> str:
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    if getattr(sys, 'frozen', False):
        base_path = os.path.join(base_path, "ui")
    return os.path.join(base_path, file_name)
