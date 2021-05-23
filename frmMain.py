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
        MainWindow.resize(1168, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_warning = QtWidgets.QFrame(self.centralwidget)
        self.frame_warning.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_warning.setStyleSheet("background-color: rgba(193, 129, 0, 0.5);\n"
"")
        self.frame_warning.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_warning.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_warning.setObjectName("frame_warning")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_warning)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_warning = QtWidgets.QLabel(self.frame_warning)
        self.lbl_warning.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: transparent;\n"
"\n"
"")
        self.lbl_warning.setObjectName("lbl_warning")
        self.horizontalLayout.addWidget(self.lbl_warning)
        self.btn_close_warning = QtWidgets.QToolButton(self.frame_warning)
        self.btn_close_warning.setStyleSheet("background-color: rgb(121, 121, 121);\n"
"color: rgb(255, 255, 255);")
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 30))
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
        self.toolbar_insertions = QtWidgets.QToolBar(MainWindow)
        self.toolbar_insertions.setObjectName("toolbar_insertions")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar_insertions)
        self.toolbar_file = QtWidgets.QToolBar(MainWindow)
        self.toolbar_file.setObjectName("toolbar_file")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar_file)
        self.toolbar_font = QtWidgets.QToolBar(MainWindow)
        self.toolbar_font.setObjectName("toolbar_font")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar_font)
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
        self.action_Set_Font_Back_to_Default_Arial_12 = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/tlb/standard_font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Set_Font_Back_to_Default_Arial_12.setIcon(icon20)
        self.action_Set_Font_Back_to_Default_Arial_12.setObjectName("action_Set_Font_Back_to_Default_Arial_12")
        self.actionLeft_outline = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/tlb/left-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft_outline.setIcon(icon21)
        self.actionLeft_outline.setObjectName("actionLeft_outline")
        self.actionRight_outline = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/tlb/right-align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight_outline.setIcon(icon22)
        self.actionRight_outline.setObjectName("actionRight_outline")
        self.actionIndent_left = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/tlb/left-indent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIndent_left.setIcon(icon23)
        self.actionIndent_left.setObjectName("actionIndent_left")
        self.actionIndent_right = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/tlb/right-indent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIndent_right.setIcon(icon24)
        self.actionIndent_right.setObjectName("actionIndent_right")
        self.actionCenter = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/tlb/align-center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter.setIcon(icon25)
        self.actionCenter.setObjectName("actionCenter")
        self.actionOutline = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/tlb/justify-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOutline.setIcon(icon26)
        self.actionOutline.setObjectName("actionOutline")
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
        self.menu_Edit.addAction(self.action_Set_Font_Back_to_Default_Arial_12)
        self.menu_Edit.addAction(self.actionBold)
        self.menu_Edit.addAction(self.actionItalic)
        self.menu_Edit.addAction(self.actionUnderline)
        self.menu_Edit.addAction(self.actionStrikethrough)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionLeft_outline)
        self.menu_Edit.addAction(self.actionRight_outline)
        self.menu_Edit.addAction(self.actionIndent_left)
        self.menu_Edit.addAction(self.actionIndent_right)
        self.menu_Edit.addAction(self.actionCenter)
        self.menu_Edit.addAction(self.actionOutline)
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
        self.toolbar_insertions.addAction(self.actionInsert_bulleted_list)
        self.toolbar_insertions.addAction(self.actionInsert_numbered_list)
        self.toolbar_insertions.addAction(self.action_insert_date)
        self.toolbar_insertions.addAction(self.action_insert_time)
        self.toolbar_file.addAction(self.actionSave)
        self.toolbar_file.addAction(self.action_Print)
        self.toolbar_file.addAction(self.action_backup)
        self.toolbar_file.addAction(self.action_Add)
        self.toolbar_file.addAction(self.actionErase)
        self.toolbar_file.addSeparator()
        self.toolbar_file.addAction(self.actionE_xit)
        self.toolbar_font.addAction(self.actionUndo)
        self.toolbar_font.addAction(self.actionRedo)
        self.toolbar_font.addAction(self.actionCut)
        self.toolbar_font.addAction(self.actionCopy)
        self.toolbar_font.addAction(self.actionPaste)
        self.toolbar_font.addSeparator()
        self.toolbar_font.addAction(self.actionBold)
        self.toolbar_font.addAction(self.actionItalic)
        self.toolbar_font.addAction(self.actionUnderline)
        self.toolbar_font.addAction(self.actionStrikethrough)
        self.toolbar_font.addSeparator()
        self.toolbar_font.addAction(self.action_Set_Font_Back_to_Default_Arial_12)
        self.toolBar.addAction(self.actionLeft_outline)
        self.toolBar.addAction(self.actionCenter)
        self.toolBar.addAction(self.actionRight_outline)
        self.toolBar.addAction(self.actionOutline)
        self.toolBar.addAction(self.actionIndent_right)
        self.toolBar.addAction(self.actionIndent_left)

        self.retranslateUi(MainWindow)
        self.actionE_xit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KDiary"))
        self.lbl_warning.setText(_translate("MainWindow", "[]"))
        self.btn_close_warning.setText(_translate("MainWindow", "..."))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuEvent_s.setTitle(_translate("MainWindow", "Ev&ents"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuInsert.setTitle(_translate("MainWindow", "&Insert"))
        self.toolbar_insertions.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolbar_file.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolbar_font.setWindowTitle(_translate("MainWindow", "toolBar"))
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
        self.action_Set_Font_Back_to_Default_Arial_12.setText(_translate("MainWindow", "Set Font Back to Default (Arial 12)"))
        self.actionLeft_outline.setText(_translate("MainWindow", "Left outline"))
        self.actionRight_outline.setText(_translate("MainWindow", "Right outline"))
        self.actionIndent_left.setText(_translate("MainWindow", "Indent left"))
        self.actionIndent_right.setText(_translate("MainWindow", "Indent right"))
        self.actionCenter.setText(_translate("MainWindow", "Center"))
        self.actionOutline.setText(_translate("MainWindow", "Outline"))
import icons_rc
