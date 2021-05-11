from PyQt5.QtCore import QDate, QDateTime, QFile
from PyQt5.QtGui import QFont, QTextCursor, QTextListFormat, QFont
from PyQt5.QtWidgets import QTextEdit


class Editor:
    """
    The editor class is a helper class that handles a lot of the manipulations
    and relieves the main class from these tasks.
    """

    def __init__(self, parent):
        # The parent here is the QTextEditor on any form
        self.parent = parent

    def set_fontbold(self):
        """
        Bold
        """
        if self.parent.fontWeight() == QFont.Bold:
            self.parent.setFontWeight(QFont.Normal)
        else:
            self.parent.setFontWeight(QFont.Bold)

    def set_fontitalic(self):
        """
        Italic
        """
        state = self.parent.fontItalic()
        self.parent.setFontItalic(not state)
