from PyQt5.QtCore import Qt, QRectF, QDate
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QCalendarWidget
from fileman import FileManager as fm
import csv


class DiaryCalendar(QCalendarWidget):
    """
      Sublassed QCalendarWidget to enable painting dates with
      an existing diary page.

    """

    def __init__(self, file_path,
                 color_weekday_background,
                 color_weekday_foreground,
                 color_weekend_background,
                 color_weekend_foreground,
                 color_select_background,
                 color_select_foreground):
        self.holidays = []
        self.load_holidays(QDate().currentDate().year())

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

    def __calc_easter(self, year):
        """ Returns Easter as a date object."""
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return QDate(year, month, day)

    def is_date_holiday(self, thedate):
        """ Check if the painted date is a holiday """
        return [holiday for holiday in self.holidays if holiday['Date'] == thedate]

    def load_holidays(self, year):
        """ Load holidays file and add easter day to the recovered data """
        with open('specialdays.csv', newline='') as holidays_file:
            reader = csv.DictReader(holidays_file)
            self.holidays = list(reader)
        # Add the date of easter to the holidays list
        easter = self.__calc_easter(year)
        day = str(easter.day()).zfill(2)
        month = str(easter.month()).zfill(2)
        easter = day + month
        # Convert to a dictionnary here
        element = {'Date': easter, 'Name': 'Easter'}
        self.holidays.append(element)

    def paintCell(self, painter, rect, date):
        """ Override the paint method """
        super(DiaryCalendar, self).paintCell(painter, rect, date)
        self.load_holidays(date.year())
        painter.fillRect(rect, self.myQColorWE)
        holiday_font = painter.font()
        holiday_font.setPixelSize(12)
        painter.setFont(holiday_font)

        painter.setRenderHint(QPainter.Antialiasing, True)
        filename = self._file_path + "/" + fm.make_diary_filename(date.year(), date.month(), date.day())

        # check if the drawing date is a holiday
        str_date = str(date.day()).zfill(2) + str(date.month()).zfill(2)
        hday = self.is_date_holiday(str_date)

        if fm.page_exists(filename):
            # We have a diary entry for this date, let the user know
            painter.fillRect(rect, self.myQColorWE)
            holiday_font = painter.font()
            holiday_font.setPixelSize(12)
            painter.setFont(holiday_font)
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
            # painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignBottom, "text")
            painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignCenter, str(date.day()))
            if self.is_date_holiday(str_date):
                holiday_font = painter.font()
                holiday_font.setPixelSize(9)
                painter.setFont(holiday_font)
                painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignBottom, hday[0]['Name'])
                holiday_font.setPixelSize(12)
                painter.setFont(holiday_font)
            painter.restore()
        else:
            # Just a normal date, no diary entry
            if self.is_date_holiday(str_date):
                painter.save()
                painter.fillRect(rect, self.myQColorWE)
                holiday_font = painter.font()
                holiday_font.setPixelSize(12)
                painter.setFont(holiday_font)
                QCalendarWidget.paintCell(self, painter, rect, date)
                painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignCenter, str(date.day()))
                holiday_font.setPixelSize(9)
                painter.setFont(holiday_font)
                painter.drawText(QRectF(rect), Qt.TextSingleLine | Qt.AlignBottom, hday[0]['Name'])
                holiday_font.setPixelSize(12)
                painter.setFont(holiday_font)
                painter.restore()
            else:
                QCalendarWidget.paintCell(self, painter, rect, date)


