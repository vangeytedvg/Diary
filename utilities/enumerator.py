""" Collection of enumerations """
from enum import Enum


class WarningLevel(Enum):
    """ This defines what colors will be shown in the warning """
    INFO = 1
    WARNING = 2
    ERROR = 3


class SlideMode(Enum):
    """ Modes for the sliding message """
    OPEN = 1
    CLOSE = 2



