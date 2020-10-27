# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 550)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/egads_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_view = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_view.setEnabled(True)
        self.tab_view.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tab_view.setFont(font)
        self.tab_view.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    top: 1px;\n"
"    bottom: 1px;\n"
"    left: 10px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-top: 1px solid rgb(180,180,180);\n"
"    border-left: 1px solid rgb(180,180,180);\n"
"    border-right: 1px solid rgb(180,180,180);\n"
"    padding: 2px 15px 2px 15px;\n"
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
"    margin-top: 4px;\n"
"    color: rgb(70,70,70);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    border-bottom: 1px solid rgb(180,180,180);\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
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
        self.tab_view.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_view.setUsesScrollButtons(True)
        self.tab_view.setDocumentMode(False)
        self.tab_view.setObjectName("tab_view")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.information_scroll_area = QtWidgets.QScrollArea(self.tab)
        self.information_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.information_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.information_scroll_area.setWidgetResizable(True)
        self.information_scroll_area.setObjectName("information_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 910, 372))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.global_container = QtWidgets.QVBoxLayout()
        self.global_container.setObjectName("global_container")
        self.gridLayout_4.addLayout(self.global_container, 1, 1, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem3, 3, 2, 1, 1)
        self.information_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.information_scroll_area, 1, 1, 1, 1)
        self.tab_view.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.information_scroll_area_2 = QtWidgets.QScrollArea(self.tab_2)
        self.information_scroll_area_2.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.information_scroll_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.information_scroll_area_2.setWidgetResizable(True)
        self.information_scroll_area_2.setObjectName("information_scroll_area_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 910, 372))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 1, 0, 1, 1)
        self.variable_widget_container = QtWidgets.QVBoxLayout()
        self.variable_widget_container.setObjectName("variable_widget_container")
        self.gridLayout_5.addLayout(self.variable_widget_container, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem7, 2, 1, 1, 1)
        self.information_scroll_area_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.information_scroll_area_2, 0, 0, 1, 1)
        self.tab_view.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tab_view, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 934, 34))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("QMenuBar {\n"
"    background-color: #f0f0f0;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px;\n"
"    padding: 5px 15px 5px 15px;\n"
"    background: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    border: 0px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: rgb(200,200,200);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding-left: 10px;\n"
"    padding-right: 30px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: black;\n"
"    border: 0px solid black;\n"
"    \n"
"}\n"
"\n"
"QMenu::icon {\n"
"   padding-left: 5px;\n"
"   width: 40px;\n"
"   height: 40px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"   background-color: rgb(220,220,220);\n"
"   height: 1px;\n"
"   margin-top: 2px;\n"
"   margin-bottom: 2px;\n"
"}\n"
"")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuFile.setFont(font)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_recent = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_recent.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuOpen_recent.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuOpen_recent.setIcon(icon1)
        self.menuOpen_recent.setObjectName("menuOpen_recent")
        self.menuQuick_access = QtWidgets.QMenu(self.menuFile)
        self.menuQuick_access.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/quick_access_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuQuick_access.setIcon(icon2)
        self.menuQuick_access.setObjectName("menuQuick_access")
        self.menuProcessings = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuProcessings.setFont(font)
        self.menuProcessings.setObjectName("menuProcessings")
        self.menuEmbedded_algorithms = QtWidgets.QMenu(self.menuProcessings)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuEmbedded_algorithms.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/new_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuEmbedded_algorithms.setIcon(icon3)
        self.menuEmbedded_algorithms.setObjectName("menuEmbedded_algorithms")
        self.menuUser_defined_algorithms = QtWidgets.QMenu(self.menuProcessings)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuUser_defined_algorithms.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/create_algo_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUser_defined_algorithms.setIcon(icon4)
        self.menuUser_defined_algorithms.setObjectName("menuUser_defined_algorithms")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.menuAbout.setFont(font)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.toolBar.setFont(font)
        self.toolBar.setStyleSheet("QToolBar {\n"
"   padding: 10px;\n"
"   background: rgb(240,240,240);\n"
"   border-bottom: 1px solid rgb(220,220,220);\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"   background-color: rgb(220,220,220);\n"
"   border: none;\n"
"}")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(35, 35))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("QStatusBar {\n"
"    background: rgb(240,240,240);\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: 0px solid black;\n"
"}")
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpenBar = QtWidgets.QAction(MainWindow)
        self.actionOpenBar.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOpenBar.setFont(font)
        self.actionOpenBar.setObjectName("actionOpenBar")
        self.actionCloseBar = QtWidgets.QAction(MainWindow)
        self.actionCloseBar.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/off_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseBar.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionCloseBar.setFont(font)
        self.actionCloseBar.setObjectName("actionCloseBar")
        self.actionAlgorithmsBar = QtWidgets.QAction(MainWindow)
        self.actionAlgorithmsBar.setEnabled(False)
        self.actionAlgorithmsBar.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionAlgorithmsBar.setFont(font)
        self.actionAlgorithmsBar.setObjectName("actionAlgorithmsBar")
        self.actionCreatealgorithmBar = QtWidgets.QAction(MainWindow)
        self.actionCreatealgorithmBar.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionCreatealgorithmBar.setFont(font)
        self.actionCreatealgorithmBar.setObjectName("actionCreatealgorithmBar")
        self.actionCreateVariableBar = QtWidgets.QAction(MainWindow)
        self.actionCreateVariableBar.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/new_var_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreateVariableBar.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionCreateVariableBar.setFont(font)
        self.actionCreateVariableBar.setObjectName("actionCreateVariableBar")
        self.actionDeleteVariableBar = QtWidgets.QAction(MainWindow)
        self.actionDeleteVariableBar.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteVariableBar.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionDeleteVariableBar.setFont(font)
        self.actionDeleteVariableBar.setObjectName("actionDeleteVariableBar")
        self.actionGlobalAttributesBar = QtWidgets.QAction(MainWindow)
        self.actionGlobalAttributesBar.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/glo_metadata_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGlobalAttributesBar.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionGlobalAttributesBar.setFont(font)
        self.actionGlobalAttributesBar.setObjectName("actionGlobalAttributesBar")
        self.actionVariableAttributesBar = QtWidgets.QAction(MainWindow)
        self.actionVariableAttributesBar.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/var_metadata_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVariableAttributesBar.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionVariableAttributesBar.setFont(font)
        self.actionVariableAttributesBar.setObjectName("actionVariableAttributesBar")
        self.actionPlotBar = QtWidgets.QAction(MainWindow)
        self.actionPlotBar.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/plot_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlotBar.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionPlotBar.setFont(font)
        self.actionPlotBar.setObjectName("actionPlotBar")
        self.actionBatch_processing = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/batch_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBatch_processing.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionBatch_processing.setFont(font)
        self.actionBatch_processing.setObjectName("actionBatch_processing")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon12)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/help_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon13)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_EGADS = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_EGADS.setIcon(icon14)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionAbout_EGADS.setFont(font)
        self.actionAbout_EGADS.setObjectName("actionAbout_EGADS")
        self.actionSeparator = QtWidgets.QAction(MainWindow)
        self.actionSeparator.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.actionSeparator.setIcon(icon15)
        self.actionSeparator.setObjectName("actionSeparator")
        self.actionSeparator2 = QtWidgets.QAction(MainWindow)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon15)
        self.actionSeparator2.setVisible(True)
        self.actionSeparator2.setIconVisibleInMenu(True)
        self.actionSeparator2.setObjectName("actionSeparator2")
        self.actionSeparator3 = QtWidgets.QAction(MainWindow)
        self.actionSeparator3.setEnabled(False)
        self.actionSeparator3.setIcon(icon15)
        self.actionSeparator3.setObjectName("actionSeparator3")
        self.actionSeparator4 = QtWidgets.QAction(MainWindow)
        self.actionSeparator4.setEnabled(False)
        self.actionSeparator4.setIcon(icon15)
        self.actionSeparator4.setObjectName("actionSeparator4")
        self.actionSaveAsBar = QtWidgets.QAction(MainWindow)
        self.actionSaveAsBar.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/save_as_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAsBar.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSaveAsBar.setFont(font)
        self.actionSaveAsBar.setObjectName("actionSaveAsBar")
        self.actionDisplayBar = QtWidgets.QAction(MainWindow)
        self.actionDisplayBar.setEnabled(False)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/data_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisplayBar.setIcon(icon17)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionDisplayBar.setFont(font)
        self.actionDisplayBar.setObjectName("actionDisplayBar")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon18)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOptions.setFont(font)
        self.actionOptions.setObjectName("actionOptions")
        self.actionSeparator5 = QtWidgets.QAction(MainWindow)
        self.actionSeparator5.setEnabled(False)
        self.actionSeparator5.setIcon(icon15)
        self.actionSeparator5.setObjectName("actionSeparator5")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/egads_update_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon19)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionUpdate.setFont(font)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setEnabled(False)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/export_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon20)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExport.setFont(font)
        self.actionExport.setObjectName("actionExport")
        self.actionClear_list = QtWidgets.QAction(MainWindow)
        self.actionClear_list.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionClear_list.setFont(font)
        self.actionClear_list.setObjectName("actionClear_list")
        self.actionTMP_2 = QtWidgets.QAction(MainWindow)
        self.actionTMP_2.setObjectName("actionTMP_2")
        self.actionTMP = QtWidgets.QAction(MainWindow)
        self.actionTMP.setObjectName("actionTMP")
        self.actionCreate_group = QtWidgets.QAction(MainWindow)
        self.actionCreate_group.setEnabled(False)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/create_group_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_group.setIcon(icon21)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        self.actionCreate_group.setFont(font)
        self.actionCreate_group.setObjectName("actionCreate_group")
        self.menuOpen_recent.addSeparator()
        self.menuFile.addAction(self.actionOpenBar)
        self.menuFile.addAction(self.menuOpen_recent.menuAction())
        self.menuFile.addAction(self.menuQuick_access.menuAction())
        self.menuFile.addAction(self.actionSaveAsBar)
        self.menuFile.addAction(self.actionCloseBar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionBatch_processing)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuProcessings.addAction(self.menuEmbedded_algorithms.menuAction())
        self.menuProcessings.addAction(self.menuUser_defined_algorithms.menuAction())
        self.menuAbout.addAction(self.actionOptions)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout_EGADS)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuProcessings.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionOpenBar)
        self.toolBar.addAction(self.actionSaveAsBar)
        self.toolBar.addAction(self.actionCloseBar)
        self.toolBar.addAction(self.actionSeparator)
        self.toolBar.addAction(self.actionGlobalAttributesBar)
        self.toolBar.addAction(self.actionVariableAttributesBar)
        self.toolBar.addAction(self.actionSeparator3)
        self.toolBar.addAction(self.actionCreate_group)
        self.toolBar.addAction(self.actionCreateVariableBar)
        self.toolBar.addAction(self.actionDeleteVariableBar)
        self.toolBar.addAction(self.actionSeparator4)
        self.toolBar.addAction(self.actionAlgorithmsBar)
        self.toolBar.addAction(self.actionCreatealgorithmBar)
        self.toolBar.addAction(self.actionSeparator2)
        self.toolBar.addAction(self.actionDisplayBar)
        self.toolBar.addAction(self.actionPlotBar)
        self.toolBar.addAction(self.actionSeparator5)
        self.toolBar.addAction(self.actionUpdate)

        self.retranslateUi(MainWindow)
        self.tab_view.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EGADS"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab), _translate("MainWindow", "Global Metadata"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab_2), _translate("MainWindow", "Variables"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_recent.setTitle(_translate("MainWindow", "Open recent..."))
        self.menuQuick_access.setTitle(_translate("MainWindow", "Quick access..."))
        self.menuProcessings.setTitle(_translate("MainWindow", "Processing"))
        self.menuEmbedded_algorithms.setTitle(_translate("MainWindow", "Embedded algorithms"))
        self.menuUser_defined_algorithms.setTitle(_translate("MainWindow", "User-defined algorithms"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpenBar.setText(_translate("MainWindow", "Open..."))
        self.actionOpenBar.setToolTip(_translate("MainWindow", "Open a file"))
        self.actionCloseBar.setText(_translate("MainWindow", "Close..."))
        self.actionCloseBar.setToolTip(_translate("MainWindow", "Close the current file"))
        self.actionAlgorithmsBar.setText(_translate("MainWindow", "Algorithms"))
        self.actionAlgorithmsBar.setToolTip(_translate("MainWindow", "Launch a process"))
        self.actionCreatealgorithmBar.setText(_translate("MainWindow", "Create Algorithm"))
        self.actionCreatealgorithmBar.setToolTip(_translate("MainWindow", "Create a new algorithm"))
        self.actionCreateVariableBar.setText(_translate("MainWindow", "Create Variable"))
        self.actionCreateVariableBar.setToolTip(_translate("MainWindow", "Create a new simple variable"))
        self.actionDeleteVariableBar.setText(_translate("MainWindow", "Delete Variable"))
        self.actionDeleteVariableBar.setToolTip(_translate("MainWindow", "Delete the selected variable(s) / group(s)"))
        self.actionGlobalAttributesBar.setText(_translate("MainWindow", "Global Attributes"))
        self.actionGlobalAttributesBar.setToolTip(_translate("MainWindow", "Add or modify global attributes"))
        self.actionVariableAttributesBar.setText(_translate("MainWindow", "Variable Attributes"))
        self.actionVariableAttributesBar.setToolTip(_translate("MainWindow", "Add or modify the selected variable attributes"))
        self.actionPlotBar.setText(_translate("MainWindow", "Plot"))
        self.actionPlotBar.setToolTip(_translate("MainWindow", "Display a graph of the selected variable"))
        self.actionBatch_processing.setText(_translate("MainWindow", "Batch processing..."))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.actionHelp.setText(_translate("MainWindow", "Help..."))
        self.actionAbout_EGADS.setText(_translate("MainWindow", "About EGADS..."))
        self.actionSeparator.setText(_translate("MainWindow", "separator"))
        self.actionSeparator2.setText(_translate("MainWindow", "separator2"))
        self.actionSeparator3.setText(_translate("MainWindow", "separator3"))
        self.actionSeparator4.setText(_translate("MainWindow", "separator4"))
        self.actionSaveAsBar.setText(_translate("MainWindow", "Save as..."))
        self.actionSaveAsBar.setToolTip(_translate("MainWindow", "Save to a new file"))
        self.actionDisplayBar.setText(_translate("MainWindow", "Display"))
        self.actionDisplayBar.setToolTip(_translate("MainWindow", "Display the selected variable"))
        self.actionOptions.setText(_translate("MainWindow", "Options..."))
        self.actionOptions.setToolTip(_translate("MainWindow", "EGADS GUI options"))
        self.actionSeparator5.setText(_translate("MainWindow", "separator5"))
        self.actionSeparator5.setToolTip(_translate("MainWindow", "separator5"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionUpdate.setToolTip(_translate("MainWindow", "An update is available. Click for more detail"))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionExport.setToolTip(_translate("MainWindow", "Export variables to another format"))
        self.actionClear_list.setText(_translate("MainWindow", "Clear list..."))
        self.actionClear_list.setToolTip(_translate("MainWindow", "Clear the list"))
        self.actionTMP_2.setText(_translate("MainWindow", "TMP"))
        self.actionTMP.setText(_translate("MainWindow", "TMP"))
        self.actionCreate_group.setText(_translate("MainWindow", "Create new group..."))
        self.actionCreate_group.setToolTip(_translate("MainWindow", "Create a new group"))

