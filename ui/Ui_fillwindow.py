# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fillwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fillWindow(object):
    def setupUi(self, fillWindow):
        fillWindow.setObjectName("fillWindow")
        fillWindow.resize(578, 232)
        fillWindow.setMinimumSize(QtCore.QSize(0, 0))
        fillWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        fillWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fillWindow.setWindowIcon(icon)
        fillWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(fillWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.fw_label_1 = QtWidgets.QLabel(fillWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fw_label_1.sizePolicy().hasHeightForWidth())
        self.fw_label_1.setSizePolicy(sizePolicy)
        self.fw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.fw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fw_label_1.setFont(font)
        self.fw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fw_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fw_label_1.setWordWrap(True)
        self.fw_label_1.setObjectName("fw_label_1")
        self.gridLayout.addWidget(self.fw_label_1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.fw_okButton = QtWidgets.QToolButton(fillWindow)
        self.fw_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.fw_okButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_okButton.setFont(font)
        self.fw_okButton.setStyleSheet("QToolButton {\n"
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
        self.fw_okButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.fw_okButton.setObjectName("fw_okButton")
        self.horizontalLayout_2.addWidget(self.fw_okButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.fw_cancelButton = QtWidgets.QToolButton(fillWindow)
        self.fw_cancelButton.setMinimumSize(QtCore.QSize(100, 27))
        self.fw_cancelButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_cancelButton.setFont(font)
        self.fw_cancelButton.setStyleSheet("QToolButton {\n"
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
        self.fw_cancelButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.fw_cancelButton.setObjectName("fw_cancelButton")
        self.horizontalLayout_2.addWidget(self.fw_cancelButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(fillWindow)
        QtCore.QMetaObject.connectSlotsByName(fillWindow)

    def retranslateUi(self, fillWindow):
        _translate = QtCore.QCoreApplication.translate
        fillWindow.setWindowTitle(_translate("fillWindow", "Warning"))
        self.fw_label_1.setText(_translate("fillWindow", "<html><head/><body><p align=\"justify\">All mandatory fields have not been filled in. You can still save your file if you want to complete/correct it later, but incomplete algorithm file will not be usable in EGADS and in the GUI until they have been completed.</p><p align=\"justify\">All fields which have not been completely filled in are indicated in <span style=\" font-weight:600; color:#c80000;\">red</span>.</p><p align=\"justify\"><span style=\" font-weight:600;\">Do not use an incomplete/incorrect algorithm for official processing.</span></p></body></html>"))
        self.fw_okButton.setText(_translate("fillWindow", "Save"))
        self.fw_cancelButton.setText(_translate("fillWindow", "Cancel"))

