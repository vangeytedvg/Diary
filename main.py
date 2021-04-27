# Main Entry point of Diary application
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QMessageBox
from PyQt5.QtGui import QFont, QTextCursor, QTextListFormat
from PyQt5.QtCore import QDate, QDateTime, QFile

from frmMain import Ui_MainWindow
from utilities import dvgFileUtils
from utilities import editor


class Diary(QMainWindow, Ui_MainWindow):

    def __init__(self):

        # instance attributes
        self._active_file = None
        self._active_date = None

        super(Diary, self).__init__()
        self.setupUi(self)

        # Some more ui related stuff
        self.cursor = QTextCursor(self.txtDiary.document())
        self.txtDiary.setAutoFormatting(QTextEdit.AutoAll)
        font = QFont('Arial', 12)
        self.txtDiary.setFont(font)

        # methods
        self.load_diary(QDate.currentDate())
        # Make sure no diary entries can be made for future dates
        self.calendarWidget.setMaximumDate(QDate.currentDate())

        # signals
        self.calendarWidget.clicked[QDate].connect(self.load_diary)
        self.action_Add.triggered.connect(self.add_new_file)
        self.action_Add.setEnabled(False)

        # self.cursor.insertBlock()
        # self.cursor.insertHtml("<h4>Hello World</h4>")
        # self.cursor.insertBlock()
        # self.cursor.insertList(QTextListFormat.ListDecimal)

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
            return

        self.action_Add.setEnabled(False)
        self.statusbar.showMessage(self._active_file)
        with open(file_name) as f:
            self.txtDiary.setHtml(f.read())

    def add_new_file(self):
        """
        Create a file with the selected date as name
        """
        answer = dvgFileUtils.ask(title="Diary",
                                  msg="Entry",
                                  explain="Create a new page?")
        if answer == QMessageBox.Ok:
            editor.create_new_file(file=self._active_file)
        else:
            print("ko")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = Diary()
    main_form.show()
    sys.exit(app.exec_())
