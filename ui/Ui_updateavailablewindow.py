# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadupdatewindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_updateAvailableWindow(object):
    def setupUi(self, downloadWindow):
        downloadWindow.setObjectName("updateAvailableWindow")
        downloadWindow.resize(520, 223)
        downloadWindow.setMinimumSize(QtCore.QSize(0, 0))
        downloadWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        downloadWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        downloadWindow.setWindowIcon(icon)
        downloadWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(downloadWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.dw_label_1 = QtWidgets.QLabel(downloadWindow)
        self.dw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.dw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_label_1.setFont(font)
        self.dw_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.dw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dw_label_1.setLineWidth(0)
        self.dw_label_1.setMidLineWidth(0)
        self.dw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.dw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.dw_label_1.setWordWrap(True)
        self.dw_label_1.setObjectName("dw_label_1")
        self.gridLayout.addWidget(self.dw_label_1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.dw_downloadButton = QtWidgets.QToolButton(downloadWindow)
        self.dw_downloadButton.setMinimumSize(QtCore.QSize(160, 27))
        self.dw_downloadButton.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_downloadButton.setFont(font)
        self.dw_downloadButton.setStyleSheet("QToolButton {\n"
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
        self.dw_downloadButton.setObjectName("dw_downloadButton")
        self.horizontalLayout.addWidget(self.dw_downloadButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.dw_downloadButton_2 = QtWidgets.QToolButton(downloadWindow)
        self.dw_downloadButton_2.setMinimumSize(QtCore.QSize(140, 27))
        self.dw_downloadButton_2.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_downloadButton_2.setFont(font)
        self.dw_downloadButton_2.setStyleSheet("QToolButton {\n"
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
        self.dw_downloadButton_2.setObjectName("dw_downloadButton_2")
        self.horizontalLayout.addWidget(self.dw_downloadButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.dw_okButton = QtWidgets.QToolButton(downloadWindow)
        self.dw_okButton.setMinimumSize(QtCore.QSize(100, 27))
        self.dw_okButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_okButton.setFont(font)
        self.dw_okButton.setStyleSheet("QToolButton {\n"
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
        self.dw_okButton.setObjectName("dw_okButton")
        self.horizontalLayout_2.addWidget(self.dw_okButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.retranslateUi(downloadWindow)
        QtCore.QMetaObject.connectSlotsByName(downloadWindow)

    def retranslateUi(self, downloadWindow):
        _translate = QtCore.QCoreApplication.translate
        downloadWindow.setWindowTitle(_translate("downloadWindow", "Information"))
        self.dw_label_1.setText(_translate("downloadWindow", "<html><head/><body><p>A new version of the EGADS GUI is available on GitHub. Click on <span style=\" font-weight:600;\">Download update</span> to download it, or click on <span style=\" font-weight:600;\">Visit GitHub</span> to have a look at the EGADS GUI repository on GitHub.</p></body></html>"))
        self.dw_downloadButton.setText(_translate("downloadWindow", "Download update"))
        self.dw_downloadButton_2.setText(_translate("downloadWindow", "Visit GitHub"))
        self.dw_okButton.setText(_translate("downloadWindow", "Ok"))

