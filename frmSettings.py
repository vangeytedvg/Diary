# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmSettings(object):
    def setupUi(self, frmSettings):
        frmSettings.setObjectName("frmSettings")
        frmSettings.resize(615, 367)
        self.horizontalLayout = QtWidgets.QHBoxLayout(frmSettings)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabSettings = QtWidgets.QTabWidget(frmSettings)
        self.tabSettings.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabSettings.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabSettings.setObjectName("tabSettings")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnOpenFolder = QtWidgets.QToolButton(self.tab)
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.gridLayout_2.addWidget(self.btnOpenFolder, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.txtPathToDiary = QtWidgets.QLineEdit(self.tab)
        self.txtPathToDiary.setObjectName("txtPathToDiary")
        self.gridLayout_2.addWidget(self.txtPathToDiary, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabSettings.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.btn_color_weekend_foreground = QtWidgets.QToolButton(self.tab_2)
        self.btn_color_weekend_foreground.setObjectName("btn_color_weekend_foreground")
        self.gridLayout.addWidget(self.btn_color_weekend_foreground, 7, 2, 1, 1)
        self.lbl_color_weekend_background = QtWidgets.QLabel(self.tab_2)
        self.lbl_color_weekend_background.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lbl_color_weekend_background.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.lbl_color_weekend_background.setText("")
        self.lbl_color_weekend_background.setObjectName("lbl_color_weekend_background")
        self.gridLayout.addWidget(self.lbl_color_weekend_background, 5, 1, 1, 1)
        self.lbl_color_weekday_foreground = QtWidgets.QLabel(self.tab_2)
        self.lbl_color_weekday_foreground.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lbl_color_weekday_foreground.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.lbl_color_weekday_foreground.setText("")
        self.lbl_color_weekday_foreground.setObjectName("lbl_color_weekday_foreground")
        self.gridLayout.addWidget(self.lbl_color_weekday_foreground, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.btn_color_weekday_background = QtWidgets.QToolButton(self.tab_2)
        self.btn_color_weekday_background.setObjectName("btn_color_weekday_background")
        self.gridLayout.addWidget(self.btn_color_weekday_background, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        self.lbl_color_weekday_background = QtWidgets.QLabel(self.tab_2)
        self.lbl_color_weekday_background.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lbl_color_weekday_background.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.lbl_color_weekday_background.setText("")
        self.lbl_color_weekday_background.setObjectName("lbl_color_weekday_background")
        self.gridLayout.addWidget(self.lbl_color_weekday_background, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.btn_color_weekday_foreground = QtWidgets.QToolButton(self.tab_2)
        self.btn_color_weekday_foreground.setObjectName("btn_color_weekday_foreground")
        self.gridLayout.addWidget(self.btn_color_weekday_foreground, 3, 2, 1, 1)
        self.lbl_color_weekend_foreground = QtWidgets.QLabel(self.tab_2)
        self.lbl_color_weekend_foreground.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lbl_color_weekend_foreground.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.lbl_color_weekend_foreground.setText("")
        self.lbl_color_weekend_foreground.setObjectName("lbl_color_weekend_foreground")
        self.gridLayout.addWidget(self.lbl_color_weekend_foreground, 7, 1, 1, 1)
        self.btn_color_weekend_background = QtWidgets.QToolButton(self.tab_2)
        self.btn_color_weekend_background.setObjectName("btn_color_weekend_background")
        self.gridLayout.addWidget(self.btn_color_weekend_background, 5, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabSettings.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rb_LocalBackup = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_LocalBackup.setObjectName("rb_LocalBackup")
        self.verticalLayout_4.addWidget(self.rb_LocalBackup)
        self.rb_CloudBackup = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_CloudBackup.setObjectName("rb_CloudBackup")
        self.verticalLayout_4.addWidget(self.rb_CloudBackup)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_backup_folder = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_backup_folder.setObjectName("lbl_backup_folder")
        self.horizontalLayout_4.addWidget(self.lbl_backup_folder)
        self.txt_backup_folder = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_backup_folder.setObjectName("txt_backup_folder")
        self.horizontalLayout_4.addWidget(self.txt_backup_folder)
        self.btn_select_backup_folder = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_select_backup_folder.setObjectName("btn_select_backup_folder")
        self.horizontalLayout_4.addWidget(self.btn_select_backup_folder)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.rb_google = QtWidgets.QRadioButton(self.groupBox)
        self.rb_google.setObjectName("rb_google")
        self.horizontalLayout_3.addWidget(self.rb_google)
        self.rb_other = QtWidgets.QRadioButton(self.groupBox)
        self.rb_other.setObjectName("rb_other")
        self.horizontalLayout_3.addWidget(self.rb_other)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 3, 0, 1, 1)
        self.tabSettings.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabSettings)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblLogo = QtWidgets.QLabel(frmSettings)
        self.lblLogo.setMaximumSize(QtCore.QSize(150, 150))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/tlb/settings-3.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")
        self.verticalLayout_2.addWidget(self.lblLogo)
        self.btnSave = QtWidgets.QPushButton(frmSettings)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_2.addWidget(self.btnSave)
        self.btnClose = QtWidgets.QPushButton(frmSettings)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout_2.addWidget(self.btnClose)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(frmSettings)
        self.tabSettings.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(frmSettings)

    def retranslateUi(self, frmSettings):
        _translate = QtCore.QCoreApplication.translate
        frmSettings.setWindowTitle(_translate("frmSettings", "Diary Settings"))
        self.btnOpenFolder.setText(_translate("frmSettings", "..."))
        self.label.setText(_translate("frmSettings", "Location of diary pages"))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tab), _translate("frmSettings", "Data"))
        self.label_6.setText(_translate("frmSettings", "Week-end diary foreground"))
        self.btn_color_weekend_foreground.setText(_translate("frmSettings", "..."))
        self.label_2.setText(_translate("frmSettings", "Weekday diary background"))
        self.btn_color_weekday_background.setText(_translate("frmSettings", "..."))
        self.label_3.setText(_translate("frmSettings", "Weekday diary foreground"))
        self.label_4.setText(_translate("frmSettings", "Week-end diary background"))
        self.btn_color_weekday_foreground.setText(_translate("frmSettings", "..."))
        self.btn_color_weekend_background.setText(_translate("frmSettings", "..."))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tab_2), _translate("frmSettings", "Colors"))
        self.groupBox_2.setTitle(_translate("frmSettings", "Type of backup"))
        self.rb_LocalBackup.setText(_translate("frmSettings", "Local Backup"))
        self.rb_CloudBackup.setText(_translate("frmSettings", "Cloud Backup"))
        self.lbl_backup_folder.setText(_translate("frmSettings", "Backup folder:"))
        self.btn_select_backup_folder.setText(_translate("frmSettings", "..."))
        self.groupBox.setTitle(_translate("frmSettings", "Cloud settings"))
        self.rb_google.setText(_translate("frmSettings", "Google Drive"))
        self.rb_other.setText(_translate("frmSettings", "Other"))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tab_3), _translate("frmSettings", "Backup"))
        self.btnSave.setText(_translate("frmSettings", "Save"))
        self.btnClose.setText(_translate("frmSettings", "Cancel"))
import icons_rc
