# Main Entry point of Diary application
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit
from PyQt5.QtGui import QFont, QTextCursor, QTextListFormat
from PyQt5.QtCore import QDate, QDateTime, QFile

from frmMain import Ui_MainWindow
from utilities import dvgFileUtils


class Diary(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Diary, self).__init__()
        self.setupUi(self)
        # Some more ui related stuff
        self.cursor = QTextCursor(self.txtDiary.document())
        self.txtDiary.setAutoFormatting(QTextEdit.AutoAll)
        font = QFont('Arial', 12)
        self.txtDiary.setFont(font)
        self.load_diary(QDate.currentDate())
        self.calendarWidget.clicked[QDate].connect(self.load_diary)
        # self.cursor.insertBlock()
        #self.cursor.insertHtml("<h4>Hello World</h4>")
        # self.cursor.insertBlock()
        # self.cursor.insertList(QTextListFormat.ListDecimal)

    def load_diary(self, dateedit):
        """
        Opens a diary day file if it exists.  If it does not exist
        the add new item button will be enabled.
        """
        print(dateedit)
        # Create date object and create a filename
        t = str(QDate(dateedit).toPyDate())
        t = t.replace("-", "") + ".html"
        print(t)
        myFile = QFile(t)
        print(myFile)
        if not myFile.exists():
            print("bliber")
            return
        with open(t) as f:
            self.txtDiary.setHtml(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = Diary()
    main_form.show()
    sys.exit(app.exec_())
