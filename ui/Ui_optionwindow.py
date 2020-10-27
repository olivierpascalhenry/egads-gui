# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(700, 350)
        optionWindow.setMinimumSize(QtCore.QSize(0, 0))
        optionWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionWindow.setWindowIcon(icon)
        optionWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
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
        self.gridLayout_15 = QtWidgets.QGridLayout(optionWindow)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_15.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ow_ok_button = QtWidgets.QToolButton(optionWindow)
        self.ow_ok_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_ok_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_ok_button.setFont(font)
        self.ow_ok_button.setStyleSheet("QToolButton {\n"
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
        self.ow_ok_button.setObjectName("ow_ok_button")
        self.horizontalLayout_2.addWidget(self.ow_ok_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ow_cancel_button = QtWidgets.QToolButton(optionWindow)
        self.ow_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.ow_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_cancel_button.setFont(font)
        self.ow_cancel_button.setStyleSheet("QToolButton {\n"
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
        self.ow_cancel_button.setObjectName("ow_cancel_button")
        self.horizontalLayout_2.addWidget(self.ow_cancel_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_15.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.ow_splitter = QtWidgets.QSplitter(optionWindow)
        self.ow_splitter.setStyleSheet("QSplitter::handle {\n"
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
        self.ow_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.ow_splitter.setObjectName("ow_splitter")
        self.ow_section_list = QtWidgets.QListWidget(self.ow_splitter)
        self.ow_section_list.setEnabled(True)
        self.ow_section_list.setMinimumSize(QtCore.QSize(0, 0))
        self.ow_section_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_section_list.setFont(font)
        self.ow_section_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ow_section_list.setStyleSheet("QListWidget {\n"
"    border-radius: 0px;\n"
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
        self.ow_section_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_section_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ow_section_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ow_section_list.setObjectName("ow_section_list")
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        self.ow_stacked_widget = QtWidgets.QStackedWidget(self.ow_splitter)
        self.ow_stacked_widget.setObjectName("ow_stacked_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ow_scroll_area_1 = QtWidgets.QScrollArea(self.page_1)
        self.ow_scroll_area_1.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.ow_scroll_area_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_1.setWidgetResizable(True)
        self.ow_scroll_area_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_1.setObjectName("ow_scroll_area_1")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 548, 266))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ow_vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_2.setObjectName("ow_vertical_layout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ow_checkbox_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_1.setFont(font)
        self.ow_checkbox_1.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_1.setObjectName("ow_checkbox_1")
        self.horizontalLayout_8.addWidget(self.ow_checkbox_1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.info_button_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
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
        self.horizontalLayout_8.addWidget(self.info_button_1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ow_checkbox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_2.setFont(font)
        self.ow_checkbox_2.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_2.setObjectName("ow_checkbox_2")
        self.horizontalLayout_10.addWidget(self.ow_checkbox_2)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
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
        self.horizontalLayout_10.addWidget(self.info_button_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.ow_checkbox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.ow_checkbox_3.setEnabled(False)
        self.ow_checkbox_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_3.setFont(font)
        self.ow_checkbox_3.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_checkbox_3.setObjectName("ow_checkbox_3")
        self.horizontalLayout_11.addWidget(self.ow_checkbox_3)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.info_button_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
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
        self.horizontalLayout_11.addWidget(self.info_button_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_11)
        self.gridLayout_2.addLayout(self.ow_vertical_layout_2, 0, 0, 1, 1)
        self.ow_scroll_area_1.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.ow_scroll_area_1, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_13.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.ow_scroll_area_5 = QtWidgets.QScrollArea(self.page_2)
        self.ow_scroll_area_5.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.ow_scroll_area_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_5.setWidgetResizable(True)
        self.ow_scroll_area_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_5.setObjectName("ow_scroll_area_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 461, 197))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.ow_checkbox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.ow_checkbox_7.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_7.setFont(font)
        self.ow_checkbox_7.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_7.setObjectName("ow_checkbox_7")
        self.horizontalLayout_20.addWidget(self.ow_checkbox_7)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem10)
        self.info_button_13 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
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
        self.horizontalLayout_20.addWidget(self.info_button_13)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.ow_checkbox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.ow_checkbox_8.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_8.setFont(font)
        self.ow_checkbox_8.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_8.setObjectName("ow_checkbox_8")
        self.horizontalLayout_21.addWidget(self.ow_checkbox_8)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem12)
        self.info_button_14 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.info_button_14.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_14.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_14.setText("")
        self.info_button_14.setIcon(icon1)
        self.info_button_14.setIconSize(QtCore.QSize(23, 23))
        self.info_button_14.setAutoRaise(False)
        self.info_button_14.setObjectName("info_button_14")
        self.horizontalLayout_21.addWidget(self.info_button_14)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.ow_label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.ow_label_9.setEnabled(False)
        self.ow_label_9.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_label_9.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_9.setFont(font)
        self.ow_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_9.setObjectName("ow_label_9")
        self.horizontalLayout_22.addWidget(self.ow_label_9)
        self.ow_line_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.ow_line_3.setEnabled(False)
        self.ow_line_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_line_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_3.setFont(font)
        self.ow_line_3.setStyleSheet("QLineEdit {\n"
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
        self.ow_line_3.setObjectName("ow_line_3")
        self.horizontalLayout_22.addWidget(self.ow_line_3)
        self.ow_openButton_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.ow_openButton_3.setEnabled(False)
        self.ow_openButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_openButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_openButton_3.setIcon(icon2)
        self.ow_openButton_3.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_3.setAutoRaise(False)
        self.ow_openButton_3.setObjectName("ow_openButton_3")
        self.horizontalLayout_22.addWidget(self.ow_openButton_3)
        spacerItem14 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem14)
        self.ow_addButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.ow_addButton_1.setEnabled(False)
        self.ow_addButton_1.setMinimumSize(QtCore.QSize(27, 27))
        self.ow_addButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_addButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_addButton_1.setIcon(icon3)
        self.ow_addButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_addButton_1.setObjectName("ow_addButton_1")
        self.horizontalLayout_22.addWidget(self.ow_addButton_1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.ow_label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.ow_label_10.setEnabled(False)
        self.ow_label_10.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_label_10.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_10.setFont(font)
        self.ow_label_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.ow_label_10.setObjectName("ow_label_10")
        self.horizontalLayout_24.addWidget(self.ow_label_10)
        self.ow_folderList_1 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_5)
        self.ow_folderList_1.setEnabled(False)
        self.ow_folderList_1.setMinimumSize(QtCore.QSize(0, 0))
        self.ow_folderList_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_folderList_1.setFont(font)
        self.ow_folderList_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ow_folderList_1.setStyleSheet("QListWidget {\n"
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
        self.ow_folderList_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_folderList_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ow_folderList_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ow_folderList_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ow_folderList_1.setObjectName("ow_folderList_1")
        self.horizontalLayout_24.addWidget(self.ow_folderList_1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.bw_del_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.bw_del_button.setEnabled(False)
        self.bw_del_button.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_del_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_del_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_del_button.setIcon(icon4)
        self.bw_del_button.setIconSize(QtCore.QSize(23, 23))
        self.bw_del_button.setAutoRaise(False)
        self.bw_del_button.setObjectName("bw_del_button")
        self.horizontalLayout_23.addWidget(self.bw_del_button)
        spacerItem16 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem16)
        self.ow_noneButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.ow_noneButton_1.setEnabled(False)
        self.ow_noneButton_1.setMinimumSize(QtCore.QSize(27, 27))
        self.ow_noneButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_noneButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_noneButton_1.setIcon(icon5)
        self.ow_noneButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_noneButton_1.setObjectName("ow_noneButton_1")
        self.horizontalLayout_23.addWidget(self.ow_noneButton_1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem18)
        self.horizontalLayout_24.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_24)
        self.gridLayout_12.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.ow_scroll_area_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_13.addWidget(self.ow_scroll_area_5, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.ow_scroll_area_6 = QtWidgets.QScrollArea(self.page_3)
        self.ow_scroll_area_6.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.ow_scroll_area_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_6.setWidgetResizable(True)
        self.ow_scroll_area_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_6.setObjectName("ow_scroll_area_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 431, 31))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.ow_vertical_layout_5 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_5.setObjectName("ow_vertical_layout_5")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.ow_checkbox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        self.ow_checkbox_11.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_11.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_11.setFont(font)
        self.ow_checkbox_11.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_checkbox_11.setChecked(True)
        self.ow_checkbox_11.setObjectName("ow_checkbox_11")
        self.horizontalLayout_28.addWidget(self.ow_checkbox_11)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem19)
        self.info_button_17 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.info_button_17.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_17.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_17.setText("")
        self.info_button_17.setIcon(icon1)
        self.info_button_17.setIconSize(QtCore.QSize(23, 23))
        self.info_button_17.setAutoRaise(False)
        self.info_button_17.setObjectName("info_button_17")
        self.horizontalLayout_28.addWidget(self.info_button_17)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem20)
        self.ow_vertical_layout_5.addLayout(self.horizontalLayout_28)
        self.gridLayout_16.addLayout(self.ow_vertical_layout_5, 0, 0, 1, 1)
        self.ow_scroll_area_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_17.addWidget(self.ow_scroll_area_6, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ow_scroll_area_2 = QtWidgets.QScrollArea(self.page_4)
        self.ow_scroll_area_2.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.ow_scroll_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_2.setWidgetResizable(True)
        self.ow_scroll_area_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_2.setObjectName("ow_scroll_area_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 324, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ow_vertical_layout = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout.setObjectName("ow_vertical_layout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ow_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_1.setFont(font)
        self.ow_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_1.setObjectName("ow_label_1")
        self.horizontalLayout_3.addWidget(self.ow_label_1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.ow_vertical_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem22)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ow_line_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ow_line_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_line_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_1.setFont(font)
        self.ow_line_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_1.setObjectName("ow_line_1")
        self.horizontalLayout.addWidget(self.ow_line_1)
        self.ow_openButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ow_openButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_openButton_1.setText("")
        self.ow_openButton_1.setIcon(icon2)
        self.ow_openButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_1.setAutoRaise(False)
        self.ow_openButton_1.setObjectName("ow_openButton_1")
        self.horizontalLayout.addWidget(self.ow_openButton_1)
        spacerItem23 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.info_button_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
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
        self.horizontalLayout.addWidget(self.info_button_5)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.ow_label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_3.setFont(font)
        self.ow_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_3.setObjectName("ow_label_3")
        self.gridLayout_3.addWidget(self.ow_label_3, 1, 0, 1, 1)
        self.ow_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_2.setFont(font)
        self.ow_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_2.setObjectName("ow_label_2")
        self.gridLayout_3.addWidget(self.ow_label_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ow_combobox_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ow_combobox_1.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_combobox_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_1.setFont(font)
        self.ow_combobox_1.setStyleSheet("QComboBox {\n"
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
        self.ow_combobox_1.setObjectName("ow_combobox_1")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.horizontalLayout_7.addWidget(self.ow_combobox_1)
        spacerItem24 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem24)
        self.info_button_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
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
        self.horizontalLayout_7.addWidget(self.info_button_4)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem25)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)
        self.ow_vertical_layout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ow_label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_4.setFont(font)
        self.ow_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_4.setObjectName("ow_label_4")
        self.horizontalLayout_4.addWidget(self.ow_label_4)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem26)
        self.ow_vertical_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem27)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ow_line_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ow_line_2.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_line_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_2.setFont(font)
        self.ow_line_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_2.setObjectName("ow_line_2")
        self.horizontalLayout_9.addWidget(self.ow_line_2)
        self.ow_openButton_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ow_openButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ow_openButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_openButton_2.setText("")
        self.ow_openButton_2.setIcon(icon2)
        self.ow_openButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ow_openButton_2.setAutoRaise(False)
        self.ow_openButton_2.setObjectName("ow_openButton_2")
        self.horizontalLayout_9.addWidget(self.ow_openButton_2)
        spacerItem28 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem28)
        self.info_button_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
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
        self.horizontalLayout_9.addWidget(self.info_button_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        self.ow_label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_6.setFont(font)
        self.ow_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_6.setObjectName("ow_label_6")
        self.gridLayout_4.addWidget(self.ow_label_6, 1, 0, 1, 1)
        self.ow_label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_5.setFont(font)
        self.ow_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_5.setObjectName("ow_label_5")
        self.gridLayout_4.addWidget(self.ow_label_5, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.ow_combobox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ow_combobox_2.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_combobox_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_2.setFont(font)
        self.ow_combobox_2.setStyleSheet("QComboBox {\n"
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
        self.ow_combobox_2.setObjectName("ow_combobox_2")
        self.ow_combobox_2.addItem("")
        self.ow_combobox_2.addItem("")
        self.ow_combobox_2.addItem("")
        self.ow_combobox_2.addItem("")
        self.ow_combobox_2.addItem("")
        self.horizontalLayout_12.addWidget(self.ow_combobox_2)
        spacerItem29 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem29)
        self.info_button_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
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
        self.horizontalLayout_12.addWidget(self.info_button_6)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem30)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.ow_vertical_layout.addLayout(self.horizontalLayout_5)
        self.gridLayout_6.addLayout(self.ow_vertical_layout, 0, 0, 1, 1)
        self.ow_scroll_area_2.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.ow_scroll_area_2, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_7.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ow_scroll_area_3 = QtWidgets.QScrollArea(self.page_5)
        self.ow_scroll_area_3.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.ow_scroll_area_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_3.setWidgetResizable(True)
        self.ow_scroll_area_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_3.setObjectName("ow_scroll_area_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 515, 247))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.ow_vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_3.setObjectName("ow_vertical_layout_3")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ow_label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_8.setFont(font)
        self.ow_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_8.setObjectName("ow_label_8")
        self.gridLayout_8.addWidget(self.ow_label_8, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.ow_combobox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.ow_combobox_3.setMinimumSize(QtCore.QSize(190, 27))
        self.ow_combobox_3.setMaximumSize(QtCore.QSize(190, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_3.setFont(font)
        self.ow_combobox_3.setStyleSheet("QComboBox {\n"
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
        self.ow_combobox_3.setObjectName("ow_combobox_3")
        self.ow_combobox_3.addItem("")
        self.ow_combobox_3.addItem("")
        self.ow_combobox_3.addItem("")
        self.horizontalLayout_13.addWidget(self.ow_combobox_3)
        spacerItem31 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem31)
        self.info_button_8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
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
        self.horizontalLayout_13.addWidget(self.info_button_8)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem32)
        self.gridLayout_8.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)
        self.ow_label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_7.setFont(font)
        self.ow_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_7.setObjectName("ow_label_7")
        self.gridLayout_8.addWidget(self.ow_label_7, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ow_combobox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.ow_combobox_4.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_combobox_4.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_4.setFont(font)
        self.ow_combobox_4.setStyleSheet("QComboBox {\n"
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
        self.ow_combobox_4.setObjectName("ow_combobox_4")
        self.ow_combobox_4.addItem("")
        self.ow_combobox_4.addItem("")
        self.horizontalLayout_14.addWidget(self.ow_combobox_4)
        spacerItem33 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem33)
        self.info_button_9 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
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
        self.horizontalLayout_14.addWidget(self.info_button_9)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem34)
        self.gridLayout_8.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)
        self.ow_vertical_layout_3.addLayout(self.gridLayout_8)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.ow_checkbox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ow_checkbox_9.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_9.setFont(font)
        self.ow_checkbox_9.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_checkbox_9.setObjectName("ow_checkbox_9")
        self.horizontalLayout_26.addWidget(self.ow_checkbox_9)
        spacerItem35 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem35)
        self.info_button_15 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_button_15.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_15.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_15.setText("")
        self.info_button_15.setIcon(icon1)
        self.info_button_15.setIconSize(QtCore.QSize(23, 23))
        self.info_button_15.setAutoRaise(False)
        self.info_button_15.setObjectName("info_button_15")
        self.horizontalLayout_26.addWidget(self.info_button_15)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem36)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem37 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem37)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ow_label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_12.setEnabled(False)
        self.ow_label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_12.setFont(font)
        self.ow_label_12.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_12.setObjectName("ow_label_12")
        self.gridLayout_9.addWidget(self.ow_label_12, 0, 0, 1, 1)
        self.ow_combobox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.ow_combobox_5.setEnabled(False)
        self.ow_combobox_5.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_combobox_5.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_5.setFont(font)
        self.ow_combobox_5.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.ow_combobox_5.setObjectName("ow_combobox_5")
        self.ow_combobox_5.addItem("")
        self.ow_combobox_5.addItem("")
        self.ow_combobox_5.addItem("")
        self.ow_combobox_5.addItem("")
        self.gridLayout_9.addWidget(self.ow_combobox_5, 0, 1, 1, 1)
        self.ow_label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_13.setEnabled(False)
        self.ow_label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_13.setFont(font)
        self.ow_label_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_13.setObjectName("ow_label_13")
        self.gridLayout_9.addWidget(self.ow_label_13, 1, 0, 1, 1)
        self.ow_combobox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.ow_combobox_6.setEnabled(False)
        self.ow_combobox_6.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_combobox_6.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_6.setFont(font)
        self.ow_combobox_6.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.ow_combobox_6.setObjectName("ow_combobox_6")
        self.ow_combobox_6.addItem("")
        self.ow_combobox_6.addItem("")
        self.ow_combobox_6.addItem("")
        self.ow_combobox_6.addItem("")
        self.gridLayout_9.addWidget(self.ow_combobox_6, 1, 1, 1, 1)
        self.ow_label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_14.setEnabled(False)
        self.ow_label_14.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_14.setFont(font)
        self.ow_label_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ow_label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_14.setObjectName("ow_label_14")
        self.gridLayout_9.addWidget(self.ow_label_14, 2, 0, 1, 1)
        self.ow_combobox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.ow_combobox_7.setEnabled(False)
        self.ow_combobox_7.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_combobox_7.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_7.setFont(font)
        self.ow_combobox_7.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.ow_combobox_7.setObjectName("ow_combobox_7")
        self.ow_combobox_7.addItem("")
        self.ow_combobox_7.addItem("")
        self.ow_combobox_7.addItem("")
        self.ow_combobox_7.addItem("")
        self.gridLayout_9.addWidget(self.ow_combobox_7, 2, 1, 1, 1)
        self.horizontalLayout_25.addLayout(self.gridLayout_9)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem38)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.ow_checkbox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.ow_checkbox_10.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_10.setFont(font)
        self.ow_checkbox_10.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_10.setObjectName("ow_checkbox_10")
        self.horizontalLayout_27.addWidget(self.ow_checkbox_10)
        spacerItem39 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem39)
        self.info_button_16 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.info_button_16.setMaximumSize(QtCore.QSize(27, 27))
        self.info_button_16.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.info_button_16.setText("")
        self.info_button_16.setIcon(icon1)
        self.info_button_16.setIconSize(QtCore.QSize(23, 23))
        self.info_button_16.setAutoRaise(False)
        self.info_button_16.setObjectName("info_button_16")
        self.horizontalLayout_27.addWidget(self.info_button_16)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem40)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_27)
        self.gridLayout_14.addLayout(self.ow_vertical_layout_3, 0, 0, 1, 1)
        self.ow_scroll_area_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.addWidget(self.ow_scroll_area_3, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_10.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ow_scroll_area_4 = QtWidgets.QScrollArea(self.page_6)
        self.ow_scroll_area_4.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.ow_scroll_area_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_4.setWidgetResizable(True)
        self.ow_scroll_area_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_4.setObjectName("ow_scroll_area_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 510, 139))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ow_vertical_layout_4 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_4.setObjectName("ow_vertical_layout_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.ow_checkbox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.ow_checkbox_4.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_4.setFont(font)
        self.ow_checkbox_4.setStyleSheet("QCheckBox {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_4.setObjectName("ow_checkbox_4")
        self.horizontalLayout_15.addWidget(self.ow_checkbox_4)
        spacerItem41 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem41)
        self.info_button_10 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
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
        self.horizontalLayout_15.addWidget(self.info_button_10)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem42)
        self.ow_vertical_layout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem43 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem43)
        self.ow_check_button_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.ow_check_button_1.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_check_button_1.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_check_button_1.setFont(font)
        self.ow_check_button_1.setStyleSheet("QToolButton {\n"
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
        self.ow_check_button_1.setObjectName("ow_check_button_1")
        self.horizontalLayout_16.addWidget(self.ow_check_button_1)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem44)
        self.ow_vertical_layout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.ow_checkbox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.ow_checkbox_5.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_checkbox_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_checkbox_5.setFont(font)
        self.ow_checkbox_5.setStyleSheet("QCheckBox {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_checkbox_5.setObjectName("ow_checkbox_5")
        self.horizontalLayout_17.addWidget(self.ow_checkbox_5)
        spacerItem45 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem45)
        self.info_button_11 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
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
        self.horizontalLayout_17.addWidget(self.info_button_11)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem46)
        self.ow_vertical_layout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem47 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem47)
        self.ow_check_button_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.ow_check_button_2.setMinimumSize(QtCore.QSize(120, 27))
        self.ow_check_button_2.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_check_button_2.setFont(font)
        self.ow_check_button_2.setStyleSheet("QToolButton {\n"
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
        self.ow_check_button_2.setObjectName("ow_check_button_2")
        self.horizontalLayout_18.addWidget(self.ow_check_button_2)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem48)
        self.ow_vertical_layout_4.addLayout(self.horizontalLayout_18)
        self.gridLayout_11.addLayout(self.ow_vertical_layout_4, 0, 0, 1, 1)
        self.ow_scroll_area_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.addWidget(self.ow_scroll_area_4, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_6)
        self.gridLayout_15.addWidget(self.ow_splitter, 0, 0, 1, 1)

        self.retranslateUi(optionWindow)
        self.ow_stacked_widget.setCurrentIndex(0)
        self.ow_combobox_3.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "Options"))
        self.ow_ok_button.setText(_translate("optionWindow", "Ok"))
        self.ow_cancel_button.setText(_translate("optionWindow", "Cancel"))
        __sortingEnabled = self.ow_section_list.isSortingEnabled()
        self.ow_section_list.setSortingEnabled(False)
        item = self.ow_section_list.item(0)
        item.setText(_translate("optionWindow", "EGADS"))
        item = self.ow_section_list.item(1)
        item.setText(_translate("optionWindow", "File & Folder"))
        item = self.ow_section_list.item(2)
        item.setText(_translate("optionWindow", "General"))
        item = self.ow_section_list.item(3)
        item.setText(_translate("optionWindow", "Log"))
        item = self.ow_section_list.item(4)
        item.setText(_translate("optionWindow", "Plots"))
        item = self.ow_section_list.item(5)
        item.setText(_translate("optionWindow", "Update"))
        self.ow_section_list.setSortingEnabled(__sortingEnabled)
        self.ow_checkbox_1.setText(_translate("optionWindow", "Read variables as float"))
        self.ow_checkbox_2.setText(_translate("optionWindow", "Replace automatically missing values in variables by NaN"))
        self.ow_checkbox_3.setText(_translate("optionWindow", "Do not replace missing values if a variable can\'t be read."))
        self.ow_checkbox_7.setText(_translate("optionWindow", "Keep a list of files opened by the user"))
        self.ow_checkbox_8.setText(_translate("optionWindow", "Enable the registration of folders for quick access"))
        self.ow_label_9.setText(_translate("optionWindow", "Folder path:"))
        self.ow_label_10.setText(_translate("optionWindow", "Folder list:"))
        self.ow_checkbox_11.setText(_translate("optionWindow", "Display a warning when deleting a dimension"))
        self.ow_label_1.setText(_translate("optionWindow", "GUI log options:"))
        self.ow_label_3.setText(_translate("optionWindow", "Logging path:"))
        self.ow_label_2.setText(_translate("optionWindow", "Logging level:"))
        self.ow_combobox_1.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.ow_combobox_1.setItemText(1, _translate("optionWindow", "INFO"))
        self.ow_combobox_1.setItemText(2, _translate("optionWindow", "WARNING"))
        self.ow_combobox_1.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.ow_combobox_1.setItemText(4, _translate("optionWindow", "ERROR"))
        self.ow_label_4.setText(_translate("optionWindow", "EGADS log options:"))
        self.ow_label_6.setText(_translate("optionWindow", "Logging path:"))
        self.ow_label_5.setText(_translate("optionWindow", "Logging level:"))
        self.ow_combobox_2.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.ow_combobox_2.setItemText(1, _translate("optionWindow", "INFO"))
        self.ow_combobox_2.setItemText(2, _translate("optionWindow", "WARNING"))
        self.ow_combobox_2.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.ow_combobox_2.setItemText(4, _translate("optionWindow", "ERROR"))
        self.ow_label_8.setText(_translate("optionWindow", "Disposition of subplots:"))
        self.ow_combobox_3.setItemText(0, _translate("optionWindow", "On the same plot"))
        self.ow_combobox_3.setItemText(1, _translate("optionWindow", "On different subplots"))
        self.ow_combobox_3.setItemText(2, _translate("optionWindow", "Always ask"))
        self.ow_label_7.setText(_translate("optionWindow", "Plot variables with the same unit:"))
        self.ow_combobox_4.setItemText(0, _translate("optionWindow", "Automatic"))
        self.ow_combobox_4.setItemText(1, _translate("optionWindow", "Manual"))
        self.ow_checkbox_9.setText(_translate("optionWindow", "Plot standard 2D and 3D data with a manual distribution"))
        self.ow_label_12.setText(_translate("optionWindow", "1st dimension:"))
        self.ow_combobox_5.setItemText(0, _translate("optionWindow", "Automatic"))
        self.ow_combobox_5.setItemText(1, _translate("optionWindow", "Row"))
        self.ow_combobox_5.setItemText(2, _translate("optionWindow", "Column"))
        self.ow_combobox_5.setItemText(3, _translate("optionWindow", "Layer"))
        self.ow_label_13.setText(_translate("optionWindow", "2nd dimension:"))
        self.ow_combobox_6.setItemText(0, _translate("optionWindow", "Automatic"))
        self.ow_combobox_6.setItemText(1, _translate("optionWindow", "Row"))
        self.ow_combobox_6.setItemText(2, _translate("optionWindow", "Column"))
        self.ow_combobox_6.setItemText(3, _translate("optionWindow", "Layer"))
        self.ow_label_14.setText(_translate("optionWindow", "3rd dimension:"))
        self.ow_combobox_7.setItemText(0, _translate("optionWindow", "Automatic"))
        self.ow_combobox_7.setItemText(1, _translate("optionWindow", "Row"))
        self.ow_combobox_7.setItemText(2, _translate("optionWindow", "Column"))
        self.ow_combobox_7.setItemText(3, _translate("optionWindow", "Layer"))
        self.ow_checkbox_10.setText(_translate("optionWindow", "Plot georeferenced 2D and 3D data as standard data"))
        self.ow_checkbox_4.setText(_translate("optionWindow", "Check EGADS Lineage GUI updates on GitHub at startup"))
        self.ow_check_button_1.setText(_translate("optionWindow", "Check now"))
        self.ow_checkbox_5.setText(_translate("optionWindow", "Check EGADS Lineage updates on GitHub at startup"))
        self.ow_check_button_2.setText(_translate("optionWindow", "Check now"))

