# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addfilename.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Addfilename(object):
    def setupUi(self, Addfilename):
        Addfilename.setObjectName("Addfilename")
        Addfilename.resize(732, 275)
        Addfilename.setMinimumSize(QtCore.QSize(0, 0))
        Addfilename.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Addfilename.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/save_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Addfilename.setWindowIcon(icon)
        Addfilename.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Addfilename)
        self.gridLayout.setObjectName("gridLayout")
        self.ac_label = QtWidgets.QLabel(Addfilename)
        self.ac_label.setMinimumSize(QtCore.QSize(0, 0))
        self.ac_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ac_label.setFont(font)
        self.ac_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ac_label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.ac_label.setWordWrap(True)
        self.ac_label.setObjectName("ac_label")
        self.gridLayout.addWidget(self.ac_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ac_line = QtWidgets.QLineEdit(Addfilename)
        self.ac_line.setMinimumSize(QtCore.QSize(0, 27))
        self.ac_line.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ac_line.setFont(font)
        self.ac_line.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45)\n"
"}")
        self.ac_line.setFrame(False)
        self.ac_line.setObjectName("ac_line")
        self.horizontalLayout_2.addWidget(self.ac_line)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.ac_submitButton = QtWidgets.QToolButton(Addfilename)
        self.ac_submitButton.setMinimumSize(QtCore.QSize(93, 27))
        self.ac_submitButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ac_submitButton.setFont(font)
        self.ac_submitButton.setStyleSheet("QToolButton {\n"
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
        self.ac_submitButton.setObjectName("ac_submitButton")
        self.horizontalLayout.addWidget(self.ac_submitButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.ac_cancelButton = QtWidgets.QToolButton(Addfilename)
        self.ac_cancelButton.setMinimumSize(QtCore.QSize(100, 27))
        self.ac_cancelButton.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ac_cancelButton.setFont(font)
        self.ac_cancelButton.setStyleSheet("QToolButton {\n"
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
        self.ac_cancelButton.setObjectName("ac_cancelButton")
        self.horizontalLayout.addWidget(self.ac_cancelButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(Addfilename)
        QtCore.QMetaObject.connectSlotsByName(Addfilename)

    def retranslateUi(self, Addfilename):
        _translate = QtCore.QCoreApplication.translate
        Addfilename.setWindowTitle(_translate("Addfilename", "Save an algorithm file"))
        self.ac_label.setText(_translate("Addfilename", "<html><head/><body><p align=\"justify\">Please, enter a name for the new algorithm file. It should follow the EGADS algorithm file naming conventions, which is all lowercase with words separated by underscores and based on the algorithm name.</p><p><span style=\" text-decoration: underline;\">Ex:</span><span style=\" font-weight:600;\"> TemperaturePressureLaboratory </span>&gt;&gt;&gt; <span style=\" font-weight:600;\">temperature_pressure_laboratory.py</span></p><p align=\"center\"><span style=\" color:#c80000;\">Once saved, the file can be found in the \'algorithm/user\' directory of EGADS.</span></p></body></html>"))
        self.ac_submitButton.setText(_translate("Addfilename", "Submit"))
        self.ac_cancelButton.setText(_translate("Addfilename", "Cancel"))

