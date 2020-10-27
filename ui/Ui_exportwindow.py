# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exportWindow(object):
    def setupUi(self, exportWindow):
        exportWindow.setObjectName("exportWindow")
        exportWindow.resize(770, 440)
        exportWindow.setMinimumSize(QtCore.QSize(0, 0))
        exportWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        exportWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/export_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        exportWindow.setWindowIcon(icon)
        exportWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.gridLayout_15 = QtWidgets.QGridLayout(exportWindow)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ew_label_1 = QtWidgets.QLabel(exportWindow)
        self.ew_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_1.setFont(font)
        self.ew_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_1.setObjectName("ew_label_1")
        self.horizontalLayout.addWidget(self.ew_label_1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ew_combobox_1 = QtWidgets.QComboBox(exportWindow)
        self.ew_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_1.setFont(font)
        self.ew_combobox_1.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_1.setObjectName("ew_combobox_1")
        self.ew_combobox_1.addItem("")
        self.ew_combobox_1.addItem("")
        self.ew_combobox_1.addItem("")
        self.horizontalLayout.addWidget(self.ew_combobox_1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.info_button_1 = QtWidgets.QToolButton(exportWindow)
        self.info_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button_1.setIcon(icon1)
        self.info_button_1.setIconSize(QtCore.QSize(23, 23))
        self.info_button_1.setAutoRaise(False)
        self.info_button_1.setObjectName("info_button_1")
        self.horizontalLayout.addWidget(self.info_button_1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_15.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_15.addItem(spacerItem3, 1, 0, 1, 1)
        self.ew_splitter = QtWidgets.QSplitter(exportWindow)
        self.ew_splitter.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: rgb(190,190,190);\n"
"}")
        self.ew_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.ew_splitter.setObjectName("ew_splitter")
        self.ew_option_list = QtWidgets.QListWidget(self.ew_splitter)
        self.ew_option_list.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_option_list.sizePolicy().hasHeightForWidth())
        self.ew_option_list.setSizePolicy(sizePolicy)
        self.ew_option_list.setMinimumSize(QtCore.QSize(0, 0))
        self.ew_option_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_option_list.setFont(font)
        self.ew_option_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ew_option_list.setStyleSheet("QListWidget {\n"
"    border-bottom-left-radius: 3px;\n"
"    border-top-left-radius: 3px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QListWidget:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QListView::item {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 1px;\n"
"    margin: 3px 3px 3px 3px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(230,230,230);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ew_option_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_option_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ew_option_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ew_option_list.setObjectName("ew_option_list")
        self.ew_stacked_widget = QtWidgets.QStackedWidget(self.ew_splitter)
        self.ew_stacked_widget.setObjectName("ew_stacked_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.ew_stacked_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ew_scroll_area_1 = QtWidgets.QScrollArea(self.page_2)
        self.ew_scroll_area_1.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ew_scroll_area_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_scroll_area_1.setWidgetResizable(True)
        self.ew_scroll_area_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ew_scroll_area_1.setObjectName("ew_scroll_area_1")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 409, 147))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ew_vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.ew_vertical_layout_1.setObjectName("ew_vertical_layout_1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ew_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ew_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_2.setFont(font)
        self.ew_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_2.setObjectName("ew_label_2")
        self.gridLayout_2.addWidget(self.ew_label_2, 0, 0, 1, 1)
        self.ew_combobox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ew_combobox_2.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_2.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_2.setFont(font)
        self.ew_combobox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_2.setObjectName("ew_combobox_2")
        self.ew_combobox_2.addItem("")
        self.gridLayout_2.addWidget(self.ew_combobox_2, 0, 1, 1, 1)
        self.ew_label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ew_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_3.setFont(font)
        self.ew_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_3.setObjectName("ew_label_3")
        self.gridLayout_2.addWidget(self.ew_label_3, 1, 0, 1, 1)
        self.ew_combobox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ew_combobox_3.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_3.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_3.setFont(font)
        self.ew_combobox_3.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_3.setObjectName("ew_combobox_3")
        self.ew_combobox_3.addItem("")
        self.gridLayout_2.addWidget(self.ew_combobox_3, 1, 1, 1, 1)
        self.ew_label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ew_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_4.setFont(font)
        self.ew_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_4.setObjectName("ew_label_4")
        self.gridLayout_2.addWidget(self.ew_label_4, 2, 0, 1, 1)
        self.ew_combobox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ew_combobox_4.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_4.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_4.setFont(font)
        self.ew_combobox_4.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_4.setObjectName("ew_combobox_4")
        self.ew_combobox_4.addItem("")
        self.gridLayout_2.addWidget(self.ew_combobox_4, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.info_button_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.info_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_2.setText("")
        self.info_button_2.setIcon(icon1)
        self.info_button_2.setIconSize(QtCore.QSize(23, 23))
        self.info_button_2.setAutoRaise(False)
        self.info_button_2.setObjectName("info_button_2")
        self.horizontalLayout_3.addWidget(self.info_button_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.ew_label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ew_label_24.setEnabled(False)
        self.ew_label_24.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_24.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_24.setFont(font)
        self.ew_label_24.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_24.setObjectName("ew_label_24")
        self.horizontalLayout_6.addWidget(self.ew_label_24)
        self.ew_combobox_9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.ew_combobox_9.setEnabled(False)
        self.ew_combobox_9.setMinimumSize(QtCore.QSize(150, 27))
        self.ew_combobox_9.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_9.setFont(font)
        self.ew_combobox_9.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_9.setObjectName("ew_combobox_9")
        self.horizontalLayout_6.addWidget(self.ew_combobox_9)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.ew_vertical_layout_1.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.ew_vertical_layout_1, 0, 0, 1, 1)
        self.ew_scroll_area_1.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.ew_scroll_area_1, 0, 0, 1, 1)
        self.ew_stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ew_scroll_area_2 = QtWidgets.QScrollArea(self.page_3)
        self.ew_scroll_area_2.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ew_scroll_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_scroll_area_2.setWidgetResizable(True)
        self.ew_scroll_area_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ew_scroll_area_2.setObjectName("ew_scroll_area_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 524, 237))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ew_vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.ew_vertical_layout_2.setObjectName("ew_vertical_layout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ew_label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ew_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_5.setFont(font)
        self.ew_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_5.setObjectName("ew_label_5")
        self.gridLayout_5.addWidget(self.ew_label_5, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ew_combobox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ew_combobox_5.setMinimumSize(QtCore.QSize(250, 27))
        self.ew_combobox_5.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_5.setFont(font)
        self.ew_combobox_5.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_5.setObjectName("ew_combobox_5")
        self.horizontalLayout_4.addWidget(self.ew_combobox_5)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.ew_add_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_add_button.setMinimumSize(QtCore.QSize(27, 27))
        self.ew_add_button.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_add_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_add_button.setIcon(icon2)
        self.ew_add_button.setIconSize(QtCore.QSize(23, 23))
        self.ew_add_button.setObjectName("ew_add_button")
        self.horizontalLayout_4.addWidget(self.ew_add_button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.ew_label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ew_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_6.setFont(font)
        self.ew_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.ew_label_6.setWordWrap(True)
        self.ew_label_6.setObjectName("ew_label_6")
        self.gridLayout_5.addWidget(self.ew_label_6, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ew_varlist_1 = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.ew_varlist_1.setEnabled(True)
        self.ew_varlist_1.setMinimumSize(QtCore.QSize(0, 150))
        self.ew_varlist_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_varlist_1.setFont(font)
        self.ew_varlist_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ew_varlist_1.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QListWidget:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QListView::item {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 1px;\n"
"    margin: 3px 3px 3px 3px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(230,230,230);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-left-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ew_varlist_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_varlist_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ew_varlist_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ew_varlist_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ew_varlist_1.setObjectName("ew_varlist_1")
        self.horizontalLayout_5.addWidget(self.ew_varlist_1)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_button_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.info_button_3.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_3.setText("")
        self.info_button_3.setIcon(icon1)
        self.info_button_3.setIconSize(QtCore.QSize(23, 23))
        self.info_button_3.setAutoRaise(False)
        self.info_button_3.setObjectName("info_button_3")
        self.verticalLayout.addWidget(self.info_button_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.ew_vertical_layout_2.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.ew_vertical_layout_2, 0, 0, 1, 1)
        self.ew_scroll_area_2.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.ew_scroll_area_2, 0, 0, 1, 1)
        self.ew_stacked_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_7.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ew_scroll_area_3 = QtWidgets.QScrollArea(self.page_4)
        self.ew_scroll_area_3.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ew_scroll_area_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_scroll_area_3.setWidgetResizable(True)
        self.ew_scroll_area_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ew_scroll_area_3.setObjectName("ew_scroll_area_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 429, 211))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ew_vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.ew_vertical_layout_3.setObjectName("ew_vertical_layout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.ew_label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ew_label_7.setEnabled(True)
        self.ew_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_7.setFont(font)
        self.ew_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_7.setObjectName("ew_label_7")
        self.horizontalLayout_12.addWidget(self.ew_label_7)
        self.ew_slider_1 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.ew_slider_1.setEnabled(True)
        self.ew_slider_1.setMinimumSize(QtCore.QSize(180, 27))
        self.ew_slider_1.setMaximumSize(QtCore.QSize(180, 27))
        self.ew_slider_1.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 1px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(0,0,200);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: rgb(145,145,145);\n"
"}\n"
"")
        self.ew_slider_1.setMinimum(1)
        self.ew_slider_1.setMaximum(20)
        self.ew_slider_1.setSingleStep(1)
        self.ew_slider_1.setPageStep(1)
        self.ew_slider_1.setProperty("value", 5)
        self.ew_slider_1.setSliderPosition(5)
        self.ew_slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.ew_slider_1.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.ew_slider_1.setObjectName("ew_slider_1")
        self.horizontalLayout_12.addWidget(self.ew_slider_1)
        self.ew_label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ew_label_8.setEnabled(True)
        self.ew_label_8.setMinimumSize(QtCore.QSize(45, 27))
        self.ew_label_8.setMaximumSize(QtCore.QSize(45, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_8.setFont(font)
        self.ew_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_8.setObjectName("ew_label_8")
        self.horizontalLayout_12.addWidget(self.ew_label_8)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.info_button_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_4.setText("")
        self.info_button_4.setIcon(icon1)
        self.info_button_4.setIconSize(QtCore.QSize(23, 23))
        self.info_button_4.setAutoRaise(False)
        self.info_button_4.setObjectName("info_button_4")
        self.horizontalLayout_12.addWidget(self.info_button_4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.ew_vertical_layout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.ew_checkbox_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ew_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_checkbox_1.setFont(font)
        self.ew_checkbox_1.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ew_checkbox_1.setObjectName("ew_checkbox_1")
        self.horizontalLayout_13.addWidget(self.ew_checkbox_1)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem14)
        self.info_button_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_button_5.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_5.setText("")
        self.info_button_5.setIcon(icon1)
        self.info_button_5.setIconSize(QtCore.QSize(23, 23))
        self.info_button_5.setAutoRaise(False)
        self.info_button_5.setObjectName("info_button_5")
        self.horizontalLayout_13.addWidget(self.info_button_5)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.ew_vertical_layout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ew_checkbox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ew_checkbox_2.setEnabled(False)
        self.ew_checkbox_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_checkbox_2.setFont(font)
        self.ew_checkbox_2.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_checkbox_2.setObjectName("ew_checkbox_2")
        self.horizontalLayout_14.addWidget(self.ew_checkbox_2)
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.info_button_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_button_6.setEnabled(False)
        self.info_button_6.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_6.setText("")
        self.info_button_6.setIcon(icon1)
        self.info_button_6.setIconSize(QtCore.QSize(23, 23))
        self.info_button_6.setAutoRaise(False)
        self.info_button_6.setObjectName("info_button_6")
        self.horizontalLayout_14.addWidget(self.info_button_6)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.ew_vertical_layout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem18)
        self.ew_label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ew_label_9.setEnabled(False)
        self.ew_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_9.setFont(font)
        self.ew_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_9.setObjectName("ew_label_9")
        self.horizontalLayout_15.addWidget(self.ew_label_9)
        self.ew_slider_2 = QtWidgets.QSlider(self.scrollAreaWidgetContents_3)
        self.ew_slider_2.setEnabled(False)
        self.ew_slider_2.setMinimumSize(QtCore.QSize(180, 27))
        self.ew_slider_2.setMaximumSize(QtCore.QSize(180, 27))
        self.ew_slider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 1px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(0,0,200);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: rgb(145,145,145);\n"
"}\n"
"")
        self.ew_slider_2.setMinimum(0)
        self.ew_slider_2.setMaximum(100)
        self.ew_slider_2.setSingleStep(1)
        self.ew_slider_2.setPageStep(1)
        self.ew_slider_2.setProperty("value", 0)
        self.ew_slider_2.setSliderPosition(0)
        self.ew_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.ew_slider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.ew_slider_2.setObjectName("ew_slider_2")
        self.horizontalLayout_15.addWidget(self.ew_slider_2)
        self.ew_label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ew_label_23.setEnabled(False)
        self.ew_label_23.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_23.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_23.setFont(font)
        self.ew_label_23.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_23.setObjectName("ew_label_23")
        self.horizontalLayout_15.addWidget(self.ew_label_23)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.ew_vertical_layout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.ew_checkbox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ew_checkbox_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_checkbox_3.setFont(font)
        self.ew_checkbox_3.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ew_checkbox_3.setObjectName("ew_checkbox_3")
        self.horizontalLayout_16.addWidget(self.ew_checkbox_3)
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem20)
        self.info_button_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_button_7.setEnabled(True)
        self.info_button_7.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_7.setText("")
        self.info_button_7.setIcon(icon1)
        self.info_button_7.setIconSize(QtCore.QSize(23, 23))
        self.info_button_7.setAutoRaise(False)
        self.info_button_7.setObjectName("info_button_7")
        self.horizontalLayout_16.addWidget(self.info_button_7)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem21)
        self.ew_vertical_layout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem22)
        self.ew_label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ew_label_10.setEnabled(False)
        self.ew_label_10.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_10.setFont(font)
        self.ew_label_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_10.setObjectName("ew_label_10")
        self.horizontalLayout_17.addWidget(self.ew_label_10)
        self.ew_line_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.ew_line_1.setEnabled(False)
        self.ew_line_1.setMinimumSize(QtCore.QSize(50, 27))
        self.ew_line_1.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_1.setFont(font)
        self.ew_line_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_1.setObjectName("ew_line_1")
        self.horizontalLayout_17.addWidget(self.ew_line_1)
        spacerItem23 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem23)
        self.ew_vertical_layout_3.addLayout(self.horizontalLayout_17)
        self.gridLayout_8.addLayout(self.ew_vertical_layout_3, 0, 0, 1, 1)
        self.ew_scroll_area_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.addWidget(self.ew_scroll_area_3, 0, 0, 1, 1)
        self.ew_stacked_widget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_9.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ew_scroll_area_4 = QtWidgets.QScrollArea(self.page_5)
        self.ew_scroll_area_4.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.ew_scroll_area_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ew_scroll_area_4.setWidgetResizable(True)
        self.ew_scroll_area_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ew_scroll_area_4.setObjectName("ew_scroll_area_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 557, 396))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ew_vertical_layout_4 = QtWidgets.QVBoxLayout()
        self.ew_vertical_layout_4.setObjectName("ew_vertical_layout_4")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.ew_label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_11.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_11.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_11.setFont(font)
        self.ew_label_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_11.setObjectName("ew_label_11")
        self.horizontalLayout_18.addWidget(self.ew_label_11)
        self.ew_combobox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.ew_combobox_6.setMinimumSize(QtCore.QSize(244, 30))
        self.ew_combobox_6.setMaximumSize(QtCore.QSize(244, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_6.setFont(font)
        self.ew_combobox_6.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_6.setIconSize(QtCore.QSize(200, 22))
        self.ew_combobox_6.setObjectName("ew_combobox_6")
        self.ew_combobox_6.addItem("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/colormap_coolwarm.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon3, "")
        self.ew_combobox_6.setItemText(1, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/colormap_jet.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon4, "")
        self.ew_combobox_6.setItemText(2, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/colormap_ocean.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon5, "")
        self.ew_combobox_6.setItemText(3, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/colormap_spectral.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon6, "")
        self.ew_combobox_6.setItemText(4, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/hot.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon7, "")
        self.ew_combobox_6.setItemText(5, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/hsv.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon8, "")
        self.ew_combobox_6.setItemText(6, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/seismic.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon9, "")
        self.ew_combobox_6.setItemText(7, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("graphic_materials/colormap_images/terrain.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_combobox_6.addItem(icon10, "")
        self.ew_combobox_6.setItemText(8, "")
        self.horizontalLayout_18.addWidget(self.ew_combobox_6)
        spacerItem24 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem24)
        self.info_button_8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.info_button_8.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_8.setText("")
        self.info_button_8.setIcon(icon1)
        self.info_button_8.setIconSize(QtCore.QSize(23, 23))
        self.info_button_8.setAutoRaise(False)
        self.info_button_8.setObjectName("info_button_8")
        self.horizontalLayout_18.addWidget(self.info_button_8)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem25)
        self.ew_vertical_layout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem26)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.ew_label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_12.setEnabled(False)
        self.ew_label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_12.setFont(font)
        self.ew_label_12.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_12.setObjectName("ew_label_12")
        self.horizontalLayout_20.addWidget(self.ew_label_12)
        self.ew_combobox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.ew_combobox_7.setEnabled(False)
        self.ew_combobox_7.setMinimumSize(QtCore.QSize(180, 27))
        self.ew_combobox_7.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_7.setFont(font)
        self.ew_combobox_7.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_7.setObjectName("ew_combobox_7")
        self.ew_combobox_7.addItem("")
        self.ew_combobox_7.addItem("")
        self.ew_combobox_7.addItem("")
        self.ew_combobox_7.addItem("")
        self.horizontalLayout_20.addWidget(self.ew_combobox_7)
        spacerItem27 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem27)
        self.info_button_9 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.info_button_9.setEnabled(False)
        self.info_button_9.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_9.setText("")
        self.info_button_9.setIcon(icon1)
        self.info_button_9.setIconSize(QtCore.QSize(23, 23))
        self.info_button_9.setAutoRaise(False)
        self.info_button_9.setObjectName("info_button_9")
        self.horizontalLayout_20.addWidget(self.info_button_9)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem28)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.ew_label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_13.setEnabled(False)
        self.ew_label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_13.setFont(font)
        self.ew_label_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ew_label_13.setObjectName("ew_label_13")
        self.horizontalLayout_22.addWidget(self.ew_label_13)
        self.ew_combobox_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.ew_combobox_8.setEnabled(False)
        self.ew_combobox_8.setMinimumSize(QtCore.QSize(120, 27))
        self.ew_combobox_8.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_combobox_8.setFont(font)
        self.ew_combobox_8.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_combobox_8.setObjectName("ew_combobox_8")
        self.ew_combobox_8.addItem("")
        self.ew_combobox_8.addItem("")
        self.ew_combobox_8.addItem("")
        self.horizontalLayout_22.addWidget(self.ew_combobox_8)
        spacerItem29 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem29)
        self.info_button_10 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.info_button_10.setEnabled(False)
        self.info_button_10.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_10.setText("")
        self.info_button_10.setIcon(icon1)
        self.info_button_10.setIconSize(QtCore.QSize(23, 23))
        self.info_button_10.setAutoRaise(False)
        self.info_button_10.setObjectName("info_button_10")
        self.horizontalLayout_22.addWidget(self.info_button_10)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem30)
        self.verticalLayout_2.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.ew_checkbox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.ew_checkbox_4.setEnabled(False)
        self.ew_checkbox_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_checkbox_4.setFont(font)
        self.ew_checkbox_4.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_checkbox_4.setObjectName("ew_checkbox_4")
        self.horizontalLayout_21.addWidget(self.ew_checkbox_4)
        spacerItem31 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem31)
        self.info_button_11 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.info_button_11.setEnabled(False)
        self.info_button_11.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_11.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_11.setText("")
        self.info_button_11.setIcon(icon1)
        self.info_button_11.setIconSize(QtCore.QSize(23, 23))
        self.info_button_11.setAutoRaise(False)
        self.info_button_11.setObjectName("info_button_11")
        self.horizontalLayout_21.addWidget(self.info_button_11)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem32)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.ew_checkbox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.ew_checkbox_5.setEnabled(False)
        self.ew_checkbox_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_checkbox_5.setFont(font)
        self.ew_checkbox_5.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_checkbox_5.setChecked(True)
        self.ew_checkbox_5.setObjectName("ew_checkbox_5")
        self.horizontalLayout_23.addWidget(self.ew_checkbox_5)
        spacerItem33 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem33)
        self.info_button_12 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.info_button_12.setEnabled(False)
        self.info_button_12.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_12.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_12.setText("")
        self.info_button_12.setIcon(icon1)
        self.info_button_12.setIconSize(QtCore.QSize(23, 23))
        self.info_button_12.setAutoRaise(False)
        self.info_button_12.setObjectName("info_button_12")
        self.horizontalLayout_23.addWidget(self.info_button_12)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem34)
        self.verticalLayout_2.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem35)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ew_label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_14.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_14.sizePolicy().hasHeightForWidth())
        self.ew_label_14.setSizePolicy(sizePolicy)
        self.ew_label_14.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_14.setFont(font)
        self.ew_label_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_14.setObjectName("ew_label_14")
        self.gridLayout_11.addWidget(self.ew_label_14, 0, 0, 1, 1)
        self.ew_line_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_2.setEnabled(False)
        self.ew_line_2.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_2.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_2.setFont(font)
        self.ew_line_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_2.setObjectName("ew_line_2")
        self.gridLayout_11.addWidget(self.ew_line_2, 0, 1, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem36, 0, 2, 2, 1)
        self.ew_label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_16.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_16.sizePolicy().hasHeightForWidth())
        self.ew_label_16.setSizePolicy(sizePolicy)
        self.ew_label_16.setMinimumSize(QtCore.QSize(100, 27))
        self.ew_label_16.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_16.setFont(font)
        self.ew_label_16.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_16.setObjectName("ew_label_16")
        self.gridLayout_11.addWidget(self.ew_label_16, 0, 3, 1, 1)
        self.ew_line_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_4.setEnabled(False)
        self.ew_line_4.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_4.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_4.setFont(font)
        self.ew_line_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_4.setObjectName("ew_line_4")
        self.gridLayout_11.addWidget(self.ew_line_4, 0, 4, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem37, 0, 5, 1, 1)
        self.ew_label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_15.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_15.sizePolicy().hasHeightForWidth())
        self.ew_label_15.setSizePolicy(sizePolicy)
        self.ew_label_15.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_15.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_15.setFont(font)
        self.ew_label_15.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_15.setObjectName("ew_label_15")
        self.gridLayout_11.addWidget(self.ew_label_15, 1, 0, 1, 1)
        self.ew_line_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_3.setEnabled(False)
        self.ew_line_3.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_3.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_3.setFont(font)
        self.ew_line_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_3.setObjectName("ew_line_3")
        self.gridLayout_11.addWidget(self.ew_line_3, 1, 1, 1, 1)
        self.ew_ticks_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.ew_ticks_button.setEnabled(False)
        self.ew_ticks_button.setMinimumSize(QtCore.QSize(160, 27))
        self.ew_ticks_button.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ew_ticks_button.setFont(font)
        self.ew_ticks_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.ew_ticks_button.setIconSize(QtCore.QSize(25, 25))
        self.ew_ticks_button.setObjectName("ew_ticks_button")
        self.gridLayout_11.addWidget(self.ew_ticks_button, 1, 3, 1, 2)
        self.pw_grid_label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.pw_grid_label_57.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pw_grid_label_57.sizePolicy().hasHeightForWidth())
        self.pw_grid_label_57.setSizePolicy(sizePolicy)
        self.pw_grid_label_57.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_grid_label_57.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(9)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_label_57.setFont(font)
        self.pw_grid_label_57.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pw_grid_label_57.setText("")
        self.pw_grid_label_57.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pw_grid_label_57.setObjectName("pw_grid_label_57")
        self.gridLayout_11.addWidget(self.pw_grid_label_57, 1, 5, 1, 1)
        self.horizontalLayout_24.addLayout(self.gridLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.ew_checkbox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.ew_checkbox_6.setEnabled(False)
        self.ew_checkbox_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_checkbox_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_checkbox_6.setFont(font)
        self.ew_checkbox_6.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_checkbox_6.setChecked(True)
        self.ew_checkbox_6.setObjectName("ew_checkbox_6")
        self.horizontalLayout_25.addWidget(self.ew_checkbox_6)
        spacerItem38 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem38)
        self.info_button_13 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.info_button_13.setEnabled(False)
        self.info_button_13.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_13.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_13.setText("")
        self.info_button_13.setIcon(icon1)
        self.info_button_13.setIconSize(QtCore.QSize(23, 23))
        self.info_button_13.setAutoRaise(False)
        self.info_button_13.setObjectName("info_button_13")
        self.horizontalLayout_25.addWidget(self.info_button_13)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem39)
        self.verticalLayout_2.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem40)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.ew_label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_17.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_17.sizePolicy().hasHeightForWidth())
        self.ew_label_17.setSizePolicy(sizePolicy)
        self.ew_label_17.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_17.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_17.setFont(font)
        self.ew_label_17.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_17.setObjectName("ew_label_17")
        self.gridLayout_12.addWidget(self.ew_label_17, 0, 0, 1, 1)
        self.ew_line_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_5.setEnabled(False)
        self.ew_line_5.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_5.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_5.setFont(font)
        self.ew_line_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_5.setObjectName("ew_line_5")
        self.gridLayout_12.addWidget(self.ew_line_5, 0, 1, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem41, 0, 2, 1, 1)
        self.ew_label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_20.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_20.sizePolicy().hasHeightForWidth())
        self.ew_label_20.setSizePolicy(sizePolicy)
        self.ew_label_20.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_20.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_20.setFont(font)
        self.ew_label_20.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_20.setObjectName("ew_label_20")
        self.gridLayout_12.addWidget(self.ew_label_20, 0, 3, 1, 1)
        self.ew_line_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_6.setEnabled(False)
        self.ew_line_6.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_6.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_6.setFont(font)
        self.ew_line_6.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_6.setObjectName("ew_line_6")
        self.gridLayout_12.addWidget(self.ew_line_6, 0, 4, 1, 1)
        self.ew_label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_18.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_18.sizePolicy().hasHeightForWidth())
        self.ew_label_18.setSizePolicy(sizePolicy)
        self.ew_label_18.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_18.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_18.setFont(font)
        self.ew_label_18.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_18.setObjectName("ew_label_18")
        self.gridLayout_12.addWidget(self.ew_label_18, 1, 0, 1, 1)
        self.ew_line_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_7.setEnabled(False)
        self.ew_line_7.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_7.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_7.setFont(font)
        self.ew_line_7.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_7.setObjectName("ew_line_7")
        self.gridLayout_12.addWidget(self.ew_line_7, 1, 1, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem42, 1, 2, 1, 1)
        self.ew_label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_21.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_21.sizePolicy().hasHeightForWidth())
        self.ew_label_21.setSizePolicy(sizePolicy)
        self.ew_label_21.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_21.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_21.setFont(font)
        self.ew_label_21.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_21.setObjectName("ew_label_21")
        self.gridLayout_12.addWidget(self.ew_label_21, 1, 3, 1, 1)
        self.ew_line_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_8.setEnabled(False)
        self.ew_line_8.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_8.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_8.setFont(font)
        self.ew_line_8.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_8.setObjectName("ew_line_8")
        self.gridLayout_12.addWidget(self.ew_line_8, 1, 4, 1, 1)
        self.ew_label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_19.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_19.sizePolicy().hasHeightForWidth())
        self.ew_label_19.setSizePolicy(sizePolicy)
        self.ew_label_19.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_19.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_19.setFont(font)
        self.ew_label_19.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_19.setObjectName("ew_label_19")
        self.gridLayout_12.addWidget(self.ew_label_19, 2, 0, 1, 1)
        self.ew_line_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_9.setEnabled(False)
        self.ew_line_9.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_9.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_9.setFont(font)
        self.ew_line_9.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_9.setObjectName("ew_line_9")
        self.gridLayout_12.addWidget(self.ew_line_9, 2, 1, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem43, 2, 2, 1, 1)
        self.ew_label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ew_label_22.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ew_label_22.sizePolicy().hasHeightForWidth())
        self.ew_label_22.setSizePolicy(sizePolicy)
        self.ew_label_22.setMinimumSize(QtCore.QSize(0, 27))
        self.ew_label_22.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_label_22.setFont(font)
        self.ew_label_22.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ew_label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ew_label_22.setObjectName("ew_label_22")
        self.gridLayout_12.addWidget(self.ew_label_22, 2, 3, 1, 1)
        self.ew_line_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ew_line_10.setEnabled(False)
        self.ew_line_10.setMinimumSize(QtCore.QSize(70, 27))
        self.ew_line_10.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ew_line_10.setFont(font)
        self.ew_line_10.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"    \n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ew_line_10.setObjectName("ew_line_10")
        self.gridLayout_12.addWidget(self.ew_line_10, 2, 4, 1, 1)
        self.horizontalLayout_26.addLayout(self.gridLayout_12)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem44)
        self.verticalLayout_2.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_19.addLayout(self.verticalLayout_2)
        self.ew_vertical_layout_4.addLayout(self.horizontalLayout_19)
        self.gridLayout_10.addLayout(self.ew_vertical_layout_4, 0, 0, 1, 1)
        self.ew_scroll_area_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_9.addWidget(self.ew_scroll_area_4, 0, 0, 1, 1)
        self.ew_stacked_widget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pw_grid_checkbox_1 = QtWidgets.QCheckBox(self.page_6)
        self.pw_grid_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_grid_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_checkbox_1.setFont(font)
        self.pw_grid_checkbox_1.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.pw_grid_checkbox_1.setObjectName("pw_grid_checkbox_1")
        self.horizontalLayout_8.addWidget(self.pw_grid_checkbox_1)
        spacerItem45 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem45)
        self.pw_grid_info_button_4 = QtWidgets.QToolButton(self.page_6)
        self.pw_grid_info_button_4.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_grid_info_button_4.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_grid_info_button_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_grid_info_button_4.setIcon(icon1)
        self.pw_grid_info_button_4.setIconSize(QtCore.QSize(23, 23))
        self.pw_grid_info_button_4.setObjectName("pw_grid_info_button_4")
        self.horizontalLayout_8.addWidget(self.pw_grid_info_button_4)
        spacerItem46 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem46)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem47 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem47)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pw_grid_label_23 = QtWidgets.QLabel(self.page_6)
        self.pw_grid_label_23.setEnabled(False)
        self.pw_grid_label_23.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_grid_label_23.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_label_23.setFont(font)
        self.pw_grid_label_23.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pw_grid_label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pw_grid_label_23.setObjectName("pw_grid_label_23")
        self.gridLayout_13.addWidget(self.pw_grid_label_23, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pw_grid_combobox_8 = QtWidgets.QComboBox(self.page_6)
        self.pw_grid_combobox_8.setEnabled(False)
        self.pw_grid_combobox_8.setMinimumSize(QtCore.QSize(140, 27))
        self.pw_grid_combobox_8.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_combobox_8.setFont(font)
        self.pw_grid_combobox_8.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_grid_combobox_8.setFrame(False)
        self.pw_grid_combobox_8.setObjectName("pw_grid_combobox_8")
        self.pw_grid_combobox_8.addItem("")
        self.pw_grid_combobox_8.addItem("")
        self.pw_grid_combobox_8.addItem("")
        self.pw_grid_combobox_8.addItem("")
        self.horizontalLayout_9.addWidget(self.pw_grid_combobox_8)
        spacerItem48 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem48)
        self.pw_grid_label_24 = QtWidgets.QLabel(self.page_6)
        self.pw_grid_label_24.setEnabled(False)
        self.pw_grid_label_24.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_grid_label_24.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_label_24.setFont(font)
        self.pw_grid_label_24.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pw_grid_label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pw_grid_label_24.setObjectName("pw_grid_label_24")
        self.horizontalLayout_9.addWidget(self.pw_grid_label_24)
        self.pw_grid_line_4 = QtWidgets.QLineEdit(self.page_6)
        self.pw_grid_line_4.setEnabled(False)
        self.pw_grid_line_4.setMinimumSize(QtCore.QSize(60, 27))
        self.pw_grid_line_4.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_line_4.setFont(font)
        self.pw_grid_line_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_grid_line_4.setObjectName("pw_grid_line_4")
        self.horizontalLayout_9.addWidget(self.pw_grid_line_4)
        spacerItem49 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem49)
        self.gridLayout_13.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.pw_grid_label_25 = QtWidgets.QLabel(self.page_6)
        self.pw_grid_label_25.setEnabled(False)
        self.pw_grid_label_25.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_grid_label_25.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_label_25.setFont(font)
        self.pw_grid_label_25.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pw_grid_label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pw_grid_label_25.setObjectName("pw_grid_label_25")
        self.gridLayout_13.addWidget(self.pw_grid_label_25, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pw_grid_combobox_18 = QtWidgets.QComboBox(self.page_6)
        self.pw_grid_combobox_18.setEnabled(False)
        self.pw_grid_combobox_18.setMinimumSize(QtCore.QSize(170, 27))
        self.pw_grid_combobox_18.setMaximumSize(QtCore.QSize(170, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_combobox_18.setFont(font)
        self.pw_grid_combobox_18.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_grid_combobox_18.setFrame(False)
        self.pw_grid_combobox_18.setObjectName("pw_grid_combobox_18")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.pw_grid_combobox_18.addItem("")
        self.horizontalLayout_10.addWidget(self.pw_grid_combobox_18)
        self.pw_grid_line_28 = QtWidgets.QLineEdit(self.page_6)
        self.pw_grid_line_28.setEnabled(False)
        self.pw_grid_line_28.setMinimumSize(QtCore.QSize(60, 27))
        self.pw_grid_line_28.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_line_28.setFont(font)
        self.pw_grid_line_28.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_grid_line_28.setObjectName("pw_grid_line_28")
        self.horizontalLayout_10.addWidget(self.pw_grid_line_28)
        self.pw_grid_line_27 = QtWidgets.QLineEdit(self.page_6)
        self.pw_grid_line_27.setEnabled(False)
        self.pw_grid_line_27.setMinimumSize(QtCore.QSize(60, 27))
        self.pw_grid_line_27.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_line_27.setFont(font)
        self.pw_grid_line_27.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_grid_line_27.setObjectName("pw_grid_line_27")
        self.horizontalLayout_10.addWidget(self.pw_grid_line_27)
        self.pw_grid_line_26 = QtWidgets.QLineEdit(self.page_6)
        self.pw_grid_line_26.setEnabled(False)
        self.pw_grid_line_26.setMinimumSize(QtCore.QSize(60, 27))
        self.pw_grid_line_26.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_grid_line_26.setFont(font)
        self.pw_grid_line_26.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_grid_line_26.setObjectName("pw_grid_line_26")
        self.horizontalLayout_10.addWidget(self.pw_grid_line_26)
        spacerItem50 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem50)
        self.gridLayout_13.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        self.horizontalLayout_11.addLayout(self.gridLayout_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.gridLayout_14.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.ew_stacked_widget.addWidget(self.page_6)
        self.gridLayout_15.addWidget(self.ew_splitter, 2, 0, 1, 2)
        spacerItem51 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_15.addItem(spacerItem51, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ew_export_button = QtWidgets.QToolButton(exportWindow)
        self.ew_export_button.setEnabled(False)
        self.ew_export_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ew_export_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ew_export_button.setFont(font)
        self.ew_export_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.ew_export_button.setObjectName("ew_export_button")
        self.horizontalLayout_2.addWidget(self.ew_export_button)
        spacerItem52 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem52)
        self.ew_cancel_button = QtWidgets.QToolButton(exportWindow)
        self.ew_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ew_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ew_cancel_button.setFont(font)
        self.ew_cancel_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.ew_cancel_button.setObjectName("ew_cancel_button")
        self.horizontalLayout_2.addWidget(self.ew_cancel_button)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem53)
        self.gridLayout_15.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)

        self.retranslateUi(exportWindow)
        self.ew_stacked_widget.setCurrentIndex(0)
        self.pw_grid_combobox_18.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(exportWindow)

    def retranslateUi(self, exportWindow):
        _translate = QtCore.QCoreApplication.translate
        exportWindow.setWindowTitle(_translate("exportWindow", "Export to"))
        self.ew_label_1.setText(_translate("exportWindow", "Choose a format:"))
        self.ew_combobox_1.setItemText(0, _translate("exportWindow", "Make a choice..."))
        self.ew_combobox_1.setItemText(1, _translate("exportWindow", "Google Earth - Time series"))
        self.ew_combobox_1.setItemText(2, _translate("exportWindow", "Google Earth - Map"))
        self.ew_label_2.setText(_translate("exportWindow", "Longitude:"))
        self.ew_combobox_2.setItemText(0, _translate("exportWindow", "Make a choice..."))
        self.ew_label_3.setText(_translate("exportWindow", "Latitude:"))
        self.ew_combobox_3.setItemText(0, _translate("exportWindow", "Make a choice..."))
        self.ew_label_4.setText(_translate("exportWindow", "Altitude:"))
        self.ew_combobox_4.setItemText(0, _translate("exportWindow", "Make a choice..."))
        self.ew_label_24.setText(_translate("exportWindow", "Navigate into layer:"))
        self.ew_label_5.setText(_translate("exportWindow", "Add one or more variables:"))
        self.ew_label_6.setText(_translate("exportWindow", "Variable(s) displayed in Google Earth:"))
        self.ew_label_7.setText(_translate("exportWindow", "Path width:"))
        self.ew_label_8.setText(_translate("exportWindow", "5 px"))
        self.ew_checkbox_1.setText(_translate("exportWindow", "Connect path to ground"))
        self.ew_checkbox_2.setText(_translate("exportWindow", "Add transparency to the wall"))
        self.ew_label_9.setText(_translate("exportWindow", "Transparency:"))
        self.ew_label_23.setText(_translate("exportWindow", "0 %"))
        self.ew_checkbox_3.setText(_translate("exportWindow", "Reduce the number of samples in time series"))
        self.ew_label_10.setText(_translate("exportWindow", "Keep 1 sample on:"))
        self.ew_label_11.setText(_translate("exportWindow", "Choose a colormap:"))
        self.ew_combobox_6.setItemText(0, _translate("exportWindow", "Make a choice..."))
        self.ew_label_12.setText(_translate("exportWindow", "Colormap position:"))
        self.ew_combobox_7.setItemText(0, _translate("exportWindow", "horizontal - bottom"))
        self.ew_combobox_7.setItemText(1, _translate("exportWindow", "horizontal - top"))
        self.ew_combobox_7.setItemText(2, _translate("exportWindow", "vertical - left"))
        self.ew_combobox_7.setItemText(3, _translate("exportWindow", "vertical - right"))
        self.ew_label_13.setText(_translate("exportWindow", "Value used for colorization:"))
        self.ew_combobox_8.setItemText(0, _translate("exportWindow", "mean"))
        self.ew_combobox_8.setItemText(1, _translate("exportWindow", "first point"))
        self.ew_combobox_8.setItemText(2, _translate("exportWindow", "last point"))
        self.ew_checkbox_4.setText(_translate("exportWindow", "Reverse colormap ?"))
        self.ew_checkbox_5.setText(_translate("exportWindow", "Handle colormap values automatically ?"))
        self.ew_label_14.setText(_translate("exportWindow", "Min:"))
        self.ew_label_16.setText(_translate("exportWindow", "Nbr of steps:"))
        self.ew_label_15.setText(_translate("exportWindow", "Max:"))
        self.ew_ticks_button.setText(_translate("exportWindow", "Set colorbar ticks"))
        self.ew_checkbox_6.setText(_translate("exportWindow", "Handle colormap dimensions automatically ?"))
        self.ew_label_17.setText(_translate("exportWindow", "Figure width:"))
        self.ew_label_20.setText(_translate("exportWindow", "Figure height:"))
        self.ew_label_18.setText(_translate("exportWindow", "Position from left:"))
        self.ew_label_21.setText(_translate("exportWindow", "Colormap width:"))
        self.ew_label_19.setText(_translate("exportWindow", "Position from bottom:"))
        self.ew_label_22.setText(_translate("exportWindow", "Colormap height:"))
        self.pw_grid_checkbox_1.setText(_translate("exportWindow", "Display grid ?"))
        self.pw_grid_label_23.setText(_translate("exportWindow", "Line style:"))
        self.pw_grid_combobox_8.setItemText(0, _translate("exportWindow", "Dashed"))
        self.pw_grid_combobox_8.setItemText(1, _translate("exportWindow", "Dash-dot"))
        self.pw_grid_combobox_8.setItemText(2, _translate("exportWindow", "Dotted"))
        self.pw_grid_combobox_8.setItemText(3, _translate("exportWindow", "Solid"))
        self.pw_grid_label_24.setText(_translate("exportWindow", "Line size:"))
        self.pw_grid_label_25.setText(_translate("exportWindow", "Line color:"))
        self.pw_grid_combobox_18.setItemText(0, _translate("exportWindow", "HEX Color"))
        self.pw_grid_combobox_18.setItemText(1, _translate("exportWindow", "RGB Color"))
        self.pw_grid_combobox_18.setItemText(2, _translate("exportWindow", "Black"))
        self.pw_grid_combobox_18.setItemText(3, _translate("exportWindow", "Blue"))
        self.pw_grid_combobox_18.setItemText(4, _translate("exportWindow", "Cyan"))
        self.pw_grid_combobox_18.setItemText(5, _translate("exportWindow", "Green"))
        self.pw_grid_combobox_18.setItemText(6, _translate("exportWindow", "Magenta"))
        self.pw_grid_combobox_18.setItemText(7, _translate("exportWindow", "Red"))
        self.pw_grid_combobox_18.setItemText(8, _translate("exportWindow", "Yellow"))
        self.pw_grid_combobox_18.setItemText(9, _translate("exportWindow", "White"))
        self.ew_export_button.setText(_translate("exportWindow", "Export"))
        self.ew_cancel_button.setText(_translate("exportWindow", "Cancel"))

