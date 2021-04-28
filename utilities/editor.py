# Editor / file manipulations
from PyQt5.QtCore import QDate, QDateTime, QFile
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont, QTextCursor


def create_new_file(file="undefined", date="no date", cursor=None):
    """
    Generate a new diary file
    """
    myFile = QFile(file)
    if not myFile.exists():
        with open(file, "w") as f:
            f.write(f"<h1><span style='text-decoration:underline'>Diary date {date.toString()}</span></h1><br/>")
    return
