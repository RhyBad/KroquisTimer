from typing import Optional, Callable

from PyQt5.QtCore import QTimer, QObject, Qt


class Timer:
    time_format = '{:02d}:{:02d}'
    interval_secs = 0.01

    def __init__(self, parent: QObject):
        self.__is_running: bool = False
        self.__schedule_msecs: int = 0
        self.__current_msecs: int = 0

        self.on_change_listener: Optional[Callable[[], None]] = None

        self.__qtimer = QTimer(parent)
        self.__qtimer.setTimerType(Qt.PreciseTimer)
        self.__qtimer.timeout.connect(self.__on_every_msecs)

    def is_running(self) -> bool:
        return self.__is_running

    def start(self):
        if not self.__qtimer.isActive():
            self.__qtimer.start(int(self.interval_secs * 1000))

        self.__is_running = True

    def pause(self):
        self.__is_running = False

    def stop(self):
        self.__qtimer.stop()

    def set_schedule_time(self, msecs: int):
        self.__schedule_msecs = msecs
        self.__current_msecs = 0

    def get_schedule_time(self) -> str:
        return self.__get_time_string(self.__schedule_msecs)

    def get_elapsed_time(self) -> str:
        return self.__get_time_string(self.__current_msecs)

    def get_remaining_time(self) -> str:
        remaining_msecs = self.__schedule_msecs - self.__current_msecs
        return self.__get_time_string(remaining_msecs)

    def get_progress_percentage(self) -> float:
        if self.__schedule_msecs == 0:
            return 0

        return self.__current_msecs / self.__schedule_msecs

    def __on_every_msecs(self):
        if self.is_running():
            self.__current_msecs += self.interval_secs * 1000
            self.on_change_listener()

    @staticmethod
    def __get_time_string(msecs: int) -> str:
        secs = msecs // 1000
        m, s = divmod(secs, 60)
        return Timer.time_format.format(int(m), int(s))
