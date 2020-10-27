# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batchprocessing.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_batchProcessingWindow(object):
    def setupUi(self, batchProcessingWindow):
        batchProcessingWindow.setObjectName("batchProcessingWindow")
        batchProcessingWindow.resize(834, 604)
        batchProcessingWindow.setMinimumSize(QtCore.QSize(0, 0))
        batchProcessingWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        batchProcessingWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/batch_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        batchProcessingWindow.setWindowIcon(icon)
        batchProcessingWindow.setStyleSheet("")
        self.gridLayout_2 = QtWidgets.QGridLayout(batchProcessingWindow)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(batchProcessingWindow)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
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
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bw_label_1 = QtWidgets.QLabel(self.tab_1)
        self.bw_label_1.setEnabled(True)
        self.bw_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_1.setFont(font)
        self.bw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bw_label_1.setObjectName("bw_label_1")
        self.horizontalLayout_3.addWidget(self.bw_label_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bw_combobox_1 = QtWidgets.QComboBox(self.tab_1)
        self.bw_combobox_1.setMinimumSize(QtCore.QSize(300, 27))
        self.bw_combobox_1.setMaximumSize(QtCore.QSize(300, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_1.setFont(font)
        self.bw_combobox_1.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_1.setFrame(False)
        self.bw_combobox_1.setObjectName("bw_combobox_1")
        self.bw_combobox_1.addItem("")
        self.bw_combobox_1.addItem("")
        self.bw_combobox_1.addItem("")
        self.bw_combobox_1.addItem("")
        self.bw_combobox_1.addItem("")
        self.bw_combobox_1.addItem("")
        self.horizontalLayout.addWidget(self.bw_combobox_1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bw_info_1 = QtWidgets.QToolButton(self.tab_1)
        self.bw_info_1.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_1.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_1.setStyleSheet("QToolButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_info_1.setIcon(icon1)
        self.bw_info_1.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_1.setObjectName("bw_info_1")
        self.horizontalLayout.addWidget(self.bw_info_1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.bw_line_1 = QtWidgets.QFrame(self.tab_1)
        self.bw_line_1.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"}")
        self.bw_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.bw_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bw_line_1.setObjectName("bw_line_1")
        self.verticalLayout.addWidget(self.bw_line_1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.processing_layout = QtWidgets.QVBoxLayout()
        self.processing_layout.setObjectName("processing_layout")
        self.verticalLayout.addLayout(self.processing_layout)
        spacerItem5 = QtWidgets.QSpacerItem(738, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bw_label_5 = QtWidgets.QLabel(self.tab_1)
        self.bw_label_5.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_5.setFont(font)
        self.bw_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bw_label_5.setObjectName("bw_label_5")
        self.horizontalLayout_4.addWidget(self.bw_label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bw_combobox_4 = QtWidgets.QComboBox(self.tab_1)
        self.bw_combobox_4.setMinimumSize(QtCore.QSize(370, 27))
        self.bw_combobox_4.setMaximumSize(QtCore.QSize(370, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_4.setFont(font)
        self.bw_combobox_4.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_4.setFrame(False)
        self.bw_combobox_4.setObjectName("bw_combobox_4")
        self.bw_combobox_4.addItem("")
        self.bw_combobox_4.addItem("")
        self.horizontalLayout_5.addWidget(self.bw_combobox_4)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.bw_info_3 = QtWidgets.QToolButton(self.tab_1)
        self.bw_info_3.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_3.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_3.setIcon(icon1)
        self.bw_info_3.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_3.setObjectName("bw_info_3")
        self.horizontalLayout_5.addWidget(self.bw_info_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 2)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem11, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 38, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bw_edit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.bw_edit_2.setEnabled(True)
        self.bw_edit_2.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_2.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_2.setFont(font)
        self.bw_edit_2.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_2.setText("")
        self.bw_edit_2.setFrame(False)
        self.bw_edit_2.setObjectName("bw_edit_2")
        self.horizontalLayout_7.addWidget(self.bw_edit_2)
        self.bw_open_button_1 = QtWidgets.QToolButton(self.tab_2)
        self.bw_open_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_open_button_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_open_button_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_open_button_1.setIcon(icon2)
        self.bw_open_button_1.setIconSize(QtCore.QSize(23, 23))
        self.bw_open_button_1.setAutoRaise(False)
        self.bw_open_button_1.setObjectName("bw_open_button_1")
        self.horizontalLayout_7.addWidget(self.bw_open_button_1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.bw_info_4 = QtWidgets.QToolButton(self.tab_2)
        self.bw_info_4.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_4.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_4.setIcon(icon1)
        self.bw_info_4.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_4.setObjectName("bw_info_4")
        self.horizontalLayout_7.addWidget(self.bw_info_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(668, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem15, 3, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(240,240,240);\n"
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
"  border-left: 0px solid white;\n"
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
"  border-bottom-right-radius: 3px;\n"
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
"  border-top-right-radius: 3px;\n"
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
"  border-bottom-right-radius: 3px;\n"
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
"border-bottom-left-radius: 3px;\n"
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
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_6.addWidget(self.listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bw_up_button = QtWidgets.QToolButton(self.tab_2)
        self.bw_up_button.setEnabled(False)
        self.bw_up_button.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_up_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_up_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/up_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_up_button.setIcon(icon3)
        self.bw_up_button.setIconSize(QtCore.QSize(23, 23))
        self.bw_up_button.setAutoRaise(False)
        self.bw_up_button.setObjectName("bw_up_button")
        self.verticalLayout_2.addWidget(self.bw_up_button)
        self.bw_down_button = QtWidgets.QToolButton(self.tab_2)
        self.bw_down_button.setEnabled(False)
        self.bw_down_button.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_down_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_down_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/down_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_down_button.setIcon(icon4)
        self.bw_down_button.setIconSize(QtCore.QSize(23, 23))
        self.bw_down_button.setAutoRaise(False)
        self.bw_down_button.setObjectName("bw_down_button")
        self.verticalLayout_2.addWidget(self.bw_down_button)
        self.bw_plus_button = QtWidgets.QToolButton(self.tab_2)
        self.bw_plus_button.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_plus_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_plus_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/plus_2_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_plus_button.setIcon(icon5)
        self.bw_plus_button.setIconSize(QtCore.QSize(23, 23))
        self.bw_plus_button.setAutoRaise(False)
        self.bw_plus_button.setObjectName("bw_plus_button")
        self.verticalLayout_2.addWidget(self.bw_plus_button)
        self.bw_del_button = QtWidgets.QToolButton(self.tab_2)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_del_button.setIcon(icon6)
        self.bw_del_button.setIconSize(QtCore.QSize(23, 23))
        self.bw_del_button.setAutoRaise(False)
        self.bw_del_button.setObjectName("bw_del_button")
        self.verticalLayout_2.addWidget(self.bw_del_button)
        self.bw_reload_button = QtWidgets.QToolButton(self.tab_2)
        self.bw_reload_button.setEnabled(True)
        self.bw_reload_button.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_reload_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_reload_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/reload_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bw_reload_button.setIcon(icon7)
        self.bw_reload_button.setIconSize(QtCore.QSize(23, 23))
        self.bw_reload_button.setAutoRaise(False)
        self.bw_reload_button.setObjectName("bw_reload_button")
        self.verticalLayout_2.addWidget(self.bw_reload_button)
        spacerItem16 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.bw_file_info = QtWidgets.QToolButton(self.tab_2)
        self.bw_file_info.setEnabled(False)
        self.bw_file_info.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_file_info.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_file_info.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_file_info.setIcon(icon1)
        self.bw_file_info.setIconSize(QtCore.QSize(23, 23))
        self.bw_file_info.setObjectName("bw_file_info")
        self.verticalLayout_2.addWidget(self.bw_file_info)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.bw_label_11 = QtWidgets.QLabel(self.tab_2)
        self.bw_label_11.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_11.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_11.setFont(font)
        self.bw_label_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bw_label_11.setObjectName("bw_label_11")
        self.gridLayout_3.addWidget(self.bw_label_11, 1, 0, 1, 1)
        self.bw_label_6 = QtWidgets.QLabel(self.tab_2)
        self.bw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_6.setFont(font)
        self.bw_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bw_label_6.setObjectName("bw_label_6")
        self.gridLayout_3.addWidget(self.bw_label_6, 0, 0, 1, 1)
        self.bw_label_7 = QtWidgets.QLabel(self.tab_2)
        self.bw_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_7.setFont(font)
        self.bw_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.bw_label_7.setObjectName("bw_label_7")
        self.gridLayout_3.addWidget(self.bw_label_7, 4, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem17)
        self.bw_radiobox_1 = QtWidgets.QRadioButton(self.tab_2)
        self.bw_radiobox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_radiobox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_radiobox_1.setFont(font)
        self.bw_radiobox_1.setStyleSheet("QRadioButton {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"   color: rgb(145,145,145);\n"
"}")
        self.bw_radiobox_1.setChecked(True)
        self.bw_radiobox_1.setObjectName("bw_radiobox_1")
        self.buttonGroup = QtWidgets.QButtonGroup(batchProcessingWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.bw_radiobox_1)
        self.horizontalLayout_17.addWidget(self.bw_radiobox_1)
        spacerItem18 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem18)
        self.bw_radiobox_2 = QtWidgets.QRadioButton(self.tab_2)
        self.bw_radiobox_2.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_radiobox_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_radiobox_2.setFont(font)
        self.bw_radiobox_2.setStyleSheet("QRadioButton {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"   color: rgb(145,145,145);\n"
"}")
        self.bw_radiobox_2.setObjectName("bw_radiobox_2")
        self.buttonGroup.addButton(self.bw_radiobox_2)
        self.horizontalLayout_17.addWidget(self.bw_radiobox_2)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem19)
        self.bw_radiobox_3 = QtWidgets.QRadioButton(self.tab_2)
        self.bw_radiobox_3.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_radiobox_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_radiobox_3.setFont(font)
        self.bw_radiobox_3.setStyleSheet("QRadioButton {\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"   color: rgb(145,145,145);\n"
"}")
        self.bw_radiobox_3.setObjectName("bw_radiobox_3")
        self.buttonGroup.addButton(self.bw_radiobox_3)
        self.horizontalLayout_17.addWidget(self.bw_radiobox_3)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem20)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(10, 38, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem21, 1, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem22, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scroll_area = QtWidgets.QScrollArea(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.scroll_area.setFont(font)
        self.scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
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
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
"  background-color: rgb(219, 219, 219);\n"
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
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 810, 506))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem23 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem23, 0, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem24, 1, 0, 1, 1)
        self.options_layout = QtWidgets.QVBoxLayout()
        self.options_layout.setObjectName("options_layout")
        self.gridLayout_7.addLayout(self.options_layout, 1, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem25, 1, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem26, 2, 1, 1, 1)
        self.scroll_area.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem27 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem27, 0, 1, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem28, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.bw_label_8 = QtWidgets.QLabel(self.tab_4)
        self.bw_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_8.setFont(font)
        self.bw_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bw_label_8.setObjectName("bw_label_8")
        self.horizontalLayout_14.addWidget(self.bw_label_8)
        self.bw_edit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.bw_edit_3.setEnabled(True)
        self.bw_edit_3.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_3.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_3.setFont(font)
        self.bw_edit_3.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_3.setText("")
        self.bw_edit_3.setFrame(False)
        self.bw_edit_3.setObjectName("bw_edit_3")
        self.horizontalLayout_14.addWidget(self.bw_edit_3)
        self.bw_open_button_2 = QtWidgets.QToolButton(self.tab_4)
        self.bw_open_button_2.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_open_button_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_open_button_2.setText("")
        self.bw_open_button_2.setIcon(icon2)
        self.bw_open_button_2.setIconSize(QtCore.QSize(23, 23))
        self.bw_open_button_2.setAutoRaise(False)
        self.bw_open_button_2.setObjectName("bw_open_button_2")
        self.horizontalLayout_14.addWidget(self.bw_open_button_2)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem29)
        self.bw_info_5 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_5.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_5.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_5.setIcon(icon1)
        self.bw_info_5.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_5.setObjectName("bw_info_5")
        self.horizontalLayout_14.addWidget(self.bw_info_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem30 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem30)
        self.bw_line_2 = QtWidgets.QFrame(self.tab_4)
        self.bw_line_2.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"}")
        self.bw_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.bw_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bw_line_2.setObjectName("bw_line_2")
        self.verticalLayout_3.addWidget(self.bw_line_2)
        spacerItem31 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem31)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.bw_label_9 = QtWidgets.QLabel(self.tab_4)
        self.bw_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_9.setFont(font)
        self.bw_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.bw_label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bw_label_9.setObjectName("bw_label_9")
        self.horizontalLayout_15.addWidget(self.bw_label_9)
        spacerItem32 = QtWidgets.QSpacerItem(588, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem32)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem33)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.bw_checkbox_1 = QtWidgets.QCheckBox(self.tab_4)
        self.bw_checkbox_1.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_checkbox_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_checkbox_1.setFont(font)
        self.bw_checkbox_1.setStyleSheet("QCheckBox {\n"
"   color: rgb(45,45,45);\n"
"}")
        self.bw_checkbox_1.setChecked(True)
        self.bw_checkbox_1.setObjectName("bw_checkbox_1")
        self.horizontalLayout_13.addWidget(self.bw_checkbox_1)
        spacerItem34 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem34)
        self.bw_info_6 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_6.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_6.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_6.setIcon(icon1)
        self.bw_info_6.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_6.setObjectName("bw_info_6")
        self.horizontalLayout_13.addWidget(self.bw_info_6)
        spacerItem35 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem35)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.bw_label_10 = QtWidgets.QLabel(self.tab_4)
        self.bw_label_10.setEnabled(False)
        self.bw_label_10.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_label_10.setFont(font)
        self.bw_label_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.bw_label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bw_label_10.setWordWrap(True)
        self.bw_label_10.setIndent(20)
        self.bw_label_10.setObjectName("bw_label_10")
        self.verticalLayout_4.addWidget(self.bw_label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.bw_edit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.bw_edit_5.setEnabled(False)
        self.bw_edit_5.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_5.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_5.setFont(font)
        self.bw_edit_5.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_5.setText("")
        self.bw_edit_5.setFrame(False)
        self.bw_edit_5.setObjectName("bw_edit_5")
        self.horizontalLayout_8.addWidget(self.bw_edit_5)
        spacerItem36 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem36)
        self.bw_combobox_5 = QtWidgets.QComboBox(self.tab_4)
        self.bw_combobox_5.setEnabled(False)
        self.bw_combobox_5.setMinimumSize(QtCore.QSize(210, 27))
        self.bw_combobox_5.setMaximumSize(QtCore.QSize(210, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_5.setFont(font)
        self.bw_combobox_5.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_5.setFrame(False)
        self.bw_combobox_5.setObjectName("bw_combobox_5")
        self.bw_combobox_5.addItem("")
        self.bw_combobox_5.addItem("")
        self.bw_combobox_5.addItem("")
        self.bw_combobox_5.addItem("")
        self.bw_combobox_5.addItem("")
        self.horizontalLayout_8.addWidget(self.bw_combobox_5)
        self.bw_info_7 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_7.setEnabled(False)
        self.bw_info_7.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_7.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_7.setIcon(icon1)
        self.bw_info_7.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_7.setObjectName("bw_info_7")
        self.horizontalLayout_8.addWidget(self.bw_info_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.bw_edit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.bw_edit_6.setEnabled(False)
        self.bw_edit_6.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_6.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_6.setFont(font)
        self.bw_edit_6.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_6.setText("")
        self.bw_edit_6.setFrame(False)
        self.bw_edit_6.setObjectName("bw_edit_6")
        self.horizontalLayout_9.addWidget(self.bw_edit_6)
        spacerItem37 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem37)
        self.bw_combobox_6 = QtWidgets.QComboBox(self.tab_4)
        self.bw_combobox_6.setEnabled(False)
        self.bw_combobox_6.setMinimumSize(QtCore.QSize(210, 27))
        self.bw_combobox_6.setMaximumSize(QtCore.QSize(210, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_6.setFont(font)
        self.bw_combobox_6.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_6.setFrame(False)
        self.bw_combobox_6.setObjectName("bw_combobox_6")
        self.bw_combobox_6.addItem("")
        self.bw_combobox_6.addItem("")
        self.bw_combobox_6.addItem("")
        self.bw_combobox_6.addItem("")
        self.bw_combobox_6.addItem("")
        self.horizontalLayout_9.addWidget(self.bw_combobox_6)
        self.bw_info_8 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_8.setEnabled(False)
        self.bw_info_8.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_8.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_8.setIcon(icon1)
        self.bw_info_8.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_8.setObjectName("bw_info_8")
        self.horizontalLayout_9.addWidget(self.bw_info_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bw_edit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.bw_edit_7.setEnabled(False)
        self.bw_edit_7.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_7.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_7.setFont(font)
        self.bw_edit_7.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_7.setText("")
        self.bw_edit_7.setFrame(False)
        self.bw_edit_7.setObjectName("bw_edit_7")
        self.horizontalLayout_10.addWidget(self.bw_edit_7)
        spacerItem38 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem38)
        self.bw_combobox_7 = QtWidgets.QComboBox(self.tab_4)
        self.bw_combobox_7.setEnabled(False)
        self.bw_combobox_7.setMinimumSize(QtCore.QSize(210, 27))
        self.bw_combobox_7.setMaximumSize(QtCore.QSize(210, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_7.setFont(font)
        self.bw_combobox_7.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_7.setFrame(False)
        self.bw_combobox_7.setObjectName("bw_combobox_7")
        self.bw_combobox_7.addItem("")
        self.bw_combobox_7.addItem("")
        self.bw_combobox_7.addItem("")
        self.bw_combobox_7.addItem("")
        self.bw_combobox_7.addItem("")
        self.horizontalLayout_10.addWidget(self.bw_combobox_7)
        self.bw_info_9 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_9.setEnabled(False)
        self.bw_info_9.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_9.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_9.setIcon(icon1)
        self.bw_info_9.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_9.setObjectName("bw_info_9")
        self.horizontalLayout_10.addWidget(self.bw_info_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.bw_edit_8 = QtWidgets.QLineEdit(self.tab_4)
        self.bw_edit_8.setEnabled(False)
        self.bw_edit_8.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_8.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_8.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_8.setFont(font)
        self.bw_edit_8.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_8.setText("")
        self.bw_edit_8.setFrame(False)
        self.bw_edit_8.setObjectName("bw_edit_8")
        self.horizontalLayout_11.addWidget(self.bw_edit_8)
        spacerItem39 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem39)
        self.bw_combobox_8 = QtWidgets.QComboBox(self.tab_4)
        self.bw_combobox_8.setEnabled(False)
        self.bw_combobox_8.setMinimumSize(QtCore.QSize(210, 27))
        self.bw_combobox_8.setMaximumSize(QtCore.QSize(210, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_8.setFont(font)
        self.bw_combobox_8.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_8.setFrame(False)
        self.bw_combobox_8.setObjectName("bw_combobox_8")
        self.bw_combobox_8.addItem("")
        self.bw_combobox_8.addItem("")
        self.bw_combobox_8.addItem("")
        self.bw_combobox_8.addItem("")
        self.bw_combobox_8.addItem("")
        self.horizontalLayout_11.addWidget(self.bw_combobox_8)
        self.bw_info_10 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_10.setEnabled(False)
        self.bw_info_10.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_10.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_10.setIcon(icon1)
        self.bw_info_10.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_10.setObjectName("bw_info_10")
        self.horizontalLayout_11.addWidget(self.bw_info_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.bw_edit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.bw_edit_9.setEnabled(False)
        self.bw_edit_9.setMinimumSize(QtCore.QSize(150, 27))
        self.bw_edit_9.setMaximumSize(QtCore.QSize(16777215, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.bw_edit_9.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_edit_9.setFont(font)
        self.bw_edit_9.setStyleSheet("QLineEdit {\n"
"   border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"   background-color: rgb(240, 240, 240);\n"
"   color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"   background-color: rgb(200,200,200);\n"
"}")
        self.bw_edit_9.setText("")
        self.bw_edit_9.setFrame(False)
        self.bw_edit_9.setObjectName("bw_edit_9")
        self.horizontalLayout_12.addWidget(self.bw_edit_9)
        spacerItem40 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem40)
        self.bw_combobox_9 = QtWidgets.QComboBox(self.tab_4)
        self.bw_combobox_9.setEnabled(False)
        self.bw_combobox_9.setMinimumSize(QtCore.QSize(210, 27))
        self.bw_combobox_9.setMaximumSize(QtCore.QSize(210, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_combobox_9.setFont(font)
        self.bw_combobox_9.setStyleSheet("QComboBox {\n"
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
        self.bw_combobox_9.setFrame(False)
        self.bw_combobox_9.setObjectName("bw_combobox_9")
        self.bw_combobox_9.addItem("")
        self.bw_combobox_9.addItem("")
        self.bw_combobox_9.addItem("")
        self.bw_combobox_9.addItem("")
        self.bw_combobox_9.addItem("")
        self.horizontalLayout_12.addWidget(self.bw_combobox_9)
        self.bw_info_11 = QtWidgets.QToolButton(self.tab_4)
        self.bw_info_11.setEnabled(False)
        self.bw_info_11.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_info_11.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_info_11.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.bw_info_11.setIcon(icon1)
        self.bw_info_11.setIconSize(QtCore.QSize(23, 23))
        self.bw_info_11.setObjectName("bw_info_11")
        self.horizontalLayout_12.addWidget(self.bw_info_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_16.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 1, 1, 2, 2)
        spacerItem41 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem41, 2, 3, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem42, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem43, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bw_button_ok = QtWidgets.QToolButton(batchProcessingWindow)
        self.bw_button_ok.setEnabled(False)
        self.bw_button_ok.setMinimumSize(QtCore.QSize(180, 27))
        self.bw_button_ok.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_button_ok.setFont(font)
        self.bw_button_ok.setStyleSheet("QToolButton {\n"
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
        self.bw_button_ok.setObjectName("bw_button_ok")
        self.horizontalLayout_2.addWidget(self.bw_button_ok)
        spacerItem44 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem44)
        self.bw_button_cancel = QtWidgets.QToolButton(batchProcessingWindow)
        self.bw_button_cancel.setMinimumSize(QtCore.QSize(100, 27))
        self.bw_button_cancel.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.bw_button_cancel.setFont(font)
        self.bw_button_cancel.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45)\n"
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
        self.bw_button_cancel.setObjectName("bw_button_cancel")
        self.horizontalLayout_2.addWidget(self.bw_button_cancel)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem45)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(batchProcessingWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(batchProcessingWindow)

    def retranslateUi(self, batchProcessingWindow):
        _translate = QtCore.QCoreApplication.translate
        batchProcessingWindow.setWindowTitle(_translate("batchProcessingWindow", "Batch processinmg"))
        self.bw_label_1.setText(_translate("batchProcessingWindow", "Processing:"))
        self.bw_combobox_1.setItemText(0, _translate("batchProcessingWindow", "Make a choice..."))
        self.bw_combobox_1.setItemText(1, _translate("batchProcessingWindow", "Concatenate multiple files"))
        self.bw_combobox_1.setItemText(2, _translate("batchProcessingWindow", "Convert between different file formats"))
        self.bw_combobox_1.setItemText(3, _translate("batchProcessingWindow", "Delete one or more global metadata"))
        self.bw_combobox_1.setItemText(4, _translate("batchProcessingWindow", "Delete one or more variables"))
        self.bw_combobox_1.setItemText(5, _translate("batchProcessingWindow", "Execute an algorithm"))
        self.bw_label_5.setText(_translate("batchProcessingWindow", "Errors:"))
        self.bw_combobox_4.setItemText(0, _translate("batchProcessingWindow", "Stop processing if an error occurs"))
        self.bw_combobox_4.setItemText(1, _translate("batchProcessingWindow", "Continue processing and display errors at the end"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("batchProcessingWindow", "Processing"))
        self.bw_label_11.setText(_translate("batchProcessingWindow", "Format:"))
        self.bw_label_6.setText(_translate("batchProcessingWindow", "Folder:"))
        self.bw_label_7.setText(_translate("batchProcessingWindow", "Files:"))
        self.bw_radiobox_1.setText(_translate("batchProcessingWindow", "NetCDF"))
        self.bw_radiobox_2.setText(_translate("batchProcessingWindow", "NASA Ames"))
        self.bw_radiobox_3.setText(_translate("batchProcessingWindow", "HDF5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("batchProcessingWindow", "Source"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("batchProcessingWindow", "Options"))
        self.bw_label_8.setText(_translate("batchProcessingWindow", "Folder:"))
        self.bw_label_9.setText(_translate("batchProcessingWindow", "File naming"))
        self.bw_checkbox_1.setText(_translate("batchProcessingWindow", "Let the GUI handle the file naming"))
        self.bw_label_10.setText(_translate("batchProcessingWindow", "exemple"))
        self.bw_combobox_5.setItemText(0, _translate("batchProcessingWindow", "Make a choice..."))
        self.bw_combobox_5.setItemText(1, _translate("batchProcessingWindow", "Date and time"))
        self.bw_combobox_5.setItemText(2, _translate("batchProcessingWindow", "Original filename"))
        self.bw_combobox_5.setItemText(3, _translate("batchProcessingWindow", "Serial number with n digit"))
        self.bw_combobox_5.setItemText(4, _translate("batchProcessingWindow", "Text"))
        self.bw_combobox_6.setItemText(0, _translate("batchProcessingWindow", "Make a choice..."))
        self.bw_combobox_6.setItemText(1, _translate("batchProcessingWindow", "Date and time"))
        self.bw_combobox_6.setItemText(2, _translate("batchProcessingWindow", "Original filename"))
        self.bw_combobox_6.setItemText(3, _translate("batchProcessingWindow", "Serial number with n digit"))
        self.bw_combobox_6.setItemText(4, _translate("batchProcessingWindow", "Text"))
        self.bw_combobox_7.setItemText(0, _translate("batchProcessingWindow", "Make a choice..."))
        self.bw_combobox_7.setItemText(1, _translate("batchProcessingWindow", "Date and time"))
        self.bw_combobox_7.setItemText(2, _translate("batchProcessingWindow", "Original filename"))
        self.bw_combobox_7.setItemText(3, _translate("batchProcessingWindow", "Serial number with n digit"))
        self.bw_combobox_7.setItemText(4, _translate("batchProcessingWindow", "Text"))
        self.bw_combobox_8.setItemText(0, _translate("batchProcessingWindow", "Make a choice..."))
        self.bw_combobox_8.setItemText(1, _translate("batchProcessingWindow", "Date and time"))
        self.bw_combobox_8.setItemText(2, _translate("batchProcessingWindow", "Original filename"))
        self.bw_combobox_8.setItemText(3, _translate("batchProcessingWindow", "Serial number with n digit"))
        self.bw_combobox_8.setItemText(4, _translate("batchProcessingWindow", "Text"))
        self.bw_combobox_9.setItemText(0, _translate("batchProcessingWindow", "Make a choice..."))
        self.bw_combobox_9.setItemText(1, _translate("batchProcessingWindow", "Date and time"))
        self.bw_combobox_9.setItemText(2, _translate("batchProcessingWindow", "Original filename"))
        self.bw_combobox_9.setItemText(3, _translate("batchProcessingWindow", "Serial number with n digit"))
        self.bw_combobox_9.setItemText(4, _translate("batchProcessingWindow", "Text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("batchProcessingWindow", "Destination"))
        self.bw_button_ok.setText(_translate("batchProcessingWindow", "Launch processing"))
        self.bw_button_cancel.setText(_translate("batchProcessingWindow", "Cancel"))

