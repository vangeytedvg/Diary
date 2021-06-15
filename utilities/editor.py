from PyQt5.QtCore import QDate, QDateTime, QFile, QTime, Qt
from PyQt5.QtGui import QFont, QTextCursor, QTextListFormat, QFont
from PyQt5.QtWidgets import QTextEdit


class EditorProxy:
    """
    The editor class is a helper class that handles a lot of the manipulations
    and relieves the main class from these tasks. These actions restrict themselves
    to markup.  Saving, loading and creating are up to the main class.
    """

    def __init__(self, parent: QTextEdit):
        """
            Ctor
        :param parent:The parent here is the QTextEditor on any form
        """
        self.parent = parent

    def set_alignment_left(self):
        """
            Align Left
        """
        self.parent.setAlignment(Qt.AlignLeft)

    def set_alignment_right(self):
        """
            Align right
        """
        self.parent.setAlignment(Qt.AlignRight)

    def set_alignment_center(self):
        """
            Align center
        """
        self.parent.setAlignment(Qt.AlignCenter)

    def set_alignment_justify(self):
        """
            Justify text
        """
        self.parent.setAlignment(Qt.AlignJustify)

    def indent(self):
        """
            Left indent the text
        """
        cursor = self.parent.textCursor()
        # Check if something is selected
        if cursor.hasSelection():
            # get the line/block nr
            temp = cursor.blockNumber()
            # Move to last line of the selection
            cursor.setPosition(cursor.selectionEnd())
            # calculate range of selection
            diff = cursor.blockNumber() - temp
            # Go over all the selected lines
            for n in range(diff + 1):
                cursor.movePosition(QTextCursor.StartOfLine)
                # insert tab
                cursor.insertText("\t")
                # move back up
                cursor.movePosition(QTextCursor.Up)
        else:
            # There is no selection, simply insert a TAB
            cursor.movePosition(QTextCursor.StartOfLine)
            cursor.insertText("\t")

    def dedent(self):
        """
            Unindent the text
        """
        cursor = self.parent.textCursor()
        # Check if something is selected
        if cursor.hasSelection():
            # get the line/block nr
            temp = cursor.blockNumber()
            # Move to last line of the selection
            cursor.setPosition(cursor.selectionEnd())
            # calculate range of selection
            diff = cursor.blockNumber() - temp
            # Go over all the selected lines
            for n in range(diff + 1):
                self.handle_dedent(cursor)
                # move back up
                cursor.movePosition(QTextCursor.Up)
        else:
            # There is no selection, simply insert a TAB
            self.handle_dedent(cursor)

    def handle_dedent(self, cursor: QTextCursor):
        """
            Dedent the selection
        :param cursor: Current active cursor in unindent action
        """
        cursor.movePosition(QTextCursor.StartOfLine)
        # Grab the current line
        line = cursor.block().text()
        # Is the line starting with a TAB?
        if line.startswith("\t"):
            # Delete TAB
            cursor.deleteChar()
        else:
            # Delete all spaces until a non space character is met
            for char in line[:8]:
                if char != " ":
                    break
                cursor.deleteChar()


    def set_font_family(self, font):
        """
            Set the editors' font
        """
        self.parent.setCurrentFont(font)

    def set_font_family_default(self):
        """
            Set the editor's default font
        """
        font = QFont('Arial', 12)
        self.parent.setCurrentFont(font)

    def set_font_size(self, fontsize):
        """
            Change the font size
        """
        self.parent.setFontPointSize(fontsize)

    def set_fontbold(self):
        """
            Set or unset font Bold
        """
        if self.parent.fontWeight() == QFont.Bold:
            self.parent.setFontWeight(QFont.Normal)
        else:
            self.parent.setFontWeight(QFont.Bold)

    def set_fontitalic(self):
        """
            Set or unset font Italic
        """
        state = self.parent.fontItalic()
        self.parent.setFontItalic(not state)

    def set_fontunderline(self):
        """
            Set or unset font Underline
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

    def insert_heading(self, heading):
        """
            Set Heading type
        :param heading: 1 - 5 for different header format
        """
        fontsize = 0
        if heading == 0:
            font = QFont('Arial')
            self.parent.setCurrentFont(font)
            self.parent.setFontWeight(QFont.Normal)
            self.parent.setFontPointSize(12)
            self.parent.setFocus()
            return
        if heading == 1:
            fontsize = 40
        if heading == 2:
            fontsize = 35
        if heading == 3:
            fontsize = 30
        if heading == 4:
            fontsize = 25
        if heading == 5:
            fontsize = 20
        cursor = self.parent.textCursor()
        font = QFont('Arial')
        self.parent.setCurrentFont(font)
        self.parent.setFontWeight(QFont.Bold)
        self.parent.setFontPointSize(fontsize)
        self.parent.setFocus()

    def insert_bulleted_list(self):
        """
            Insert bulleted list
        """
        cursor = self.parent.textCursor()
        cursor.insertList(QTextListFormat.ListDisc)

    def insert_numbered_list(self):
        """
            Insert a numbered list
        """
        cursor = self.parent.textCursor()
        cursor.insertList(QTextListFormat.ListDecimal)

    def insert_date_text(self):
        """
            Insert current date
        """
        cursor = self.parent.textCursor()
        cursor.insertText(QDate().currentDate().toString())

    def insert_time_text(self):
        """
            Insert current time
        """
        cursor = self.parent.textCursor()
        cursor.insertText(QTime().currentTime().toString(Qt.DefaultLocaleShortDate))
