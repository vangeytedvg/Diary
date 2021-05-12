# Main Entry point of Diary application
import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QTextEdit, QMessageBox)
from PyQt5.QtPrintSupport import (QPrintDialog,
                                  QPrinter,
                                  QPrintPreviewDialog)
from PyQt5.QtGui import (QFont,
                         QTextCursor, QTextListFormat)
from PyQt5.QtCore import (QDate, QDateTime,
                          QFile, QTime,
                          QSettings, QByteArray)

from frmMain import Ui_MainWindow
from utilities import dvgFileUtils
from utilities.setting import Settings
from utilities.editor import EditorProxy

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

        self.ed = EditorProxy(self.txtDiary)

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
        self.action_Print.triggered.connect(self.print_preview)
        # delegated to the editor proxy
        self.actionInsert_bulleted_list.triggered.connect(self.ed.insert_bulleted_list)
        self.actionInsert_numbered_list.triggered.connect(self.ed.insert_numbered_list)
        self.actionBold.triggered.connect(self.ed.set_fontbold)
        self.actionItalic.triggered.connect(self.ed.set_fontitalic)
        self.actionUnderline.triggered.connect(self.ed.set_fontunderline)
        self.actionStrikethrough.triggered.connect(self.ed.set_fontstrikethrough)
        # shorthand actions
        self.actionCut.triggered.connect(self.txtDiary.cut)
        self.actionCopy.triggered.connect(self.txtDiary.copy)
        self.actionPaste.triggered.connect(self.txtDiary.paste)

    def print_preview(self):
        """
        Print preview
        """
        # Create an instance of the preview dialog
        preview = QPrintPreviewDialog()
        preview.paintRequested.connect(lambda prt: self.txtDiary.print_(prt))
        # show it
        preview.exec_()

    def show_cursor_position(self):
        """
        Shows the line and column position and sets the flags of the
        bold, italic, underline and strikethrough actions
        """

        fmt = self.txtDiary.currentCharFormat()

        # Bold
        if fmt.fontWeight() == QFont.Bold:
            self.actionBold.setChecked(True)
        else:
            self.actionBold.setChecked(False)
        # Italic
        self.actionItalic.setChecked(fmt.fontItalic())
        # underline
        self.actionUnderline.setChecked(fmt.fontUnderline())
        # strike through
        self.actionStrikethrough.setChecked(fmt.fontStrikeOut())

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
            # As long as we have no file, disable all the cut, paste etc controls
            self.EnableEditControls(False)
            self.action_Add.setEnabled(True)
            return

        self.action_Add.setEnabled(False)
        self.statusbar.showMessage(self._active_file)
        with open(file_name, 'r') as f:
            self.txtDiary.setHtml(f.read())
        self._editorDirty = True
        self.txtDiary.moveCursor(QTextCursor.End)
        self.txtDiary.setFocus()
        self.EnableEditControls(True)

    def EnableEditControls(self, state):
        """
        Enable or Disable actions
        param state, boolean
        """

        self.actionBold.setEnabled(state)
        self.actionItalic.setEnabled(state)
        self.actionUnderline.setEnabled(state)
        self.actionStrikethrough.setEnabled(state)
        self.actionCut.setEnabled(state)
        self.actionCopy.setEnabled(state)
        self.actionPaste.setEnabled(state)
        self.actionInsert_bulleted_list.setEnabled(state)
        self.actionInsert_numbered_list.setEnabled(state)
        self.action_insert_date.setEnabled(state)
        self.action_insert_time.setEnabled(state)
        self.actionSave.setEnabled(state)
        self.actionErase.setEnabled(state)
        self.actionUndo.setEnabled(state)
        self.actionRedo.setEnabled(state)
        self.action_Print.setEnabled(state)

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
