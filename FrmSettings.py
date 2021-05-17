from PyQt5.QtWidgets import QDialog, QFileDialog, QColorDialog
from PyQt5.QtCore import QDate
from frmSettings import Ui_frmSettings
from utilities.setting import Settings


class FrmSettings(QDialog, Ui_frmSettings):
    """
    Settings form 
    """

    def __init__(self, parent):
        """
            Ctor
        :param parent,the caller
        """
        super(FrmSettings, self).__init__()
        self.setupUi(self)
        self.parent = parent
        # settings methods and members
        self.__color_weekday_background = ""
        self.__color_weekday_foreground = ""
        self.__color_weekend_background = ""
        self.__color_weekend_foreground = ""
        self.rb_google.setEnabled(False)
        self.rb_other.setEnabled(False)
        self.load_settings()
        # Actions
        self.btnSave.clicked.connect(self.save_and_close)
        self.btnClose.clicked.connect(self.close)
        # Data
        self.btnOpenFolder.clicked.connect(self.choose_folder)
        # Colors
        self.btn_color_weekday_background.clicked.connect(self.set_color_workday_background)
        self.btn_color_weekday_foreground.clicked.connect(self.set_color_workday_foreground)
        self.btn_color_weekend_background.clicked.connect(self.set_color_weekend_background)
        self.btn_color_weekend_foreground.clicked.connect(self.set_color_weekend_foreground)
        # Backup
        self.rb_LocalBackup.toggled.connect(lambda: self.set_backup_type(self.rb_LocalBackup))
        self.rb_CloudBackup.toggled.connect(lambda: self.set_backup_type(self.rb_CloudBackup))

    def set_backup_type(self, rb):
        if rb.text() == "Local Backup":
            self.rb_google.setEnabled(False)
            self.rb_other.setEnabled(False)
            pass
        if rb.text() == "Cloud Backup":
            self.rb_google.setEnabled(True)
            self.rb_google.setFocus()
            self.rb_other.setEnabled(True)
            pass

    def set_color_workday_background(self):
        self.__color_weekday_background = QColorDialog(parent=self).getColor().name()
        self.lbl_color_weekday_background.setStyleSheet("background-color: %s" % self.__color_weekday_background)

    def set_color_workday_foreground(self):
        self.__color_weekday_foreground = QColorDialog(parent=self).getColor().name()
        self.lbl_color_weekday_foreground.setStyleSheet("background-color: %s" % self.__color_weekday_foreground)

    def set_color_weekend_background(self):
        self.__color_weekend_background = QColorDialog(parent=self).getColor().name()
        self.lbl_color_weekend_background.setStyleSheet("background-color: %s" % self.__color_weekend_background)

    def set_color_weekend_foreground(self):
        self.__color_weekend_foreground = QColorDialog(parent=self).getColor().name()
        self.lbl_color_weekend_foreground.setStyleSheet("background-color: %s" % self.__color_weekend_foreground)

    def load_settings(self):
        params = Settings(self, "DenkaTech", "KDiary")
        # file settings
        file_path = params.load_setting("paths", "file_location")
        self.txtPathToDiary.setText(file_path)
        # color settings
        self.__color_weekday_background = params.load_setting("colors", "weekday_background")
        self.__color_weekday_foreground = params.load_setting("colors", "weekday_foreground")
        self.__color_weekend_foreground = params.load_setting("colors", "weekend_foreground")
        self.__color_weekend_background = params.load_setting("colors", "weekend_background")
        if self.__color_weekday_background:
            self.lbl_color_weekday_background.setStyleSheet("background-color: %s" % self.__color_weekday_background)
        if self.__color_weekday_foreground:
            self.lbl_color_weekday_foreground.setStyleSheet("background-color: %s" % self.__color_weekday_foreground)
        if self.__color_weekend_background:
            self.lbl_color_weekend_background.setStyleSheet("background-color: %s" % self.__color_weekend_background)
        if self.__color_weekend_foreground:
            self.lbl_color_weekend_foreground.setStyleSheet("background-color: %s" % self.__color_weekend_foreground)

    def save_and_close(self):
        """
        Write the settings 
        """
        params = Settings(self, "DenkaTech", "KDiary")
        params.save_setting("paths", "file_location", self.txtPathToDiary.text())
        params.save_setting("colors", "weekday_background", self.__color_weekday_background)
        params.save_setting("colors", "weekday_foreground", self.__color_weekday_foreground)
        params.save_setting("colors", "weekend_background", self.__color_weekend_background)
        params.save_setting("colors", "weekend_foreground", self.__color_weekend_foreground)
        self.close()

    def choose_folder(self):
        """
        Select the folder where the diary files will reside
        """
        dir = QFileDialog.getExistingDirectory(self, "Open Directory",
                                               "/home",
                                               QFileDialog.ShowDirsOnly |
                                               QFileDialog.DontResolveSymlinks)
        if dir:
            self.txtPathToDiary.setText(dir)

