import logging
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_createvariablewindow import Ui_createvariableWindow
from ui.Ui_setlistwindow import Ui_setlistWindow
from functions.utils import clear_layout


class MyVariable(QtWidgets.QDialog, Ui_createvariableWindow):
    def __init__(self):
        logging.debug('gui - other_windows_functions.py - MyVariable - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.gridLayout_4.setAlignment(QtCore.Qt.AlignTop)
        self.cvw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.custom_dict = {}
        self.new_variable = None
        self.egads_instance = None
        self.cvw_cancel_button.clicked.connect(self.closeWindow)
        self.cvw_create_button.clicked.connect(self.create_variable)
        self.cvw_combobox_1.currentIndexChanged.connect(self.set_creation_option)
        self.cvw_line_4.setText('9.969209968386869e+36')
        self.cvw_line_1.textChanged.connect(self.activate_create_button)
        self.cvw_line_2.textChanged.connect(self.activate_create_button)
        self.cvw_line_4.textChanged.connect(self.activate_create_button)
        self.cvw_label_14.setVisible(False)
        self.cvw_label_13.setVisible(False)
        self.cvw_label_12.setVisible(False)
        self.cvw_combobox_6.setVisible(False)
        self.cvw_combobox_7.setVisible(False)
        self.cvw_combobox_8.setVisible(False)

    def set_creation_option(self):
        clear_layout(self.cvw_vertical_layout)
        if self.cvw_combobox_1.currentIndex() == 1:
            self.set_scalar_options()
        elif self.cvw_combobox_1.currentIndex() == 2:
            self.set_vector_options()
        elif self.cvw_combobox_1.currentIndex() == 3:
            self.set_array_options()

    def set_scalar_options(self):
        font1 = QtGui.QFont()
        font1.setFamily("Source Sans Pro")
        font1.setPointSize(11)
        font1.setKerning(True)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("Source Sans Pro")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.cvw_label_6 = QtWidgets.QLabel()
        self.cvw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_6.setFont(font1)
        self.cvw_label_6.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_6.setLineWidth(0)
        self.cvw_label_6.setMidLineWidth(0)
        self.cvw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignCenter)
        self.cvw_label_6.setWordWrap(True)
        self.cvw_label_6.setObjectName("cvw_label_6")
        self.horizontalLayout.addWidget(self.cvw_label_6)
        self.cvw_line_5 = QtWidgets.QLineEdit()
        self.cvw_line_5.setEnabled(True)
        self.cvw_line_5.setMinimumSize(QtCore.QSize(100, 27))
        self.cvw_line_5.setMaximumSize(QtCore.QSize(100, 27))
        self.cvw_line_5.setFont(font2)
        self.cvw_line_5.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_5.setObjectName("cvw_line_5")
        self.horizontalLayout.addWidget(self.cvw_line_5)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.info_button_6 = QtWidgets.QToolButton()
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
        self.horizontalLayout.addWidget(self.info_button_6)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.cvw_vertical_layout.addLayout(self.horizontalLayout)
        self.cvw_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.cvw_label_6.setText("Value:")
        self.cvw_line_5.textChanged.connect(self.activate_create_button)

    def set_vector_options(self):
        font1 = QtGui.QFont()
        font1.setFamily("Source Sans Pro")
        font1.setPointSize(11)
        font1.setKerning(True)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("Source Sans Pro")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cvw_label_6 = QtWidgets.QLabel()
        self.cvw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_6.setFont(font1)
        self.cvw_label_6.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_6.setLineWidth(0)
        self.cvw_label_6.setMidLineWidth(0)
        self.cvw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cvw_label_6.setWordWrap(False)
        self.cvw_label_6.setObjectName("cvw_label_6")
        self.gridLayout.addWidget(self.cvw_label_6, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(7, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cvw_spinbox_1 = QtWidgets.QSpinBox()
        self.cvw_spinbox_1.setMinimumSize(QtCore.QSize(100, 27))
        self.cvw_spinbox_1.setMaximumSize(QtCore.QSize(100, 27))
        self.cvw_spinbox_1.setStyleSheet("QSpinBox {\n"
                                         "    border-radius: 3px;\n"
                                         "    padding: 1px 4px 1px 4px;\n"
                                         "    background-color:  rgb(240, 240, 240);\n"
                                         "    color: rgb(45,45,45);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox:disabled {\n"
                                         "    background-color:  rgb(200,200,200);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::up-button {\n"
                                         "    subcontrol-origin: border;\n"
                                         "    subcontrol-position: top right;\n"
                                         "    width: 20px;\n"
                                         "    border-width: 1px;\n"
                                         "    background-color: rgb(205, 205, 205);\n"
                                         "    border: 1px solid rgb(180, 180, 180);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::up-button:hover {\n"
                                         "    background-color: rgb(166, 166, 166);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::up-button:pressed {\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::up-arrow {\n"
                                         "    image: url(icons/up_arrow_icon.svg); \n"
                                         "    width: 11px;\n"
                                         "    height: 11px\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::down-button {\n"
                                         "    subcontrol-origin: border;\n"
                                         "    subcontrol-position: bottom right;\n"
                                         "    width: 20px;\n"
                                         "    border-width: 1px;\n"
                                         "    background-color: rgb(205, 205, 205);\n"
                                         "    border: 1px solid rgb(180, 180, 180);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::down-button:hover {\n"
                                         "    background-color: rgb(166, 166, 166);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::down-button:pressed {\n"
                                         "    background-color: rgb(96, 96, 96);\n"
                                         "}\n"
                                         "\n"
                                         "QSpinBox::down-arrow {\n"
                                         "    image: url(icons/down_arrow_icon.svg); \n"
                                         "    width: 11px;\n"
                                         "    height: 11px\n"
                                         "}")
        self.cvw_spinbox_1.setMinimum(2)
        self.cvw_spinbox_1.setMaximum(16777215)
        self.cvw_spinbox_1.setObjectName("cvw_spinbox_1")
        self.horizontalLayout.addWidget(self.cvw_spinbox_1)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cvw_label_12 = QtWidgets.QLabel()
        self.cvw_label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_12.setFont(font1)
        self.cvw_label_12.setStyleSheet("QLabel {\n"
                                        "   color: rgb(45,45,45);\n"
                                        "}")
        self.cvw_label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_12.setLineWidth(0)
        self.cvw_label_12.setMidLineWidth(0)
        self.cvw_label_12.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_12.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_12.setWordWrap(False)
        self.cvw_label_12.setObjectName("cvw_label_12")
        self.horizontalLayout_3.addWidget(self.cvw_label_12)
        self.cvw_combobox_3 = QtWidgets.QComboBox()
        self.cvw_combobox_3.setMinimumSize(QtCore.QSize(120, 27))
        self.cvw_combobox_3.setMaximumSize(QtCore.QSize(120, 27))
        self.cvw_combobox_3.setFont(font2)
        self.cvw_combobox_3.setStyleSheet("QComboBox {\n"
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
        self.cvw_combobox_3.setFrame(False)
        self.cvw_combobox_3.setObjectName("cvw_combobox_3")
        self.cvw_combobox_3.addItem("")
        self.cvw_combobox_3.addItem("")
        self.cvw_combobox_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout_3.addWidget(self.cvw_combobox_3)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_7 = QtWidgets.QToolButton()
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
        self.horizontalLayout_3.addWidget(self.info_button_7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.cvw_label_7 = QtWidgets.QLabel()
        self.cvw_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_7.setFont(font1)
        self.cvw_label_7.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_7.setLineWidth(0)
        self.cvw_label_7.setMidLineWidth(0)
        self.cvw_label_7.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cvw_label_7.setWordWrap(False)
        self.cvw_label_7.setObjectName("cvw_label_7")
        self.gridLayout.addWidget(self.cvw_label_7, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cvw_combobox_2 = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvw_combobox_2.sizePolicy().hasHeightForWidth())
        self.cvw_combobox_2.setSizePolicy(sizePolicy)
        self.cvw_combobox_2.setMinimumSize(QtCore.QSize(160, 27))
        self.cvw_combobox_2.setMaximumSize(QtCore.QSize(160, 27))
        self.cvw_combobox_2.setFont(font2)
        self.cvw_combobox_2.setStyleSheet("QComboBox {\n"
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
        self.cvw_combobox_2.setFrame(False)
        self.cvw_combobox_2.setObjectName("cvw_combobox_2")
        self.cvw_combobox_2.addItem("")
        self.cvw_combobox_2.addItem("")
        self.cvw_combobox_2.addItem("")
        self.cvw_combobox_2.addItem("")
        self.cvw_combobox_2.addItem("")
        self.cvw_combobox_2.addItem("")
        self.cvw_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout_2.addWidget(self.cvw_combobox_2)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cvw_label_8 = QtWidgets.QLabel()
        self.cvw_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_8.setFont(font1)
        self.cvw_label_8.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_8.setLineWidth(0)
        self.cvw_label_8.setMidLineWidth(0)
        self.cvw_label_8.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_8.setWordWrap(False)
        self.cvw_label_8.setObjectName("cvw_label_8")
        self.horizontalLayout_4.addWidget(self.cvw_label_8)
        self.cvw_line_6 = QtWidgets.QLineEdit()
        self.cvw_line_6.setEnabled(True)
        self.cvw_line_6.setMinimumSize(QtCore.QSize(40, 27))
        self.cvw_line_6.setMaximumSize(QtCore.QSize(40, 27))
        self.cvw_line_6.setFont(font2)
        self.cvw_line_6.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_6.setObjectName("cvw_line_6")
        self.horizontalLayout_4.addWidget(self.cvw_line_6)
        self.cvw_set_button = QtWidgets.QToolButton()
        self.cvw_set_button.setMinimumSize(QtCore.QSize(100, 27))
        self.cvw_set_button.setMaximumSize(QtCore.QSize(100, 27))
        self.cvw_set_button.setFont(font1)
        self.cvw_set_button.setStyleSheet("QToolButton {\n"
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
        self.cvw_set_button.setIconSize(QtCore.QSize(25, 25))
        self.cvw_set_button.setObjectName("cvw_set_button")
        self.horizontalLayout_4.addWidget(self.cvw_set_button)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_8 = QtWidgets.QToolButton()
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
        self.horizontalLayout_4.addWidget(self.info_button_8)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)
        self.gridLayout.addItem(QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding,
                                                      QtWidgets.QSizePolicy.Minimum), 2, 0, 1, 1)
        self.cvw_label_9 = QtWidgets.QLabel()
        self.cvw_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_9.setMaximumSize(QtCore.QSize(16777215, 54))
        self.cvw_label_9.setFont(font1)
        self.cvw_label_9.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "   margin-left: 7px;\n"
                                       "}")
        self.cvw_label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_9.setLineWidth(0)
        self.cvw_label_9.setMidLineWidth(0)
        self.cvw_label_9.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_9.setWordWrap(False)
        self.cvw_label_9.setObjectName("cvw_label_9")
        self.gridLayout.addWidget(self.cvw_label_9, 2, 1, 1, 2)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.cvw_parse_button = QtWidgets.QToolButton()
        self.cvw_parse_button.setMaximumSize(QtCore.QSize(27, 27))
        self.cvw_parse_button.setStyleSheet("QToolButton {\n"
                                            "    border: 1px solid transparent;\n"
                                            "    background-color: transparent;\n"
                                            "    width: 27px;\n"
                                            "    height: 27px;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:flat {\n"
                                            "    border: none;\n"
                                            "}")
        self.cvw_parse_button.setText("")
        self.cvw_parse_button.setIcon(icon2)
        self.cvw_parse_button.setIconSize(QtCore.QSize(23, 23))
        self.cvw_parse_button.setAutoRaise(False)
        self.cvw_parse_button.setObjectName("cvw_parse_button")
        self.horizontalLayout_5.addWidget(self.cvw_parse_button)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.cvw_ln_1 = QtWidgets.QFrame()
        self.cvw_ln_1.setStyleSheet("QFrame {\n"
                                      "   background: rgb(190,190,190);\n"
                                      "   height: 5px;\n"
                                      "   border: 0px solid black;\n"
                                      "}")
        self.cvw_ln_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.cvw_ln_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cvw_ln_1.setObjectName("cvw_ln_1")
        self.verticalLayout.addWidget(self.cvw_ln_1)
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.cvw_table_1 = QtWidgets.QTableWidget()
        self.cvw_table_1.setMinimumSize(QtCore.QSize(0, 100))
        self.cvw_table_1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.cvw_table_1.setFont(font2)
        self.cvw_table_1.setStyleSheet("QTableWidget {\n"
                                       "    background-color: rgb(240,240,240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
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
        self.cvw_table_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_table_1.setGridStyle(QtCore.Qt.SolidLine)
        self.cvw_table_1.setColumnCount(0)
        self.cvw_table_1.setObjectName("cvw_table_1")
        self.cvw_table_1.setRowCount(0)
        self.verticalLayout.addWidget(self.cvw_table_1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.cvw_vertical_layout.addLayout(self.horizontalLayout_6)
        self.cvw_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.cvw_label_6.setText("Vector size:")
        self.cvw_label_12.setText("Vector direction:")
        self.cvw_combobox_3.setItemText(0, "Horizontal")
        self.cvw_combobox_3.setItemText(1, "Vertical")
        self.cvw_label_7.setText("Fill vector with:")
        self.cvw_combobox_2.setItemText(0, "Make a choice...")
        self.cvw_combobox_2.setItemText(1, "zeros")
        self.cvw_combobox_2.setItemText(2, "ones")
        self.cvw_combobox_2.setItemText(3, "custom value")
        self.cvw_combobox_2.setItemText(4, "values from 0 to 2")
        self.cvw_combobox_2.setItemText(5, "values from n to m")
        self.cvw_label_8.setText("Value:")
        self.cvw_set_button.setText("Set")
        self.cvw_label_8.setVisible(False)
        self.cvw_label_9.setVisible(False)
        self.cvw_set_button.setVisible(False)
        self.cvw_line_6.setVisible(False)
        self.cvw_parse_button.setEnabled(False)
        self.cvw_label_12.setEnabled(False)
        self.cvw_combobox_3.setEnabled(False)
        self.custom_dict = {}
        self.cvw_combobox_2.currentIndexChanged.connect(self.set_fill_options)
        self.cvw_spinbox_1.valueChanged.connect(self.set_length_value)
        self.cvw_combobox_2.currentIndexChanged.connect(self.activate_preview_button)
        self.cvw_spinbox_1.valueChanged.connect(self.activate_preview_button)
        self.cvw_line_6.textChanged.connect(self.activate_preview_button)
        self.cvw_parse_button.clicked.connect(self.create_variable_preview)
        self.cvw_set_button.clicked.connect(self.set_list_options)

    def set_array_options(self):
        font1 = QtGui.QFont()
        font1.setFamily("Source Sans Pro")
        font1.setPointSize(11)
        font1.setKerning(True)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("Source Sans Pro")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cvw_label_6 = QtWidgets.QLabel()
        self.cvw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_6.setFont(font1)
        self.cvw_label_6.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_6.setLineWidth(0)
        self.cvw_label_6.setMidLineWidth(0)
        self.cvw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cvw_label_6.setWordWrap(False)
        self.cvw_label_6.setObjectName("cvw_label_6")
        self.gridLayout.addWidget(self.cvw_label_6, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cvw_combobox_4 = QtWidgets.QComboBox()
        self.cvw_combobox_4.setMinimumSize(QtCore.QSize(60, 27))
        self.cvw_combobox_4.setMaximumSize(QtCore.QSize(60, 27))
        self.cvw_combobox_4.setFont(font2)
        self.cvw_combobox_4.setStyleSheet("QComboBox {\n"
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
        self.cvw_combobox_4.setFrame(False)
        self.cvw_combobox_4.setObjectName("cvw_combobox_4")
        self.cvw_combobox_4.addItem("")
        self.cvw_combobox_4.addItem("")
        self.cvw_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout.addWidget(self.cvw_combobox_4)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.cvw_label_8 = QtWidgets.QLabel()
        self.cvw_label_8.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_8.setFont(font1)
        self.cvw_label_8.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_8.setLineWidth(0)
        self.cvw_label_8.setMidLineWidth(0)
        self.cvw_label_8.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_8.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_8.setWordWrap(False)
        self.cvw_label_8.setObjectName("cvw_label_8")
        self.horizontalLayout.addWidget(self.cvw_label_8)
        self.cvw_line_9 = QtWidgets.QLineEdit()
        self.cvw_line_9.setEnabled(True)
        self.cvw_line_9.setMinimumSize(QtCore.QSize(40, 27))
        self.cvw_line_9.setMaximumSize(QtCore.QSize(40, 27))
        self.cvw_line_9.setFont(font2)
        self.cvw_line_9.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_9.setObjectName("cvw_line_9")
        self.horizontalLayout.addWidget(self.cvw_line_9)
        self.cvw_label_9 = QtWidgets.QLabel()
        self.cvw_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_9.setFont(font1)
        self.cvw_label_9.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_9.setLineWidth(0)
        self.cvw_label_9.setMidLineWidth(0)
        self.cvw_label_9.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_9.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_9.setWordWrap(False)
        self.cvw_label_9.setObjectName("cvw_label_9")
        self.horizontalLayout.addWidget(self.cvw_label_9)
        self.cvw_line_10 = QtWidgets.QLineEdit()
        self.cvw_line_10.setEnabled(True)
        self.cvw_line_10.setMinimumSize(QtCore.QSize(40, 27))
        self.cvw_line_10.setMaximumSize(QtCore.QSize(40, 27))
        self.cvw_line_10.setFont(font2)
        self.cvw_line_10.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_10.setObjectName("cvw_line_10")
        self.horizontalLayout.addWidget(self.cvw_line_10)
        self.cvw_label_11 = QtWidgets.QLabel()
        self.cvw_label_11.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_11.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_11.setFont(font1)
        self.cvw_label_11.setStyleSheet("QLabel {\n"
                                        "   color: rgb(45,45,45);\n"
                                        "}")
        self.cvw_label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_11.setLineWidth(0)
        self.cvw_label_11.setMidLineWidth(0)
        self.cvw_label_11.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_11.setWordWrap(False)
        self.cvw_label_11.setObjectName("cvw_label_11")
        self.horizontalLayout.addWidget(self.cvw_label_11)
        self.cvw_line_11 = QtWidgets.QLineEdit()
        self.cvw_line_11.setEnabled(True)
        self.cvw_line_11.setMinimumSize(QtCore.QSize(40, 27))
        self.cvw_line_11.setMaximumSize(QtCore.QSize(40, 27))
        self.cvw_line_11.setFont(font2)
        self.cvw_line_11.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_11.setObjectName("cvw_line_11")
        self.horizontalLayout.addWidget(self.cvw_line_11)
        self.horizontalLayout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Minimum))
        self.info_button_9 = QtWidgets.QToolButton()
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
        self.horizontalLayout.addWidget(self.info_button_9)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.cvw_label_7 = QtWidgets.QLabel()
        self.cvw_label_7.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_7.setFont(font1)
        self.cvw_label_7.setStyleSheet("QLabel {\n"
                                       "   color: rgb(45,45,45);\n"
                                       "}")
        self.cvw_label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_7.setLineWidth(0)
        self.cvw_label_7.setMidLineWidth(0)
        self.cvw_label_7.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cvw_label_7.setWordWrap(False)
        self.cvw_label_7.setObjectName("cvw_label_7")
        self.gridLayout.addWidget(self.cvw_label_7, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cvw_combobox_5 = QtWidgets.QComboBox()
        self.cvw_combobox_5.setMinimumSize(QtCore.QSize(230, 27))
        self.cvw_combobox_5.setMaximumSize(QtCore.QSize(230, 27))
        self.cvw_combobox_5.setFont(font2)
        self.cvw_combobox_5.setStyleSheet("QComboBox {\n"
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
        self.cvw_combobox_5.setFrame(False)
        self.cvw_combobox_5.setObjectName("cvw_combobox_5")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.addItem("")
        self.cvw_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout_2.addWidget(self.cvw_combobox_5)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.cvw_label_15 = QtWidgets.QLabel()
        self.cvw_label_15.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_15.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_15.setFont(font1)
        self.cvw_label_15.setStyleSheet("QLabel {\n"
                                        "   color: rgb(45,45,45);\n"
                                        "}")
        self.cvw_label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_15.setLineWidth(0)
        self.cvw_label_15.setMidLineWidth(0)
        self.cvw_label_15.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_15.setWordWrap(False)
        self.cvw_label_15.setObjectName("cvw_label_15")
        self.horizontalLayout_2.addWidget(self.cvw_label_15)
        self.cvw_line_7 = QtWidgets.QLineEdit()
        self.cvw_line_7.setEnabled(True)
        self.cvw_line_7.setMinimumSize(QtCore.QSize(40, 27))
        self.cvw_line_7.setMaximumSize(QtCore.QSize(40, 27))
        self.cvw_line_7.setFont(font2)
        self.cvw_line_7.setStyleSheet("QLineEdit {\n"
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
        self.cvw_line_7.setObjectName("cvw_line_7")
        self.horizontalLayout_2.addWidget(self.cvw_line_7)
        self.cvw_set_button = QtWidgets.QToolButton()
        self.cvw_set_button.setMinimumSize(QtCore.QSize(100, 27))
        self.cvw_set_button.setMaximumSize(QtCore.QSize(100, 27))
        self.cvw_set_button.setFont(font1)
        self.cvw_set_button.setStyleSheet("QToolButton {\n"
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
        self.cvw_set_button.setIconSize(QtCore.QSize(25, 25))
        self.cvw_set_button.setObjectName("cvw_set_button")
        self.horizontalLayout_2.addWidget(self.cvw_set_button)
        self.cvw_combobox_6 = QtWidgets.QComboBox()
        self.cvw_combobox_6.setMinimumSize(QtCore.QSize(110, 27))
        self.cvw_combobox_6.setMaximumSize(QtCore.QSize(110, 27))
        self.cvw_combobox_6.setFont(font2)
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
        self.cvw_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout_2.addWidget(self.cvw_combobox_6)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.info_button_10 = QtWidgets.QToolButton()
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
        self.horizontalLayout_2.addWidget(self.info_button_10)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.gridLayout.addItem(QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding,
                                                      QtWidgets.QSizePolicy.Minimum), 2, 0, 1, 1)
        self.cvw_label_10 = QtWidgets.QLabel()
        self.cvw_label_10.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_10.setMaximumSize(QtCore.QSize(16777215, 54))
        self.cvw_label_10.setFont(font1)
        self.cvw_label_10.setStyleSheet("QLabel {\n"
                                        "   color: rgb(45,45,45);\n"
                                        "}")
        self.cvw_label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_10.setLineWidth(0)
        self.cvw_label_10.setMidLineWidth(0)
        self.cvw_label_10.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_10.setWordWrap(False)
        self.cvw_label_10.setObjectName("cvw_label_10")
        self.gridLayout.addWidget(self.cvw_label_10, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.cvw_parse_button = QtWidgets.QToolButton()
        self.cvw_parse_button.setMaximumSize(QtCore.QSize(27, 27))
        self.cvw_parse_button.setStyleSheet("QToolButton {\n"
                                            "    border: 1px solid transparent;\n"
                                            "    background-color: transparent;\n"
                                            "    width: 27px;\n"
                                            "    height: 27px;\n"
                                            "}\n"
                                            "\n"
                                            "QToolButton:flat {\n"
                                            "    border: none;\n"
                                            "}")
        self.cvw_parse_button.setText("")
        self.cvw_parse_button.setIcon(icon2)
        self.cvw_parse_button.setIconSize(QtCore.QSize(23, 23))
        self.cvw_parse_button.setAutoRaise(False)
        self.cvw_parse_button.setObjectName("cvw_parse_button")
        self.horizontalLayout_3.addWidget(self.cvw_parse_button)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.cvw_ln_1 = QtWidgets.QFrame()
        self.cvw_ln_1.setStyleSheet("QFrame {\n"
                                      "   background: rgb(190,190,190);\n"
                                      "   height: 5px;\n"
                                      "   border: 0px solid black;\n"
                                      "}")
        self.cvw_ln_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.cvw_ln_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cvw_ln_1.setObjectName("cvw_ln_1")
        self.verticalLayout.addWidget(self.cvw_ln_1)
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cvw_label_12 = QtWidgets.QLabel()
        self.cvw_label_12.setEnabled(False)
        self.cvw_label_12.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_12.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_12.setFont(font1)
        self.cvw_label_12.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
        self.cvw_label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_12.setLineWidth(0)
        self.cvw_label_12.setMidLineWidth(0)
        self.cvw_label_12.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_12.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_12.setWordWrap(False)
        self.cvw_label_12.setObjectName("cvw_label_12")
        self.horizontalLayout_4.addWidget(self.cvw_label_12)
        self.ew_slider_2 = QtWidgets.QSlider()
        self.ew_slider_2.setEnabled(False)
        self.ew_slider_2.setMinimumSize(QtCore.QSize(300, 27))
        self.ew_slider_2.setMaximumSize(QtCore.QSize(300, 27))
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
        self.ew_slider_2.setMinimum(1)
        self.ew_slider_2.setMaximum(100)
        self.ew_slider_2.setSingleStep(1)
        self.ew_slider_2.setPageStep(1)
        self.ew_slider_2.setProperty("value", 1)
        self.ew_slider_2.setSliderPosition(1)
        self.ew_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.ew_slider_2.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.ew_slider_2.setObjectName("ew_slider_2")
        self.horizontalLayout_4.addWidget(self.ew_slider_2)
        self.cvw_navigate_1 = QtWidgets.QToolButton()
        self.cvw_navigate_1.setEnabled(False)
        self.cvw_navigate_1.setMaximumSize(QtCore.QSize(27, 27))
        self.cvw_navigate_1.setStyleSheet("QToolButton {\n"
                                          "    border: 1px solid transparent;\n"
                                          "    background-color: transparent;\n"
                                          "    width: 27px;\n"
                                          "    height: 27px;\n"
                                          "}\n"
                                          "\n"
                                          "QToolButton:flat {\n"
                                          "    border: none;\n"
                                          "}")
        self.cvw_navigate_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/left_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cvw_navigate_1.setIcon(icon3)
        self.cvw_navigate_1.setIconSize(QtCore.QSize(23, 23))
        self.cvw_navigate_1.setAutoRaise(False)
        self.cvw_navigate_1.setObjectName("cvw_navigate_1")
        self.horizontalLayout_4.addWidget(self.cvw_navigate_1)
        self.cvw_navigate_2 = QtWidgets.QToolButton()
        self.cvw_navigate_2.setEnabled(False)
        self.cvw_navigate_2.setMaximumSize(QtCore.QSize(27, 27))
        self.cvw_navigate_2.setStyleSheet("QToolButton {\n"
                                          "    border: 1px solid transparent;\n"
                                          "    background-color: transparent;\n"
                                          "    width: 27px;\n"
                                          "    height: 27px;\n"
                                          "}\n"
                                          "\n"
                                          "QToolButton:flat {\n"
                                          "    border: none;\n"
                                          "}")
        self.cvw_navigate_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/right_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cvw_navigate_2.setIcon(icon4)
        self.cvw_navigate_2.setIconSize(QtCore.QSize(23, 23))
        self.cvw_navigate_2.setAutoRaise(False)
        self.cvw_navigate_2.setObjectName("cvw_navigate_2")
        self.horizontalLayout_4.addWidget(self.cvw_navigate_2)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.cvw_label_13 = QtWidgets.QLabel()
        self.cvw_label_13.setEnabled(False)
        self.cvw_label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_13.setFont(font1)
        self.cvw_label_13.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
        self.cvw_label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_13.setLineWidth(0)
        self.cvw_label_13.setMidLineWidth(0)
        self.cvw_label_13.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cvw_label_13.setWordWrap(True)
        self.cvw_label_13.setObjectName("cvw_label_13")
        self.horizontalLayout_4.addWidget(self.cvw_label_13)
        self.cvw_label_14 = QtWidgets.QLabel()
        self.cvw_label_14.setEnabled(False)
        self.cvw_label_14.setMinimumSize(QtCore.QSize(0, 27))
        self.cvw_label_14.setMaximumSize(QtCore.QSize(16777215, 27))
        self.cvw_label_14.setFont(font1)
        self.cvw_label_14.setStyleSheet("QLabel {\n"
                                        "    color: rgb(45,45,45);\n"
                                        "}\n"
                                        "\n"
                                        "QLabel:disabled {\n"
                                        "    color: rgb(145,145,145);\n"
                                        "}")
        self.cvw_label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cvw_label_14.setLineWidth(0)
        self.cvw_label_14.setMidLineWidth(0)
        self.cvw_label_14.setTextFormat(QtCore.Qt.AutoText)
        self.cvw_label_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cvw_label_14.setWordWrap(True)
        self.cvw_label_14.setObjectName("cvw_label_14")
        self.horizontalLayout_4.addWidget(self.cvw_label_14)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.cvw_table_1 = QtWidgets.QTableWidget()
        self.cvw_table_1.setMinimumSize(QtCore.QSize(0, 0))
        self.cvw_table_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cvw_table_1.setFont(font2)
        self.cvw_table_1.setStyleSheet("QTableWidget {\n"
                                       "    background-color: rgb(240,240,240);\n"
                                       "    color: rgb(45,45,45);\n"
                                       "}\n"
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
        self.cvw_table_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cvw_table_1.setGridStyle(QtCore.Qt.SolidLine)
        self.cvw_table_1.setObjectName("cvw_table_1")
        self.cvw_table_1.setColumnCount(0)
        self.cvw_table_1.setRowCount(0)
        self.cvw_table_1.horizontalHeader().setDefaultSectionSize(100)
        self.cvw_table_1.horizontalHeader().setMinimumSectionSize(80)
        self.cvw_table_1.verticalHeader().setDefaultSectionSize(30)
        self.cvw_table_1.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.cvw_table_1)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.cvw_vertical_layout.addLayout(self.horizontalLayout_5)
        self.cvw_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.cvw_label_6.setText("Array dimensions:")
        self.cvw_combobox_4.setItemText(0, "2")
        self.cvw_combobox_4.setItemText(1, "3")
        self.cvw_label_8.setText("Number of rows:")
        self.cvw_label_9.setText("columns:")
        self.cvw_label_11.setText("layers:")
        self.cvw_label_7.setText("Fill array with:")
        self.cvw_combobox_5.setItemText(0, "Make a choice...")
        self.cvw_combobox_5.setItemText(1, "zeros")
        self.cvw_combobox_5.setItemText(2, "ones")
        self.cvw_combobox_5.setItemText(3, "custom value")
        self.cvw_combobox_5.setItemText(4, "custom value for each layer")
        self.cvw_combobox_5.setItemText(5, "values from 0 to n")
        self.cvw_combobox_5.setItemText(6, "values from 0 to n for each layer")
        self.cvw_combobox_5.setItemText(7, "values from n to m")
        self.cvw_combobox_5.setItemText(8, "values from n to m for each layer")
        self.cvw_combobox_6.setItemText(0, "Horizontal")
        self.cvw_combobox_6.setItemText(1, "Vertical")
        self.cvw_label_12.setText("Navigate into layers:")
        self.cvw_label_13.setText("Layer #")
        self.cvw_label_14.setText("1")
        self.cvw_label_15.setText("Value:")
        self.cvw_set_button.setText("Set")
        self.cvw_label_15.setVisible(False)
        self.cvw_label_10.setVisible(False)
        self.cvw_set_button.setVisible(False)
        self.cvw_line_7.setVisible(False)
        self.cvw_label_11.setVisible(False)
        self.cvw_line_11.setVisible(False)
        self.cvw_line_11.setText('')
        self.cvw_combobox_6.setVisible(False)
        self.cvw_parse_button.setEnabled(False)
        self.custom_dict = {}
        self.cvw_combobox_5.currentIndexChanged.connect(self.set_fill_options)
        self.cvw_combobox_4.currentIndexChanged.connect(self.set_layer_options)
        self.cvw_parse_button.clicked.connect(self.create_variable_preview)
        self.cvw_line_9.textChanged.connect(self.set_n_value)
        self.cvw_line_10.textChanged.connect(self.set_n_value)
        self.cvw_line_11.textChanged.connect(self.set_n_value)
        self.cvw_combobox_6.currentTextChanged.connect(self.set_n_value)
        self.cvw_line_9.textChanged.connect(self.activate_preview_button)
        self.cvw_line_10.textChanged.connect(self.activate_preview_button)
        self.cvw_line_11.textChanged.connect(self.activate_preview_button)
        self.cvw_combobox_5.currentTextChanged.connect(self.activate_preview_button)
        self.cvw_line_7.textChanged.connect(self.activate_preview_button)

    def set_list_options(self):
        set_list = MySet()
        set_list.exec_()
        if self.cvw_combobox_1.currentIndex() == 2:
            if set_list.start is not None and set_list.end is not None:
                self.custom_dict.clear()
                self.custom_dict['start'] = set_list.start
                self.custom_dict['end'] = set_list.end
                self.cvw_label_9.setText('Start: ' + str(set_list.start) + ' / End: ' + str(set_list.end) + ' / Steps: '
                                         + str(self.cvw_spinbox_1.value() - 2))
                self.activate_preview_button()


    def set_n_value(self):
        n_2 = 'n'
        try:
            row = int(self.cvw_line_9.text())
        except ValueError:
            row = None
        try:
            col = int(self.cvw_line_10.text())
        except ValueError:
            col = None

        if self.cvw_combobox_4.currentIndex() == 0:
            try:
                n_1 = str(row * col - 1)
            except TypeError:
                n_1 = 'n'
        else:
            try:
                lay = int(self.cvw_line_11.text())
            except ValueError:
                lay = None
            try:
                n_1 = str(row * col * lay - 1)
            except TypeError:
                n_1 = 'n'
        self.cvw_combobox_5.setItemText(5, "values from 0 to " + n_1)
        if self.cvw_combobox_6.currentIndex() == 0:
            try:
                n_2 = str(int(self.cvw_line_10.text()) - 1)
            except ValueError:
                n_2 = 'n'
        elif self.cvw_combobox_6.currentIndex() == 1:
            try:
                n_2 = str(int(self.cvw_line_9.text()) - 1)
            except ValueError:
                n_2 = 'n'
        self.cvw_combobox_5.setItemText(6, "values from 0 to " + n_2 + " for each layer")

    def set_length_value(self, val):
        self.cvw_combobox_2.setItemText(4, 'values from 0 to ' + str(val - 1))
        if self.cvw_label_9.isVisible():
            if 'Start:' in self.cvw_label_9.text():
                self.cvw_label_9.setText('Start: ' + str(self.custom_dict['start']) + ' / End: '
                                         + str(self.custom_dict['end']) + ' / Steps: '
                                         + str(self.cvw_spinbox_1.value() - 2))


    def set_layer_options(self, val):
        if val == 0:
            self.cvw_label_11.setVisible(False)
            self.cvw_line_11.setVisible(False)
            self.cvw_line_11.setText('')
        else:
            self.cvw_label_11.setVisible(True)
            self.cvw_line_11.setVisible(True)
            self.cvw_line_11.setText('')

    def set_fill_options(self, val):
        if self.sender().objectName() == 'cvw_combobox_2':
            if val == 3:
                self.cvw_label_8.setVisible(True)
                self.cvw_line_6.setVisible(True)
                self.cvw_line_6.setText('')
                self.cvw_label_9.setVisible(False)
                self.cvw_label_9.setText('')
                self.cvw_set_button.setVisible(False)
            elif val == 5:
                self.cvw_label_8.setVisible(False)
                self.cvw_line_6.setVisible(False)
                self.cvw_line_6.setText('')
                self.cvw_label_9.setVisible(True)
                self.cvw_label_9.setText('Standby...')
                self.cvw_set_button.setVisible(True)
            else:
                self.cvw_label_8.setVisible(False)
                self.cvw_label_9.setVisible(False)
                self.cvw_label_9.setText('')
                self.cvw_set_button.setVisible(False)
                self.cvw_line_6.setVisible(False)
                self.cvw_line_6.setText('')
        elif self.sender().objectName() == 'cvw_combobox_5':
            if val == 3:
                self.cvw_label_15.setVisible(True)
                self.cvw_line_7.setVisible(True)
                self.cvw_line_7.setText('')
                self.cvw_label_10.setVisible(False)
                self.cvw_label_10.setText('')
                self.cvw_set_button.setVisible(False)
                self.cvw_combobox_6.setVisible(False)
            elif val == 4 or val == 7 or val == 8:
                self.cvw_label_15.setVisible(False)
                self.cvw_line_7.setVisible(False)
                self.cvw_line_7.setText('')
                self.cvw_label_10.setVisible(True)
                self.cvw_label_10.setText('Standby...')
                self.cvw_set_button.setVisible(True)
                self.cvw_combobox_6.setVisible(False)
            elif val == 5 or val == 6:
                self.cvw_label_15.setVisible(False)
                self.cvw_line_7.setVisible(False)
                self.cvw_line_7.setText('')
                self.cvw_label_10.setVisible(False)
                self.cvw_label_10.setText('')
                self.cvw_set_button.setVisible(False)
                self.cvw_combobox_6.setVisible(True)
            else:
                self.cvw_label_15.setVisible(False)
                self.cvw_label_10.setVisible(False)
                self.cvw_label_10.setText('')
                self.cvw_set_button.setVisible(False)
                self.cvw_line_7.setVisible(False)
                self.cvw_line_7.setText('')

    def activate_preview_button(self):
        if self.cvw_combobox_1.currentIndex() == 2:
            length = True
            custom = True
            if not self.cvw_spinbox_1.value():
                length = False
            if self.cvw_combobox_2.currentIndex() == 0:
                fill = False
            else:
                fill = True
                if self.cvw_combobox_2.currentIndex() == 3:
                    if not self.cvw_line_6.text():
                        custom = False
                    else:
                        try:
                            float(self.cvw_line_6.text())
                        except ValueError:
                            custom = False
                elif self.cvw_combobox_2.currentIndex() == 5:
                    if not self.custom_dict:
                        custom = False
            if length and custom and fill:
                self.cvw_parse_button.setEnabled(True)
            else:
                self.cvw_parse_button.setEnabled(False)
        elif self.cvw_combobox_1.currentIndex() == 3:
            custom = True
            row = True
            col = True
            lay = True
            if not self.cvw_line_9.text():
                row = False
            else:
                try:
                    int(self.cvw_line_9.text())
                except ValueError:
                    row = False
            if not self.cvw_line_10.text():
                col = False
            else:
                try:
                    int(self.cvw_line_10.text())
                except ValueError:
                    col = False
            if self.cvw_combobox_4.currentIndex() == 1:
                if not self.cvw_line_11.text():
                    lay = False
                else:
                    try:
                        int(self.cvw_line_11.text())
                    except ValueError:
                        lay = False
            val = self.cvw_combobox_5.currentIndex()
            if val == 0:
                fill = False
            else:
                fill = True
                if val == 3:
                    if not self.cvw_line_7.text():
                        custom = False
                    else:
                        try:
                            float(self.cvw_line_7.text())
                        except ValueError:
                            custom = False
                elif val == 4 or val == 7 or val == 8:
                    if not self.custom_dict:
                        custom = False
            if custom and fill and row and col and lay:
                self.cvw_parse_button.setEnabled(True)
            else:
                self.cvw_parse_button.setEnabled(False)

    def create_variable_preview(self):
        if self.cvw_combobox_1.currentIndex() == 2:
            try:
                self.cvw_table_1.cellChanged.disconnect(self.set_cell_value)
            except TypeError:
                pass
            self.cvw_table_1.clear()
            self.cvw_table_1.setMinimumSize(QtCore.QSize(0, 100))
            self.cvw_table_1.setMaximumSize(QtCore.QSize(16777215, 100))
            self.cvw_table_1.setColumnCount(self.cvw_spinbox_1.value())
            self.cvw_table_1.setRowCount(1)
            if self.cvw_combobox_2.currentIndex() == 1:
                for i in range(0, self.cvw_spinbox_1.value()):
                    self.cvw_table_1.setItem(0, i, QtWidgets.QTableWidgetItem('0'))
                self.new_variable = numpy.zeros((self.cvw_spinbox_1.value(),))
            elif self.cvw_combobox_2.currentIndex() == 2:
                for i in range(0, self.cvw_spinbox_1.value()):
                    self.cvw_table_1.setItem(0, i, QtWidgets.QTableWidgetItem('1'))
                self.new_variable = numpy.ones((self.cvw_spinbox_1.value(),))
            elif self.cvw_combobox_2.currentIndex() == 3:
                for i in range(0, self.cvw_spinbox_1.value()):
                    self.cvw_table_1.setItem(0, i, QtWidgets.QTableWidgetItem(self.cvw_line_6.text()))
                self.new_variable = numpy.ones((self.cvw_spinbox_1.value(),)) * float(self.cvw_line_6.text())
            elif self.cvw_combobox_2.currentIndex() == 4:
                self.new_variable = numpy.ndarray((self.cvw_spinbox_1.value(),))
                for i in range(0, self.cvw_spinbox_1.value()):
                    self.cvw_table_1.setItem(0, i, QtWidgets.QTableWidgetItem(str(i)))
                    self.new_variable[i] = float(i)
            elif self.cvw_combobox_2.currentIndex() == 5:
                self.new_variable = numpy.ndarray((self.cvw_spinbox_1.value(),))
                tmp = numpy.linspace(self.custom_dict['start'], self.custom_dict['end'],
                                     int(self.cvw_spinbox_1.value()))

                for i in range(0, self.cvw_spinbox_1.value()):
                    self.cvw_table_1.setItem(0, i, QtWidgets.QTableWidgetItem(str(tmp[i])))
                    self.new_variable[i] = tmp[i]



            self.cvw_table_1.cellChanged.connect(self.set_cell_value)
            self.activate_create_button()

    def set_cell_value(self, row, col):
        if self.cvw_combobox_1.currentIndex() == 2:
            self.new_variable[col] = float(self.cvw_table_1.item(row, col).text())



    def activate_create_button(self):
        var_name = True
        std_name = True
        fillvalue = True
        if not self.cvw_line_1.text():
            var_name = False
        if not self.cvw_line_2.text():
            std_name = False
        if not self.cvw_line_4.text():
            fillvalue = False
        else:
            try:
                float(self.cvw_line_4.text())
            except ValueError:
                fillvalue = False

        var_type = True
        if self.cvw_combobox_1.currentIndex() == 1:
            if not self.cvw_line_5.text():
                var_type = False
            else:
                try:
                    float(self.cvw_line_5.text())
                except ValueError:
                    var_type = False
        elif self.cvw_combobox_1.currentIndex() == 2:
            if self.new_variable is None:
                var_type = False
        elif self.cvw_combobox_1.currentIndex() == 3:
            var_type = False
        elif self.cvw_combobox_1.currentIndex() == 0:
            var_type = False

        if var_name and std_name and fillvalue and var_type:
            self.cvw_create_button.setEnabled(True)
        else:
            self.cvw_create_button.setEnabled(False)

    def create_variable(self):
        pass
        # var_dict =


        # self.egads_instance =

    def closeWindow(self):
        logging.debug('gui - variable_functions.py - MyVariable - closeWindow')
        self.close()


class MySet(QtWidgets.QDialog, Ui_setlistWindow):
    def __init__(self):
        logging.debug('gui - variable_functions.py - MySet - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.slw_ok_button.clicked.connect(self.set_list_values)
        self.slw_cancel_button.clicked.connect(self.closeWindow)
        self.start = None
        self.end = None
        self.slw_line_1.textChanged.connect(self.activate_ok_button)
        self.slw_line_2.textChanged.connect(self.activate_ok_button)
        logging.info('gui - variable_functions.py - MySet - ready')

    def activate_ok_button(self):
        logging.debug('gui - variable_functions.py - MySet - activate_ok_button')
        edit_1 = True
        edit_2 = True
        try:
            float(self.slw_line_1.text())
        except ValueError:
            edit_1 = False
        try:
            float(self.slw_line_2.text())
        except ValueError:
            edit_2 = False
        if edit_1 and edit_2:
            self.slw_ok_button.setEnabled(True)
        else:
            self.slw_ok_button.setEnabled(False)

    def set_list_values(self):
        logging.debug('gui - variable_functions.py - MySet - set_list_values')
        self.start = float(self.slw_line_1.text())
        self.end = float(self.slw_line_2.text())
        self.close()

    def closeWindow(self):
        logging.debug('gui - variable_functions.py - MySet - closeWindow')
        self.close()
