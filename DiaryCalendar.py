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
        filename = fm.make_diary_filename(date.year(), date.month(), date.day())
        if fm.page_exists(filename):
            # We have a diary entry for this date, let the user know
            painter.save()
            painter.setPen(Qt.darkGreen)
            painter.drawEllipse(rect)
            painter.setPen(Qt.green)
            painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            QCalendarWidget.paintCell(self, painter, rect, date)
