# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createvariablewindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createvariableWindow(object):
    def setupUi(self, createvariableWindow):
        createvariableWindow.setObjectName("createvariableWindow")
        createvariableWindow.resize(850, 510)
        createvariableWindow.setMinimumSize(QtCore.QSize(0, 0))
        createvariableWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        createvariableWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new_var_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        createvariableWindow.setWindowIcon(icon)
        createvariableWindow.setStyleSheet("QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
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
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
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
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
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
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
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
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
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
        self.gridLayout_3 = QtWidgets.QGridLayout(createvariableWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cvw_create_button = QtWidgets.QToolButton(createvariableWindow)
        self.cvw_create_button.setEnabled(False)
        self.cvw_create_button.setMinimumSize(QtCore.QSize(100, 27))
        self.cvw_create_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cvw_create_button.setFont(font)
        self.cvw_create_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.cvw_create_button.setIconSize(QtCore.QSize(25, 25))
        self.cvw_create_button.setObjectName("cvw_create_button")
        self.horizontalLayout.addWidget(self.cvw_create_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cvw_cancel_button = QtWidgets.QToolButton(createvariableWindow)
        self.cvw_cancel_button.setMinimumSize(QtCore.QSize(100, 27))
        self.cvw_cancel_button.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cvw_cancel_button.setFont(font)
        self.cvw_cancel_button.setStyleSheet("QToolButton {\n"
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
        self.cvw_cancel_button.setIconSize(QtCore.QSize(25, 25))
        self.cvw_cancel_button.setObjectName("cvw_cancel_button")
        self.horizontalLayout.addWidget(self.cvw_cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.cvw_tabwidget = QtWidgets.QTabWidget(createvariableWindow)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_tabwidget.setFont(font)
        self.cvw_tabwidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    top: -1px;\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(180,180,180);\n"
"    border-left: 1px solid rgb(180,180,180);\n"
"    border-right: 1px solid rgb(180,180,180);\n"
"    border-top-right-radius: 5px;\n"
"    border-top-left-radius: 5px;\n"
"    padding: 2px 10px 2px 10px;\n"
"    margin-right: 2px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px; \n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QTabBar QToolButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(icons/right_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(icons/left_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}")
        self.cvw_tabwidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.cvw_tabwidget.setUsesScrollButtons(True)
        self.cvw_tabwidget.setObjectName("cvw_tabwidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 1, 0, 1, 1)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scrollArea_4.setFont(font)
        self.scrollArea_4.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 770, 364))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cvw_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_1.sizePolicy().hasHeightForWidth())
        self.cvw_label_1.setSizePolicy(sizePolicy)
        self.cvw_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_1.setFont(font)
        self.cvw_label_1.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_1.setLineWidth(0)
        self.cvw_label_1.setMidLineWidth(0)
        self.cvw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_1.setWordWrap(True)
        self.cvw_label_1.setObjectName("cvw_label_1")
        self.horizontalLayout_6.addWidget(self.cvw_label_1)
        self.cvw_combobox_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.cvw_combobox_1.setMinimumSize(QtCore.QSize(160, 27))
        self.cvw_combobox_1.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_combobox_1.setFont(font)
        self.cvw_combobox_1.setStyleSheet("QComboBox {\n"
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
"}")
        self.cvw_combobox_1.setFrame(False)
        self.cvw_combobox_1.setObjectName("cvw_combobox_1")
        self.cvw_combobox_1.addItem("")
        self.cvw_combobox_1.addItem("")
        self.cvw_combobox_1.addItem("")
        self.cvw_combobox_1.addItem("")
        self.horizontalLayout_6.addWidget(self.cvw_combobox_1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.info_button_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button_5.setIcon(icon1)
        self.info_button_5.setIconSize(QtCore.QSize(23, 23))
        self.info_button_5.setAutoRaise(False)
        self.info_button_5.setObjectName("info_button_5")
        self.horizontalLayout_6.addWidget(self.info_button_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem8, 1, 0, 1, 1)
        self.cvw_vertical_layout = QtWidgets.QVBoxLayout()
        self.cvw_vertical_layout.setObjectName("cvw_vertical_layout")
        self.gridLayout_4.addLayout(self.cvw_vertical_layout, 2, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.addWidget(self.scrollArea_4, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem9, 1, 2, 1, 1)
        self.cvw_tabwidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem10, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cvw_line_2 = QtWidgets.QLineEdit(self.tab_2)
        self.cvw_line_2.setEnabled(True)
        self.cvw_line_2.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_line_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_line_2.setFont(font)
        self.cvw_line_2.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_2.setObjectName("cvw_line_2")
        self.horizontalLayout_3.addWidget(self.cvw_line_2)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.info_button_2 = QtWidgets.QToolButton(self.tab_2)
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
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.cvw_label_3 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_3.sizePolicy().hasHeightForWidth())
        self.cvw_label_3.setSizePolicy(sizePolicy)
        self.cvw_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_3.setFont(font)
        self.cvw_label_3.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_3.setLineWidth(0)
        self.cvw_label_3.setMidLineWidth(0)
        self.cvw_label_3.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_3.setWordWrap(False)
        self.cvw_label_3.setObjectName("cvw_label_3")
        self.gridLayout.addWidget(self.cvw_label_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cvw_line_1 = QtWidgets.QLineEdit(self.tab_2)
        self.cvw_line_1.setEnabled(True)
        self.cvw_line_1.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_line_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_line_1.setFont(font)
        self.cvw_line_1.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_1.setObjectName("cvw_line_1")
        self.horizontalLayout_2.addWidget(self.cvw_line_1)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.info_button_1 = QtWidgets.QToolButton(self.tab_2)
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
        self.info_button_1.setIcon(icon1)
        self.info_button_1.setIconSize(QtCore.QSize(23, 23))
        self.info_button_1.setAutoRaise(False)
        self.info_button_1.setObjectName("info_button_1")
        self.horizontalLayout_2.addWidget(self.info_button_1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.cvw_label_5 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_5.sizePolicy().hasHeightForWidth())
        self.cvw_label_5.setSizePolicy(sizePolicy)
        self.cvw_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_5.setFont(font)
        self.cvw_label_5.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_5.setLineWidth(0)
        self.cvw_label_5.setMidLineWidth(0)
        self.cvw_label_5.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_5.setWordWrap(True)
        self.cvw_label_5.setObjectName("cvw_label_5")
        self.gridLayout.addWidget(self.cvw_label_5, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cvw_line_3 = QtWidgets.QLineEdit(self.tab_2)
        self.cvw_line_3.setEnabled(True)
        self.cvw_line_3.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_line_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_line_3.setFont(font)
        self.cvw_line_3.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_3.setObjectName("cvw_line_3")
        self.horizontalLayout_4.addWidget(self.cvw_line_3)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.info_button_3 = QtWidgets.QToolButton(self.tab_2)
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
        self.horizontalLayout_4.addWidget(self.info_button_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.cvw_label_4 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_4.sizePolicy().hasHeightForWidth())
        self.cvw_label_4.setSizePolicy(sizePolicy)
        self.cvw_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_4.setFont(font)
        self.cvw_label_4.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_4.setLineWidth(0)
        self.cvw_label_4.setMidLineWidth(0)
        self.cvw_label_4.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_4.setWordWrap(True)
        self.cvw_label_4.setObjectName("cvw_label_4")
        self.gridLayout.addWidget(self.cvw_label_4, 2, 0, 1, 1)
        self.cvw_label_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_2.sizePolicy().hasHeightForWidth())
        self.cvw_label_2.setSizePolicy(sizePolicy)
        self.cvw_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_2.setFont(font)
        self.cvw_label_2.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_2.setLineWidth(0)
        self.cvw_label_2.setMidLineWidth(0)
        self.cvw_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_2.setWordWrap(False)
        self.cvw_label_2.setObjectName("cvw_label_2")
        self.gridLayout.addWidget(self.cvw_label_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cvw_line_4 = QtWidgets.QLineEdit(self.tab_2)
        self.cvw_line_4.setEnabled(True)
        self.cvw_line_4.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_line_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_line_4.setFont(font)
        self.cvw_line_4.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_4.setObjectName("cvw_line_4")
        self.horizontalLayout_5.addWidget(self.cvw_line_4)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.info_button_4 = QtWidgets.QToolButton(self.tab_2)
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
        self.horizontalLayout_5.addWidget(self.info_button_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.cvw_label_15 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_15.sizePolicy().hasHeightForWidth())
        self.cvw_label_15.setSizePolicy(sizePolicy)
        self.cvw_label_15.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_15.setFont(font)
        self.cvw_label_15.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_15.setLineWidth(0)
        self.cvw_label_15.setMidLineWidth(0)
        self.cvw_label_15.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.cvw_label_15.setWordWrap(True)
        self.cvw_label_15.setObjectName("cvw_label_15")
        self.gridLayout.addWidget(self.cvw_label_15, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cvw_label_12 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_12.sizePolicy().hasHeightForWidth())
        self.cvw_label_12.setSizePolicy(sizePolicy)
        self.cvw_label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_12.setFont(font)
        self.cvw_label_12.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_12.setLineWidth(0)
        self.cvw_label_12.setMidLineWidth(0)
        self.cvw_label_12.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_12.setWordWrap(True)
        self.cvw_label_12.setObjectName("cvw_label_12")
        self.gridLayout_2.addWidget(self.cvw_label_12, 0, 0, 1, 1)
        self.cvw_combobox_6 = QtWidgets.QComboBox(self.tab_2)
        self.cvw_combobox_6.setMinimumSize(QtCore.QSize(200, 27))
        self.cvw_combobox_6.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_combobox_6.setFont(font)
        self.cvw_combobox_6.setStyleSheet("QComboBox {\n"
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
"}")
        self.cvw_combobox_6.setFrame(False)
        self.cvw_combobox_6.setObjectName("cvw_combobox_6")
        self.cvw_combobox_6.addItem("")
        self.cvw_combobox_6.addItem("")
        self.cvw_combobox_6.addItem("")
        self.cvw_combobox_6.addItem("")
        self.gridLayout_2.addWidget(self.cvw_combobox_6, 0, 1, 1, 1)
        self.cvw_label_13 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_13.sizePolicy().hasHeightForWidth())
        self.cvw_label_13.setSizePolicy(sizePolicy)
        self.cvw_label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_13.setFont(font)
        self.cvw_label_13.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_13.setLineWidth(0)
        self.cvw_label_13.setMidLineWidth(0)
        self.cvw_label_13.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_13.setWordWrap(True)
        self.cvw_label_13.setObjectName("cvw_label_13")
        self.gridLayout_2.addWidget(self.cvw_label_13, 1, 0, 1, 1)
        self.cvw_combobox_7 = QtWidgets.QComboBox(self.tab_2)
        self.cvw_combobox_7.setMinimumSize(QtCore.QSize(200, 27))
        self.cvw_combobox_7.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_combobox_7.setFont(font)
        self.cvw_combobox_7.setStyleSheet("QComboBox {\n"
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
"}")
        self.cvw_combobox_7.setFrame(False)
        self.cvw_combobox_7.setObjectName("cvw_combobox_7")
        self.cvw_combobox_7.addItem("")
        self.cvw_combobox_7.addItem("")
        self.cvw_combobox_7.addItem("")
        self.cvw_combobox_7.addItem("")
        self.gridLayout_2.addWidget(self.cvw_combobox_7, 1, 1, 1, 1)
        self.cvw_label_14 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_label_14.sizePolicy().hasHeightForWidth())
        self.cvw_label_14.setSizePolicy(sizePolicy)
        self.cvw_label_14.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_label_14.setFont(font)
        self.cvw_label_14.setStyleSheet("QLabel {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.cvw_label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_14.setLineWidth(0)
        self.cvw_label_14.setMidLineWidth(0)
        self.cvw_label_14.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cvw_label_14.setWordWrap(True)
        self.cvw_label_14.setObjectName("cvw_label_14")
        self.gridLayout_2.addWidget(self.cvw_label_14, 2, 0, 1, 1)
        self.cvw_combobox_8 = QtWidgets.QComboBox(self.tab_2)
        self.cvw_combobox_8.setMinimumSize(QtCore.QSize(200, 27))
        self.cvw_combobox_8.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cvw_combobox_8.setFont(font)
        self.cvw_combobox_8.setStyleSheet("QComboBox {\n"
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
"}")
        self.cvw_combobox_8.setFrame(False)
        self.cvw_combobox_8.setObjectName("cvw_combobox_8")
        self.cvw_combobox_8.addItem("")
        self.cvw_combobox_8.addItem("")
        self.cvw_combobox_8.addItem("")
        self.cvw_combobox_8.addItem("")
        self.gridLayout_2.addWidget(self.cvw_combobox_8, 2, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_button_11 = QtWidgets.QToolButton(self.tab_2)
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
        self.verticalLayout.addWidget(self.info_button_11)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 1, 1, 2, 2)
        spacerItem18 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem18, 1, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem19, 2, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem20, 3, 2, 1, 1)
        self.cvw_tabwidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.cvw_tabwidget, 0, 0, 1, 1)

        self.retranslateUi(createvariableWindow)
        self.cvw_tabwidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(createvariableWindow)

    def retranslateUi(self, createvariableWindow):
        _translate = QtCore.QCoreApplication.translate
        createvariableWindow.setWindowTitle(_translate("createvariableWindow", "Warning"))
        self.cvw_create_button.setText(_translate("createvariableWindow", "Create"))
        self.cvw_cancel_button.setText(_translate("createvariableWindow", "Cancel"))
        self.cvw_label_1.setText(_translate("createvariableWindow", "Select a data type:"))
        self.cvw_combobox_1.setItemText(0, _translate("createvariableWindow", "Make a choice..."))
        self.cvw_combobox_1.setItemText(1, _translate("createvariableWindow", "Scalar"))
        self.cvw_combobox_1.setItemText(2, _translate("createvariableWindow", "Vector"))
        self.cvw_combobox_1.setItemText(3, _translate("createvariableWindow", "Array"))
        self.cvw_tabwidget.setTabText(self.cvw_tabwidget.indexOf(self.tab_1), _translate("createvariableWindow", "Type"))
        self.cvw_label_3.setText(_translate("createvariableWindow", "Standard name:"))
        self.cvw_label_5.setText(_translate("createvariableWindow", "_FillValue:"))
        self.cvw_label_4.setText(_translate("createvariableWindow", "Units:"))
        self.cvw_label_2.setText(_translate("createvariableWindow", "Variable name:"))
        self.cvw_label_15.setText(_translate("createvariableWindow", "Dimension(s):"))
        self.cvw_label_12.setText(_translate("createvariableWindow", "rows:"))
        self.cvw_combobox_6.setItemText(0, _translate("createvariableWindow", "Make a choice..."))
        self.cvw_combobox_6.setItemText(1, _translate("createvariableWindow", "Scalar"))
        self.cvw_combobox_6.setItemText(2, _translate("createvariableWindow", "Vector"))
        self.cvw_combobox_6.setItemText(3, _translate("createvariableWindow", "Array"))
        self.cvw_label_13.setText(_translate("createvariableWindow", "columns:"))
        self.cvw_combobox_7.setItemText(0, _translate("createvariableWindow", "Make a choice..."))
        self.cvw_combobox_7.setItemText(1, _translate("createvariableWindow", "Scalar"))
        self.cvw_combobox_7.setItemText(2, _translate("createvariableWindow", "Vector"))
        self.cvw_combobox_7.setItemText(3, _translate("createvariableWindow", "Array"))
        self.cvw_label_14.setText(_translate("createvariableWindow", "layers:"))
        self.cvw_combobox_8.setItemText(0, _translate("createvariableWindow", "Make a choice..."))
        self.cvw_combobox_8.setItemText(1, _translate("createvariableWindow", "Scalar"))
        self.cvw_combobox_8.setItemText(2, _translate("createvariableWindow", "Vector"))
        self.cvw_combobox_8.setItemText(3, _translate("createvariableWindow", "Array"))
        self.cvw_tabwidget.setTabText(self.cvw_tabwidget.indexOf(self.tab_2), _translate("createvariableWindow", "Metadata"))

