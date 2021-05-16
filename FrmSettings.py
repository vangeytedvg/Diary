from PyQt5.QtWidgets import QDialog, QFileDialog
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
        self.load_settings()
        # Actions
        self.btnSave.clicked.connect(self.save_and_close)
        self.btnClose.clicked.connect(self.close)
        self.btnOpenFolder.clicked.connect(self.choose_folder)

    def load_settings(self):
        params = Settings(self, "DenkaTech", "KDiary")
        file_path = params.load_setting("paths", "file_location")
        self.txtPathToDiary.setText(file_path)

    def save_and_close(self):
        """
        Write the settings 
        """
        params = Settings(self, "DenkaTech", "KDiary")
        params.save_setting("paths", "file_location", self.txtPathToDiary.text())
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

