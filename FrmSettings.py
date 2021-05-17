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
        self.__backup_local = False
        self.__backup_cloud = False
        self.__backup_google_drive = False
        self.__backup_cloud_other = False
        self.__back_file_path = ""

        self.rb_LocalBackup.setChecked(True)
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
        self.rb_LocalBackup.toggled.connect(self.set_local_backup)
        self.rb_CloudBackup.toggled.connect(self.set_cloud_backup)
        self.rb_google.toggled.connect(self.set_google_backup)
        # TODO : Add agenda mode setting, agenda mode allows the user to enter events
        # in the future, like planning etc...

    def set_local_backup(self):
        self.__backup_local = True
        # Disable other controls
        self.rb_CloudBackup.setEnabled(False)
        self.rb_google.setEnabled(False)
        self.rb_other.setEnabled(False)
        pass

    def set_cloud_backup(self):
        pass

    def set_google_backup(self):
        if self.sender().isChecked() == True:
            self.__backup_google_drive = True
        else:
            self.__backup_google_drive = False

    def set_backup_type(self, rb):
        """
        Handle backup type selection
        """
        if rb.text() == "Local Backup":
            pass
        if rb.text() == "Cloud Backup":
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
        """
        Restore the saved settings
        """
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
        # Backup settings
        self.__backup_local = params.load_setting("backup", "backup_to_local_file")
        self.__backup_cloud = params.load_setting("backup", "backup_to_cloud")
        self.__backup_google_drive = params.load_setting("backup", "backup_to_google_drive")

    def save_and_close(self):
        """
        Write the settings to disk
        """
        params = Settings(self, "DenkaTech", "KDiary")
        # Diary location
        params.save_setting("paths", "file_location", self.txtPathToDiary.text())
        # Colors
        params.save_setting("colors", "weekday_background", self.__color_weekday_background)
        params.save_setting("colors", "weekday_foreground", self.__color_weekday_foreground)
        params.save_setting("colors", "weekend_background", self.__color_weekend_background)
        params.save_setting("colors", "weekend_foreground", self.__color_weekend_foreground)
        # Backup settings
        params.save_setting("backup", "backup_to_local_file", self.__backup_local)
        params.save_setting("backup", "backup_to_cloud", self.__backup_cloud)
        params.save_setting("backup", "backup_to_google_drive", self.__backup_google_drive)
        self.close()

    def choose_folder(self):
        """
        Select the folder where the diary files will reside
        """
        dir = QFileDialog.getExistingDirectory(self, "Open Directory",
                                               "/home",
                                               QFileDialog.ShowDirsOnly
                                               | QFileDialog.DontResolveSymlinks)
        if dir:
            self.txtPathToDiary.setText(dir)

