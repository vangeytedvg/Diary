from PyQt5.QtCore import Qt, QRectF, QDate
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QCalendarWidget
from fileman import FileManager as fm


class DiaryCalendar(QCalendarWidget):
    """
      Sublassed QCalendarWidget to enable painting dates with 
      an existing diary page.
      If a given date has a corresponding diary file, the code
      below will draw a circle arround that specific date.
      Because this is a dynamic internal function, if a file is deleted,
      or for that matter added for a given date, the circle is either removed
      or added.
    """
    myQColor = QColor(25, 30, 30)
    myQColorWE = QColor(25, 30, 40)
    myQColor_sel_bg = QColor(40, 172, 212)
    myQColor_sel_fg = QColor(255, 255, 255)
    myColorWEDay = QColor(168, 88, 50)

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        filename = fm.make_diary_filename(date.year(), date.month(), date.day())
        # if date.day() == QDate().currentDate().day():
        # print("today")
        if fm.page_exists(filename):
            # We have a diary entry for this date, let the user know
            painter.save()
            if date.dayOfWeek() > 5:
                # Weekend colors
                painter.fillRect(rect, self.myQColorWE)
                painter.setPen(self.myColorWEDay)
            else:
                painter.fillRect(rect, self.myQColor)
                painter.setPen(Qt.darkGreen)
            if self.selectedDate().day() == date.day():
                painter.setPen(self.myQColor_sel_fg)
                painter.fillRect(rect, self.myQColor_sel_bg)
            painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            QCalendarWidget.paintCell(self, painter, rect, date)
