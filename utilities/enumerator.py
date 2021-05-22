""" Collection of enumerations """
from enum import Enum


class WarningLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3


class SlideMode(Enum):
    OPEN = 1
    CLOSE = 2
