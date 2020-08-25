# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unitwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_unitWindow(object):
    def setupUi(self, unitWindow):
        unitWindow.setObjectName("unitWindow")
        unitWindow.resize(567, 278)
        unitWindow.setMinimumSize(QtCore.QSize(0, 0))
        unitWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        unitWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/unit_validation_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        unitWindow.setWindowIcon(icon)
        unitWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(unitWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.uw_label = QtWidgets.QLabel(unitWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uw_label.sizePolicy().hasHeightForWidth())
        self.uw_label.setSizePolicy(sizePolicy)
        self.uw_label.setMinimumSize(QtCore.QSize(341, 120))
        self.uw_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.uw_label.setFont(font)
        self.uw_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.uw_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.uw_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.uw_label.setLineWidth(0)
        self.uw_label.setMidLineWidth(0)
        self.uw_label.setText("")
        self.uw_label.setTextFormat(QtCore.Qt.AutoText)
        self.uw_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.uw_label.setWordWrap(True)
        self.uw_label.setObjectName("uw_label")
        self.gridLayout.addWidget(self.uw_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.uw_okButton = QtWidgets.QToolButton(unitWindow)
        self.uw_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.uw_okButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.uw_okButton.setFont(font)
        self.uw_okButton.setStyleSheet("QToolButton {\n"
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
        self.uw_okButton.setObjectName("uw_okButton")
        self.horizontalLayout_2.addWidget(self.uw_okButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.uw_cancelButton = QtWidgets.QToolButton(unitWindow)
        self.uw_cancelButton.setMinimumSize(QtCore.QSize(100, 27))
        self.uw_cancelButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.uw_cancelButton.setFont(font)
        self.uw_cancelButton.setStyleSheet("QToolButton {\n"
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
        self.uw_cancelButton.setObjectName("uw_cancelButton")
        self.horizontalLayout_2.addWidget(self.uw_cancelButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(unitWindow)
        QtCore.QMetaObject.connectSlotsByName(unitWindow)

    def retranslateUi(self, unitWindow):
        _translate = QtCore.QCoreApplication.translate
        unitWindow.setWindowTitle(_translate("unitWindow", "Unit validation"))
        self.uw_okButton.setText(_translate("unitWindow", "Continue"))
        self.uw_cancelButton.setText(_translate("unitWindow", "Cancel"))

