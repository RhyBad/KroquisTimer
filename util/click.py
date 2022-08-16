from PyQt5.QtCore import QObject, QEvent
from skimage.viewer.qt import Signal


def click(widget):
    class Filter(QObject):
        clicked = Signal()

        def eventFilter(self, obj, event):
            if obj == widget and event.type() == QEvent.MouseButtonPress:
                self.clicked.emit()
                return True
            return False

    event_filter = Filter(widget)
    widget.installEventFilter(event_filter)
    return event_filter.clicked