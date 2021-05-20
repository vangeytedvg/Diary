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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_warning = QtWidgets.QFrame(self.centralwidget)
        self.frame_warning.setMaximumSize(QtCore.QSize(16777215, 0))
        self.frame_warning.setStyleSheet("background-color: rgb(255, 171, 230);")
        self.frame_warning.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_warning.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_warning.setObjectName("frame_warning")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_warning)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_warning = QtWidgets.QLabel(self.frame_warning)
        self.lbl_warning.setStyleSheet("color: rgb(0, 0, 0);")
        self.lbl_warning.setObjectName("lbl_warning")
        self.horizontalLayout.addWidget(self.lbl_warning)
        self.btn_close_warning = QtWidgets.QToolButton(self.frame_warning)
        self.btn_close_warning.setObjectName("btn_close_warning")
        self.horizontalLayout.addWidget(self.btn_close_warning)
        self.verticalLayout.addWidget(self.frame_warning)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.txtDiary = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDiary.setObjectName("txtDiary")
        self.gridLayout.addWidget(self.txtDiary, 0, 1, 3, 1)
        self.testFrame = QtWidgets.QVBoxLayout()
        self.testFrame.setObjectName("testFrame")
        self.gridLayout.addLayout(self.testFrame, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 30))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuEvent_s = QtWidgets.QMenu(self.menubar)
        self.menuEvent_s.setObjectName("menuEvent_s")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menuInsert = QtWidgets.QMenu(self.menubar)
        self.menuInsert.setObjectName("menuInsert")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tlb/poweroff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionE_xit.setIcon(icon)
        self.actionE_xit.setObjectName("actionE_xit")
        self.action_Add = QtWidgets.QAction(MainWindow)
        self.action_Add.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tlb/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Add.setIcon(icon1)
        self.action_Add.setObjectName("action_Add")
        self.actionInsert_numbered_list = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tlb/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert_numbered_list.setIcon(icon2)
        self.actionInsert_numbered_list.setObjectName("actionInsert_numbered_list")
        self.actionInsert_bulleted_list = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tlb/bullet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert_bulleted_list.setIcon(icon3)
        self.actionInsert_bulleted_list.setObjectName("actionInsert_bulleted_list")
        self.actionBold = QtWidgets.QAction(MainWindow)
        self.actionBold.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tlb/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon4)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(MainWindow)
        self.actionItalic.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tlb/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon5)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(MainWindow)
        self.actionUnderline.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/tlb/underlined-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon6)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/tlb/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon7)
        self.actionSave.setObjectName("actionSave")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/tlb/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon8)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/tlb/copytext.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon9)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/tlb/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon10)
        self.actionPaste.setObjectName("actionPaste")
        self.actionErase = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/tlb/recycle-bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionErase.setIcon(icon11)
        self.actionErase.setObjectName("actionErase")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/tlb/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon12)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/tlb/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon13)
        self.actionRedo.setObjectName("actionRedo")
        self.action_Print = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/tlb/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Print.setIcon(icon14)
        self.action_Print.setObjectName("action_Print")
        self.action_insert_date = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/tlb/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_insert_date.setIcon(icon15)
        self.action_insert_date.setObjectName("action_insert_date")
        self.action_insert_time = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/tlb/time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_insert_time.setIcon(icon16)
        self.action_insert_time.setObjectName("action_insert_time")
        self.actionStrikethrough = QtWidgets.QAction(MainWindow)
        self.actionStrikethrough.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/tlb/strikethrough.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStrikethrough.setIcon(icon17)
        self.actionStrikethrough.setObjectName("actionStrikethrough")
        self.action_backup = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/tlb/sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_backup.setIcon(icon18)
        self.action_backup.setObjectName("action_backup")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/tlb/settings-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Preferences.setIcon(icon19)
        self.action_Preferences.setObjectName("action_Preferences")
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.action_Print)
        self.menu_File.addAction(self.action_backup)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menuEvent_s.addAction(self.action_Add)
        self.menuEvent_s.addAction(self.actionErase)
        self.menu_Edit.addAction(self.actionUndo)
        self.menu_Edit.addAction(self.actionRedo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionCut)
        self.menu_Edit.addAction(self.actionCopy)
        self.menu_Edit.addAction(self.actionPaste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionBold)
        self.menu_Edit.addAction(self.actionItalic)
        self.menu_Edit.addAction(self.actionUnderline)
        self.menu_Edit.addAction(self.actionStrikethrough)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Preferences)
        self.menuInsert.addAction(self.action_insert_date)
        self.menuInsert.addAction(self.action_insert_time)
        self.menuInsert.addAction(self.actionInsert_bulleted_list)
        self.menuInsert.addAction(self.actionInsert_numbered_list)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuEvent_s.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.toolBar_2.addAction(self.actionInsert_bulleted_list)
        self.toolBar_2.addAction(self.actionInsert_numbered_list)
        self.toolBar_2.addAction(self.action_insert_date)
        self.toolBar_2.addAction(self.action_insert_time)
        self.toolBar_3.addAction(self.actionSave)
        self.toolBar_3.addAction(self.action_Print)
        self.toolBar_3.addAction(self.action_backup)
        self.toolBar_3.addAction(self.action_Add)
        self.toolBar_3.addAction(self.actionErase)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addAction(self.actionE_xit)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionUnderline)
        self.toolBar.addAction(self.actionStrikethrough)

        self.retranslateUi(MainWindow)
        self.actionE_xit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KDiary"))
        self.lbl_warning.setText(_translate("MainWindow", "TextLabel"))
        self.btn_close_warning.setText(_translate("MainWindow", "..."))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuEvent_s.setTitle(_translate("MainWindow", "Ev&ents"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuInsert.setTitle(_translate("MainWindow", "&Insert"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionE_xit.setText(_translate("MainWindow", "&Quit"))
        self.actionE_xit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_Add.setText(_translate("MainWindow", "&Add"))
        self.actionInsert_numbered_list.setText(_translate("MainWindow", "Insert numbered list"))
        self.actionInsert_numbered_list.setShortcut(_translate("MainWindow", "Ctrl+I, B"))
        self.actionInsert_bulleted_list.setText(_translate("MainWindow", "Insert bulleted list"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionUnderline.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionErase.setText(_translate("MainWindow", "Erase &and renew"))
        self.actionErase.setToolTip(_translate("MainWindow", "Erase current diary entry file"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.action_Print.setText(_translate("MainWindow", "&Print"))
        self.action_Print.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_insert_date.setText(_translate("MainWindow", "Date"))
        self.action_insert_date.setToolTip(_translate("MainWindow", "Insert date stamp"))
        self.action_insert_time.setText(_translate("MainWindow", "Time"))
        self.action_insert_time.setToolTip(_translate("MainWindow", "Insert time stamp"))
        self.actionStrikethrough.setText(_translate("MainWindow", "Strikethrough"))
        self.action_backup.setText(_translate("MainWindow", "Backup diary files"))
        self.action_backup.setToolTip(_translate("MainWindow", "Backup"))
        self.action_Preferences.setText(_translate("MainWindow", "Preferences"))
import icons_rc
