# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName("plotWindow")
        plotWindow.resize(1250, 750)
        plotWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/plot_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        plotWindow.setWindowIcon(icon)
        plotWindow.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(plotWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.pw_toolbar_fr = QtWidgets.QVBoxLayout()
        self.pw_toolbar_fr.setObjectName("pw_toolbar_fr")
        self.gridLayout.addLayout(self.pw_toolbar_fr, 0, 0, 1, 1)
        self.tab_view = QtWidgets.QTabWidget(plotWindow)
        self.tab_view.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
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
        self.tab_view.setObjectName("tab_view")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pw_plot_fr = QtWidgets.QVBoxLayout()
        self.pw_plot_fr.setObjectName("pw_plot_fr")
        self.gridLayout_2.addLayout(self.pw_plot_fr, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pw_plotWindow_lb_1 = QtWidgets.QLabel(self.tab)
        self.pw_plotWindow_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_plotWindow_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_plotWindow_lb_1.setFont(font)
        self.pw_plotWindow_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_plotWindow_lb_1.setObjectName("pw_plotWindow_lb_1")
        self.horizontalLayout_6.addWidget(self.pw_plotWindow_lb_1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.pw_plotWindow_cb_1 = QtWidgets.QComboBox(self.tab)
        self.pw_plotWindow_cb_1.setEnabled(True)
        self.pw_plotWindow_cb_1.setMinimumSize(QtCore.QSize(180, 27))
        self.pw_plotWindow_cb_1.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_plotWindow_cb_1.setFont(font)
        self.pw_plotWindow_cb_1.setStyleSheet("QComboBox {\n"
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
        self.pw_plotWindow_cb_1.setObjectName("pw_plotWindow_cb_1")
        self.horizontalLayout_6.addWidget(self.pw_plotWindow_cb_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pw_navigate_bt_1 = QtWidgets.QToolButton(self.tab)
        self.pw_navigate_bt_1.setMinimumSize(QtCore.QSize(23, 23))
        self.pw_navigate_bt_1.setMaximumSize(QtCore.QSize(23, 23))
        self.pw_navigate_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/left_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_navigate_bt_1.setIcon(icon1)
        self.pw_navigate_bt_1.setIconSize(QtCore.QSize(27, 27))
        self.pw_navigate_bt_1.setObjectName("pw_navigate_bt_1")
        self.horizontalLayout_6.addWidget(self.pw_navigate_bt_1)
        self.pw_navigate_bt_2 = QtWidgets.QToolButton(self.tab)
        self.pw_navigate_bt_2.setMinimumSize(QtCore.QSize(23, 23))
        self.pw_navigate_bt_2.setMaximumSize(QtCore.QSize(23, 23))
        self.pw_navigate_bt_2.setStyleSheet("QToolButton {\n"
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
        icon2.addPixmap(QtGui.QPixmap("icons/right_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_navigate_bt_2.setIcon(icon2)
        self.pw_navigate_bt_2.setIconSize(QtCore.QSize(27, 27))
        self.pw_navigate_bt_2.setObjectName("pw_navigate_bt_2")
        self.horizontalLayout_6.addWidget(self.pw_navigate_bt_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.tab_view.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pw_figureOptions_sa = QtWidgets.QScrollArea(self.tab_2)
        self.pw_figureOptions_sa.setMinimumSize(QtCore.QSize(0, 0))
        self.pw_figureOptions_sa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_figureOptions_sa.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.pw_figureOptions_sa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pw_figureOptions_sa.setWidgetResizable(True)
        self.pw_figureOptions_sa.setObjectName("pw_figureOptions_sa")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1226, 596))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.pw_figureOptions_la = QtWidgets.QVBoxLayout()
        self.pw_figureOptions_la.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.pw_figureOptions_la.setSpacing(7)
        self.pw_figureOptions_la.setObjectName("pw_figureOptions_la")
        self.gridLayout_3.addLayout(self.pw_figureOptions_la, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 2, 1, 1)
        self.pw_figureOptions_sa.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.pw_figureOptions_sa, 0, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem7, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.pw_update_bt_1 = QtWidgets.QToolButton(self.tab_2)
        self.pw_update_bt_1.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_update_bt_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_update_bt_1.setFont(font)
        self.pw_update_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
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
        self.pw_update_bt_1.setObjectName("pw_update_bt_1")
        self.horizontalLayout_2.addWidget(self.pw_update_bt_1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem10, 3, 0, 1, 1)
        self.tab_view.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pw_plotOptions_sa = QtWidgets.QScrollArea(self.tab_4)
        self.pw_plotOptions_sa.setMinimumSize(QtCore.QSize(540, 0))
        self.pw_plotOptions_sa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_plotOptions_sa.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.pw_plotOptions_sa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pw_plotOptions_sa.setWidgetResizable(True)
        self.pw_plotOptions_sa.setObjectName("pw_plotOptions_sa")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1226, 596))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem11, 0, 1, 1, 1)
        self.pw_plotOptions_la = QtWidgets.QVBoxLayout()
        self.pw_plotOptions_la.setObjectName("pw_plotOptions_la")
        self.gridLayout_5.addLayout(self.pw_plotOptions_la, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 1, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 1, 0, 1, 1)
        self.pw_plotOptions_sa.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_7.addWidget(self.pw_plotOptions_sa, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem14, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.pw_update_bt_2 = QtWidgets.QToolButton(self.tab_4)
        self.pw_update_bt_2.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_update_bt_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_update_bt_2.setFont(font)
        self.pw_update_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
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
        self.pw_update_bt_2.setObjectName("pw_update_bt_2")
        self.horizontalLayout_4.addWidget(self.pw_update_bt_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem17, 3, 0, 1, 1)
        self.tab_view.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pw_saveOptions_sa = QtWidgets.QScrollArea(self.tab_3)
        self.pw_saveOptions_sa.setMinimumSize(QtCore.QSize(540, 0))
        self.pw_saveOptions_sa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pw_saveOptions_sa.setStyleSheet("QScrollArea { background: transparent; }\n"
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
        self.pw_saveOptions_sa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pw_saveOptions_sa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pw_saveOptions_sa.setWidgetResizable(True)
        self.pw_saveOptions_sa.setObjectName("pw_saveOptions_sa")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1226, 686))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem18 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem18, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem19, 2, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem20, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pw_saveOptions_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_1.setFont(font)
        self.pw_saveOptions_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_1.setObjectName("pw_saveOptions_lb_1")
        self.horizontalLayout_3.addWidget(self.pw_saveOptions_lb_1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem22)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pw_saveOptions_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_2.setMinimumSize(QtCore.QSize(70, 27))
        self.pw_saveOptions_lb_2.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_2.setFont(font)
        self.pw_saveOptions_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pw_saveOptions_lb_2.setObjectName("pw_saveOptions_lb_2")
        self.gridLayout_6.addWidget(self.pw_saveOptions_lb_2, 0, 0, 1, 1)
        self.pw_saveOptions_ln_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_ln_1.setEnabled(False)
        self.pw_saveOptions_ln_1.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_1.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ln_1.setFont(font)
        self.pw_saveOptions_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pw_saveOptions_ln_1.setObjectName("pw_saveOptions_ln_1")
        self.gridLayout_6.addWidget(self.pw_saveOptions_ln_1, 0, 1, 1, 1)
        self.pw_saveOptions_cb_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_cb_1.setEnabled(False)
        self.pw_saveOptions_cb_1.setMinimumSize(QtCore.QSize(130, 27))
        self.pw_saveOptions_cb_1.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_cb_1.setFont(font)
        self.pw_saveOptions_cb_1.setStyleSheet("QComboBox {\n"
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
        self.pw_saveOptions_cb_1.setObjectName("pw_saveOptions_cb_1")
        self.pw_saveOptions_cb_1.addItem("")
        self.pw_saveOptions_cb_1.addItem("")
        self.gridLayout_6.addWidget(self.pw_saveOptions_cb_1, 0, 2, 1, 1)
        self.pw_saveOptions_lb_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_3.setMinimumSize(QtCore.QSize(70, 27))
        self.pw_saveOptions_lb_3.setMaximumSize(QtCore.QSize(70, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_3.setFont(font)
        self.pw_saveOptions_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pw_saveOptions_lb_3.setObjectName("pw_saveOptions_lb_3")
        self.gridLayout_6.addWidget(self.pw_saveOptions_lb_3, 1, 0, 1, 1)
        self.pw_saveOptions_ln_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_ln_2.setEnabled(False)
        self.pw_saveOptions_ln_2.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_2.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ln_2.setFont(font)
        self.pw_saveOptions_ln_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pw_saveOptions_ln_2.setObjectName("pw_saveOptions_ln_2")
        self.gridLayout_6.addWidget(self.pw_saveOptions_ln_2, 1, 1, 1, 1)
        self.pw_saveOptions_cb_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_cb_2.setEnabled(False)
        self.pw_saveOptions_cb_2.setMinimumSize(QtCore.QSize(130, 27))
        self.pw_saveOptions_cb_2.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_cb_2.setFont(font)
        self.pw_saveOptions_cb_2.setStyleSheet("QComboBox {\n"
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
        self.pw_saveOptions_cb_2.setObjectName("pw_saveOptions_cb_2")
        self.pw_saveOptions_cb_2.addItem("")
        self.pw_saveOptions_cb_2.addItem("")
        self.gridLayout_6.addWidget(self.pw_saveOptions_cb_2, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_6)
        spacerItem23 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.pw_lock_bt_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.pw_lock_bt_1.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_lock_bt_1.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_lock_bt_1.setStyleSheet("QToolButton {\n"
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
        icon3.addPixmap(QtGui.QPixmap("icons/lock_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_lock_bt_1.setIcon(icon3)
        self.pw_lock_bt_1.setIconSize(QtCore.QSize(23, 23))
        self.pw_lock_bt_1.setObjectName("pw_lock_bt_1")
        self.horizontalLayout.addWidget(self.pw_lock_bt_1)
        spacerItem24 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem24)
        self.pw_info_bt_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.pw_info_bt_1.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_1.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pw_info_bt_1.setIcon(icon4)
        self.pw_info_bt_1.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt_1.setObjectName("pw_info_bt_1")
        self.horizontalLayout.addWidget(self.pw_info_bt_1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem25)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem26)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pw_saveOptions_lb_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_4.setFont(font)
        self.pw_saveOptions_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_4.setObjectName("pw_saveOptions_lb_4")
        self.horizontalLayout_7.addWidget(self.pw_saveOptions_lb_4)
        self.pw_saveOptions_ln_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_ln_3.setMinimumSize(QtCore.QSize(100, 27))
        self.pw_saveOptions_ln_3.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ln_3.setFont(font)
        self.pw_saveOptions_ln_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_ln_3.setObjectName("pw_saveOptions_ln_3")
        self.horizontalLayout_7.addWidget(self.pw_saveOptions_ln_3)
        spacerItem27 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem27)
        self.pw_info_bt_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.pw_info_bt_2.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_2.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt_2.setIcon(icon4)
        self.pw_info_bt_2.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt_2.setObjectName("pw_info_bt_2")
        self.horizontalLayout_7.addWidget(self.pw_info_bt_2)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem28)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem29)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pw_saveOptions_lb_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_6.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_6.setFont(font)
        self.pw_saveOptions_lb_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_6.setObjectName("pw_saveOptions_lb_6")
        self.horizontalLayout_9.addWidget(self.pw_saveOptions_lb_6)
        self.pw_saveOptions_sl_1 = QtWidgets.QSlider(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_sl_1.setMinimumSize(QtCore.QSize(200, 0))
        self.pw_saveOptions_sl_1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pw_saveOptions_sl_1.setStyleSheet("QSlider::groove:horizontal {\n"
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
" }\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(0,0,200);\n"
"}")
        self.pw_saveOptions_sl_1.setMinimum(1)
        self.pw_saveOptions_sl_1.setMaximum(100)
        self.pw_saveOptions_sl_1.setProperty("value", 95)
        self.pw_saveOptions_sl_1.setOrientation(QtCore.Qt.Horizontal)
        self.pw_saveOptions_sl_1.setObjectName("pw_saveOptions_sl_1")
        self.horizontalLayout_9.addWidget(self.pw_saveOptions_sl_1)
        self.pw_saveOptions_lb_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_7.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_7.setFont(font)
        self.pw_saveOptions_lb_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_7.setObjectName("pw_saveOptions_lb_7")
        self.horizontalLayout_9.addWidget(self.pw_saveOptions_lb_7)
        spacerItem30 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem30)
        self.pw_info_bt_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.pw_info_bt_4.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_4.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt_4.setIcon(icon4)
        self.pw_info_bt_4.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt_4.setObjectName("pw_info_bt_4")
        self.horizontalLayout_9.addWidget(self.pw_info_bt_4)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem31)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem32 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem32)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pw_saveOptions_lb_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_lb_5.setMinimumSize(QtCore.QSize(0, 27))
        self.pw_saveOptions_lb_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_lb_5.setFont(font)
        self.pw_saveOptions_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pw_saveOptions_lb_5.setObjectName("pw_saveOptions_lb_5")
        self.horizontalLayout_8.addWidget(self.pw_saveOptions_lb_5)
        self.pw_saveOptions_ck_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_6)
        self.pw_saveOptions_ck_1.setMinimumSize(QtCore.QSize(20, 20))
        self.pw_saveOptions_ck_1.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pw_saveOptions_ck_1.setFont(font)
        self.pw_saveOptions_ck_1.setStyleSheet("")
        self.pw_saveOptions_ck_1.setText("")
        self.pw_saveOptions_ck_1.setObjectName("pw_saveOptions_ck_1")
        self.horizontalLayout_8.addWidget(self.pw_saveOptions_ck_1)
        spacerItem33 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem33)
        self.pw_info_bt_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.pw_info_bt_3.setMinimumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_3.setMaximumSize(QtCore.QSize(27, 27))
        self.pw_info_bt_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pw_info_bt_3.setIcon(icon4)
        self.pw_info_bt_3.setIconSize(QtCore.QSize(23, 23))
        self.pw_info_bt_3.setObjectName("pw_info_bt_3")
        self.horizontalLayout_8.addWidget(self.pw_info_bt_3)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem34)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem35)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 1, 1, 2, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem36, 3, 1, 1, 1)
        self.pw_saveOptions_sa.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_8.addWidget(self.pw_saveOptions_sa, 0, 0, 1, 1)
        self.tab_view.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tab_view, 1, 0, 1, 1)

        self.retranslateUi(plotWindow)
        self.tab_view.setCurrentIndex(0)
        self.pw_plotWindow_cb_1.setCurrentIndex(-1)
        self.pw_saveOptions_cb_1.setCurrentIndex(1)
        self.pw_saveOptions_cb_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        _translate = QtCore.QCoreApplication.translate
        plotWindow.setWindowTitle(_translate("plotWindow", "Data Plot"))
        self.pw_plotWindow_lb_1.setText(_translate("plotWindow", "Time:"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab), _translate("plotWindow", "Plot window"))
        self.pw_update_bt_1.setText(_translate("plotWindow", "Update"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab_2), _translate("plotWindow", "Figure options"))
        self.pw_update_bt_2.setText(_translate("plotWindow", "Update"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab_4), _translate("plotWindow", "Plot options"))
        self.pw_saveOptions_lb_1.setText(_translate("plotWindow", "Figure dimensions:"))
        self.pw_saveOptions_lb_2.setText(_translate("plotWindow", "height:"))
        self.pw_saveOptions_cb_1.setItemText(0, _translate("plotWindow", "Centimeters"))
        self.pw_saveOptions_cb_1.setItemText(1, _translate("plotWindow", "Inches"))
        self.pw_saveOptions_lb_3.setText(_translate("plotWindow", "width:"))
        self.pw_saveOptions_cb_2.setItemText(0, _translate("plotWindow", "Centimeters"))
        self.pw_saveOptions_cb_2.setItemText(1, _translate("plotWindow", "Inches"))
        self.pw_saveOptions_lb_4.setText(_translate("plotWindow", "Figure resolution:"))
        self.pw_saveOptions_lb_6.setText(_translate("plotWindow", "Figure quality (JPEG only):"))
        self.pw_saveOptions_lb_7.setText(_translate("plotWindow", "TMP"))
        self.pw_saveOptions_lb_5.setText(_translate("plotWindow", "Transparent background ?"))
        self.tab_view.setTabText(self.tab_view.indexOf(self.tab_3), _translate("plotWindow", "Save options"))

