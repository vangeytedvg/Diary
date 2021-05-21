#!/usr/bin/env python3
# Main Entry point of Diary application
import sys

from pathlib import Path
from os import remove
from enum import Enum

from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QTextEdit, QMessageBox, QLabel, QFrame)
from PyQt5.QtPrintSupport import (QPrintDialog,
                                  QPrinter,
                                  QPrintPreviewDialog)
from PyQt5.QtGui import (QFont,
                         QTextCursor, QTextListFormat, QColor)
from PyQt5.QtCore import (QDate, QDateTime,
                          QFile, QTime,
                          QSettings, QByteArray,
                          QPropertyAnimation, QEasingCurve)

from frmMain import Ui_MainWindow
from FrmSettings import FrmSettings
from utilities import dvgFileUtils
from utilities.setting import Settings
from utilities.editor import EditorProxy
from utilities.cloudbackup import *
from fileman import FileManager as fm
from DiaryCalendar import DiaryCalendar


class WarningLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3


class SlideMode(Enum):
    OPEN = 1
    CLOSE = 2


class Diary(QMainWindow, Ui_MainWindow):

    # These are class variables, the go with each copy of the class
    __diary_pages_path = ""
    __color_weekday_background = ""
    __color_weekday_foreground = ""
    __color_weekend_foreground = ""
    __color_weekend_background = ""
    __color_select_foreground = ""
    __color_select_background = ""
    __local_backup = False
    __local_backup_folder = ""
    __cloudBackup = False
    __backup_to_google = False
    __google_folder_id = ""
    __backup_to_other = False
    __last_backup_date = None
    __last_backup_time = None
    __backup_interval = 0
    __days_until_backup = 0
    __should_backup_now = False

    def __init__(self):

        # instance attributes
        self._active_file = None
        self._active_date = None
        self._editorDirty = False
        self._isDirty = False

        super(Diary, self).__init__()
        self.setupUi(self)
        self.config_status_bar()
        # configure statusbar
        self.loadsettings()
        self.frame_warning.setMaximumHeight(0)
        self.ed = EditorProxy(self.txtDiary)
        # Some more ui related stuff
        self.cursor = QTextCursor(self.txtDiary.document())
        self.txtDiary.setAutoFormatting(QTextEdit.AutoAll)
        font = QFont('Arial', 12)
        self.txtDiary.setFont(font)
        self.txtDiary.setEnabled(False)

        # Make sure no diary entries can be made for future dates
        self.calendarWidget = DiaryCalendar(self.__diary_pages_path,
                                            self.__color_weekday_background,
                                            self.__color_weekday_foreground,
                                            self.__color_weekend_background,
                                            self.__color_weekend_foreground,
                                            self.__color_select_background,
                                            self.__color_select_foreground)

        self.calendarWidget.setMaximumWidth(350)
        self.calendarWidget.setMaximumHeight(350)
        self.calendarWidget.setMaximumDate(QDate.currentDate())
        # make an option from this
        self.calendarWidget.setGridVisible(True)
        self.testFrame.addWidget(self.calendarWidget)

        # signals
        self.init_signal_handlers()

        # methods
        self.load_diary_page(QDate.currentDate())
        # Check if backup is needed
        if self.__should_backup_now:
            self.lbl_warning.setText("Please consider making a backup of your diary now!")
            self.drawer_slide("open", "", "")

    def drawer_slide(self, open_or_close: SlideMode, message: str, msg_type: WarningLevel):
        """
            Animate the message frame
        :return:
        """
        new_height = 0
        self.animation = QPropertyAnimation(self.frame_warning, b"maximumHeight")
        height = self.frame_warning.height()
        if open_or_close == SlideMode.OPEN:
            height = 0
            new_height = 200
            self.lbl_warning.setText(message)
            if msg_type == WarningLevel.INFO:
                self.frame_warning.setStyleSheet("background-color: rgba(118, 236, 0, 0.5);")
            if msg_type == WarningLevel.WARNING:
                self.frame_warning.setStyleSheet("background-color: rgba(193, 129, 0, 0.5);")
            if msg_type == WarningLevel.ERROR:
                self.frame_warning.setStyleSheet("background-color: rgba(255, 171, 230, 0.5;")
        elif open_or_close == SlideMode.CLOSE:
            height = 200
            new_height = 0
        # Now we are going to animate the transition
        self.animation.setDuration(250)
        self.animation.setStartValue(height)
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def config_status_bar(self):
        """
        Add labels to the statusbar for line, col and file name
        """
        self.lbl_line_nr_info = QLabel("LINE")
        self.lbl_line_nr = QLabel("0")
        self.lbl_line_nr.setFrameShadow(QFrame.Raised)
        self.lbl_line_nr.setFrameShape(QFrame.Panel)
        self.lbl_col_nr_info = QLabel("COL")
        self.lbl_col_nr = QLabel("0")
        self.lbl_col_nr.setFrameShadow(QFrame.Raised)
        self.lbl_col_nr.setFrameShape(QFrame.Panel)
        self.lbl_file_name_info = QLabel("File")
        self.lbl_file_name = QLabel("none")
        self.lbl_changed_info = QLabel("Changed")
        self.lbl_changed = QLabel("no")
        self.lbl_backup_days_info = QLabel("Next Backup in days")
        self.lbl_backup_days = QLabel("0")
        self.lbl_changed.setFrameShadow(QFrame.Raised)
        self.lbl_changed.setFrameShape(QFrame.Panel)
        self.lbl_file_name.setFrameShadow(QFrame.Raised)
        self.lbl_file_name.setFrameShape(QFrame.Panel)
        self.lbl_backup_days.setFrameShadow(QFrame.Raised)
        self.lbl_backup_days.setFrameShape(QFrame.Panel)
        self.statusbar.addPermanentWidget(self.lbl_line_nr_info)
        self.statusbar.addPermanentWidget(self.lbl_line_nr)
        self.statusbar.addPermanentWidget(self.lbl_col_nr_info)
        self.statusbar.addPermanentWidget(self.lbl_col_nr)
        self.statusbar.addPermanentWidget(self.lbl_file_name_info)
        self.statusbar.addPermanentWidget(self.lbl_file_name)
        self.statusbar.addPermanentWidget(self.lbl_changed_info)
        self.statusbar.addPermanentWidget(self.lbl_changed)
        self.statusbar.addPermanentWidget(self.lbl_backup_days_info)
        self.statusbar.addPermanentWidget(self.lbl_backup_days)

    def init_signal_handlers(self):
        """
        Connect the signals on our actions
        """
        self.txtDiary.cursorPositionChanged.connect(self.show_cursor_position)
        self.txtDiary.textChanged.connect(self.set_dirty)
        self.calendarWidget.clicked[QDate].connect(self.load_diary_page)
        self.calendarWidget.selectionChanged.connect(self.save_changes)
        # actions
        self.action_Add.triggered.connect(self.add_new_file)
        self.actionErase.triggered.connect(self.erase_diary_entry)
        self.actionSave.triggered.connect(self.save_changes)
        self.action_Print.triggered.connect(self.print_preview)
        self.action_Preferences.triggered.connect(self.open_settings)
        # delegated to the editor proxy
        self.actionInsert_bulleted_list.triggered.connect(self.ed.insert_bulleted_list)
        self.actionInsert_numbered_list.triggered.connect(self.ed.insert_numbered_list)
        self.actionBold.triggered.connect(self.ed.set_fontbold)
        self.actionItalic.triggered.connect(self.ed.set_fontitalic)
        self.actionUnderline.triggered.connect(self.ed.set_fontunderline)
        self.actionStrikethrough.triggered.connect(self.ed.set_fontstrikethrough)
        # shorthand actions
        self.actionUndo.triggered.connect(self.txtDiary.undo)
        self.actionRedo.triggered.connect(self.txtDiary.redo)
        self.actionCut.triggered.connect(self.txtDiary.cut)
        self.actionCopy.triggered.connect(self.txtDiary.copy)
        self.actionPaste.triggered.connect(self.txtDiary.paste)
        self.action_insert_date.triggered.connect(self.ed.insert_date_text)
        self.action_insert_time.triggered.connect(self.ed.insert_time_text)
        self.action_backup.triggered.connect(self._backup)
        self.btn_close_warning.clicked.connect(self.close_warning_box)

    def close_warning_box(self):
        self.drawer_slide("close", "", None)

    def open_settings(self):
        settings = FrmSettings(self)
        res = settings.exec_()
        self.loadsettings()
        self.calendarWidget.myQColor = QColor(self.__color_weekday_background)
        self.calendarWidget.myQColor_day = QColor(self.__color_weekday_foreground)
        self.calendarWidget.myColorWEDay = QColor(self.__color_weekend_foreground)
        self.calendarWidget.myQColorWE = QColor(self.__color_weekend_background)
        self.calendarWidget.myQColor_sel_bg = QColor(self.__color_select_background)
        self.calendarWidget.myQColor_sel_fg = QColor(self.__color_select_foreground)

    def backup(self, destination: Backup):
        """
        Perform the backup using Polymorphism!
        """
        if not destination:
            raise Excepion("No destination class set")

        try:
            # Zip the file and then send it to google. Note, we do not have
            # to pass any parameters here, they were already set in the
            # contructor call in the _backup method
            destination.zip_diary()
            result = destination.push_to_path()
            # TODO check contents of the result

            # save the date and time of the last backup to the config file
            mySettings = Settings(self, "DenkaTech", "KDiary")
            mySettings.save_setting("last_backup", "date", QDate.currentDate())
            mySettings.save_setting("last_backup", "time", QTime.currentTime())
            #mySettings.save_setting("last_backup", "date", QDate(2021, 5, 10))
            # Be sure to save the active diary entry
            self.save_changes()
            self.__should_backup_now = False
            self.drawer_slide(SlideMode.OPEN, f"Backup to Google Drive completed.  File name = {result}", WarningLevel.INFO)
        except FileNotFoundError:
            dvgFileUtils.warn(self, "IO Error",
                              "Path not found!",
                              destination._source_path)
        except NoDiaryPagesFound:
            dvgFileUtils.warn(self, "IO Error",
                              "No diary files found in",
                              destination._source_path)

    def _backup(self):
        """
        Make a backup to google drive or local.  The 'other' option
        is not yet implemented.
        """
        # Check what kind of backup to perform
        my_backup = None
        if self.__local_backup:
            # local backup
            my_backup = LocalBackup()
            # use polymorphism here
            self.backup(my_backup)
        if self.__backup_to_google:
            my_backup = GoogleBackup(self.__diary_pages_path,
                                     self.__google_folder_id)
            # use polymorphism here
            self.backup(my_backup)

    def set_dirty(self):
        """
        Flags when the text has been changed by the user.
        """
        self._isDirty = True
        self.lbl_changed.setText("yes")

    def print_preview(self):
        """
          Print preview
        :return: nothing
        """
        # Create an instance of the preview dialog
        preview = QPrintPreviewDialog()
        preview.paintRequested.connect(lambda prt: self.txtDiary.print_(prt))
        # show it
        preview.exec_()

    def erase_diary_entry(self):
        """
          Remove a selected diary page
        :return: nothing
        """
        answer = dvgFileUtils.ask(title="Diary",
                                  msg="Entry",
                                  explain="Delete the current page?")
        if answer == QMessageBox.Ok:
            remove(self._active_file)
            self.EnableEditControls(False)
            self.action_Add.setEnabled(True)
            self.txtDiary.clear()
            self.txtDiary.clearFocus()
            self.txtDiary.setEnabled(False)
            self._isDirty = False
            self.lbl_file_name.setText("not existing")
            self.lbl_changed.setText("no")
            self.drawer_slide(SlideMode.OPEN, "Page removed from disk", WarningLevel.WARNING)

    def show_cursor_position(self):
        """
          Shows the line and column position and sets the flags of the
          bold, italic, underline and strikethrough actions
          :return: nothing
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
        # position of the cursor
        cursor = self.txtDiary.textCursor()
        self.lbl_line_nr.setText(str(cursor.blockNumber() + 1))
        self.lbl_col_nr.setText(str(cursor.columnNumber()))

    def save_changes(self):
        """
          Save our active file.  If the file is inexisting, clear the content
          of the text editor.  Otherwise, when we jump to another date the
          old text remains visible, which may lead to user confusion.
        :return: nothing
        """
        if QFile(self._active_file).exists():
            with open(self._active_file, 'w') as my_file:
                my_file.write(self.txtDiary.toHtml())
            self._isDirty = False
            self.lbl_changed.setText("no")
            return
        self.txtDiary.clear()

    def load_diary_page(self, dateedit):
        """
          Opens a diary day file if it exists.  If it does not exist
          the add new item button will be enabled.
        :return: nothing
        """
        # Create date object and create a filename based on the
        # dateedit parameter.

        file_name = str(QDate(dateedit).toPyDate())
        file_name = self.__diary_pages_path + "/" + file_name.replace("-", "") + ".html"
        self._active_file = file_name
        self._active_date = QDate(dateedit)
        self.lbl_file_name.setText(file_name)

        if not fm.page_exists(file_name):
            self.action_Add.setEnabled(True)
            self.txtDiary.clear()
            # As long as we have no file, disable all the cut, paste etc controls
            self.EnableEditControls(False)
            self.action_Add.setEnabled(True)
            self.lbl_file_name.setText("not existing")
            self.lbl_changed.setText("no")
            return

        self.action_Add.setEnabled(False)
        with open(file_name, 'r') as f:
            self.txtDiary.setHtml(f.read())
        self._editorDirty = False
        self.txtDiary.moveCursor(QTextCursor.End)
        self.txtDiary.setFocus()
        self.EnableEditControls(True)
        self.lbl_changed.setText("no")

    def EnableEditControls(self, state):
        """
          Enable or Disable actions
        :param state, boolean
        """
        self.txtDiary.setEnabled(state)
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
        if state:
            self.txtDiary.setFocus()

    def add_new_file(self):
        """
          Create a file with the selected date as name
        :return: nothing
        """
        answer = dvgFileUtils.ask(title="Diary",
                                  msg="Entry",
                                  explain="Create a new page?")
        if answer == QMessageBox.Ok:
            self.create_new_file(file=self._active_file,
                                 date=self._active_date)
            self.load_diary_page(self._active_date)
            self.cursor.setPosition(0)
            self.cursor.insertBlock()
            self.cursor.insertHtml(f"<h1>Diary entry {self._active_date.toString()}<br />")
            self.cursor.insertHtml("<h2>Today's events</h2><br />")
            self.cursor.setPosition(0)

    def create_new_file(self, file="undefined", date="no date", cursor=None):
        """
          Generate a new diary file using the pathlib module, just like
          the unix touch command would do.
        :return: nothing
        """
        Path(file).touch()
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
        # Be sure to save the active diary entry
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
        # -- > this part needs to be migrated to the Settings class
        settings = QSettings("DenkaTech", "KDiary")
        settings.beginGroup("mainwindow")
        self.restoreState(settings.value("frm_main/state", QByteArray()))
        self.restoreGeometry(settings.value("frm_main/geometry", QByteArray()))
        settings.endGroup()
        # Document settings

        # color settings
        params = Settings(self, "DenkaTech", "KDiary")
        self.__diary_pages_path = params.load_setting("paths", "file_location")
        self.__color_weekday_background = params.load_setting("colors",
                                                              "weekday_background")
        self.__color_weekday_foreground = params.load_setting("colors",
                                                              "weekday_foreground")
        self.__color_weekend_foreground = params.load_setting("colors",
                                                              "weekend_foreground")
        self.__color_weekend_background = params.load_setting("colors",
                                                              "weekend_background")
        self.__color_select_foreground = params.load_setting("colors",
                                                             "select_foreground")
        self.__color_select_background = params.load_setting("colors",
                                                             "select_background")

        # Backup settings
        self.__local_backup = dvgFileUtils.str_to_bool(params.load_setting("backup",
                                                                           "backup_to_local_file"))
        self.__local_backup_folder = params.load_setting("backup",
                                                         "back_to_local_file_path")
        self.__cloudBackup = dvgFileUtils.str_to_bool(params.load_setting("backup",
                                                                          "backup_to_cloud"))
        self.__backup_to_google = dvgFileUtils.str_to_bool(params.load_setting("backup",
                                                                               "backup_to_google_drive"))
        self.__google_folder_id = params.load_setting("backup", "google_id")
        self.__backup_to_other = dvgFileUtils.str_to_bool(params.load_setting("backup",
                                                                              "backup_to_other"))
        self.__last_backup_date = QDate(params.load_setting_from_byte_array("last_backup", "date"))
        self.__last_backup_time = QTime(params.load_setting_from_byte_array("last_backup", "time"))
        self.__backup_interval = params.load_setting("backup",
                                                     "push_interval_days")

        self.__backup_interval = params.load_setting("backup", "push_interval_days")
        self.__days_until_backup = int(self.__backup_interval) - self.__last_backup_date.daysTo(QDate().currentDate())
        self.lbl_backup_days.setText(str(self.__days_until_backup))
        # Check if a backup is desirable
        if int(self.__backup_interval) <= self.__last_backup_date.daysTo(QDate().currentDate()):
            self.__should_backup_now = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = Diary()
    main_form.show()
    sys.exit(app.exec_())
