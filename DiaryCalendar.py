from PyQt5.QtCore import Qt, QRectF, QDate
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QCalendarWidget
from fileman import FileManager as fm
import csv


class DiaryCalendar(QCalendarWidget):
    """
      Sublassed QCalendarWidget to enable painting dates with
      an existing diary page.

    """
    # myQColor = QColor(25, 30, 30)
    # myQColor_day = QColor(255, 255, 255)
    # myQColorWE = QColor(25, 30, 40)
    # myQColor_sel_bg = QColor(30, 150, 22)
    # myQColor_sel_fg = QColor(255, 255, 255)
    # myColorWEDay = QColor(168, 88, 50)

    def __init__(self, file_path,
                 color_weekday_background,
                 color_weekday_foreground,
                 color_weekend_background,
                 color_weekend_foreground,
                 color_select_background,
                 color_select_foreground):
        self.holidays = []
        self.load_holidays()

        """
        Constructore override, need the path to the diary pages,
        so it is passed in the constructor.
        """
        self._file_path = file_path
        self.myQColor = QColor(color_weekday_background)
        self.myQColor_day = QColor(color_weekday_foreground)
        self.myColorWEDay = QColor(color_weekend_foreground)
        self.myQColorWE = QColor(color_weekend_background)
        self.myQColor_sel_bg = QColor(color_select_background)
        self.myQColor_sel_fg = QColor(color_select_foreground)

        super(DiaryCalendar, self).__init__()

    def load_holidays(self):
        """ Load holidays file and add easter day to the recovered data """
        with open('specialdays.csv', newline='') as holidays_file:
            reader = csv.DictReader(holidays_file)
            self.holidays = list(reader)

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        filename = self._file_path + "/" + fm.make_diary_filename(date.year(), date.month(), date.day())
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
                # normal day
                painter.fillRect(rect, self.myQColor)
                painter.setPen(self.myQColor_day)
            if self.selectedDate().day() == date.day():
                # ignore the above color when the date is selected by the user
                painter.setPen(self.myQColor_sel_fg)
                painter.fillRect(rect, self.myQColor_sel_bg)
            #painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignBottom, "text")
            painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            # Just a normal date, no diary entry
            QCalendarWidget.paintCell(self, painter, rect, date)
