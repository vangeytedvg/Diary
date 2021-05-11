# Main Entry point of Diary application
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QMessageBox
from PyQt5.QtGui import QFont, QTextCursor, QTextListFormat, QFont
from PyQt5.QtCore import QDate, QDateTime, QFile, QTime, QSettings, QByteArray

from frmMain import Ui_MainWindow
from utilities import dvgFileUtils
from utilities.setting import Settings

class Diary(QMainWindow, Ui_MainWindow):

    def __init__(self):

        # instance attributes
        self._active_file = None
        self._active_date = None
        self._editorDirty = False
        self._isDirty = False

        super(Diary, self).__init__()
        self.setupUi(self)

        self.loadsettings()

        # Some more ui related stuff
        self.cursor = QTextCursor(self.txtDiary.document())
        self.txtDiary.setAutoFormatting(QTextEdit.AutoAll)
        font = QFont('Arial', 12)
        self.txtDiary.setFont(font)

        # methods
        self.load_diary(QDate.currentDate())
        # Make sure no diary entries can be made for future dates
        self.calendarWidget.setMaximumDate(QDate.currentDate())
        # self.txtDiary.textChanged.connect(self.setdirty)

        # signals
        self.txtDiary.cursorPositionChanged.connect(self.show_cursor_position)
        self.calendarWidget.clicked[QDate].connect(self.load_diary)
        self.calendarWidget.selectionChanged.connect(self.save_changes)
        # actions
        self.action_Add.triggered.connect(self.add_new_file)
        self.action_Add.setEnabled(False)
        self.actionSave.triggered.connect(self.save_changes)
        self.actionInsert_bulleted_list.triggered.connect(self.insert_bulleted_list)
        self.actionInsert_numbered_list.triggered.connect(self.insert_numbered_list)
        self.actionBold.triggered.connect(self.set_fontbold)
        self.actionItalic.triggered.connect(self.set_fontitalic)
        # shorthand actions
        self.actionCut.triggered.connect(self.txtDiary.cut)
        self.actionCopy.triggered.connect(self.txtDiary.copy)
        self.actionPaste.triggered.connect(self.txtDiary.paste)

    def set_fontbold(self):
        """
        Bold
        """
        if self.txtDiary.fontWeight() == QFont.Bold:
            self.txtDiary.setFontWeight(QFont.Normal)
        else:
            self.txtDiary.setFontWeight(QFont.Bold)

    def set_fontitalic(self):
        """
        Italic
        """
        state = self.txtDiary.fontItalic()
        self.txtDiary.setFontItalic(not state)

    def insert_bulleted_list(self):
        """
        Insert a bulleted list at the cursor position
        """
        cursor = self.txtDiary.textCursor()
        cursor.insertList(QTextListFormat.ListDisc)

    def insert_numbered_list(self):
        """
        Insert a numbered list 
        """
        cursor = self.txtDiary.textCursor()
        cursor.insertList(QTextListFormat.ListDecimal)

    def show_cursor_position(self):
        """
        Shows the line and column position
        """
        cursor = self.txtDiary.textCursor()
        self.statusbar.showMessage(f"Line {cursor.blockNumber()+1} | Column {cursor.columnNumber()}")

    def setdirty(self):
        """
        Handle changes in the editor
        """
        self._isDirty = True

    def save_changes(self):
        if QFile(self._active_file).exists():
            # Save our active file
            print(self._active_file)
            with open(self._active_file, 'w') as my_file:
                my_file.write(self.txtDiary.toHtml())
        else:
            # Clear the text field
            self.txtDiary.clear()

    def load_diary(self, dateedit):
        """
        Opens a diary day file if it exists.  If it does not exist
        the add new item button will be enabled.
        """
        # Create date object and create a filename based on the
        # dateedit parameter.
        file_name = str(QDate(dateedit).toPyDate())
        file_name = file_name.replace("-", "") + ".html"
        self._active_file = file_name
        self._active_date = QDate(dateedit)

        myFile = QFile(file_name)
        if not myFile.exists():
            self.action_Add.setEnabled(True)
            self.statusbar.showMessage(file_name + " **")
            self.txtDiary.clear()
            return

        self.action_Add.setEnabled(False)
        self.statusbar.showMessage(self._active_file)
        with open(file_name, 'r') as f:
            self.txtDiary.setHtml(f.read())
        self._editorDirty = True
        self.txtDiary.moveCursor(QTextCursor.End)
        # self.cursor.beginEditBlock()
        # self.cursor.insertBlock()
        # self.txtDiary.setFontPointSize(int(12))
        #self.txtDiary.insertHtml(QTime.currentTime().toString() + " : ")
        # self.cursor.endEditBlock()

        self.txtDiary.setFocus()

    def add_new_file(self):
        """
        Create a file with the selected date as name
        """
        answer = dvgFileUtils.ask(title="Diary",
                                  msg="Entry",
                                  explain="Create a new page?")
        if answer == QMessageBox.Ok:
            self.create_new_file(file=self._active_file,
                                 date=self._active_date)
            self.load_diary(self._active_date)
            self.cursor.setPosition(0)
            self.cursor.insertBlock()
            self.cursor.insertHtml(f"<h1>Diary entry {self._active_date.toString()}<br />")
            self.cursor.insertHtml("<h2>Today's events</h2><br />")
            self.cursor.setPosition(0)
        else:
            print("ko")

    def create_new_file(self, file="undefined", date="no date", cursor=None):
        """
        Generate a new diary file
        """
        myFile = QFile(file)
        if not myFile.exists():
            with open(file, "w") as f:
                f.write("")
        return

    """
    SETTINGS SECTION
    """

    def closeEvent(self, event):
        """
            Overrides the base close event
        :param event: event to override
        :return: nothing
        """
        mySettings = Settings(self, "DenkaTech", "KDiary")
        mySettings.save_form_settings("mainwindow", "frm_main/geometry")
        self.savesettings()
        self.save_changes()

    def savesettings(self):
        """
            Save settings to the registry (windows) or setting file (linux)
        :return: nothing
        """
        settings = QSettings("DenkaTech", "KDiary")
        settings.beginGroup("mainwindow")
        settings.setValue("frm_main/geometry", self.saveGeometry())
        settings.setValue("frm_main/state", self.saveState())
        settings.endGroup()

    def loadsettings(self):
        """
            Load the settings from the registry (windows) or settings file (linux)
        :return: nothing
        """
        settings = QSettings("DenkaTech", "KDiary")
        settings.beginGroup("mainwindow")
        self.restoreState(settings.value("frm_main/state", QByteArray()))
        self.restoreGeometry(settings.value("frm_main/geometry", QByteArray()))
        settings.endGroup()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = Diary()
    main_form.show()
    sys.exit(app.exec_())
