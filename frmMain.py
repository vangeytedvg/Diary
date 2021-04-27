# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.txtDiary = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDiary.setObjectName("txtDiary")
        self.gridLayout.addWidget(self.txtDiary, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 30))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuEvent_s = QtWidgets.QMenu(self.menubar)
        self.menuEvent_s.setObjectName("menuEvent_s")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.action_Add = QtWidgets.QAction(MainWindow)
        self.action_Add.setObjectName("action_Add")
        self.menu_File.addAction(self.actionE_xit)
        self.menuEvent_s.addAction(self.action_Add)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEvent_s.menuAction())
        self.toolBar.addAction(self.actionE_xit)
        self.toolBar.addAction(self.action_Add)

        self.retranslateUi(MainWindow)
        self.actionE_xit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KDiary"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuEvent_s.setTitle(_translate("MainWindow", "Event&s"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))
        self.action_Add.setText(_translate("MainWindow", "&Add"))
