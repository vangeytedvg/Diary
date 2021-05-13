from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QCalendarWidget
from fileman import FileManager as fm


class DiaryCalendar(QCalendarWidget):
    """
      Sublassed QCalendarWidget to enable painting dates with 
      an existing diary page.
    """

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        = str(date.year()) +
        if fm.page_exists_(filename):
            pass
        QCalendarWidget.paintCell(self, painter, rect, date)
