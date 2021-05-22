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


class Headings(Enum):
    """ Values for the headings """
    HEAD_1 = 0
    HEAD_2 = 1
    HEAD_3 = 2
    HEAD_4 = 3
    HEAD_5 = 4
