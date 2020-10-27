import logging
import pathlib
import egads
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_displayalgorithmwindow import Ui_displayAlgorithmWindow
from ui.Ui_processingwindow import Ui_processingWindow
from ui.Ui_creationwindow import Ui_creationWindow
from functions.utils import (Highlighter, create_datestring, prepare_long_string, check_string_max_length,
                             write_algorithm, clear_layout, font_creation_function, stylesheet_creation_function,
                             icon_creation_function)
from functions.window_functions.other_windows_functions import (MyInfo, MyFill, MyUnit, MyFilename, MyCategory,
                                                                MyOverwriteFilename, MyWait, MyCoeff,
                                                                MyExistingVariable)
from functions.thread_functions.processing_functions import VariableProcessingThread
from functions.help_functions import algorithm_creation_information_text


class MyAlgorithmDisplay(QtWidgets.QDialog, Ui_displayAlgorithmWindow):
    def __init__(self, algorithm_dict):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithmDisplay - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.algorithm_dict = algorithm_dict
        self.setWindowTitle('Algorithm - ' + self.algorithm_dict['File'])
        self.daw_okButton.clicked.connect(self.closeWindow)
        self.input_layout.setAlignment(QtCore.Qt.AlignTop)
        self.output_layout.setAlignment(QtCore.Qt.AlignTop)
        self.input_label_1 = []
        self.input_label_2 = []
        self.input_label_3 = []
        self.input_edit_1 = []
        self.input_edit_2 = []
        self.input_edit_3 = []
        self.input_line = []
        self.input_hor_lay_1 = []
        self.input_hor_lay_2 = []
        self.input_hor_lay_3 = []
        self.input_hor_lay_4 = []
        self.input_ver_lay_1 = []
        self.input_ver_lay_2 = []
        self.input_ver_lay_3 = []
        self.input_nbr = 0
        self.output_label_1 = []
        self.output_label_2 = []
        self.output_label_3 = []
        self.output_label_4 = []
        self.output_label_5 = []
        self.output_label_6 = []
        self.output_edit_1 = []
        self.output_edit_2 = []
        self.output_edit_3 = []
        self.output_edit_4 = []
        self.output_edit_5 = []
        self.output_edit_6 = []
        self.output_line = []
        self.output_hor_lay_1 = []
        self.output_hor_lay_2 = []
        self.output_hor_lay_3 = []
        self.output_hor_lay_4 = []
        self.output_nbr = 0
        self.highlighter = None
        self.populate_information()
        self.populate_algorithm()
        self.populate_inputs()
        self.populate_outputs()
        logging.info('gui - algorithm_windows_functions.py - MyAlgorithmDisplay ready')

    def populate_information(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithmDisplay - populate_information')
        self.daw_line_1.setText(self.algorithm_dict['Name'])
        self.daw_line_2.setText(self.algorithm_dict['Date'])
        self.daw_line_3.setText(self.algorithm_dict['Version'])
        self.daw_plain_1.setPlainText(self.algorithm_dict['Purpose'])
        self.daw_plain_2.setPlainText(self.algorithm_dict['Description'])
        self.daw_plain_3.setPlainText(self.algorithm_dict['Source'])
        self.daw_plain_4.setPlainText(self.algorithm_dict['References'])

    def populate_inputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithmDisplay - populate_inputs')
        font = font_creation_function('normal')
        font2 = font_creation_function('small')
        for input_dict in self.algorithm_dict['Input']:
            self.input_hor_lay_1.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_1[self.input_nbr].setObjectName('input_hor_lay_1_' + str(self.input_nbr))
            self.input_ver_lay_1.append(QtWidgets.QVBoxLayout())
            self.input_ver_lay_1[self.input_nbr].setObjectName('input_ver_lay_1_' + str(self.input_nbr))
            self.input_hor_lay_2.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_2[self.input_nbr].setObjectName('input_hor_lay_2_' + str(self.input_nbr))
            self.input_hor_lay_3.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_3[self.input_nbr].setObjectName('input_hor_lay_3_' + str(self.input_nbr))
            self.input_label_1.append(QtWidgets.QLabel())
            self.input_label_1[self.input_nbr].setMinimumSize(QtCore.QSize(80, 27))
            self.input_label_1[self.input_nbr].setMaximumSize(QtCore.QSize(80, 27))
            self.input_label_1[self.input_nbr].setFont(font)
            self.input_label_1[self.input_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.input_label_1[self.input_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                            QtCore.Qt.AlignTrailing |
                                                            QtCore.Qt.AlignVCenter)
            self.input_label_1[self.input_nbr].setObjectName('input_label_1_' + str(self.input_nbr))
            self.input_label_1[self.input_nbr].setText('Symbol:')
            self.input_hor_lay_2[self.input_nbr].addWidget(self.input_label_1[self.input_nbr])
            self.input_edit_1.append(QtWidgets.QLineEdit())
            self.input_edit_1[self.input_nbr].setEnabled(True)
            self.input_edit_1[self.input_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.input_edit_1[self.input_nbr].setMaximumSize(QtCore.QSize(150, 27))
            self.input_edit_1[self.input_nbr].setFont(font2)
            self.input_edit_1[self.input_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_edit_1[self.input_nbr].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.input_edit_1[self.input_nbr].setText('')
            self.input_edit_1[self.input_nbr].setFrame(False)
            self.input_edit_1[self.input_nbr].setReadOnly(True)
            self.input_edit_1[self.input_nbr].setObjectName('input_edit_1_' + str(self.input_nbr))
            self.input_hor_lay_2[self.input_nbr].addWidget(self.input_edit_1[self.input_nbr])
            self.input_ver_lay_1[self.input_nbr].addLayout(self.input_hor_lay_2[self.input_nbr])
            self.input_label_2.append(QtWidgets.QLabel())
            self.input_label_2[self.input_nbr].setMinimumSize(QtCore.QSize(80, 27))
            self.input_label_2[self.input_nbr].setMaximumSize(QtCore.QSize(80, 27))
            self.input_label_2[self.input_nbr].setFont(font)
            self.input_label_2[self.input_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.input_label_2[self.input_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                            QtCore.Qt.AlignTrailing |
                                                            QtCore.Qt.AlignVCenter)
            self.input_label_2[self.input_nbr].setObjectName('input_label_2_' + str(self.input_nbr))
            self.input_label_2[self.input_nbr].setText('Units:')
            self.input_hor_lay_3[self.input_nbr].addWidget(self.input_label_2[self.input_nbr])
            self.input_edit_2.append(QtWidgets.QLineEdit())
            self.input_edit_2[self.input_nbr].setEnabled(True)
            self.input_edit_2[self.input_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.input_edit_2[self.input_nbr].setMaximumSize(QtCore.QSize(150, 27))
            self.input_edit_2[self.input_nbr].setFont(font2)
            self.input_edit_2[self.input_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_edit_2[self.input_nbr].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.input_edit_2[self.input_nbr].setText('')
            self.input_edit_2[self.input_nbr].setFrame(False)
            self.input_edit_2[self.input_nbr].setReadOnly(True)
            self.input_edit_2[self.input_nbr].setObjectName('input_edit_2_' + str(self.input_nbr))
            self.input_hor_lay_3[self.input_nbr].addWidget(self.input_edit_2[self.input_nbr])
            self.input_ver_lay_1[self.input_nbr].addLayout(self.input_hor_lay_3[self.input_nbr])
            self.input_hor_lay_1[self.input_nbr].addLayout(self.input_ver_lay_1[self.input_nbr])
            self.input_hor_lay_4.append(QtWidgets.QHBoxLayout())
            self.input_hor_lay_4[self.input_nbr].setObjectName('input_hor_lay_4_' + str(self.input_nbr))
            self.input_ver_lay_2.append(QtWidgets.QHBoxLayout())
            self.input_ver_lay_2[self.input_nbr].setObjectName('input_ver_lay_2_' + str(self.input_nbr))
            self.input_label_3.append(QtWidgets.QLabel())
            self.input_label_3[self.input_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.input_label_3[self.input_nbr].setMaximumSize(QtCore.QSize(100, 16777215))
            self.input_label_3[self.input_nbr].setFont(font)
            self.input_label_3[self.input_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.input_label_3[self.input_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                            QtCore.Qt.AlignTrailing |
                                                            QtCore.Qt.AlignTop)
            self.input_label_3[self.input_nbr].setObjectName('input_label_3_' + str(self.input_nbr))
            self.input_label_3[self.input_nbr].setText('Description:')
            self.input_ver_lay_2[self.input_nbr].addWidget(self.input_label_3[self.input_nbr])
            self.input_hor_lay_4[self.input_nbr].addLayout(self.input_ver_lay_2[self.input_nbr])
            self.input_edit_3.append(QtWidgets.QPlainTextEdit())
            self.input_edit_3[self.input_nbr].setEnabled(True)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.input_edit_3[self.input_nbr].sizePolicy().hasHeightForWidth())
            self.input_edit_3[self.input_nbr].setSizePolicy(size_policy)
            self.input_edit_3[self.input_nbr].setMinimumSize(QtCore.QSize(200, 60))
            self.input_edit_3[self.input_nbr].setMaximumSize(QtCore.QSize(16777215, 60))
            self.input_edit_3[self.input_nbr].setFont(font2)
            self.input_edit_3[self.input_nbr].viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_edit_3[self.input_nbr].setStyleSheet(stylesheet_creation_function('qplaintextedit'))
            self.input_edit_3[self.input_nbr].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.input_edit_3[self.input_nbr].setReadOnly(True)
            self.input_edit_3[self.input_nbr].setPlainText("")
            self.input_edit_3[self.input_nbr].setObjectName('input_edit_3_' + str(self.input_nbr))
            self.input_hor_lay_4[self.input_nbr].addWidget(self.input_edit_3[self.input_nbr])
            self.input_hor_lay_1[self.input_nbr].addLayout(self.input_hor_lay_4[self.input_nbr])
            self.input_layout.addLayout(self.input_hor_lay_1[self.input_nbr])
            self.input_line.append(QtWidgets.QFrame())
            self.input_line[self.input_nbr].setFrameShape(QtWidgets.QFrame.HLine)
            self.input_line[self.input_nbr].setFrameShadow(QtWidgets.QFrame.Sunken)
            self.input_line[self.input_nbr].setObjectName('input_line_' + str(self.input_nbr))
            self.input_line[self.input_nbr].setStyleSheet(stylesheet_creation_function('qframe_algo'))
            self.input_layout.addWidget(self.input_line[self.input_nbr])
            self.input_edit_1[self.input_nbr].setText(input_dict['Symbol'])
            self.input_edit_2[self.input_nbr].setText(str(input_dict['Units']))
            self.input_edit_3[self.input_nbr].setPlainText(input_dict['Description'])
            self.input_nbr += 1

    def populate_outputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithmDisplay - populate_outputs')
        font = font_creation_function('normal')
        font2 = font_creation_function('small')
        for output_dict in self.algorithm_dict['Output']:
            self.output_hor_lay_1.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_1[self.output_nbr].setObjectName('output_hor_lay_1_' + str(self.output_nbr))
            self.output_hor_lay_2.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_2[self.output_nbr].setObjectName('output_hor_lay_2_' + str(self.output_nbr))
            self.output_hor_lay_3.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_3[self.output_nbr].setObjectName('output_hor_lay_3_' + str(self.output_nbr))
            self.output_hor_lay_4.append(QtWidgets.QHBoxLayout())
            self.output_hor_lay_4[self.output_nbr].setObjectName('output_hor_lay_4_' + str(self.output_nbr))
            self.output_label_1.append(QtWidgets.QLabel())
            self.output_label_1[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_1[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_label_1[self.output_nbr].setFont(font)
            self.output_label_1[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.output_label_1[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_1[self.output_nbr].setObjectName('output_label_1_' + str(self.output_nbr))
            self.output_label_1[self.output_nbr].setText('Symbol:')
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_label_1[self.output_nbr])
            self.output_edit_1.append(QtWidgets.QLineEdit())
            self.output_edit_1[self.output_nbr].setEnabled(True)
            self.output_edit_1[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_edit_1[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_edit_1[self.output_nbr].setFont(font2)
            self.output_edit_1[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_1[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.output_edit_1[self.output_nbr].setText('')
            self.output_edit_1[self.output_nbr].setFrame(False)
            self.output_edit_1[self.output_nbr].setReadOnly(True)
            self.output_edit_1[self.output_nbr].setObjectName('output_edit_1_' + str(self.output_nbr))
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_edit_1[self.output_nbr])
            self.output_label_2.append(QtWidgets.QLabel())
            self.output_label_2[self.output_nbr].setMinimumSize(QtCore.QSize(130, 27))
            self.output_label_2[self.output_nbr].setMaximumSize(QtCore.QSize(130, 27))
            self.output_label_2[self.output_nbr].setFont(font)
            self.output_label_2[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.output_label_2[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_2[self.output_nbr].setObjectName('output_label_2_' + str(self.output_nbr))
            self.output_label_2[self.output_nbr].setText('Standard Name:')
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_label_2[self.output_nbr])
            self.output_edit_2.append(QtWidgets.QLineEdit())
            self.output_edit_2[self.output_nbr].setEnabled(True)
            self.output_edit_2[self.output_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.output_edit_2[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 27))
            self.output_edit_2[self.output_nbr].setFont(font2)
            self.output_edit_2[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_2[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.output_edit_2[self.output_nbr].setText('')
            self.output_edit_2[self.output_nbr].setFrame(False)
            self.output_edit_2[self.output_nbr].setReadOnly(True)
            self.output_edit_2[self.output_nbr].setObjectName('output_edit_2_' + str(self.output_nbr))
            self.output_hor_lay_1[self.output_nbr].addWidget(self.output_edit_2[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_1[self.output_nbr])
            self.output_label_3.append(QtWidgets.QLabel())
            self.output_label_3[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_3[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_label_3[self.output_nbr].setFont(font)
            self.output_label_3[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.output_label_3[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_3[self.output_nbr].setObjectName('output_label_3_' + str(self.output_nbr))
            self.output_label_3[self.output_nbr].setText('Units:')
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_label_3[self.output_nbr])
            self.output_edit_3.append(QtWidgets.QLineEdit())
            self.output_edit_3[self.output_nbr].setEnabled(True)
            self.output_edit_3[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_edit_3[self.output_nbr].setMaximumSize(QtCore.QSize(100, 27))
            self.output_edit_3[self.output_nbr].setFont(font2)
            self.output_edit_3[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_3[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.output_edit_3[self.output_nbr].setText('')
            self.output_edit_3[self.output_nbr].setFrame(False)
            self.output_edit_3[self.output_nbr].setReadOnly(True)
            self.output_edit_3[self.output_nbr].setObjectName('output_edit_3_' + str(self.output_nbr))
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_edit_3[self.output_nbr])
            self.output_label_4.append(QtWidgets.QLabel())
            self.output_label_4[self.output_nbr].setMinimumSize(QtCore.QSize(130, 27))
            self.output_label_4[self.output_nbr].setMaximumSize(QtCore.QSize(130, 27))
            self.output_label_4[self.output_nbr].setFont(font)
            self.output_label_4[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.output_label_4[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignVCenter)
            self.output_label_4[self.output_nbr].setObjectName('output_label_4_' + str(self.output_nbr))
            self.output_label_4[self.output_nbr].setText('Long Name:')
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_label_4[self.output_nbr])
            self.output_edit_4.append(QtWidgets.QLineEdit())
            self.output_edit_4[self.output_nbr].setEnabled(True)
            self.output_edit_4[self.output_nbr].setMinimumSize(QtCore.QSize(150, 27))
            self.output_edit_4[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 27))
            self.output_edit_4[self.output_nbr].setFont(font2)
            self.output_edit_4[self.output_nbr].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_4[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.output_edit_4[self.output_nbr].setText('')
            self.output_edit_4[self.output_nbr].setFrame(False)
            self.output_edit_4[self.output_nbr].setReadOnly(True)
            self.output_edit_4[self.output_nbr].setObjectName('output_edit_4_' + str(self.output_nbr))
            self.output_hor_lay_2[self.output_nbr].addWidget(self.output_edit_4[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_2[self.output_nbr])
            self.output_label_5.append(QtWidgets.QLabel())
            self.output_label_5[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_5[self.output_nbr].setMaximumSize(QtCore.QSize(100, 16777215))
            self.output_label_5[self.output_nbr].setFont(font)
            self.output_label_5[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.output_label_5[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignTop)
            self.output_label_5[self.output_nbr].setObjectName('output_label_5_' + str(self.output_nbr))
            self.output_label_5[self.output_nbr].setText('Description:')
            self.output_hor_lay_3[self.output_nbr].addWidget(self.output_label_5[self.output_nbr])
            self.output_edit_5.append(QtWidgets.QPlainTextEdit())
            self.output_edit_5[self.output_nbr].setEnabled(True)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.output_edit_5[self.output_nbr].sizePolicy().hasHeightForWidth())
            self.output_edit_5[self.output_nbr].setSizePolicy(size_policy)
            self.output_edit_5[self.output_nbr].setMinimumSize(QtCore.QSize(200, 60))
            self.output_edit_5[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 60))
            self.output_edit_5[self.output_nbr].setFont(font2)
            self.output_edit_5[self.output_nbr].viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_5[self.output_nbr].setStyleSheet(stylesheet_creation_function('qplaintextedit'))
            self.output_edit_5[self.output_nbr].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.output_edit_5[self.output_nbr].setReadOnly(True)
            self.output_edit_5[self.output_nbr].setPlainText("")
            self.output_edit_5[self.output_nbr].setObjectName('output_edit_5_' + str(self.output_nbr))
            self.output_hor_lay_3[self.output_nbr].addWidget(self.output_edit_5[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_3[self.output_nbr])
            self.output_label_6.append(QtWidgets.QLabel())
            self.output_label_6[self.output_nbr].setMinimumSize(QtCore.QSize(100, 27))
            self.output_label_6[self.output_nbr].setMaximumSize(QtCore.QSize(100, 16777215))
            self.output_label_6[self.output_nbr].setFont(font)
            self.output_label_6[self.output_nbr].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.output_label_6[self.output_nbr].setAlignment(QtCore.Qt.AlignRight |
                                                              QtCore.Qt.AlignTrailing |
                                                              QtCore.Qt.AlignTop)
            self.output_label_6[self.output_nbr].setObjectName('output_label_6_' + str(self.output_nbr))
            self.output_label_6[self.output_nbr].setText('Category:')
            self.output_hor_lay_4[self.output_nbr].addWidget(self.output_label_6[self.output_nbr])
            self.output_edit_6.append(QtWidgets.QPlainTextEdit())
            self.output_edit_6[self.output_nbr].setEnabled(True)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.output_edit_6[self.output_nbr].sizePolicy().hasHeightForWidth())
            self.output_edit_6[self.output_nbr].setSizePolicy(size_policy)
            self.output_edit_6[self.output_nbr].setMinimumSize(QtCore.QSize(200, 60))
            self.output_edit_6[self.output_nbr].setMaximumSize(QtCore.QSize(16777215, 60))
            self.output_edit_6[self.output_nbr].setFont(font2)
            self.output_edit_6[self.output_nbr].viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_edit_6[self.output_nbr].setStyleSheet(stylesheet_creation_function('qplaintextedit'))
            self.output_edit_6[self.output_nbr].setFrameShape(QtWidgets.QFrame.NoFrame)
            self.output_edit_6[self.output_nbr].setReadOnly(True)
            self.output_edit_6[self.output_nbr].setPlainText("")
            self.output_edit_6[self.output_nbr].setObjectName('output_edit_6_' + str(self.output_nbr))
            self.output_hor_lay_4[self.output_nbr].addWidget(self.output_edit_6[self.output_nbr])
            self.output_layout.addLayout(self.output_hor_lay_4[self.output_nbr])
            self.output_line.append(QtWidgets.QFrame())
            self.output_line[self.output_nbr].setFrameShape(QtWidgets.QFrame.HLine)
            self.output_line[self.output_nbr].setFrameShadow(QtWidgets.QFrame.Sunken)
            self.output_line[self.output_nbr].setObjectName('output_line_' + str(self.output_nbr))
            self.output_line[self.output_nbr].setStyleSheet(stylesheet_creation_function('qframe_algo'))
            self.output_layout.addWidget(self.output_line[self.output_nbr])
            self.output_edit_1[self.output_nbr].setText(output_dict['Symbol'])
            self.output_edit_2[self.output_nbr].setText(output_dict['StandardName'])
            self.output_edit_3[self.output_nbr].setText(output_dict['Units'])
            self.output_edit_4[self.output_nbr].setText(output_dict['LongName'])
            self.output_edit_5[self.output_nbr].setPlainText(output_dict['Description'])
            if isinstance(output_dict['Category'], list):
                category_str = ''
                for category in output_dict['Category']:
                    category_str += category + ', '
                category_str = category_str[0:-2]
                self.output_edit_6[self.output_nbr].setPlainText(category_str)
            else:
                self.output_edit_6[self.output_nbr].setPlainText(output_dict['Category'])
            self.output_nbr += 1

    def populate_algorithm(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithmDisplay - populate_algorithm')
        self.daw_plain_5.setPlainText(self.algorithm_dict['Algorithm'])
        self.highlighter = Highlighter(self.daw_plain_5.document())

    def closeWindow(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithmDisplay - closeWindow')
        self.close()


class MyProcessing(QtWidgets.QDialog, Ui_processingWindow):
    def __init__(self, list_of_algorithms, list_of_variables_and_attributes):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.aw_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.list_of_algorithms = list_of_algorithms
        self.new_var_list = None
        self.list_of_variables_and_attributes = self.prepare_variable_dict(list_of_variables_and_attributes)
        self.algorithm = None
        self.types_for_combobox = ['vector', 'array', 'vector_optional', 'array_optional']
        self.wait_window = None
        self.thread = None
        self.input_activate = 0
        self.list_of_inputs = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.list_label_output = []
        self.list_edit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.output_activate = 0
        self.list_of_outputs = {}
        self.input_num = 0
        self.coefficient_matrix_values = {}
        self.aw_okButton.clicked.connect(self.execute_processing)
        self.aw_cancelButton.clicked.connect(self.close_window)
        self.aw_combobox_1.activated.connect(self.populate_combobox_algorithms)
        self.aw_combobox_2.activated.connect(self.load_algorithm_information)
        self.aw_combobox_2.activated.connect(self.populate_inputs)
        self.aw_combobox_2.activated.connect(self.populate_outputs)
        self.populate_combobox_category()
        logging.info('gui - algorithm_windows_functions.py - MyProcessing ready')

    def execute_processing(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_window_save : algorithm '
                      + self.algorithm().metadata["Processor"])
        output_names = [str(widget.text()) for widget in self.list_edit_output]
        filtered_list = [string for string in output_names if ('/' + string) in self.list_of_variables_and_attributes]
        if filtered_list:
            if len(filtered_list) > 1:
                text = 'The following variable already exist in the Variables workspace:<ul>'
                for var in filtered_list:
                    text += '<li>' + var + '</li>'
                text += ('</ul>Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on <b>Cancel</b> '
                         'to cancel the processing.')
            else:
                text = ('The following variable, ' + filtered_list[0] + ', already exists in the Variables '
                        'workspace. Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on '
                        '<b>Cancel</b> to cancel the processing.')
            existing_window = MyExistingVariable(text)
            existing_window.exec_()
            if not existing_window.overwrite:
                return
        self.thread = VariableProcessingThread(self.algorithm, self.list_combobox_input,
                                               self.coefficient_matrix_values, self.list_edit_output,
                                               self.list_of_variables_and_attributes)
        self.thread.started.connect(self.launch_wait_window)
        self.thread.finished.connect(self.close_wait_window)
        self.thread.error.connect(self.processing_error)
        self.thread.start()

    def launch_wait_window(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - wait_window')
        info_text = 'Processing data, please wait...'
        self.wait_window = MyWait(info_text)
        self.wait_window.exec_()

    def close_wait_window(self, val):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_wait_window')
        self.new_var_list = val
        self.wait_window.close()
        self.close()

    def processing_error(self, val):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - processing_error')
        exc_type = val[0]
        exc_value = val[1]
        info_str = ('An important exception occurred during the processing. Please try to launch it again. If the '
                    'process is still not working, please check the log file for details about the exception and '
                    'review the algorithm for any coding issue. Do not hesitate to contact the developer. <br><br>'
                    'Exception type: ' + exc_type + '<br><br>Exception value: ' + exc_value)
        self.wait_window.close()
        info_window = MyInfo(info_str)
        info_window.exec_()
        self.close_window()

    def close_window(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - close_window')
        self.new_var_list = None
        self.close()

    def populate_combobox_category(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - populate_combobox_category')
        self.aw_combobox_1.addItem("Make a choice...")
        folder_list = []
        for key in self.list_of_algorithms.keys():
            folder_list.append(key[:key.find(' - ')].title())
        self.aw_combobox_1.addItems(sorted(list(dict.fromkeys(folder_list))))

    def populate_combobox_algorithms(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - populate_combobox_algorithms')
        self.setWindowTitle('Processing')
        self.aw_okButton.setEnabled(False)
        self.aw_combobox_2.clear()
        self.aw_edit_1.setText('')
        self.aw_edit_2.setText('')
        clear_layout(self.input_layout)
        clear_layout(self.output_layout)
        if self.aw_combobox_1.currentText() == "Make a choice...":
            self.aw_combobox_2.setEnabled(False)
            self.aw_combobox_2.clear()
        else:
            self.aw_combobox_2.setEnabled(True)
            self.aw_combobox_2.addItem("Make a choice...")
            algo_list = []
            for key in self.list_of_algorithms.keys():
                if str(self.aw_combobox_1.currentText()).lower() in key:
                    idx = key.find(' - ')
                    algo_list.append(key[idx + 3:])
            self.aw_combobox_2.addItems(sorted(algo_list))

    def load_algorithm_information(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - load_algorithm_information : algorithm '
                      + str(self.aw_combobox_2.currentText()))
        self.setWindowTitle('Processing')
        self.aw_okButton.setEnabled(False)
        if self.aw_combobox_2.currentText() != "Make a choice...":
            rep, algo = str(self.aw_combobox_1.currentText()).lower(), str(self.aw_combobox_2.currentText())
            self.setWindowTitle('Processing - ' + algo)
            self.aw_edit_1.setText('')
            self.aw_edit_2.setText('')
            self.algorithm = self.list_of_algorithms[rep + ' - ' + algo]['method']
            try:
                self.aw_edit_2.setText(str(self.algorithm().metadata["Description"]))
            except KeyError:
                pass
            try:
                self.aw_edit_1.setText(str(self.algorithm().metadata["Purpose"]))
            except KeyError:
                pass

    def populate_inputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - populate_inputs')
        clear_layout(self.input_layout)
        self.input_activate = 0
        self.list_of_inputs = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.input_num = 0
        self.coefficient_matrix_values = {}
        if self.aw_combobox_2.currentText() != "Make a choice...":
            font = font_creation_function('normal')
            font2 = font_creation_function('small')
            icon = icon_creation_function('info_icon.svg')
            for index, item in enumerate(self.algorithm().metadata["Inputs"]):
                self.list_label_input.append(QtWidgets.QLabel())
                self.list_label_input[self.input_num].setFont(font)
                self.list_label_input[self.input_num].setText(item + ':')
                self.list_label_input[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
                self.list_label_input[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.list_label_input[self.input_num].setObjectName("list_label_input_" + str(self.input_num))
                self.list_label_input[self.input_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                self.list_label_input[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                   QtCore.Qt.AlignVCenter)
                self.input_layout.addWidget(self.list_label_input[self.input_num], self.input_num, 0, 1, 1)
                input_type = self.algorithm().metadata["InputTypes"][index]
                combobox_widget = False
                for var_type in self.types_for_combobox:
                    if var_type in input_type:
                        combobox_widget = True
                if combobox_widget:
                    self.list_combobox_input.append(QtWidgets.QComboBox())
                    self.list_combobox_input[self.input_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
                    self.list_combobox_input[self.input_num].setEnabled(True)
                    self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                    self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                    self.list_combobox_input[self.input_num].setFrame(False)
                    self.list_combobox_input[self.input_num].setFont(font2)
                    self.list_combobox_input[self.input_num].setStyleSheet(stylesheet_creation_function('qcombobox'))
                    self.list_combobox_input[self.input_num].setObjectName("list_combobox_input_" + str(self.input_num))
                    self.list_combobox_input[self.input_num].addItem("Make a choice...")
                    self.list_combobox_input[self.input_num].addItems(self.prepare_variable_list())
                    self.list_combobox_input[self.input_num].activated.connect(self.activate_save_button)
                    self.input_layout.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                else:
                    if "coeff.[" in self.algorithm().metadata["InputTypes"][index] or "coeff[" in self.algorithm(
                    ).metadata["InputTypes"][index]:
                        self.list_combobox_input.append(QtWidgets.QHBoxLayout())
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_tmp_layout")
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("tmp_layout")
                        tmp_button = QtWidgets.QToolButton()
                        tmp_button.setMinimumSize(QtCore.QSize(150, 27))
                        tmp_button.setMaximumSize(QtCore.QSize(150, 27))
                        tmp_button.setFont(font)
                        tmp_button.setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                        tmp_button.setObjectName("coeff_set_button_" + str(index))
                        tmp_button.setText('Set coefficient')
                        tmp_button.clicked.connect(self.launch_coeff_window)
                        self.list_combobox_input[self.input_num].addWidget(tmp_button)
                        tmp_label = QtWidgets.QLabel()
                        tmp_label.setFont(font)
                        tmp_label.setText('')
                        tmp_label.setMinimumSize(QtCore.QSize(0, 27))
                        tmp_label.setMaximumSize(QtCore.QSize(16777215, 27))
                        tmp_label.setObjectName("coeff_set_label" + str(index))
                        tmp_label.setStyleSheet(stylesheet_creation_function('qlabel'))
                        self.list_combobox_input[self.input_num].addWidget(tmp_label)
                        self.input_layout.addLayout(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                    else:
                        self.list_combobox_input.append(QtWidgets.QLineEdit())
                        self.list_combobox_input[self.input_num].setEnabled(True)
                        self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setFrame(False)
                        self.list_combobox_input[self.input_num].setFont(font2)
                        self.list_combobox_input[self.input_num].setStyleSheet(stylesheet_creation_function(
                            'qlineedit'))
                        self.list_combobox_input[self.input_num].textChanged.connect(self.activate_save_button)
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_list_lineedit_input_" +
                                                                                   str(self.input_num))
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("list_edit_input_" +
                                                                                   str(self.input_num))
                        self.input_layout.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2, 1, 1)
                self.list_button_input.append(QtWidgets.QToolButton())
                self.list_button_input[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setText("")
                self.list_button_input[self.input_num].setIcon(icon)
                self.list_button_input[self.input_num].setIconSize(QtCore.QSize(23, 23))
                self.list_button_input[self.input_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                    self.list_button_input[self.input_num].setObjectName("optional_list_button_input_" + str(
                        self.input_num))
                else:
                    self.list_button_input[self.input_num].setObjectName("list_button_input_" + str(self.input_num))
                self.input_layout.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                QtWidgets.QSizePolicy.Minimum), self.input_num, 3, 1, 1)
                self.list_button_input[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                self.list_button_input[self.input_num].clicked.connect(self.information_button)
                self.input_layout.addWidget(self.list_button_input[self.input_num], self.input_num, 4, 1, 1)
                self.input_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum),
                    self.input_num, 5, 1, 1)
                self.input_num += 1

    def populate_outputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - populate_outputs')
        clear_layout(self.output_layout)
        self.list_label_output = []
        self.list_edit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.output_activate = 0
        self.list_of_outputs = {}
        if self.aw_combobox_2.currentText() != "Make a choice...":
            font = font_creation_function('normal')
            font2 = font_creation_function('small')
            icon = icon_creation_function('info_icon.svg')
            for item in self.algorithm().metadata["Outputs"]:
                self.list_label_output.append(QtWidgets.QLabel())
                self.list_label_output[self.output_num].setText(item + ':')
                self.list_label_output[self.output_num].setFont(font)
                self.list_label_output[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
                self.list_label_output[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.list_label_output[self.output_num].setObjectName("list_label_output_" + str(self.output_num))
                self.list_label_output[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                self.list_label_output[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                self.output_layout.addWidget(self.list_label_output[self.output_num], self.output_num, 0, 1, 1)
                self.output_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum),
                    self.output_num, 1, 1, 1)
                self.list_edit_output.append(QtWidgets.QLineEdit())
                self.list_edit_output[self.output_num].setEnabled(True)
                self.list_edit_output[self.output_num].setFont(font2)
                self.list_edit_output[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
                self.list_edit_output[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
                self.list_edit_output[self.output_num].setFrame(False)
                self.list_edit_output[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                self.list_edit_output[self.output_num].setObjectName("list_edit_output_" + str(self.output_num))
                self.list_edit_output[self.output_num].textChanged.connect(self.activate_save_button)
                self.output_layout.addWidget(self.list_edit_output[self.output_num], self.output_num, 2, 1, 1)
                self.list_button_output.append(QtWidgets.QToolButton())
                self.list_button_output[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
                self.list_button_output[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
                self.list_button_output[self.output_num].setText("")
                self.list_button_output[self.output_num].setIcon(icon)
                self.list_button_output[self.output_num].setIconSize(QtCore.QSize(23, 23))
                self.list_button_output[self.output_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                self.list_button_output[self.output_num].setObjectName("list_button_output_" + str(self.output_num))
                self.output_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum),
                    self.output_num, 3, 1, 1)
                self.list_button_output[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                self.list_button_output[self.output_num].clicked.connect(self.information_button)
                self.output_layout.addWidget(self.list_button_output[self.output_num], self.output_num, 4, 1, 1)
                self.output_layout.addItem(
                    QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum),
                    self.output_num, 5, 1, 1)
                self.output_num += 1

    def launch_coeff_window(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - launch_coeff_window')
        index = int(self.sender().objectName()[17:])
        matrix_nbr_idx = self.algorithm().metadata["InputTypes"][index].index('[')
        matrix_nbr_str = self.algorithm().metadata["InputTypes"][index][matrix_nbr_idx + 1:-1]
        matrix_nbr_str = matrix_nbr_str.split(',')
        try:
            coefficient_data = self.coefficient_matrix_values[self.sender().objectName()]
        except KeyError:
            coefficient_data = None
        coef_window = MyCoeff(matrix_nbr_str, coefficient_data, self.list_of_variables_and_attributes)
        coef_window.exec_()
        if coef_window.coef_array is not None:
            self.coefficient_matrix_values[self.sender().objectName()] = coef_window.coef_array
        self.activate_save_button()

    def prepare_variable_list(self):
        logging.debug('gui - algorithm_windows_functions.py - MyProcessing - prepare_variable_list')
        variable_list = []
        for var in self.list_of_variables_and_attributes:
            if var[0] == '/':
                var = var[1:]
            variable_list.append(var)
        return sorted(variable_list)

    @staticmethod
    def prepare_variable_dict(var_dict):
        new_dict = {}
        for key, value in var_dict.items():
            if isinstance(value[0], egads.EgadsData):
                new_dict[key] = value
        return new_dict

    def activate_save_button(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - activate_save_button')
        input_activate = 1
        for widget in self.list_combobox_input:
            if "optional" not in widget.objectName():
                if isinstance(widget, QtWidgets.QComboBox):
                    if widget.currentText() == "Make a choice...":
                        input_activate = 0
                elif isinstance(widget, QtWidgets.QLineEdit):
                    if widget.text() == '':
                        input_activate = 0
                elif isinstance(widget, QtWidgets.QHBoxLayout):
                    if widget.itemAt(0).widget().objectName()not in self.coefficient_matrix_values:
                        input_activate = 0
        output_activate = 1
        for widget in self.list_edit_output:
            if widget.text() == "":
                output_activate = 0
        if input_activate == 1 & output_activate == 1:
            self.aw_okButton.setEnabled(True)
        else:
            self.aw_okButton.setEnabled(False)
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - activate_save_button : '
                      'aw_okButton.isEnabled() ' + str(self.aw_okButton.isEnabled()))

    def information_button(self):
        logging.debug('gui - algorithm_window_functions.py - MyProcessing - information_button : sender().objectName() '
                      + str(self.sender().objectName()))
        if "optional" in self.sender().objectName():
            optional_str = '[Optional] '
            index = 27
        else:
            optional_str = ''
            index = 18
        if "input" in self.sender().objectName():
            description = self.algorithm().metadata["InputDescription"][int(self.sender().objectName()[index:])]
            units = self.algorithm().metadata["InputUnits"][int(self.sender().objectName()[index:])]
            if units is None:
                units = ''
            information_str = '<u>Description:</u> ' + optional_str + description + '<br><br><u>Units:</u> ' + units
        else:
            description = self.algorithm().metadata["OutputDescription"][int(self.sender().objectName()[index + 1:])]
            units = self.algorithm().metadata["OutputUnits"][int(self.sender().objectName()[index + 1:])]
            if units is None:
                units = ''
            if isinstance(self.algorithm().output_metadata, list):
                output_metadata = self.algorithm().output_metadata[int(self.sender().objectName()[index + 1:])]
            else:
                output_metadata = self.algorithm().output_metadata
            standard_name = output_metadata["standard_name"]
            long_name = output_metadata["long_name"]
            if isinstance(output_metadata["Category"], list):
                category_str = ''
                for category in output_metadata["Category"]:
                    category_str += category + ', '
                category_str = category_str[0:-2]
            else:
                category_str = output_metadata["Category"]
            information_str = '<u>Description:</u> ' + optional_str + description + '<br><br><u>Units:</u> ' + units \
                              + '<br><br><u>Standard name:</u> ' + standard_name + '<br><br><u>Long name:</u> ' + \
                              long_name + '<br><br><u>Category:</u> ' + category_str
        info_window = MyInfo(information_str)
        info_window.exec_()


class MyAlgorithm(QtWidgets.QDialog, Ui_creationWindow):
    def __init__(self, algorithm_categories, output_categories):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.information_text = algorithm_creation_information_text()
        self.algorithm_categories = algorithm_categories
        self.output_categories = output_categories
        self.highlighter = Highlighter(self.cw_plain_4.document())
        self.cw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.reset_tab_title_color()
        self.cancel = True
        self.cw_input_vl.setAlignment(QtCore.Qt.AlignTop)
        self.cw_output_vl.setAlignment(QtCore.Qt.AlignTop)
        self.cw_okButton.clicked.connect(self.prepare_algorithm_creation)
        self.cw_cancelButton.clicked.connect(self.closeWindow)
        self.cw_add_1.clicked.connect(self.add_input)
        self.cw_add_2.clicked.connect(self.add_output)
        self.cw_combobox_1.currentIndexChanged.connect(self.add_algorithm_category)
        self.cw_info_3.clicked.connect(self.algorithm_button_info)
        self.cw_info_4.clicked.connect(self.algorithm_button_info)
        self.cw_info_5.clicked.connect(self.algorithm_button_info)
        self.cw_info_6.clicked.connect(self.algorithm_button_info)
        self.cw_info_7.clicked.connect(self.algorithm_button_info)
        self.cw_info_8.clicked.connect(self.algorithm_button_info)
        self.cw_info_9.clicked.connect(self.algorithm_button_info)
        self.cw_info_10.clicked.connect(self.algorithm_button_info)
        self.cw_label_11.setVisible(False)
        self.cw_line_5.setVisible(False)
        self.cw_info_1.setEnabled(False)
        self.cw_info_2.setEnabled(False)
        self.cw_info_1.setVisible(False)
        self.cw_info_2.setVisible(False)
        self.prepare_algorithm_categories()
        self.cw_input_vl_1 = []
        self.cw_input_hl_1 = []
        self.cw_input_gd_1 = []
        self.cw_input_lb_1 = []
        self.cw_input_lb_2 = []
        self.cw_input_lb_3 = []
        self.cw_input_lb_4 = []
        self.cw_input_lb_5 = []
        self.cw_input_ln_1 = []
        self.cw_input_ln_2 = []
        self.cw_input_ln_3 = []
        self.cw_input_ln_4 = []
        self.cw_input_bt_1 = []
        self.cw_info_bt_1 = []
        self.cw_info_bt_2 = []
        self.cw_info_bt_3 = []
        self.cw_info_bt_4 = []
        self.cw_input_del_1 = []
        self.cw_input_li_1 = []
        self.input_num = 0
        self.cw_output_vl_1 = []
        self.cw_output_vl_2 = []
        self.cw_output_vl_3 = []
        self.cw_output_hl_1 = []
        self.cw_output_hl_2 = []
        self.cw_output_hl_3 = []
        self.cw_output_hl_4 = []
        self.cw_output_hl_5 = []
        self.cw_output_hl_6 = []
        self.cw_output_hl_7 = []
        self.cw_output_hl_8 = []
        self.cw_output_hl_9 = []
        self.cw_output_gd_1 = []
        self.cw_output_lb_1 = []
        self.cw_output_lb_2 = []
        self.cw_output_lb_3 = []
        self.cw_output_lb_4 = []
        self.cw_output_lb_5 = []
        self.cw_output_lb_6 = []
        self.cw_output_lb_7 = []
        self.cw_output_ln_1 = []
        self.cw_output_ln_2 = []
        self.cw_output_ln_3 = []
        self.cw_output_ln_4 = []
        self.cw_output_ln_5 = []
        self.cw_output_ln_6 = []
        self.cw_output_cb_1 = []
        self.cw_output_lw_1 = []
        self.cw_info_bt_5 = []
        self.cw_info_bt_6 = []
        self.cw_info_bt_7 = []
        self.cw_info_bt_8 = []
        self.cw_info_bt_9 = []
        self.cw_info_bt_10 = []
        self.cw_info_bt_11 = []
        self.cw_output_del_1 = []
        self.cw_output_add_1 = []
        self.cw_output_li_1 = []
        self.output_num = 0
        self.algorithm_mandatory_fields = {self.cw_line_1: self.cw_label_3,
                                           self.cw_line_2: self.cw_label_4,
                                           self.cw_plain_1: self.cw_label_7,
                                           self.cw_plain_2: self.cw_label_8,
                                           self.cw_plain_4: self.cw_label_10}
        self.categoryWindow = None
        self.success = None
        self.algorithm_filename = None
        self.algorithm_category = None
        self.algorithm_name = None
        self.setTabOrder(self.cw_line_1, self.cw_line_3)
        self.setTabOrder(self.cw_line_3, self.cw_line_2)
        self.setTabOrder(self.cw_line_2, self.cw_line_4)
        self.setTabOrder(self.cw_line_4, self.cw_plain_2)
        self.setTabOrder(self.cw_plain_2, self.cw_plain_1)
        self.setTabOrder(self.cw_plain_1, self.cw_plain_4)
        logging.info('gui - algorithm_windows_functions.py - MyAlgorithm -  ready')

    def add_input(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - add_input')
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("Source Sans Pro")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/unit_validation_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_input_vl_1.append(QtWidgets.QVBoxLayout())
        self.cw_input_vl_1[self.input_num].setObjectName('cw_input_vl_1_' + str(self.input_num))
        self.cw_input_hl_1.append(QtWidgets.QHBoxLayout())
        self.cw_input_hl_1[self.input_num].setObjectName('cw_input_hl_1_' + str(self.input_num))
        self.cw_input_vl_1[self.input_num].addLayout(self.cw_input_hl_1[self.input_num])
        self.cw_input_del_1.append(QtWidgets.QToolButton())
        self.cw_input_del_1[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_input_del_1[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_input_del_1[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_input_del_1[self.input_num].setIcon(icon)
        self.cw_input_del_1[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_input_del_1[self.input_num].setObjectName('cw_input_del_1_' + str(self.input_num))
        self.cw_input_hl_1[self.input_num].addWidget(self.cw_input_del_1[self.input_num])
        self.cw_input_hl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.cw_input_gd_1.append(QtWidgets.QGridLayout())
        self.cw_input_gd_1[self.input_num].setObjectName('cw_input_gd_1_' + str(self.input_num))
        self.cw_input_hl_1[self.input_num].addLayout(self.cw_input_gd_1[self.input_num])
        self.cw_input_lb_1.append(QtWidgets.QLabel())
        self.cw_input_lb_1[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_1[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_1[self.input_num].setFont(font)
        self.cw_input_lb_1[self.input_num].setText('Input symbols:')
        self.cw_input_lb_1[self.input_num].setObjectName('cw_input_lb_1_' + str(self.input_num))
        self.cw_input_lb_1[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_1[self.input_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_1[self.input_num], 0, 0, 1, 1)
        self.cw_input_ln_1.append(QtWidgets.QLineEdit())
        self.cw_input_ln_1[self.input_num].setEnabled(True)
        self.cw_input_ln_1[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_1[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_1[self.input_num].setFont(font2)
        self.cw_input_ln_1[self.input_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_input_ln_1[self.input_num].setText('')
        self.cw_input_ln_1[self.input_num].setFrame(False)
        self.cw_input_ln_1[self.input_num].setObjectName('cw_input_ln_1_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_1[self.input_num], 0, 1, 1, 1)

        in_hor_lay = QtWidgets.QHBoxLayout()
        in_hor_lay.setObjectName('in_hor_lay_1_' + str(self.input_num))
        in_hor_lay.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                 QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_1.append(QtWidgets.QToolButton())
        self.cw_info_bt_1[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_1[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_1[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_1[self.input_num].setIcon(icon2)
        self.cw_info_bt_1[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_1[self.input_num].setObjectName('cw_info_bt_1_' + str(self.input_num))

        in_hor_lay.addWidget(self.cw_info_bt_1[self.input_num])
        self.cw_input_gd_1[self.input_num].addLayout(in_hor_lay, 0, 2, 1, 1)
        self.cw_input_gd_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 0, 3, 1, 1)
        self.cw_input_lb_2.append(QtWidgets.QLabel())
        self.cw_input_lb_2[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_2[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_2[self.input_num].setFont(font)
        self.cw_input_lb_2[self.input_num].setText('Input units:')
        self.cw_input_lb_2[self.input_num].setObjectName('cw_input_lb_2_' + str(self.input_num))
        self.cw_input_lb_2[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_2[self.input_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_2[self.input_num], 1, 0, 1, 1)
        self.cw_input_ln_2.append(QtWidgets.QLineEdit())
        self.cw_input_ln_2[self.input_num].setEnabled(True)
        self.cw_input_ln_2[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_2[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_2[self.input_num].setFont(font2)
        self.cw_input_ln_2[self.input_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_input_ln_2[self.input_num].setText('')
        self.cw_input_ln_2[self.input_num].setFrame(False)
        self.cw_input_ln_2[self.input_num].setObjectName('cw_input_ln_2_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_2[self.input_num], 1, 1, 1, 1)

        in_hor_lay = QtWidgets.QHBoxLayout()
        in_hor_lay.setObjectName('in_hor_lay_2_' + str(self.input_num))
        in_hor_lay.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                 QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_2.append(QtWidgets.QToolButton())
        self.cw_info_bt_2[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_2[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_2[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_2[self.input_num].setIcon(icon2)
        self.cw_info_bt_2[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_2[self.input_num].setObjectName('cw_info_bt_2_' + str(self.input_num))

        in_hor_lay.addWidget(self.cw_info_bt_2[self.input_num])
        self.cw_input_gd_1[self.input_num].addLayout(in_hor_lay, 1, 2, 1, 1)

        self.cw_input_gd_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 1, 3, 1, 1)
        self.cw_input_lb_3.append(QtWidgets.QLabel())
        self.cw_input_lb_3[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_3[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_3[self.input_num].setFont(font)
        self.cw_input_lb_3[self.input_num].setText('Input type:')
        self.cw_input_lb_3[self.input_num].setObjectName('cw_input_lb_3_' + str(self.input_num))
        self.cw_input_lb_3[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_3[self.input_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_3[self.input_num], 2, 0, 1, 1)
        self.cw_input_ln_3.append(QtWidgets.QLineEdit())
        self.cw_input_ln_3[self.input_num].setEnabled(True)
        self.cw_input_ln_3[self.input_num].setMinimumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_3[self.input_num].setMaximumSize(QtCore.QSize(200, 27))
        self.cw_input_ln_3[self.input_num].setFont(font2)
        self.cw_input_ln_3[self.input_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_input_ln_3[self.input_num].setText('')
        self.cw_input_ln_3[self.input_num].setFrame(False)
        self.cw_input_ln_3[self.input_num].setObjectName('cw_input_ln_3_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_3[self.input_num], 2, 1, 1, 1)

        in_hor_lay = QtWidgets.QHBoxLayout()
        in_hor_lay.setObjectName('in_hor_lay_3_' + str(self.input_num))
        in_hor_lay.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                 QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_3.append(QtWidgets.QToolButton())
        self.cw_info_bt_3[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_3[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_3[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_3[self.input_num].setIcon(icon2)
        self.cw_info_bt_3[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_3[self.input_num].setObjectName('cw_info_bt_3_' + str(self.input_num))

        in_hor_lay.addWidget(self.cw_info_bt_3[self.input_num])
        self.cw_input_gd_1[self.input_num].addLayout(in_hor_lay, 2, 2, 1, 1)

        self.cw_input_gd_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum), 2, 3, 1, 1)
        self.cw_input_lb_4.append(QtWidgets.QLabel())
        self.cw_input_lb_4[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_input_lb_4[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_input_lb_4[self.input_num].setFont(font)
        self.cw_input_lb_4[self.input_num].setText('Input description:')
        self.cw_input_lb_4[self.input_num].setObjectName('cw_input_lb_4_' + str(self.input_num))
        self.cw_input_lb_4[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                        QtCore.Qt.AlignVCenter)
        self.cw_input_lb_4[self.input_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_lb_4[self.input_num], 3, 0, 1, 1)
        self.cw_input_ln_4.append(QtWidgets.QLineEdit())
        self.cw_input_ln_4[self.input_num].setEnabled(True)
        self.cw_input_ln_4[self.input_num].setMinimumSize(QtCore.QSize(500, 27))
        self.cw_input_ln_4[self.input_num].setMaximumSize(QtCore.QSize(500, 27))
        self.cw_input_ln_4[self.input_num].setFont(font2)
        self.cw_input_ln_4[self.input_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_input_ln_4[self.input_num].setText('')
        self.cw_input_ln_4[self.input_num].setFrame(False)
        self.cw_input_ln_4[self.input_num].setObjectName('cw_input_ln_4_' + str(self.input_num))
        self.cw_input_gd_1[self.input_num].addWidget(self.cw_input_ln_4[self.input_num], 3, 1, 1, 3)

        in_hor_lay = QtWidgets.QHBoxLayout()
        in_hor_lay.setObjectName('in_hor_lay_4_' + str(self.input_num))
        in_hor_lay.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                 QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_4.append(QtWidgets.QToolButton())
        self.cw_info_bt_4[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_4[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_4[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_4[self.input_num].setIcon(icon2)
        self.cw_info_bt_4[self.input_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_4[self.input_num].setObjectName('cw_info_bt_4_' + str(self.input_num))

        in_hor_lay.addWidget(self.cw_info_bt_4[self.input_num])
        self.cw_input_gd_1[self.input_num].addLayout(in_hor_lay, 3, 42, 1, 1)

        self.cw_input_hl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.cw_input_vl.addLayout(self.cw_input_vl_1[self.input_num])
        self.cw_input_vl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_input_li_1.append(QtWidgets.QFrame())
        self.cw_input_li_1[self.input_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.cw_input_li_1[self.input_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cw_input_li_1[self.input_num].setObjectName("cw_input_li_1_" + str(self.input_num))
        self.cw_input_li_1[self.input_num].setStyleSheet(stylesheet_creation_function('qframe_algo'))
        self.cw_input_vl_1[self.input_num].addWidget(self.cw_input_li_1[self.input_num])
        self.cw_input_vl_1[self.input_num].addItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
        self.cw_input_del_1[self.input_num].clicked.connect(self.del_input)
        self.cw_info_bt_1[self.input_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_2[self.input_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_3[self.input_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_4[self.input_num].clicked.connect(self.input_output_button_info)
        self.setTabOrder(self.cw_input_ln_1[self.input_num], self.cw_input_ln_2[self.input_num])
        self.setTabOrder(self.cw_input_ln_2[self.input_num], self.cw_input_ln_3[self.input_num])
        self.setTabOrder(self.cw_input_ln_3[self.input_num], self.cw_input_ln_4[self.input_num])
        self.input_num += 1

    def del_input(self, index=None):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - del_input : index ' + str(index)
                      + ', sender().objectName() ' + str(self.sender().objectName()))
        if index is None:
            index = int(self.sender().objectName()[15:])
        self.cw_input_vl_1[index].deleteLater()
        self.cw_input_vl_1.pop(index)
        self.cw_input_li_1[index].deleteLater()
        self.cw_input_li_1.pop(index)
        self.cw_input_hl_1[index].deleteLater()
        self.cw_input_hl_1.pop(index)
        self.cw_input_del_1[index].deleteLater()
        self.cw_input_del_1.pop(index)
        self.cw_input_gd_1[index].deleteLater()
        self.cw_input_gd_1.pop(index)
        self.cw_input_lb_1[index].deleteLater()
        self.cw_input_lb_1.pop(index)
        self.cw_input_ln_1[index].deleteLater()
        self.cw_input_ln_1.pop(index)
        self.cw_info_bt_1[index].deleteLater()
        self.cw_info_bt_1.pop(index)
        self.cw_input_lb_2[index].deleteLater()
        self.cw_input_lb_2.pop(index)
        self.cw_input_ln_2[index].deleteLater()
        self.cw_input_ln_2.pop(index)
        self.cw_info_bt_2[index].deleteLater()
        self.cw_info_bt_2.pop(index)
        self.cw_input_lb_3[index].deleteLater()
        self.cw_input_lb_3.pop(index)
        self.cw_input_ln_3[index].deleteLater()
        self.cw_input_ln_3.pop(index)
        self.cw_info_bt_3[index].deleteLater()
        self.cw_info_bt_3.pop(index)
        self.cw_input_lb_4[index].deleteLater()
        self.cw_input_lb_4.pop(index)
        self.cw_input_ln_4[index].deleteLater()
        self.cw_input_ln_4.pop(index)
        self.cw_info_bt_4[index].deleteLater()
        self.cw_info_bt_4.pop(index)
        self.input_num -= 1
        if len(self.cw_input_vl_1) > 0:
            for i in range(0, len(self.cw_input_vl_1)):
                self.cw_input_vl_1[i].setObjectName('cw_input_vl_1_' + str(i))
                self.cw_input_li_1[i].setObjectName("cw_input_li_1_" + str(i))
                self.cw_input_hl_1[i].setObjectName('cw_input_hl_1_' + str(i))
                self.cw_input_del_1[i].setObjectName('cw_input_del_1_' + str(i))
                self.cw_input_gd_1[i].setObjectName('cw_input_gd_1_' + str(i))
                self.cw_input_lb_1[i].setObjectName('cw_input_lb_1_' + str(i))
                self.cw_input_ln_1[i].setObjectName('cw_input_ln_1_' + str(i))
                self.cw_info_bt_1[i].setObjectName('cw_info_bt_1_' + str(i))
                self.cw_input_lb_2[i].setObjectName('cw_input_lb_2_' + str(i))
                self.cw_input_ln_2[i].setObjectName('cw_input_ln_2_' + str(i))
                self.cw_info_bt_2[i].setObjectName('cw_info_bt_2_' + str(i))
                self.cw_input_lb_3[i].setObjectName('cw_input_lb_3_' + str(i))
                self.cw_input_ln_3[i].setObjectName('cw_input_ln_3_' + str(i))
                self.cw_info_bt_3[i].setObjectName('cw_info_bt_3_' + str(i))
                self.cw_input_lb_4[i].setObjectName('cw_input_lb_4_' + str(i))
                self.cw_input_ln_4[i].setObjectName('cw_input_ln_4_' + str(i))
                self.cw_info_bt_4[i].setObjectName('cw_info_bt_4_' + str(i))

    def add_output(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_output')
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("Source Sans Pro")
        font2.setPointSize(10)
        font2.setKerning(True)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cw_output_vl_3.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_3[self.output_num].setObjectName('cw_output_vl_3_' + str(self.output_num))
        self.cw_output_hl_9.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_9[self.output_num].setObjectName('cw_output_hl_9_' + str(self.output_num))
        self.cw_output_del_1.append(QtWidgets.QToolButton())
        self.cw_output_del_1[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_output_del_1[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_output_del_1[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_output_del_1[self.output_num].setIcon(icon)
        self.cw_output_del_1[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_output_del_1[self.output_num].setObjectName('cw_output_del_1_' + str(self.output_num))
        self.cw_output_hl_9[self.output_num].addWidget(self.cw_output_del_1[self.output_num])
        self.cw_output_hl_9[self.output_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1.append(QtWidgets.QGridLayout())
        self.cw_output_gd_1[self.output_num].setContentsMargins(0, 0, 0, 0)
        self.cw_output_gd_1[self.output_num].setObjectName("cw_output_gd_1_" + str(self.output_num))
        self.cw_output_lb_1.append(QtWidgets.QLabel())
        self.cw_output_lb_1[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_1[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_1[self.output_num].setFont(font)
        self.cw_output_lb_1[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_1[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_1[self.output_num].setObjectName("cw_output_lb_1_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_1[self.output_num], 0, 0, 1, 1)
        self.cw_output_hl_1.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_1[self.output_num].setObjectName("cw_output_hl_1_" + str(self.output_num))
        self.cw_output_ln_1.append(QtWidgets.QLineEdit())
        self.cw_output_ln_1[self.output_num].setEnabled(True)
        self.cw_output_ln_1[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_1[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_1[self.output_num].setFont(font2)
        self.cw_output_ln_1[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_output_ln_1[self.output_num].setText("")
        self.cw_output_ln_1[self.output_num].setFrame(False)
        self.cw_output_ln_1[self.output_num].setObjectName("cw_output_ln_1_" + str(self.output_num))
        self.cw_output_hl_1[self.output_num].addWidget(self.cw_output_ln_1[self.output_num])

        self.cw_output_hl_1[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_5.append(QtWidgets.QToolButton())
        self.cw_info_bt_5[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_5[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_5[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_5[self.output_num].setIcon(icon2)
        self.cw_info_bt_5[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_5[self.output_num].setObjectName("cw_info_bt_5_" + str(self.output_num))
        self.cw_output_hl_1[self.output_num].addWidget(self.cw_info_bt_5[self.output_num])
        self.cw_output_hl_1[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_1[self.output_num], 0, 1, 1, 1)
        self.cw_output_lb_5.append(QtWidgets.QLabel())
        self.cw_output_lb_5[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_5[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_5[self.output_num].setFont(font)
        self.cw_output_lb_5[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_5[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                          QtCore.Qt.AlignVCenter)
        self.cw_output_lb_5[self.output_num].setObjectName("cw_output_lb_5_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_5[self.output_num], 0, 2, 1, 1)
        self.cw_output_hl_5.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_5[self.output_num].setObjectName("cw_output_hl_5_" + str(self.output_num))
        self.cw_output_ln_5.append(QtWidgets.QLineEdit())
        self.cw_output_ln_5[self.output_num].setEnabled(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cw_output_ln_5[self.output_num].sizePolicy().hasHeightForWidth())
        self.cw_output_ln_5[self.output_num].setSizePolicy(size_policy)
        self.cw_output_ln_5[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_5[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_ln_5[self.output_num].setFont(font2)
        self.cw_output_ln_5[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_output_ln_5[self.output_num].setText("")
        self.cw_output_ln_5[self.output_num].setFrame(False)
        self.cw_output_ln_5[self.output_num].setObjectName("cw_output_ln_5_" + str(self.output_num))
        self.cw_output_hl_5[self.output_num].addWidget(self.cw_output_ln_5[self.output_num])
        self.cw_output_hl_5[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_9.append(QtWidgets.QToolButton())
        self.cw_info_bt_9[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_9[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_9[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_9[self.output_num].setIcon(icon2)
        self.cw_info_bt_9[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_9[self.output_num].setObjectName("cw_info_bt_9_" + str(self.output_num))
        self.cw_output_hl_5[self.output_num].addWidget(self.cw_info_bt_9[self.output_num])
        self.cw_output_hl_5[self.output_num].addItem(QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_5[self.output_num], 0, 3, 1, 1)
        self.cw_output_lb_2.append(QtWidgets.QLabel())
        self.cw_output_lb_2[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_2[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_2[self.output_num].setFont(font)
        self.cw_output_lb_2[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_2[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_2[self.output_num].setObjectName("cw_output_lb_2_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_2[self.output_num], 1, 0, 1, 1)
        self.cw_output_hl_2.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_2[self.output_num].setObjectName("cw_output_hl_2_" + str(self.output_num))
        self.cw_output_ln_2.append(QtWidgets.QLineEdit())
        self.cw_output_ln_2[self.output_num].setEnabled(True)
        self.cw_output_ln_2[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_2[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_2[self.output_num].setFont(font2)
        self.cw_output_ln_2[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_output_ln_2[self.output_num].setText("")
        self.cw_output_ln_2[self.output_num].setFrame(False)
        self.cw_output_ln_2[self.output_num].setObjectName("cw_output_ln_2_" + str(self.output_num))
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_output_ln_2[self.output_num])

        self.cw_output_hl_2[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_6.append(QtWidgets.QToolButton())
        self.cw_info_bt_6[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_6[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_6[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_6[self.output_num].setIcon(icon2)
        self.cw_info_bt_6[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_6[self.output_num].setObjectName("cw_info_bt_6_" + str(self.output_num))
        self.cw_output_hl_2[self.output_num].addWidget(self.cw_info_bt_6[self.output_num])
        self.cw_output_hl_2[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_2[self.output_num], 1, 1, 1, 1)
        self.cw_output_lb_6.append(QtWidgets.QLabel())
        self.cw_output_lb_6[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_6[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_6[self.output_num].setFont(font)
        self.cw_output_lb_6[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_6[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_6[self.output_num].setObjectName("cw_output_lb_6_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_6[self.output_num], 1, 2, 1, 1)
        self.cw_output_hl_6.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_6[self.output_num].setObjectName("cw_output_hl_6_" + str(self.output_num))
        self.cw_output_ln_6.append(QtWidgets.QLineEdit())
        self.cw_output_ln_6[self.output_num].setEnabled(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cw_output_ln_6[self.output_num].sizePolicy().hasHeightForWidth())
        self.cw_output_ln_6[self.output_num].setSizePolicy(size_policy)
        self.cw_output_ln_6[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_6[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_ln_6[self.output_num].setFont(font2)
        self.cw_output_ln_6[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_output_ln_6[self.output_num].setText("")
        self.cw_output_ln_6[self.output_num].setFrame(False)
        self.cw_output_ln_6[self.output_num].setObjectName("cw_output_ln_6_" + str(self.output_num))
        self.cw_output_hl_6[self.output_num].addWidget(self.cw_output_ln_6[self.output_num])

        self.cw_output_hl_6[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_10.append(QtWidgets.QToolButton())
        self.cw_info_bt_10[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_10[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_10[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_10[self.output_num].setIcon(icon2)
        self.cw_info_bt_10[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_10[self.output_num].setObjectName("cw_info_bt_10_" + str(self.output_num))
        self.cw_output_hl_6[self.output_num].addWidget(self.cw_info_bt_10[self.output_num])
        self.cw_output_hl_6[self.output_num].addItem(QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_6[self.output_num], 1, 3, 1, 1)
        self.cw_output_lb_3.append(QtWidgets.QLabel())
        self.cw_output_lb_3[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_3[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_3[self.output_num].setFont(font)
        self.cw_output_lb_3[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_3[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_3[self.output_num].setObjectName("cw_output_lb_3_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_3[self.output_num], 2, 0, 1, 1)
        self.cw_output_hl_3.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_3[self.output_num].setObjectName("cw_output_hl_3_" + str(self.output_num))
        self.cw_output_ln_3.append(QtWidgets.QLineEdit())
        self.cw_output_ln_3[self.output_num].setEnabled(True)
        self.cw_output_ln_3[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_3[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_3[self.output_num].setFont(font2)
        self.cw_output_ln_3[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_output_ln_3[self.output_num].setText("")
        self.cw_output_ln_3[self.output_num].setFrame(False)
        self.cw_output_ln_3[self.output_num].setObjectName("cw_output_ln_3_" + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_output_ln_3[self.output_num])

        self.cw_output_hl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_7.append(QtWidgets.QToolButton())
        self.cw_info_bt_7[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_7[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_7[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_7[self.output_num].setIcon(icon2)
        self.cw_info_bt_7[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_7[self.output_num].setObjectName("cw_info_bt_7_" + str(self.output_num))
        self.cw_output_hl_3[self.output_num].addWidget(self.cw_info_bt_7[self.output_num])
        self.cw_output_hl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_3[self.output_num], 2, 1, 1, 3)
        self.cw_output_lb_4.append(QtWidgets.QLabel())
        self.cw_output_lb_4[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_lb_4[self.output_num].setFont(font)
        self.cw_output_lb_4[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_4[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_4[self.output_num].setObjectName("cw_output_lb_4_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_4[self.output_num], 3, 0, 1, 1)
        self.cw_output_hl_4.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_4[self.output_num].setObjectName("cw_output_hl_4_" + str(self.output_num))
        self.cw_output_ln_4.append(QtWidgets.QLineEdit())
        self.cw_output_ln_4[self.output_num].setEnabled(True)
        self.cw_output_ln_4[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_ln_4[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.cw_output_ln_4[self.output_num].setFont(font2)
        self.cw_output_ln_4[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
        self.cw_output_ln_4[self.output_num].setText("")
        self.cw_output_ln_4[self.output_num].setFrame(False)
        self.cw_output_ln_4[self.output_num].setObjectName("cw_output_ln_4_" + str(self.output_num))
        self.cw_output_hl_4[self.output_num].addWidget(self.cw_output_ln_4[self.output_num])

        self.cw_output_hl_4[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_info_bt_8.append(QtWidgets.QToolButton())
        self.cw_info_bt_8[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_8[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_8[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_8[self.output_num].setIcon(icon2)
        self.cw_info_bt_8[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_8[self.output_num].setObjectName("cw_info_bt_8_" + str(self.output_num))
        self.cw_output_hl_4[self.output_num].addWidget(self.cw_info_bt_8[self.output_num])
        self.cw_output_hl_4[self.output_num].addItem(QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_4[self.output_num], 3, 1, 1, 3)
        self.cw_output_lb_7.append(QtWidgets.QLabel())
        self.cw_output_lb_7[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
        self.cw_output_lb_7[self.output_num].setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cw_output_lb_7[self.output_num].setFont(font)
        self.cw_output_lb_7[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
        self.cw_output_lb_7[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                          QtCore.Qt.AlignTrailing)
        self.cw_output_lb_7[self.output_num].setObjectName("cw_output_lb_7_" + str(self.output_num))
        self.cw_output_gd_1[self.output_num].addWidget(self.cw_output_lb_7[self.output_num], 4, 0, 1, 1)
        self.cw_output_hl_8.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_8[self.output_num].setObjectName("cw_output_hl_8_" + str(self.output_num))
        self.cw_output_vl_1.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_1[self.output_num].setObjectName("cw_output_vl_1_" + str(self.output_num))
        self.cw_output_hl_7.append(QtWidgets.QHBoxLayout())
        self.cw_output_hl_7[self.output_num].setObjectName("cw_output_hl_7_" + str(self.output_num))
        self.cw_output_cb_1.append(QtWidgets.QComboBox())
        self.cw_output_cb_1[self.output_num].setMinimumSize(QtCore.QSize(150, 27))
        self.cw_output_cb_1[self.output_num].setMaximumSize(QtCore.QSize(150, 27))
        self.cw_output_cb_1[self.output_num].setFont(font2)
        self.cw_output_cb_1[self.output_num].setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.cw_output_cb_1[self.output_num].setFrame(False)
        self.cw_output_cb_1[self.output_num].setObjectName("cw_output_cb_1_" + str(self.output_num))
        self.cw_output_cb_1[self.output_num].addItems(['Make a choice...', 'Other...'] + self.output_categories)
        self.cw_output_cb_1[self.output_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.cw_output_hl_7[self.output_num].addWidget(self.cw_output_cb_1[self.output_num])

        self.cw_output_hl_7[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_output_add_1.append(QtWidgets.QToolButton())
        self.cw_output_add_1[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_output_add_1[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_output_add_1[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_output_add_1[self.output_num].setIcon(icon3)
        self.cw_output_add_1[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_output_add_1[self.output_num].setObjectName("cw_output_add_1_" + str(self.output_num))
        self.cw_output_hl_7[self.output_num].addWidget(self.cw_output_add_1[self.output_num])
        self.cw_output_vl_1[self.output_num].addLayout(self.cw_output_hl_7[self.output_num])
        self.cw_output_vl_1[self.output_num].addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Expanding))
        self.cw_output_hl_8[self.output_num].addLayout(self.cw_output_vl_1[self.output_num])

        self.cw_output_hl_8[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_output_lw_1.append(QtWidgets.QListWidget())
        self.cw_output_lw_1[self.output_num].setMinimumSize(QtCore.QSize(250, 100))
        self.cw_output_lw_1[self.output_num].setMaximumSize(QtCore.QSize(250, 100))
        self.cw_output_lw_1[self.output_num].setFont(font2)
        self.cw_output_lw_1[self.output_num].setFocusPolicy(QtCore.Qt.NoFocus)
        self.cw_output_lw_1[self.output_num].setStyleSheet(stylesheet_creation_function('qlistwidget'))
        self.cw_output_lw_1[self.output_num].setObjectName("cw_output_lw_1_" + str(self.output_num))
        self.cw_output_hl_8[self.output_num].addWidget(self.cw_output_lw_1[self.output_num])

        self.cw_output_hl_8[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                           QtWidgets.QSizePolicy.Minimum))

        self.cw_output_vl_2.append(QtWidgets.QVBoxLayout())
        self.cw_output_vl_2[self.output_num].setObjectName("cw_output_vl_2_" + str(self.output_num))
        self.cw_info_bt_11.append(QtWidgets.QToolButton())
        self.cw_info_bt_11[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_11[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
        self.cw_info_bt_11[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.cw_info_bt_11[self.output_num].setIcon(icon2)
        self.cw_info_bt_11[self.output_num].setIconSize(QtCore.QSize(23, 23))
        self.cw_info_bt_11[self.output_num].setObjectName("cw_info_bt_11_" + str(self.output_num))
        self.cw_output_vl_2[self.output_num].addWidget(self.cw_info_bt_11[self.output_num])
        self.cw_output_vl_2[self.output_num].addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Expanding))
        self.cw_output_hl_8[self.output_num].addLayout(self.cw_output_vl_2[self.output_num])
        self.cw_output_hl_8[self.output_num].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                                           QtWidgets.QSizePolicy.Minimum))
        self.cw_output_gd_1[self.output_num].addLayout(self.cw_output_hl_8[self.output_num], 4, 1, 1, 3)
        self.cw_output_hl_9[self.output_num].addLayout(self.cw_output_gd_1[self.output_num])
        self.cw_output_vl_3[self.output_num].addLayout(self.cw_output_hl_9[self.output_num])
        self.cw_output_vl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Fixed))
        self.cw_output_li_1.append(QtWidgets.QFrame())
        self.cw_output_li_1[self.output_num].setFrameShape(QtWidgets.QFrame.HLine)
        self.cw_output_li_1[self.output_num].setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cw_output_li_1[self.output_num].setStyleSheet(stylesheet_creation_function('qframe_algo'))
        self.cw_output_li_1[self.output_num].setObjectName("cw_output_li_1_" + str(self.output_num))
        self.cw_output_vl_3[self.output_num].addWidget(self.cw_output_li_1[self.output_num])
        self.cw_output_vl_3[self.output_num].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                                           QtWidgets.QSizePolicy.Fixed))
        self.cw_output_vl.addLayout(self.cw_output_vl_3[self.output_num])
        self.cw_output_lb_1[self.output_num].setText("Output symbol:")
        self.cw_output_lb_5[self.output_num].setText("Output standard name:")
        self.cw_output_lb_2[self.output_num].setText("Output units:")
        self.cw_output_lb_6[self.output_num].setText("Output long name:")
        self.cw_output_lb_3[self.output_num].setText("Output type:")
        self.cw_output_lb_4[self.output_num].setText("Output description:")
        self.cw_output_lb_7[self.output_num].setText("Output category:")
        self.cw_output_del_1[self.output_num].clicked.connect(self.del_output)
        self.cw_output_add_1[self.output_num].clicked.connect(self.add_output_category)
        self.cw_output_lw_1[self.output_num].itemDoubleClicked.connect(self.remove_output_category)
        self.cw_info_bt_5[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_6[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_7[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_8[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_9[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_10[self.output_num].clicked.connect(self.input_output_button_info)
        self.cw_info_bt_11[self.output_num].clicked.connect(self.input_output_button_info)
        self.setTabOrder(self.cw_output_ln_1[self.output_num], self.cw_output_ln_5[self.output_num])
        self.setTabOrder(self.cw_output_ln_5[self.output_num], self.cw_output_ln_2[self.output_num])
        self.setTabOrder(self.cw_output_ln_2[self.output_num], self.cw_output_ln_6[self.output_num])
        self.setTabOrder(self.cw_output_ln_6[self.output_num], self.cw_output_ln_3[self.output_num])
        self.setTabOrder(self.cw_output_ln_3[self.output_num], self.cw_output_ln_4[self.output_num])
        self.output_num += 1

    def del_output(self, index=None):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - del_output : index ' + str(index)
                      + ', sender().objectName() ' + str(self.sender().objectName()))
        if index is None:
            index = int(self.sender().objectName()[16:])
        self.cw_output_vl_1[index].deleteLater()
        self.cw_output_vl_1.pop(index)
        self.cw_output_vl_2[index].deleteLater()
        self.cw_output_vl_2.pop(index)
        self.cw_output_vl_3[index].deleteLater()
        self.cw_output_vl_3.pop(index)
        self.cw_output_hl_1[index].deleteLater()
        self.cw_output_hl_1.pop(index)
        self.cw_output_hl_2[index].deleteLater()
        self.cw_output_hl_2.pop(index)
        self.cw_output_hl_3[index].deleteLater()
        self.cw_output_hl_3.pop(index)
        self.cw_output_hl_4[index].deleteLater()
        self.cw_output_hl_4.pop(index)
        self.cw_output_hl_5[index].deleteLater()
        self.cw_output_hl_5.pop(index)
        self.cw_output_hl_6[index].deleteLater()
        self.cw_output_hl_6.pop(index)
        self.cw_output_hl_7[index].deleteLater()
        self.cw_output_hl_7.pop(index)
        self.cw_output_hl_8[index].deleteLater()
        self.cw_output_hl_8.pop(index)
        self.cw_output_hl_9[index].deleteLater()
        self.cw_output_hl_9.pop(index)
        self.cw_output_gd_1[index].deleteLater()
        self.cw_output_gd_1.pop(index)
        self.cw_output_lb_1[index].deleteLater()
        self.cw_output_lb_1.pop(index)
        self.cw_output_lb_2[index].deleteLater()
        self.cw_output_lb_2.pop(index)
        self.cw_output_lb_3[index].deleteLater()
        self.cw_output_lb_3.pop(index)
        self.cw_output_lb_4[index].deleteLater()
        self.cw_output_lb_4.pop(index)
        self.cw_output_lb_5[index].deleteLater()
        self.cw_output_lb_5.pop(index)
        self.cw_output_lb_6[index].deleteLater()
        self.cw_output_lb_6.pop(index)
        self.cw_output_lb_7[index].deleteLater()
        self.cw_output_lb_7.pop(index)
        self.cw_output_ln_1[index].deleteLater()
        self.cw_output_ln_1.pop(index)
        self.cw_output_ln_2[index].deleteLater()
        self.cw_output_ln_2.pop(index)
        self.cw_output_ln_3[index].deleteLater()
        self.cw_output_ln_3.pop(index)
        self.cw_output_ln_4[index].deleteLater()
        self.cw_output_ln_4.pop(index)
        self.cw_output_ln_5[index].deleteLater()
        self.cw_output_ln_5.pop(index)
        self.cw_output_ln_6[index].deleteLater()
        self.cw_output_ln_6.pop(index)
        self.cw_output_cb_1[index].deleteLater()
        self.cw_output_cb_1.pop(index)
        self.cw_output_lw_1[index].deleteLater()
        self.cw_output_lw_1.pop(index)
        self.cw_info_bt_5[index].deleteLater()
        self.cw_info_bt_5.pop(index)
        self.cw_info_bt_6[index].deleteLater()
        self.cw_info_bt_6.pop(index)
        self.cw_info_bt_7[index].deleteLater()
        self.cw_info_bt_7.pop(index)
        self.cw_info_bt_8[index].deleteLater()
        self.cw_info_bt_8.pop(index)
        self.cw_info_bt_9[index].deleteLater()
        self.cw_info_bt_9.pop(index)
        self.cw_info_bt_10[index].deleteLater()
        self.cw_info_bt_10.pop(index)
        self.cw_info_bt_11[index].deleteLater()
        self.cw_info_bt_11.pop(index)
        self.cw_output_del_1[index].deleteLater()
        self.cw_output_del_1.pop(index)
        self.cw_output_add_1[index].deleteLater()
        self.cw_output_add_1.pop(index)
        self.cw_output_li_1[index].deleteLater()
        self.cw_output_li_1.pop(index)
        self.output_num -= 1
        if len(self.cw_output_vl_1) > 0:
            for i in range(0, len(self.cw_output_vl_1)):
                self.cw_output_hl_9[i].setObjectName('cw_output_hl_9_' + str(i))
                self.cw_output_vl_1[i].setObjectName('cw_output_vl_1_' + str(i))
                self.cw_output_hl_1[i].setObjectName('cw_output_hl_1_' + str(i))
                self.cw_output_del_1[i].setObjectName('cw_output_del_1_' + str(i))
                self.cw_output_vl_2[i].setObjectName('cw_output_vl_2_' + str(i))
                self.cw_output_vl_3[i].setObjectName('cw_output_vl_3_' + str(i))
                self.cw_output_gd_1[i].setObjectName('cw_output_gd_1_' + str(i))
                self.cw_output_lb_1[i].setObjectName('cw_output_lb_1_' + str(i))
                self.cw_output_ln_1[i].setObjectName('cw_output_ln_1_' + str(i))
                self.cw_info_bt_5[i].setObjectName('cw_info_bt_5_' + str(i))
                self.cw_output_lb_2[i].setObjectName('cw_output_lb_2_' + str(i))
                self.cw_output_ln_2[i].setObjectName('cw_output_ln_2_' + str(i))
                self.cw_info_bt_6[i].setObjectName('cw_info_bt_6_' + str(i))
                self.cw_output_lb_3[i].setObjectName('cw_output_lb_3_' + str(i))
                self.cw_output_ln_3[i].setObjectName('cw_output_ln_3_' + str(i))
                self.cw_info_bt_7[i].setObjectName('cw_info_bt_7_' + str(i))
                self.cw_output_lb_4[i].setObjectName('cw_output_lb_4_' + str(i))
                self.cw_output_ln_4[i].setObjectName('cw_output_ln_4_' + str(i))
                self.cw_info_bt_8[i].setObjectName('cw_info_bt_8_' + str(i))
                self.cw_output_hl_2[i].setObjectName('cw_output_hl_2_' + str(i))
                self.cw_output_lb_5[i].setObjectName('cw_output_lb_5_' + str(i))
                self.cw_output_ln_5[i].setObjectName('cw_output_ln_5_' + str(i))
                self.cw_output_ln_6[i].setObjectName('cw_output_ln_6_' + str(i))
                self.cw_info_bt_9[i].setObjectName('cw_info_bt_9_' + str(i))
                self.cw_info_bt_10[i].setObjectName('cw_info_bt_10_' + str(i))
                self.cw_info_bt_11[i].setObjectName('cw_info_bt_11_' + str(i))
                self.cw_output_hl_3[i].setObjectName('cw_output_hl_3_' + str(i))
                self.cw_output_lb_6[i].setObjectName('cw_output_lb_6_' + str(i))
                self.cw_output_lb_7[i].setObjectName('cw_output_lb_7_' + str(i))
                self.cw_output_add_1[i].setObjectName("cw_output_add_1_" + str(i))
                self.cw_output_lw_1[i].setObjectName("cw_output_lw_1_" + str(i))
                self.cw_output_li_1[i].setObjectName("cw_output_li_1_" + str(i))

    def prepare_algorithm_categories(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_categories')
        self.cw_combobox_1.clear()
        self.cw_combobox_1.addItems(['Make a choice...', 'Other...'] + sorted(self.algorithm_categories))

    def add_output_category(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - add_output_category')
        index = int(self.sender().objectName()[16:])
        category = ''
        in_list = False
        if self.cw_output_cb_1[index].currentText() == 'Other...':
            self.categoryWindow = MyCategory()
            if self.categoryWindow.exec_():
                category = str(self.categoryWindow.ac_line.text())
        elif self.cw_output_cb_1[index].currentText() != 'Make a choice...':
            category = str(self.cw_output_cb_1[index].currentText())
        if category:
            for i in range(0, self.cw_output_lw_1[index].count()):
                if category == str(self.cw_output_lw_1[index].item(i).text()):
                    in_list = True
                    break
            if not in_list:
                self.cw_output_lw_1[index].addItem(category)

    def remove_output_category(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - remove_output_category')
        index = int(self.sender().objectName()[15:])
        self.cw_output_lw_1[index].takeItem(self.cw_output_lw_1[index].currentRow())

    def add_algorithm_category(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - add_algorithm_category')
        if self.cw_combobox_1.currentText() == 'Other...':
            self.cw_line_5.setText('')
            self.cw_label_11.setVisible(True)
            self.cw_line_5.setVisible(True)
        else:
            self.cw_line_5.setText('')
            self.cw_label_11.setVisible(False)
            self.cw_line_5.setVisible(False)

    def remove_algorithm_category(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - remove_algorithm_category')
        self.category_list.takeItem(self.category_list.currentRow())

    def prepare_algorithm_creation(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_creation')
        cancel = self.check_all_fields()
        if cancel:
            return
        category = ''
        if self.cw_combobox_1.currentText() == 'Other...':
            category = str(self.cw_line_5.text())
        elif self.cw_combobox_1.currentText() != 'Make a choice...':
            category = str(self.cw_combobox_1.currentText())
        try:
            getattr(getattr(egads.algorithms.user, category.lower()), str(self.cw_line_1.text()))
            info_text = ('An algorithm with the same name and in the same folder already exists in EGADS. Although it '
                         + 'is still possible to create it manually, they will be seen as one and only algorithm '
                         + 'once loaded into EGADS. Please change the name of the new algorithm before saving it.')
            info_window = MyInfo(info_text)
            info_window.exec_()
        except AttributeError:
            units_list = self.units_validation()
            if units_list:
                unit_window = MyUnit(units_list)
                if unit_window.exec_():
                    self.choose_filename()
            else:
                self.choose_filename()

    def choose_filename(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - choose_filename')
        category = ''
        if self.cw_combobox_1.currentText() == 'Other...':
            category = str(self.cw_line_5.text())
        elif self.cw_combobox_1.currentText() != 'Make a choice...':
            category = str(self.cw_combobox_1.currentText())
        filename_window = MyFilename()
        if filename_window.exec_():
            filename = str(filename_window.ac_line.text())
            if '.py' in filename:
                filename = filename[:-3]
            if filename:
                file_path = pathlib.Path(egads.user_path).joinpath('user_algorithms', category, filename + '.py')
                if pathlib.Path(file_path).is_file():
                    overwrite_window = MyOverwriteFilename(filename, category)
                    if overwrite_window.exec_():
                        filename = str(overwrite_window.ac_line.text())
                        if '.py' in filename:
                            filename = filename[:-3]
                        if filename:
                            self.create_algorithm(filename, category)
                else:
                    self.create_algorithm(filename, category)

    def create_algorithm(self, filename, category):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - create_algorithm - filename: '
                      + filename + ', category: ' + category)
        author = '__author__ = "' + str(self.cw_line_2.text()) + '"\n'
        date = '__date__ = "' + create_datestring() + '"\n'
        version = '__version__ = "1.0"\n'
        alg_all = '__all__ = ["' + str(self.cw_line_1.text()) + '"]\n\n\n'
        alg_imports = 'import egads.core.egads_core as egads_core\nimport egads.core.metadata as ' \
                      'egads_metadata\n\n'
        alg_class = 'class ' + str(self.cw_line_1.text()) + '(egads_core.EgadsAlgorithm):\n\n'
        purpose = prepare_long_string(str(self.cw_plain_2.toPlainText()), 75, 16)
        description = prepare_long_string(str(self.cw_plain_1.toPlainText()), 75, 16)
        source = prepare_long_string(str(self.cw_line_3.text()), 75, 16)
        reference = prepare_long_string(str(self.cw_line_4.text()), 75, 16)
        alg_input = self.prepare_inputs()
        alg_output = self.prepare_outputs()
        alg_help = ('    """\n'
                    + '    FILE        ' + filename + '.py\n'
                    + '\n'
                    + '    VERSION     1.0\n'
                    + '\n'
                    + '    CATEGORY    ' + category + '\n'
                    + '\n'
                    + '    PURPOSE     ' + purpose + '\n'
                    + '\n'
                    + '    DESCRIPTION ' + description + '\n'
                    + '\n'
                    + '    INPUT       ' + alg_input
                    + '\n'
                    + '    OUTPUT      ' + alg_output
                    + '\n'
                    + '    SOURCE      ' + source + '\n'
                    + '\n'
                    + '    REFERENCES  ' + reference + '\n'
                    + '    """\n\n')
        alg_init = ('    def __init__(self, return_Egads=True):\n        '
                    + 'egads_core.EgadsAlgorithm.__init__(self, return_Egads)\n\n')
        alg_out_metadata = self.prepare_output_metadata()
        alg_metadata = self.prepare_algorithm_metadata()
        alg_run = self.prepare_algorithm_run()
        algorithm = self.prepare_algorithm_text()
        complete_string = (author + date + version + alg_all + alg_imports + alg_class + alg_help
                           + alg_init + alg_out_metadata + alg_metadata + alg_run + algorithm)
        try:
            write_algorithm(filename, complete_string, category, str(self.cw_line_2.text()))
            self.success = True
        except Exception:
            logging.exception('gui - algorithm_window_functions.py - MyAlgorithm - prepare_algorithm : an '
                              'exception occurred when writing the algorithm file.')
            self.success = False
        self.algorithm_filename = filename
        self.algorithm_category = category
        self.algorithm_name = str(self.cw_line_1.text())
        self.cancel = False
        self.close()

    def prepare_inputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_inputs')
        input_string = ''
        input_symbols = []
        input_types = []
        input_units = []
        input_description = []
        for i in range(len(self.cw_input_vl_1)):
            input_symbols.append(str(self.cw_input_ln_1[i].text()))
            if str(self.cw_input_ln_2[i].text()) == 'None' or str(self.cw_input_ln_2[i].text()) == ' ':
                input_units.append('_')
            else:
                input_units.append(str(self.cw_input_ln_2[i].text()))
            input_types.append(str(self.cw_input_ln_3[i].text()))
            input_description.append(str(self.cw_input_ln_4[i].text()))
        max_symbols_length = check_string_max_length(input_symbols)
        max_units_length = check_string_max_length(input_units)
        max_types_length = check_string_max_length(input_types)
        for i in range(len(self.cw_input_vl_1)):
            tmp_string = ' ' * 16
            tmp_string += (input_symbols[i] + ' ' * (max_symbols_length - len(input_symbols[i]) + 4)
                           + input_types[i] + ' ' * (max_types_length - len(input_types[i]) + 4)
                           + input_units[i] + ' ' * (max_units_length - len(input_units[i]) + 4)
                           + input_description[i])
            carriage_length = max_symbols_length + max_types_length + max_units_length + 28
            tmp_string = prepare_long_string(tmp_string, 75, carriage_length)
            input_string += tmp_string + '\n'
        return input_string[16:]

    def prepare_outputs(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_outputs')
        output_string = ''
        output_symbols = []
        output_types = []
        output_units = []
        output_description = []
        for i in range(len(self.cw_output_vl_1)):
            output_symbols.append(str(self.cw_output_ln_1[i].text()))
            if str(self.cw_output_ln_3[i].text()):
                if 'input' in str(self.cw_output_ln_2[i].text()):
                    output_units.append('_')
                else:
                    output_units.append(str(self.cw_output_ln_2[i].text()))
            else:
                output_units.append('_')
            output_types.append(str(self.cw_output_ln_3[i].text()))
            output_description.append(str(self.cw_output_ln_4[i].text()))
        max_symbols_length = check_string_max_length(output_symbols)
        max_units_length = check_string_max_length(output_units)
        max_types_length = check_string_max_length(output_types)
        for i in range(len(self.cw_output_vl_1)):
            tmp_string = ' ' * 16
            tmp_string += (output_symbols[i] + ' ' * (max_symbols_length - len(output_symbols[i]) + 4)
                           + output_types[i] + ' ' * (max_types_length - len(output_types[i]) + 4)
                           + output_units[i] + ' ' * (max_units_length - len(output_units[i]) + 4)
                           + output_description[i])
            carriage_length = max_symbols_length + max_types_length + max_units_length + 28
            tmp_string = prepare_long_string(tmp_string, 75, carriage_length)
            output_string += tmp_string + '\n'
        return output_string[16:]

    def prepare_output_metadata(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_output_metadata')
        output_string = ''
        if len(self.cw_output_vl_1) > 1:
            output_string += '        self.output_metadata = []\n'
            for i in range(len(self.cw_output_vl_1)):
                units = str(self.cw_output_ln_2[i].text())
                long_name = str(self.cw_output_ln_6[i].text())
                standard_name = str(self.cw_output_ln_5[i].text())
                if self.cw_output_lw_1[i].count() > 0:
                    category = '['
                    for j in range(self.cw_output_lw_1[i].count()):
                        category += "'" + self.cw_output_lw_1[i].item(j).text() + "',"
                    category = category[:-1] + ']'
                else:
                    category = "['']"

                ##########################
                #
                # temporaire
                #
                ##########################
                output_string += ("        self.output_metadata.append(egads_metadata.VariableMetadata({"
                                  + "'units':'" + units + "',\n"
                                  + ' ' * 64 + "'long_name':'" + long_name + "',\n"
                                  + ' ' * 64 + "'standard_name':'" + standard_name + "',\n"
                                  + ' ' * 64 + "'Category':" + category + "}))\n\n")

        elif len(self.cw_output_vl_1) == 1:
            units = str(self.cw_output_ln_2[0].text())
            long_name = str(self.cw_output_ln_6[0].text())
            standard_name = str(self.cw_output_ln_5[0].text())
            if self.cw_output_lw_1[0].count() > 0:
                category = '['
                for j in range(self.cw_output_lw_1[0].count()):
                    category += "'" + self.cw_output_lw_1[0].item(j).text() + "',"
                category = category[:-1] + ']'
            else:
                category = "['']"

            ##########################
            #
            # temporaire
            #
            #########################
            output_string += ("        self.output_metadata = egads_metadata.VariableMetadata({"
                              + "'units':'" + units + "',\n"
                              + ' ' * 63 + "'long_name':'" + long_name + "',\n"
                              + ' ' * 63 + "'standard_name':'" + standard_name + "',\n"
                              + ' ' * 63 + "'Category':" + category + "})\n\n")

        return output_string

    def prepare_algorithm_metadata(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_metadata')
        input_symbols = ''
        input_units = ''
        input_types = ''
        input_description = ''
        output_symbols = ''
        output_description = ''
        output_units = ''
        output_types = ''
        for i in range(len(self.cw_input_vl_1)):
            if i == 0:
                input_symbols = '['
                input_units = '['
                input_types = '['
                input_description = '['
            input_symbols += "'" + str(self.cw_input_ln_1[i].text()) + "',"
            if str(self.cw_input_ln_2[i].text()) == 'None':
                input_units += "None,"
            elif str(self.cw_input_ln_2[i].text()) == ' ':
                input_units += "'',"
            else:
                input_units += "'" + str(self.cw_input_ln_2[i].text()) + "',"
            input_types += "'" + str(self.cw_input_ln_3[i].text()) + "',"
            input_description += "'" + str(self.cw_input_ln_4[i].text()) + "',"
        input_symbols = input_symbols[:-1] + ']'
        input_units = input_units[:-1] + ']'
        input_types = input_types[:-1] + ']'
        input_description = input_description[:-1] + ']'
        for i in range(len(self.cw_output_vl_1)):
            if i == 0:
                output_symbols = '['
                output_description = '['
                output_units = '['
                output_types = '['
            output_symbols += "'" + str(self.cw_output_ln_1[i].text()) + "',"
            output_description += "'" + str(self.cw_output_ln_4[i].text()) + "',"
            output_units += "'" + str(self.cw_output_ln_2[i].text()) + "',"
            output_types += "'" + str(self.cw_output_ln_3[i].text()) + "',"
        output_symbols = output_symbols[:-1] + ']'
        output_description = output_description[:-1] + ']'
        output_units = output_units[:-1] + ']'
        output_types = output_types[:-1] + ']'
        category = ''
        if self.cw_combobox_1.currentText() == 'Other...':
            category = str(self.cw_line_5.text())
        elif self.cw_combobox_1.currentText() != 'Make a choice...':
            category = str(self.cw_combobox_1.currentText())
        space_string = "                                                          "
        metadata_string = ("        self.metadata = egads_metadata.AlgorithmMetadata({'Inputs':" + input_symbols + ",\n"
                           + space_string + "'InputUnits':" + input_units + ",\n"
                           + space_string + "'InputTypes':" + input_types + ",\n"
                           + space_string + "'InputDescription':" + input_description + ",\n"
                           + space_string + "'Outputs':" + output_symbols + ",\n"
                           + space_string + "'OutputUnits':" + output_units + ",\n"
                           + space_string + "'OutputTypes':" + output_types + ",\n"
                           + space_string + "'OutputDescription':" + output_description + ",\n"
                           + space_string + "'Purpose':'" + str(self.cw_plain_2.toPlainText()) + "',\n"
                           + space_string + "'Description':'" + str(self.cw_plain_1.toPlainText()) + "',\n"
                           + space_string + "'Category':'" + category + "',\n"
                           + space_string + "'Source':'" + str(self.cw_line_3.text()) + "',\n"
                           + space_string + "'References':'" + str(self.cw_line_4.text()) + "',\n"
                           + space_string + "'Processor':self.name,\n"
                           + space_string + "'ProcessorDate':__date__,\n"
                           + space_string + "'ProcessorVersion':__version__,\n"
                           + space_string + "'DateProcessed':self.now()},\n"
                           + space_string + "self.output_metadata)\n\n")
        return metadata_string

    def prepare_algorithm_run(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_run')
        run_string = ''
        input_symbols = ''
        for i in range(len(self.cw_input_vl_1)):
            input_symbols += str(self.cw_input_ln_1[i].text()) + ", "
        input_symbols = input_symbols[:-2]
        run_string += ("    def run(self, " + input_symbols + "):\n"
                       + "        return egads_core.EgadsAlgorithm.run(self, " + input_symbols + ")\n\n"
                       + "    def _algorithm(self, " + input_symbols + "):\n")
        return run_string

    def prepare_algorithm_text(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - prepare_algorithm_text')
        algorithm_string = ''
        if self.cw_plain_4.toPlainText():
            algorithm = ' ' * 8 + str(self.cw_plain_4.toPlainText())
            algorithm_string = algorithm.replace('\n', '\n        ')
            algorithm_string += '\n'
        return algorithm_string

    def units_validation(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - validate_units')
        units_list = []
        for i in range(len(self.cw_input_vl_1)):
            if str(self.cw_input_ln_2[i].text()):
                if str(self.cw_input_ln_2[i].text()) == 'None' or str(self.cw_input_ln_2[i].text()) == ' ':
                    pass
                else:
                    unit_validation = egads.EgadsData(value=[0], units=str(self.cw_input_ln_2[i].text()))
                    units_list.append([str(self.cw_input_ln_1[i].text()), str(self.cw_input_ln_2[i].text()),
                                       unit_validation.units, 'input'])
        for i in range(len(self.cw_output_vl_1)):
            if str(self.cw_output_ln_2[i].text()):
                if 'input' in str(self.cw_output_ln_2[i].text()):
                    pass
                else:
                    unit_validation = egads.EgadsData(value=[0], units=str(self.cw_output_ln_2[i].text()))
                    units_list.append([str(self.cw_output_ln_1[i].text()), str(self.cw_output_ln_2[i].text()),
                                      unit_validation.units, 'output'])
        return units_list

    def check_all_fields(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithm - check_all_fields')
        self.reset_tab_title_color()
        self.reset_labels_color()
        algorithm_section = True
        for widget, label in self.algorithm_mandatory_fields.items():
            if isinstance(widget, QtWidgets.QLineEdit):
                if not widget.text():
                    algorithm_section = False
                    label.setStyleSheet("QLabel {\n"
                                        "    color: rgb(200,0,0);\n"
                                        "}")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            elif isinstance(widget, QtWidgets.QTextEdit):
                if not widget.toPlainText():
                    algorithm_section = False
                    label.setStyleSheet("QLabel {\n"
                                        "    color: rgb(200,0,0);\n"
                                        "}")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            elif isinstance(widget, QtWidgets.QPlainTextEdit):
                if not widget.toPlainText():
                    algorithm_section = False
                    label.setStyleSheet("QLabel {\n"
                                        "    color: rgb(200,0,0);\n"
                                        "}")
                    self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))

        if self.cw_combobox_1.currentText() == 'Make a choice...':
            algorithm_section = False
            self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            self.cw_label_9.setStyleSheet("QLabel {\n"
                                          "    color: rgb(200,0,0);\n"
                                          "}")
        elif self.cw_combobox_1.currentText() == 'Other...' and self.cw_line_5.text() == '':
            algorithm_section = False
            self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(200, 0, 0))
            self.cw_label_9.setStyleSheet("QLabel {\n"
                                          "    color: rgb(200,0,0);\n"
                                          "}")
        input_section = True
        if self.cw_input_vl_1:
            widget_list = self.tab_2.findChildren(QtWidgets.QLineEdit)
            for widget in widget_list:
                if 'cw_input_ln_2' not in widget.objectName():
                    if not widget.text():
                        input_section = False
                        label = self.tab_2.findChildren(QtWidgets.QLabel, widget.objectName()[:9] + 'lb' +
                                                        widget.objectName()[11:])[0]
                        label.setStyleSheet("QLabel {\n"
                                            "    color: rgb(200,0,0);\n"
                                            "}")
                        self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200, 0, 0))
        else:
            input_section = False
            self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200, 0, 0))
        output_section = True
        if self.cw_output_vl_1:
            widget_list = self.tab_3.findChildren(QtWidgets.QLineEdit)
            for widget in widget_list:
                if ('cw_output_ln_2' not in widget.objectName()) and ('cw_output_ln_6' not in widget.objectName()):
                    if not widget.text():
                        output_section = False
                        label = self.tab_3.findChildren(QtWidgets.QLabel, widget.objectName()[:10] + 'lb' +
                                                        widget.objectName()[12:])[0]
                        label.setStyleSheet("QLabel {\n"
                                            "    color: rgb(200,0,0);\n"
                                            "}")
                        self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200, 0, 0))
        else:
            output_section = False
            self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200, 0, 0))
        if not output_section or not input_section or not algorithm_section:
            fill_window = MyFill()
            fill_window.exec_()
            result = fill_window.cancel
        else:
            result = False
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - check_all_fields : result ' + str(result))
        return result

    def reset_tab_title_color(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - reset_tab_title_color')
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(45, 45, 45))

    def reset_labels_color(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - reset_labels_color')
        for label in self.findChildren(QtWidgets.QLabel):
            label.setStyleSheet("QLabel {\n"
                                "    color: rgb(45,45,45);\n"
                                "}")

    def algorithm_button_info(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - algorithm_button_info')
        info_window = MyInfo(self.information_text[self.sender().objectName()])
        info_window.exec_()

    def input_output_button_info(self):
        logging.debug('gui - algorithm_windows_functions.py - MyAlgorithm - input_output_button_info')
        index = -1 * (int(''.join(reversed(self.sender().objectName())).find('_')) + 1)
        info_window = MyInfo(self.information_text[self.sender().objectName()[:index]])
        info_window.exec_()

    def closeWindow(self):
        logging.debug('gui - algorithm_window_functions.py - MyAlgorithmDisplay - closeWindow')
        self.close()
