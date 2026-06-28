from enum import Enum, auto


class AppState(Enum):

    IDLE = auto()

    FOLDER_SELECTED = auto()

    SCANNING = auto()

    READY = auto()

    ORGANIZING = auto()

    FINISHED = auto()