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
        self.load_settings()
        # Actions
        self.btnSave.clicked.connect(self.save_and_close)
        self.btnClose.clicked.connect(self.close)
        self.btnOpenFolder.clicked.connect(self.choose_folder)
        self.btn_color_weekday_background.clicked.connect(self.set_color_workday_background)

    def set_color_workday_background(self):
        self.__color_weekday_background = QColorDialog(parent=self).getColor()
        self.lbl_color_weekday_background.setStyleSheet("background-color: %s" % self.__color_weekday_background.name())

    def load_settings(self):
        params = Settings(self, "DenkaTech", "KDiary")
        # file settings
        file_path = params.load_setting("paths", "file_location")
        self.txtPathToDiary.setText(file_path)
        # color settings
        self.__color_weekday_background = params.load_setting("colors", "weekday_background")
        print("COLO", self.__color_weekday_background)
        if self.__color_weekday_background:
            self.lbl_color_weekday_background.setStyleSheet("background-color: %s" % self.__color_weekday_background)

    def save_and_close(self):
        """
        Write the settings 
        """
        params = Settings(self, "DenkaTech", "KDiary")
        params.save_setting("paths", "file_location", self.txtPathToDiary.text())
        params.save_setting("colors", "weekday_background", self.__color_weekday_background.name())
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

