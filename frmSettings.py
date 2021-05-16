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
        self.tabSettings.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(frmSettings)
        self.tabSettings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmSettings)

    def retranslateUi(self, frmSettings):
        _translate = QtCore.QCoreApplication.translate
        frmSettings.setWindowTitle(_translate("frmSettings", "Diary Settings"))
        self.btnOpenFolder.setText(_translate("frmSettings", "..."))
        self.label.setText(_translate("frmSettings", "Location of diary pages"))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tab), _translate("frmSettings", "Data"))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tab_2), _translate("frmSettings", "Colors"))
        self.checkBox.setText(_translate("frmSettings", "Allow backups to Google Drive"))
        self.tabSettings.setTabText(self.tabSettings.indexOf(self.tab_3), _translate("frmSettings", "Cloud backup"))
        self.btnSave.setText(_translate("frmSettings", "Save"))
        self.btnClose.setText(_translate("frmSettings", "Cancel"))
import icons_rc
