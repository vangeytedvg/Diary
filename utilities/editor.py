from PyQt5.QtCore import QDate, QDateTime, QFile
from PyQt5.QtGui import QFont, QTextCursor, QTextListFormat, QFont
from PyQt5.QtWidgets import QTextEdit


class EditorProxy:
    """
    The editor class is a helper class that handles a lot of the manipulations
    and relieves the main class from these tasks. These actions restrict themselves
    to markup.  Saving, loading and creating are up to the main class.
    """

    def __init__(self, parent: QTextEdit):
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

    def set_fontunderline(self):
        """
        Underline
        """
        state = self.parent.fontUnderline()
        self.parent.setFontUnderline(not state)

    def set_fontstrikethrough(self):
        """
        Strikethrough
        """
        fmt = self.parent.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.parent.setCurrentCharFormat(fmt)

    def insert_bulleted_list(self):
        """
        Insert a bulleted list at the cursor position
        """
        cursor = self.parent.textCursor()
        cursor.insertList(QTextListFormat.ListDisc)

    def insert_numbered_list(self):
        """
        Insert a numbered list 
        """
        cursor = self.parent.textCursor()
        cursor.insertList(QTextListFormat.ListDecimal)
