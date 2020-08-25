import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from functions.utils import populate_combobox, font_creation_function, icon_creation_function
from functions.window_functions.plot_ts_option_secondary_functions import activate_ts_grid_options, update_ts_slider_value
from functions.window_functions.plot_ts_option_secondary_functions import activate_ts_line_color, activate_ts_opacity_options
from functions.window_functions.plot_ts_option_secondary_functions import activate_ts_line_style
from functions.material_functions import line_style_list, colors_dict
import matplotlib.pyplot as plt


def add_figure_options(self, subplot=None):
    logging.debug('gui - plot_ts_main_functions.py - add_figure_options')
    font3 = font_creation_function('small')
    font2 = font_creation_function('big')
    font = font_creation_function('normal')
    icon = icon_creation_function('info_icon.svg')
    if self.figure_option_num == 0:
        figure_options_sliders(self)
    self.pw_figureOptions_vl_1.append(QtWidgets.QVBoxLayout())
    self.pw_figureOptions_vl_1[self.figure_option_num].setObjectName("pw_figureOptions_vl_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_1.append(QtWidgets.QHBoxLayout())
    self.pw_figureOptions_hl_1[self.figure_option_num].setObjectName("pw_figureOptions_hl_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_1.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_1[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_1[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_1[self.figure_option_num].setFont(font2)
    if self.subplot_ts_fig_list:
        text = 'Subplot ' + str(self.figure_option_num + 1) + ': Figure options'
    else:
        text = 'Figure options:'
    self.pw_figureOptions_lb_1[self.figure_option_num].setText(text)
    self.pw_figureOptions_lb_1[self.figure_option_num].setObjectName("pw_figureOptions_lb_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_1[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_hl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_1[
                                                                     self.figure_option_num])
    self.pw_figureOptions_hl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.
                                      QSizePolicy.Minimum))
    self.pw_figureOptions_vl_1[self.figure_option_num].addLayout(self.pw_figureOptions_hl_1[
                                                                     self.figure_option_num])
    self.pw_figureOptions_hl_2.append(QtWidgets.QHBoxLayout())
    self.pw_figureOptions_hl_2[self.figure_option_num].setObjectName("pw_figureOptions_hl_2_" + str(
        self.figure_option_num))
    self.pw_figureOptions_hl_2[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_gl_1.append(QtWidgets.QGridLayout())
    self.pw_figureOptions_gl_1[self.figure_option_num].setObjectName("pw_figureOptions_gl_1_" + str(
        self.figure_option_num))
    self.pw_figureOptions_hl_2[self.figure_option_num].addLayout(self.pw_figureOptions_gl_1[
                                                                     self.figure_option_num])
    self.pw_figureOptions_lb_2.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_2[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_2[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_2[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_2[self.figure_option_num].setText("Figure title:")
    self.pw_figureOptions_lb_2[self.figure_option_num].setObjectName("pw_figureOptions_lb_2_" + str(
        self.figure_option_num))
    self.pw_figureOptions_lb_2[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num].addWidget(self.pw_figureOptions_lb_2[
                                                                     self.figure_option_num], 0, 0, 1, 1)
    self.pw_figureOptions_ln_1.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_ln_1[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
    self.pw_figureOptions_ln_1[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
    self.pw_figureOptions_ln_1[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_1[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "    padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color:  rgb(240, "
                                                                     "240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_1[self.figure_option_num].setObjectName("pw_lineEdit_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_1[self.figure_option_num], 0, 1, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 0, 2, 1, 1)
    self.pw_figureOptions_lb_3.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_3[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_3[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_3[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_3[self.figure_option_num].setText("Font:")
    self.pw_figureOptions_lb_3[self.figure_option_num].setObjectName("pw_figureOptions_lb_3_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_3[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_3[self.figure_option_num], 0, 3, 1, 1)
    self.pw_figureOptions_cb_1.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_1[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_1[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
    self.pw_figureOptions_cb_1[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
    self.pw_figureOptions_cb_1[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_1[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #f0f0f0, "
                                                                     "stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #ecf4fc, "
                                                                     "stop: 1 #dcecfc);\n"
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
                                                                     "    border-bottom-right-radius: "
                                                                     "3px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow {\n"
                                                                     "    image: "
                                                                     "url(icons/down_arrow_icon.svg); \n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_1[self.figure_option_num].setObjectName("pw_figureOptions_cb_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_1[self.figure_option_num], 0, 4, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 0, 5, 1, 1)
    self.pw_figureOptions_lb_4.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_4[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_4[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_4[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_4[self.figure_option_num].setText("Size:")
    self.pw_figureOptions_lb_4[self.figure_option_num].setObjectName("pw_figureOptions_lb_4_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_4[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_4[self.figure_option_num], 0, 6, 1, 1)
    self.pw_figureOptions_cb_2.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_2[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_2[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_cb_2[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_cb_2[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_2[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #f0f0f0, "
                                                                     "stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #ecf4fc, "
                                                                     "stop: 1 #dcecfc);\n"
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
                                                                     "    border-bottom-right-radius: "
                                                                     "3px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow {\n"
                                                                     "    image: "
                                                                     "url(icons/down_arrow_icon.svg); \n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_2[self.figure_option_num].setObjectName("pw_figureOptions_cb_2_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_2[self.figure_option_num], 0, 7, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 0, 8, 1, 1)
    self.pw_figureOptions_lb_5.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_5[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_5[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_5[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_5[self.figure_option_num].setText("X axis label:")
    self.pw_figureOptions_lb_5[self.figure_option_num].setObjectName("pw_figureOptions_lb_5_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_5[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_5[self.figure_option_num], 1, 0, 1, 1)
    self.pw_figureOptions_ln_2.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_ln_2[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
    self.pw_figureOptions_ln_2[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
    self.pw_figureOptions_ln_2[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_2[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "    padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_2[self.figure_option_num].setObjectName("pw_lineEdit_2_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_2[self.figure_option_num], 1, 1, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 1, 2, 1, 1)
    self.pw_figureOptions_lb_6.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_6[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_6[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_6[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_6[self.figure_option_num].setText("Font:")
    self.pw_figureOptions_lb_6[self.figure_option_num].setObjectName("pw_figureOptions_lb_6_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_6[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_6[self.figure_option_num], 1, 3, 1, 1)
    self.pw_figureOptions_cb_3.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_3[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_3[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
    self.pw_figureOptions_cb_3[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
    self.pw_figureOptions_cb_3[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_3[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #f0f0f0, "
                                                                     "stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #ecf4fc, "
                                                                     "stop: 1 #dcecfc);\n"
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
                                                                     "    border-bottom-right-radius: "
                                                                     "3px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow {\n"
                                                                     "    image: "
                                                                     "url(icons/down_arrow_icon.svg); \n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_3[self.figure_option_num].setFrame(False)
    self.pw_figureOptions_cb_3[self.figure_option_num].setObjectName("pw_figureOptions_cb_3_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_3[self.figure_option_num], 1, 4, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 1, 5, 1, 1)
    self.pw_figureOptions_lb_7.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_7[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_7[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_7[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_7[self.figure_option_num].setText("Size:")
    self.pw_figureOptions_lb_7[self.figure_option_num].setObjectName("pw_figureOptions_lb_7_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_7[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_7[self.figure_option_num], 1, 6, 1, 1)
    self.pw_figureOptions_cb_4.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_4[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_4[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_cb_4[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_cb_4[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_4[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #f0f0f0, "
                                                                     "stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #ecf4fc, "
                                                                     "stop: 1 #dcecfc);\n"
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
                                                                     "    border-bottom-right-radius: "
                                                                     "3px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow {\n"
                                                                     "    image: "
                                                                     "url(icons/down_arrow_icon.svg); \n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_4[self.figure_option_num].setFrame(False)
    self.pw_figureOptions_cb_4[self.figure_option_num].setObjectName("pw_figureOptions_cb_4_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_4[self.figure_option_num], 1, 7, 1, 1)
    self.pw_figureOptions_lb_8.append(QtWidgets.QLabel(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_lb_8[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_8[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_8[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_8[self.figure_option_num].setText("Y axis label:")
    self.pw_figureOptions_lb_8[self.figure_option_num].setObjectName("pw_figureOptions_lb_8_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_8[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_8[self.figure_option_num], 2, 0, 1, 1)
    self.pw_figureOptions_ln_3.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3))
    self.pw_figureOptions_ln_3[self.figure_option_num].setMinimumSize(QtCore.QSize(500, 27))
    self.pw_figureOptions_ln_3[self.figure_option_num].setMaximumSize(QtCore.QSize(500, 27))
    self.pw_figureOptions_ln_3[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_3[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "   padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_3[self.figure_option_num].setObjectName("pw_lineEdit_3_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_3[self.figure_option_num], 2, 1, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 2, 2, 1, 1)
    self.pw_figureOptions_lb_9.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_9[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_9[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_9[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_9[self.figure_option_num].setText("Font:")
    self.pw_figureOptions_lb_9[self.figure_option_num].setObjectName("pw_figureOptions_lb_9_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_lb_9[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_9[self.figure_option_num], 2, 3, 1, 1)
    self.pw_figureOptions_cb_5.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_5[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_5[self.figure_option_num].setMinimumSize(QtCore.QSize(240, 27))
    self.pw_figureOptions_cb_5[self.figure_option_num].setMaximumSize(QtCore.QSize(240, 27))
    self.pw_figureOptions_cb_5[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_5[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #f0f0f0, "
                                                                     "stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #ecf4fc, "
                                                                     "stop: 1 #dcecfc);\n"
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
                                                                     "    border-bottom-right-radius: "
                                                                     "3px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow {\n"
                                                                     "    image: "
                                                                     "url(icons/down_arrow_icon.svg); \n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_5[self.figure_option_num].setFrame(False)
    self.pw_figureOptions_cb_5[self.figure_option_num].setObjectName("pw_figureOptions_cb_5_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_5[self.figure_option_num], 2, 4, 1, 1)
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 2, 5, 1, 1)
    self.pw_figureOptions_lb_10.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_10[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_10[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_10[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_10[self.figure_option_num].setText("Size:")
    self.pw_figureOptions_lb_10[self.figure_option_num].setObjectName("pw_figureOptions_lb_10_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_10[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_10[self.figure_option_num], 2, 6, 1, 1)
    self.pw_figureOptions_cb_6.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_6[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_6[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_cb_6[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_cb_6[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_6[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #f0f0f0, "
                                                                     "stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: "
                                                                     "qlineargradient(x1: 0, y1: 0, "
                                                                     "x2: 0, y2: 1, \n"
                                                                     "                                "
                                                                     "stop: 0 #ecf4fc, "
                                                                     "stop: 1 #dcecfc);\n"
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
                                                                     "    border-bottom-right-radius: "
                                                                     "3px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow {\n"
                                                                     "    image: "
                                                                     "url(icons/down_arrow_icon.svg); \n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: "
                                                                     "rgb(200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_6[self.figure_option_num].setFrame(False)
    self.pw_figureOptions_cb_6[self.figure_option_num].setObjectName("pw_figureOptions_cb_6_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_1[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_6[self.figure_option_num], 2, 7, 1, 1)
    self.pw_figureOptions_hl_2[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_bt_1.append(QtWidgets.QToolButton())
    self.pw_figureOptions_bt_1[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_1[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_1[self.figure_option_num].setStyleSheet("QToolButton {\n"
                                                                     "    border: 1px solid transparent;\n"
                                                                     "    background-color: transparent;\n"
                                                                     "    width: 27px;\n"
                                                                     "    height: 27px;\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QToolButton:flat {\n"
                                                                     "    border: none;\n"
                                                                     "}")
    self.pw_figureOptions_bt_1[self.figure_option_num].setText("")
    self.pw_figureOptions_bt_1[self.figure_option_num].setIcon(icon)
    self.pw_figureOptions_bt_1[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_figureOptions_bt_1[self.figure_option_num].setAutoRaise(False)
    self.pw_figureOptions_bt_1[self.figure_option_num].setObjectName("pw_figureOptions_bt_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_bt_1[self.figure_option_num])
    self.pw_figureOptions_hl_2[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_vl_1[self.figure_option_num]. \
        addLayout(self.pw_figureOptions_hl_2[self.figure_option_num])
    self.pw_figureOptions_hl_3.append(QtWidgets.QHBoxLayout())
    self.pw_figureOptions_hl_3[self.figure_option_num].setObjectName("pw_figureOptions_hl_3_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_gl_2.append(QtWidgets.QGridLayout())
    self.pw_figureOptions_gl_2[self.figure_option_num].setObjectName("pw_figureOptions_gl_2_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_3[self.figure_option_num]. \
        addLayout(self.pw_figureOptions_gl_2[self.figure_option_num])
    self.pw_figureOptions_lb_11.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_11[self.figure_option_num].setMinimumSize(QtCore.QSize(200, 27))
    self.pw_figureOptions_lb_11[self.figure_option_num].setMaximumSize(QtCore.QSize(200, 27))
    self.pw_figureOptions_lb_11[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_11[self.figure_option_num].setText("X min / max / tick step:")
    self.pw_figureOptions_lb_11[self.figure_option_num].setObjectName("pw_figureOptions_lb_11_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_11[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_11[self.figure_option_num], 0, 0, 1, 1)
    self.pw_figureOptions_ln_4.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_4[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_4[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_4[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_4[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "    padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_4[self.figure_option_num].setObjectName("pw_figureOptions_ln_4_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_4[self.figure_option_num], 0, 1, 1, 1)
    self.pw_figureOptions_ln_5.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_5[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_5[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_5[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_5[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "    padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_5[self.figure_option_num].setObjectName("pw_figureOptions_ln_5_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_5[self.figure_option_num], 0, 2, 1, 1)
    self.pw_figureOptions_ln_6.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_6[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_6[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_6[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_6[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "    padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_6[self.figure_option_num].setObjectName("pw_figureOptions_ln_6_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_6[self.figure_option_num], 0, 3, 1, 1)
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 0, 4, 1, 1)
    self.pw_figureOptions_lb_13.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_13[self.figure_option_num].setMinimumSize(QtCore.QSize(200, 27))
    self.pw_figureOptions_lb_13[self.figure_option_num].setMaximumSize(QtCore.QSize(200, 27))
    self.pw_figureOptions_lb_13[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_13[self.figure_option_num].setText("Y min / max / tick step:")
    self.pw_figureOptions_lb_13[self.figure_option_num].setObjectName("pw_figureOptions_lb_13_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_13[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_13[self.figure_option_num], 1, 0, 1, 1)
    self.pw_figureOptions_ln_7.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_7[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_7[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_7[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_7[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "    padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_ln_7[self.figure_option_num].setObjectName("pw_figureOptions_ln_7_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_7[self.figure_option_num], 1, 1, 1, 1)
    self.pw_figureOptions_ln_8.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_8[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_8[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_8[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_8[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "   padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "}")
    self.pw_figureOptions_ln_8[self.figure_option_num].setObjectName("pw_figureOptions_ln_8_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_8[self.figure_option_num], 1, 2, 1, 1)
    self.pw_figureOptions_ln_9.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_9[self.figure_option_num].setMinimumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_9[self.figure_option_num].setMaximumSize(QtCore.QSize(70, 27))
    self.pw_figureOptions_ln_9[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_9[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                     "    border-radius: 3px;\n"
                                                                     "   padding: 1px 4px 1px 4px;\n"
                                                                     "    background-color: "
                                                                     "rgb(240, 240, 240);\n"
                                                                     "}")
    self.pw_figureOptions_ln_9[self.figure_option_num].setObjectName("pw_figureOptions_ln_9_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_9[self.figure_option_num], 1, 3, 1, 1)
    self.pw_figureOptions_gl_2[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.
                                      Minimum), 1, 4, 1, 1)
    self.pw_figureOptions_bt_2.append(QtWidgets.QToolButton())
    self.pw_figureOptions_bt_2[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_2[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_2[self.figure_option_num].setStyleSheet("QToolButton {\n"
                                                                     "    border: 1px solid transparent;\n"
                                                                     "    background-color: transparent;\n"
                                                                     "    width: 27px;\n"
                                                                     "    height: 27px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QToolButton:flat {\n"
                                                                     "    border: none;\n"
                                                                     "}")
    self.pw_figureOptions_bt_2[self.figure_option_num].setText("")
    self.pw_figureOptions_bt_2[self.figure_option_num].setIcon(icon)
    self.pw_figureOptions_bt_2[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_figureOptions_bt_2[self.figure_option_num].setAutoRaise(False)
    self.pw_figureOptions_bt_2[self.figure_option_num].setObjectName("pw_figureOptions_bt_2_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_bt_2[self.figure_option_num])
    self.pw_figureOptions_hl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.
                                      QSizePolicy.Minimum))
    self.pw_figureOptions_vl_1[self.figure_option_num]. \
        addLayout(self.pw_figureOptions_hl_3[self.figure_option_num])
    self.pw_figureOptions_hl_4.append(QtWidgets.QHBoxLayout())
    self.pw_figureOptions_hl_4[self.figure_option_num].setObjectName("pw_figureOptions_hl_4_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_4[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_gl_3.append(QtWidgets.QGridLayout())
    self.pw_figureOptions_gl_3[self.figure_option_num].setObjectName("pw_figureOptions_gl_3_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_hl_4[self.figure_option_num]. \
        addLayout(self.pw_figureOptions_gl_3[self.figure_option_num])
    self.pw_figureOptions_lb_15.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_15[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_15[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_15[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_15[self.figure_option_num].setText("Display grid ?")
    self.pw_figureOptions_lb_15[self.figure_option_num].setObjectName("pw_figureOptions_lb_15_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_15[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_15[self.figure_option_num], 0, 0, 1, 1)
    self.pw_figureOptions_ck_1.append(QtWidgets.QCheckBox())
    self.pw_figureOptions_ck_1[self.figure_option_num].setMinimumSize(QtCore.QSize(25, 20))
    self.pw_figureOptions_ck_1[self.figure_option_num].setMaximumSize(QtCore.QSize(25, 20))
    self.pw_figureOptions_ck_1[self.figure_option_num].setText("")
    self.pw_figureOptions_ck_1[self.figure_option_num].setObjectName("pw_figureOptions_ck_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_ck_1[self.figure_option_num].setStyleSheet("QCheckBox {\n"
                                                                     "    spacing: 5px;\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ck_1[self.figure_option_num], 0, 1, 1, 1)
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                      QSizePolicy.Minimum), 0, 2, 1, 1)
    self.pw_figureOptions_lb_16.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_16[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_16[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_16[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_16[self.figure_option_num].setText("Style:")
    self.pw_figureOptions_lb_16[self.figure_option_num].setObjectName("pw_figureOptions_lb_16_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_16[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_16[self.figure_option_num], 0, 3, 1, 1)
    self.pw_figureOptions_cb_9.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_9[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_9[self.figure_option_num].setEnabled(False)
    self.pw_figureOptions_cb_9[self.figure_option_num].setMinimumSize(QtCore.QSize(160, 27))
    self.pw_figureOptions_cb_9[self.figure_option_num].setMaximumSize(QtCore.QSize(160, 27))
    self.pw_figureOptions_cb_9[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_9[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                     "    border: 1px solid #acacac;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    padding-left: 5px;\n"
                                                                     "    background-color: qlineargradient("
                                                                     "x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                                                     "                                stop: "
                                                                     "0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:disabled {\n"
                                                                     "    background-color: rgb(200,200,200);\n"
                                                                     "    color: rgb(145,145,145);\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox:hover {\n"
                                                                     "    border: 1px solid #7eb4ea;\n"
                                                                     "    border-radius: 1px;\n"
                                                                     "    background-color: qlineargradient("
                                                                     "x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                                                     "                                stop: "
                                                                     "0 #ecf4fc, stop: 1 #dcecfc);\n"
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
                                                                     "    image: url("
                                                                     "icons/down_arrow_icon.svg);\n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox::down-arrow:disabled {\n"
                                                                     "    image: url("
                                                                     "icons/down_arrow_icon_deactivated.svg);\n"
                                                                     "    width: 16px;\n"
                                                                     "    height: 16px\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView {\n"
                                                                     "    selection-background-color: rgb("
                                                                     "200,200,200);\n"
                                                                     "    selection-color: black;\n"
                                                                     "    background: #f0f0f0;\n"
                                                                     "    border: 0px solid #f0f0f0;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QComboBox QAbstractItemView::item {\n"
                                                                     "    margin: 5px 5px 5px 5px;\n"
                                                                     "}")
    self.pw_figureOptions_cb_9[self.figure_option_num].setFrame(False)
    self.pw_figureOptions_cb_9[self.figure_option_num].setObjectName("pw_figureOptions_cb_9_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_9[self.figure_option_num], 0, 4, 1, 1)
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                      QSizePolicy.Minimum), 0, 5, 1, 1)
    self.pw_figureOptions_lb_17.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_17[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_17[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_17[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_17[self.figure_option_num].setText("Size:")
    self.pw_figureOptions_lb_17[self.figure_option_num].setObjectName("pw_figureOptions_lb_17_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_17[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_17[self.figure_option_num], 0, 6, 1, 1)
    self.pw_figureOptions_ln_10.append(QtWidgets.QLineEdit())
    self.pw_figureOptions_ln_10[self.figure_option_num].setEnabled(False)
    self.pw_figureOptions_ln_10[self.figure_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_ln_10[self.figure_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_figureOptions_ln_10[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_ln_10[self.figure_option_num].setStyleSheet("QLineEdit {\n"
                                                                      "    border-radius: 3px;\n"
                                                                      "    padding: 1px 4px 1px 4px;\n"
                                                                      "    background-color: rgb(240, 240, 240);\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QLineEdit:disabled {\n"
                                                                      "    background-color: rgb(200,200,200);\n"
                                                                      "    color: rgb(145,145,145);\n"
                                                                      "}")
    self.pw_figureOptions_ln_10[self.figure_option_num].setObjectName("pw_figureOptions_ln_10_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ln_10[self.figure_option_num], 0, 7, 1, 1)
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                      QSizePolicy.Minimum), 0, 8, 1, 1)
    self.pw_figureOptions_lb_19.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_19[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_19[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_19[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_19[self.figure_option_num].setText("Color:")
    self.pw_figureOptions_lb_19[self.figure_option_num].setObjectName("pw_figureOptions_lb_19_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_19[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_19[self.figure_option_num], 0, 9, 1, 1)
    self.pw_figureOptions_cb_10.append(QtWidgets.QComboBox())
    self.pw_figureOptions_cb_10[self.figure_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_figureOptions_cb_10[self.figure_option_num].setEnabled(False)
    self.pw_figureOptions_cb_10[self.figure_option_num].setMinimumSize(QtCore.QSize(160, 27))
    self.pw_figureOptions_cb_10[self.figure_option_num].setMaximumSize(QtCore.QSize(160, 27))
    self.pw_figureOptions_cb_10[self.figure_option_num].setFont(font3)
    self.pw_figureOptions_cb_10[self.figure_option_num].setStyleSheet("QComboBox {\n"
                                                                      "    border: 1px solid #acacac;\n"
                                                                      "    border-radius: 1px;\n"
                                                                      "    padding-left: 5px;\n"
                                                                      "    background-color: qlineargradient("
                                                                      "x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                                                      "                                stop: "
                                                                      "0 #f0f0f0, stop: 1 #e5e5e5);\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QComboBox:disabled {\n"
                                                                      "    background-color: rgb(200,200,"
                                                                      "200);\n"
                                                                      "    color: rgb(145,145,145);\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QComboBox:hover {\n"
                                                                      "    border: 1px solid #7eb4ea;\n"
                                                                      "    border-radius: 1px;\n"
                                                                      "    background-color: qlineargradient("
                                                                      "x1: 0, y1: 0, x2: 0, y2: 1, \n"
                                                                      "                                stop: "
                                                                      "0 #ecf4fc, stop: 1 #dcecfc);\n"
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
                                                                      "    image: url("
                                                                      "icons/down_arrow_icon.svg); \n"
                                                                      "    width: 16px;\n"
                                                                      "    height: 16px\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QComboBox::down-arrow:disabled {\n"
                                                                      "    image: url("
                                                                      "icons/down_arrow_icon_"
                                                                      "deactivated.svg);\n"
                                                                      "    width: 16px;\n"
                                                                      "    height: 16px\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QComboBox QAbstractItemView {\n"
                                                                      "    selection-background-color: rgb("
                                                                      "200,200,200);\n"
                                                                      "    selection-color: black;\n"
                                                                      "    background: #f0f0f0;\n"
                                                                      "    border: 0px solid #f0f0f0;\n"
                                                                      "}\n"
                                                                      "\n"
                                                                      "QComboBox QAbstractItemView::item {\n"
                                                                      "    margin: 5px 5px 5px 5px;\n"
                                                                      "}")
    self.pw_figureOptions_cb_10[self.figure_option_num].setFrame(False)
    self.pw_figureOptions_cb_10[self.figure_option_num].setObjectName("pw_figureOptions_cb_10_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_cb_10[self.figure_option_num], 0, 10, 1, 1)
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                      QSizePolicy.Minimum), 0, 11, 1, 1)
    self.pw_figureOptions_bt_6.append(QtWidgets.QToolButton())
    self.pw_figureOptions_bt_6[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_6[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_6[self.figure_option_num].setStyleSheet("QToolButton {\n"
                                                                     "    border: 1px solid transparent;\n"
                                                                     "    background-color: transparent;\n"
                                                                     "    width: 27px;\n"
                                                                     "    height: 27px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QToolButton:flat {\n"
                                                                     "    border: none;\n"
                                                                     "}")
    self.pw_figureOptions_bt_6[self.figure_option_num].setText("")
    self.pw_figureOptions_bt_6[self.figure_option_num].setIcon(icon)
    self.pw_figureOptions_bt_6[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_figureOptions_bt_6[self.figure_option_num].setAutoRaise(False)
    self.pw_figureOptions_bt_6[self.figure_option_num].setObjectName("pw_figureOptions_bt_6_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_bt_6[self.figure_option_num], 0, 12, 1, 1)
    self.pw_figureOptions_lb_18.append(QtWidgets.QLabel())
    self.pw_figureOptions_lb_18[self.figure_option_num].setMinimumSize(QtCore.QSize(0, 27))
    self.pw_figureOptions_lb_18[self.figure_option_num].setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_figureOptions_lb_18[self.figure_option_num].setFont(font)
    self.pw_figureOptions_lb_18[self.figure_option_num].setText("Display Legend ?")
    self.pw_figureOptions_lb_18[self.figure_option_num].setObjectName("pw_figureOptions_lb_18_"
                                                                      + str(self.figure_option_num))
    self.pw_figureOptions_lb_18[self.figure_option_num].setStyleSheet("QLabel {\n"
                                                                      "    color: rgb(45,45,45);\n"
                                                                      "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_lb_18[self.figure_option_num], 1, 0, 1, 1)
    self.pw_figureOptions_ck_2.append(QtWidgets.QCheckBox())
    self.pw_figureOptions_ck_2[self.figure_option_num].setMinimumSize(QtCore.QSize(25, 20))
    self.pw_figureOptions_ck_2[self.figure_option_num].setMaximumSize(QtCore.QSize(25, 20))
    self.pw_figureOptions_ck_2[self.figure_option_num].setText("")
    self.pw_figureOptions_ck_2[self.figure_option_num].setChecked(True)
    self.pw_figureOptions_ck_2[self.figure_option_num].setObjectName("pw_figureOptions_ck_2_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_ck_2[self.figure_option_num].setStyleSheet("QCheckBox {\n"
                                                                     "    spacing: 5px;\n"
                                                                     "    color: rgb(45,45,45);\n"
                                                                     "}")
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_ck_2[self.figure_option_num], 1, 1, 1, 1)
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                      QSizePolicy.Minimum), 1, 2, 1, 1)
    self.pw_figureOptions_bt_7.append(QtWidgets.QToolButton())
    self.pw_figureOptions_bt_7[self.figure_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_7[self.figure_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_figureOptions_bt_7[self.figure_option_num].setStyleSheet("QToolButton {\n"
                                                                     "    border: 1px solid transparent;\n"
                                                                     "    background-color: transparent;\n"
                                                                     "    width: 27px;\n"
                                                                     "    height: 27px;\n"
                                                                     "}\n"
                                                                     "\n"
                                                                     "QToolButton:flat {\n"
                                                                     "    border: none;\n"
                                                                     "}")
    self.pw_figureOptions_bt_7[self.figure_option_num].setText("")
    self.pw_figureOptions_bt_7[self.figure_option_num].setIcon(icon)
    self.pw_figureOptions_bt_7[self.figure_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_figureOptions_bt_7[self.figure_option_num].setAutoRaise(False)
    self.pw_figureOptions_bt_7[self.figure_option_num].setObjectName("pw_figureOptions_bt_7_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addWidget(self.pw_figureOptions_bt_7[self.figure_option_num], 1, 3, 1, 1)
    self.pw_figureOptions_gl_3[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Minimum), 1, 4, 1, 1)
    self.pw_figureOptions_hl_4[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                      QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_vl_1[self.figure_option_num]. \
        addLayout(self.pw_figureOptions_hl_4[self.figure_option_num])
    self.pw_figureOptions_vl_1[self.figure_option_num]. \
        addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
    self.pw_figureOptions_li_1.append(QtWidgets.QFrame())
    self.pw_figureOptions_li_1[self.figure_option_num].setFrameShape(QtWidgets.QFrame.HLine)
    self.pw_figureOptions_li_1[self.figure_option_num].setFrameShadow(QtWidgets.QFrame.Sunken)
    self.pw_figureOptions_li_1[self.figure_option_num].setStyleSheet("QFrame {\n"
                                                                     "    background: rgb(190,190,190);\n"
                                                                     "    height: 5px;\n"
                                                                     "    border: 0px solid black;\n"
                                                                     "}")
    self.pw_figureOptions_li_1[self.figure_option_num].setObjectName("pw_figureOptions_li_1_"
                                                                     + str(self.figure_option_num))
    self.pw_figureOptions_vl_1[self.figure_option_num].addWidget(self.pw_figureOptions_li_1[self.figure_option_num])
    self.pw_figureOptions_vl_1[self.figure_option_num].addItem(QtWidgets.QSpacerItem(20, 10,
                                                                                     QtWidgets.QSizePolicy.Minimum,
                                                                                     QtWidgets.QSizePolicy.Fixed))
    self.pw_figureOptions_la.addLayout(self.pw_figureOptions_vl_1[self.figure_option_num])
    self.pw_figureOptions_la.setAlignment(QtCore.Qt.AlignTop)
    populate_combobox(self.pw_figureOptions_cb_1[self.figure_option_num], self.font_list, False, self.default_font)
    populate_combobox(self.pw_figureOptions_cb_3[self.figure_option_num], self.font_list, False, self.default_font)
    populate_combobox(self.pw_figureOptions_cb_5[self.figure_option_num], self.font_list, False, self.default_font)
    populate_combobox(self.pw_figureOptions_cb_2[self.figure_option_num], [str(x) for x in range(1, 49, 1)], False, 9)
    populate_combobox(self.pw_figureOptions_cb_4[self.figure_option_num], [str(x) for x in range(1, 49, 1)], False, 9)
    populate_combobox(self.pw_figureOptions_cb_6[self.figure_option_num], [str(x) for x in range(1, 49, 1)], False, 9)
    populate_combobox(self.pw_figureOptions_cb_9[self.figure_option_num], line_style_list(), False, 3)
    populate_combobox(self.pw_figureOptions_cb_10[self.figure_option_num], sorted(list(colors_dict().keys())), False)
    self.pw_figureOptions_ln_10[self.figure_option_num].setText('0.5')
    self.pw_figureOptions_ck_1[self.figure_option_num].stateChanged.connect(lambda: activate_ts_grid_options(self))
    self.pw_figureOptions_bt_1[self.figure_option_num].clicked.connect(self.figure_button_information)
    self.pw_figureOptions_bt_2[self.figure_option_num].clicked.connect(self.figure_button_information)
    self.pw_figureOptions_bt_6[self.figure_option_num].clicked.connect(self.figure_button_information)
    self.pw_figureOptions_bt_7[self.figure_option_num].clicked.connect(self.figure_button_information)
    if self.subplot_ts_fig_list:
        self.pw_figureOptions_ln_2[self.figure_option_num].setText(subplot.axes.xaxis.get_label_text())
        self.pw_figureOptions_ln_2[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_3[self.figure_option_num].setText(subplot.axes.yaxis.get_label_text())
        self.pw_figureOptions_ln_3[self.figure_option_num].setCursorPosition(0)
        xlim_up = subplot.axes.get_xlim()[1]
        xlim_dn = subplot.axes.get_xlim()[0]
        ylim_up = subplot.axes.get_ylim()[1]
        ylim_dn = subplot.axes.get_ylim()[0]
        xstep = subplot.axes.get_xticks()[1] - subplot.axes.get_xticks()[0]
        ystep = subplot.axes.get_yticks()[1] - subplot.axes.get_yticks()[0]
        self.pw_figureOptions_ln_4[self.figure_option_num].setText(str(xlim_dn))
        self.pw_figureOptions_ln_4[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_5[self.figure_option_num].setText(str(xlim_up))
        self.pw_figureOptions_ln_5[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_6[self.figure_option_num].setText(str(xstep))
        self.pw_figureOptions_ln_6[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_7[self.figure_option_num].setText(str(ylim_dn))
        self.pw_figureOptions_ln_7[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_8[self.figure_option_num].setText(str(ylim_up))
        self.pw_figureOptions_ln_8[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_9[self.figure_option_num].setText(str(ystep))
        self.pw_figureOptions_ln_9[self.figure_option_num].setCursorPosition(0)
    else:
        self.pw_figureOptions_ln_2[self.figure_option_num].setText(self.ts_plot.get_xlabel())
        self.pw_figureOptions_ln_2[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_3[self.figure_option_num].setText(self.ts_plot.get_ylabel())
        self.pw_figureOptions_ln_3[self.figure_option_num].setCursorPosition(0)
        xlim_up = self.ts_plot.get_xlim()[1]
        xlim_dn = self.ts_plot.get_xlim()[0]
        ylim_up = self.ts_plot.get_ylim()[1]
        ylim_dn = self.ts_plot.get_ylim()[0]
        xstep = self.ts_plot.get_xticks()[1] - self.ts_plot.get_xticks()[0]
        ystep = self.ts_plot.get_yticks()[1] - self.ts_plot.get_yticks()[0]
        self.pw_figureOptions_ln_4[self.figure_option_num].setText(str(xlim_dn))
        self.pw_figureOptions_ln_4[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_5[self.figure_option_num].setText(str(xlim_up))
        self.pw_figureOptions_ln_5[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_6[self.figure_option_num].setText(str(xstep))
        self.pw_figureOptions_ln_6[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_7[self.figure_option_num].setText(str(ylim_dn))
        self.pw_figureOptions_ln_7[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_8[self.figure_option_num].setText(str(ylim_up))
        self.pw_figureOptions_ln_8[self.figure_option_num].setCursorPosition(0)
        self.pw_figureOptions_ln_9[self.figure_option_num].setText(str(ystep))
        self.pw_figureOptions_ln_9[self.figure_option_num].setCursorPosition(0)
    self.figure_option_num += 1


def add_plot_options(self, plot_options):
    logging.debug('gui - plot_ts_main_functions.py - add_plot_options')
    font3 = font_creation_function('small')
    font2 = font_creation_function('big')
    font = font_creation_function('normal')
    icon = icon_creation_function('info_icon.svg')

    self.pw_plotOptions_vl_1.append(QtWidgets.QVBoxLayout())
    self.pw_plotOptions_vl_1[self.plot_option_num].setObjectName("pw_plotOptions_vl_1_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_1.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_1[self.plot_option_num].setObjectName("pw_plotOptions_hl_1_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_1.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_1[self.plot_option_num].setMinimumSize(QtCore.QSize(700, 27))
    self.pw_plotOptions_lb_1[self.plot_option_num].setMaximumSize(QtCore.QSize(700, 27))
    self.pw_plotOptions_lb_1[self.plot_option_num].setFont(font2)
    if self.subplot_ts_plt_list:
        text = 'Subplot ' + str(self.plot_option_num + 1) + ': Plot options - '
    else:
        text = 'Plot options - '
    self.pw_plotOptions_lb_1[self.plot_option_num].setText(text + plot_options['legend_label'] + ":")
    self.pw_plotOptions_lb_1[self.plot_option_num].setObjectName("pw_plotOptions_lb_1_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_1[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_1[self.plot_option_num].addWidget(self.pw_plotOptions_lb_1[self.plot_option_num])
    self.pw_plotOptions_hl_1[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_1[self.plot_option_num])
    self.pw_plotOptions_hl_2.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_2[self.plot_option_num].setObjectName("pw_plotOptions_hl_2_"
                                                                 + str(self.plot_option_num))
    self.pw_plotOptions_hl_2[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_2.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_2[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_2[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_2[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_2[self.plot_option_num].setText("Line style:")
    self.pw_plotOptions_lb_2[self.plot_option_num].setObjectName("pw_plotOptions_lb_2_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_2[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_2[self.plot_option_num].addWidget(self.pw_plotOptions_lb_2[self.plot_option_num])
    self.pw_plotOptions_hl_3.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_3[self.plot_option_num].setObjectName("pw_plotOptions_hl_3_" + str(self.plot_option_num))
    self.pw_plotOptions_rb_1.append(QtWidgets.QRadioButton())
    self.pw_plotOptions_rb_1[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_rb_1[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_rb_1[self.plot_option_num].setFont(font)
    self.pw_plotOptions_rb_1[self.plot_option_num].setText("Line")
    self.pw_plotOptions_rb_1[self.plot_option_num].setObjectName("pw_plotOptions_rb_1_" + str(self.plot_option_num))
    self.pw_plotOptions_rb_1[self.plot_option_num].setStyleSheet("QRadioButton {\n"
                                                                 "    spacing: 5px;\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_3[self.plot_option_num].addWidget(self.pw_plotOptions_rb_1[self.plot_option_num])
    self.pw_plotOptions_rb_2.append(QtWidgets.QRadioButton())
    self.pw_plotOptions_rb_2[self.plot_option_num].setMinimumSize(QtCore.QSize(90, 27))
    self.pw_plotOptions_rb_2[self.plot_option_num].setMaximumSize(QtCore.QSize(90, 27))
    self.pw_plotOptions_rb_2[self.plot_option_num].setFont(font)
    self.pw_plotOptions_rb_2[self.plot_option_num].setText("Marker")
    self.pw_plotOptions_rb_2[self.plot_option_num].setObjectName("pw_plotOptions_rb_2_" + str(self.plot_option_num))
    self.pw_plotOptions_rb_2[self.plot_option_num].setStyleSheet("QRadioButton {\n"
                                                                 "    spacing: 5px;\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_3[self.plot_option_num].addWidget(self.pw_plotOptions_rb_2[self.plot_option_num])
    self.pw_plotOptions_bg_1.append(QtWidgets.QButtonGroup())
    self.pw_plotOptions_bg_1[self.plot_option_num].setObjectName("pw_plotOptions_bg_1_" + str(self.plot_option_num))
    self.pw_plotOptions_bg_1[self.plot_option_num].addButton(self.pw_plotOptions_rb_1[self.plot_option_num])
    self.pw_plotOptions_bg_1[self.plot_option_num].addButton(self.pw_plotOptions_rb_2[self.plot_option_num])
    self.pw_plotOptions_hl_2[self.plot_option_num].addLayout(self.pw_plotOptions_hl_3[self.plot_option_num])
    self.pw_plotOptions_cb_1.append(QtWidgets.QComboBox())
    self.pw_plotOptions_cb_1[self.plot_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_plotOptions_cb_1[self.plot_option_num].setMinimumSize(QtCore.QSize(180, 27))
    self.pw_plotOptions_cb_1[self.plot_option_num].setMaximumSize(QtCore.QSize(180, 27))
    self.pw_plotOptions_cb_1[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_cb_1[self.plot_option_num].setStyleSheet("QComboBox {\n"
                                                                 "    border: 1px solid #acacac;\n"
                                                                 "    border-radius: 1px;\n"
                                                                 "    padding-left: 5px;\n"
                                                                 "    background-color: qlineargradient("
                                                                 "x1: 0, y1: 0, "
                                                                 "x2: 0, y2: 1, \n"
                                                                 "                                stop: 0 "
                                                                 "#f0f0f0, "
                                                                 "stop: 1 #e5e5e5);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox:disabled {\n"
                                                                 "    background-color: rgb(200,200,200);\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox:hover {\n"
                                                                 "    border: 1px solid #7eb4ea;\n"
                                                                 "    border-radius: 1px;\n"
                                                                 "    background-color: qlineargradient("
                                                                 "x1: 0, y1: 0, "
                                                                 "x2: 0, y2: 1, \n"
                                                                 "                                stop: 0 "
                                                                 "#ecf4fc, "
                                                                 "stop: 1 #dcecfc);\n"
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
                                                                 "    image: url("
                                                                 "icons/down_arrow_icon.svg); \n"
                                                                 "    width: 16px;\n"
                                                                 "    height: 16px\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox QAbstractItemView {\n"
                                                                 "    selection-background-color: rgb("
                                                                 "200,200,200);\n"
                                                                 "    selection-color: black;\n"
                                                                 "    background: #f0f0f0;\n"
                                                                 "    border: 0px solid #f0f0f0;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox QAbstractItemView::item {\n"
                                                                 "    margin: 5px 5px 5px 5px;\n"
                                                                 "}")
    self.pw_plotOptions_cb_1[self.plot_option_num].setObjectName("pw_plotOptions_cb_1_"
                                                                 + str(self.plot_option_num))
    self.pw_plotOptions_hl_2[self.plot_option_num].addWidget(self.pw_plotOptions_cb_1[self.plot_option_num])
    self.pw_plotOptions_hl_2[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_bt_1.append(QtWidgets.QToolButton())
    self.pw_plotOptions_bt_1[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_1[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_1[self.plot_option_num].setStyleSheet("QToolButton {\n"
                                                                 "    border: 1px solid transparent;\n"
                                                                 "    background-color: transparent;\n"
                                                                 "    width: 27px;\n"
                                                                 "    height: 27px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QToolButton:flat {\n"
                                                                 "    border: none;\n"
                                                                 "}")
    self.pw_plotOptions_bt_1[self.plot_option_num].setText("")
    self.pw_plotOptions_bt_1[self.plot_option_num].setIcon(icon)
    self.pw_plotOptions_bt_1[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_plotOptions_bt_1[self.plot_option_num].setAutoRaise(False)
    self.pw_plotOptions_bt_1[self.plot_option_num].setObjectName("pw_plotOptions_bt_1_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_2[self.plot_option_num].addWidget(self.pw_plotOptions_bt_1[self.plot_option_num])
    self.pw_plotOptions_hl_2[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_2[self.plot_option_num])
    self.pw_plotOptions_hl_4.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_4[self.plot_option_num].setObjectName("pw_plotOptions_hl_4_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_4[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_3.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_3[self.plot_option_num].setMinimumSize(QtCore.QSize(200, 27))
    self.pw_plotOptions_lb_3[self.plot_option_num].setMaximumSize(QtCore.QSize(200, 27))
    self.pw_plotOptions_lb_3[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_3[self.plot_option_num].setText("Line / Marker color:")
    self.pw_plotOptions_lb_3[self.plot_option_num].setObjectName("pw_plotOptions_lb_3_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_3[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_4[self.plot_option_num].addWidget(self.pw_plotOptions_lb_3[self.plot_option_num])
    self.pw_plotOptions_cb_2.append(QtWidgets.QComboBox())
    self.pw_plotOptions_cb_2[self.plot_option_num].setItemDelegate(QtWidgets.QStyledItemDelegate())
    self.pw_plotOptions_cb_2[self.plot_option_num].setMinimumSize(QtCore.QSize(170, 27))
    self.pw_plotOptions_cb_2[self.plot_option_num].setMaximumSize(QtCore.QSize(170, 27))
    self.pw_plotOptions_cb_2[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_cb_2[self.plot_option_num].setStyleSheet("QComboBox {\n"
                                                                 "    border: 1px solid #acacac;\n"
                                                                 "    border-radius: 1px;\n"
                                                                 "    padding-left: 5px;\n"
                                                                 "    background-color: qlineargradient("
                                                                 "x1: 0, y1: 0, "
                                                                 "x2: 0, y2: 1, \n"
                                                                 "                                stop: 0 "
                                                                 "#f0f0f0, "
                                                                 "stop: 1 #e5e5e5);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox:disabled {\n"
                                                                 "    background-color: rgb(200,200,200);\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox:hover {\n"
                                                                 "    border: 1px solid #7eb4ea;\n"
                                                                 "    border-radius: 1px;\n"
                                                                 "    background-color: qlineargradient("
                                                                 "x1: 0, y1: 0, "
                                                                 "x2: 0, y2: 1, \n"
                                                                 "                                stop: 0 "
                                                                 "#ecf4fc, "
                                                                 "stop: 1 #dcecfc);\n"
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
                                                                 "    image: url("
                                                                 "icons/down_arrow_icon.svg); \n"
                                                                 "    width: 16px;\n"
                                                                 "    height: 16px\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox QAbstractItemView {\n"
                                                                 "    selection-background-color: rgb("
                                                                 "200,200,200);\n"
                                                                 "    selection-color: black;\n"
                                                                 "    background: #f0f0f0;\n"
                                                                 "    border: 0px solid #f0f0f0;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QComboBox QAbstractItemView::item {\n"
                                                                 "    margin: 5px 5px 5px 5px;\n"
                                                                 "}")
    self.pw_plotOptions_cb_2[self.plot_option_num].setObjectName("pw_plotOptions_cb_2_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_4[self.plot_option_num].addWidget(self.pw_plotOptions_cb_2[self.plot_option_num])
    self.pw_plotOptions_hl_5.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_5[self.plot_option_num].setObjectName("pw_plotOptions_hl_5_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_5[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_8.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_8[self.plot_option_num].setMinimumSize(QtCore.QSize(80, 27))
    self.pw_plotOptions_lb_8[self.plot_option_num].setMaximumSize(QtCore.QSize(80, 27))
    self.pw_plotOptions_lb_8[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_8[self.plot_option_num].setText("RGB code:")
    self.pw_plotOptions_lb_8[self.plot_option_num].setObjectName("pw_plotOptions_lb_8_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_8[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_lb_8[self.plot_option_num].hide()
    self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_lb_8[self.plot_option_num])
    self.pw_plotOptions_ln_3.append(QtWidgets.QLineEdit())
    self.pw_plotOptions_ln_3[self.plot_option_num].setMinimumSize(QtCore.QSize(130, 27))
    self.pw_plotOptions_ln_3[self.plot_option_num].setMaximumSize(QtCore.QSize(130, 27))
    self.pw_plotOptions_ln_3[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_ln_3[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                                                                 "    border-radius: 3px;\n"
                                                                 "    padding: 1px 4px 1px 4px;\n"
                                                                 "    background-color:  rgb(240, 240, "
                                                                 "240);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_ln_3[self.plot_option_num].setObjectName("pw_plotOptions_ln_3_" + str(self.plot_option_num))
    self.pw_plotOptions_ln_3[self.plot_option_num].hide()
    self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_ln_3[self.plot_option_num])
    self.pw_plotOptions_ln_5.append(QtWidgets.QLineEdit())
    self.pw_plotOptions_ln_5[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_5[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_5[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_ln_5[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                                                                 "    border-radius: 3px;\n"
                                                                 "    padding: 1px 4px 1px 4px;\n"
                                                                 "    background-color:  rgb(240, 240, "
                                                                 "240);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_ln_5[self.plot_option_num].setObjectName("pw_plotOptions_ln_5_" + str(self.plot_option_num))
    self.pw_plotOptions_ln_5[self.plot_option_num].hide()
    self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_ln_5[self.plot_option_num])
    self.pw_plotOptions_ln_6.append(QtWidgets.QLineEdit())
    self.pw_plotOptions_ln_6[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_6[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_6[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_ln_6[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                                                                 "    border-radius: 3px;\n"
                                                                 "    padding: 1px 4px 1px 4px;\n"
                                                                 "    background-color:  rgb(240, 240, "
                                                                 "240);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_ln_6[self.plot_option_num].setObjectName("pw_plotOptions_ln_6_" + str(self.plot_option_num))
    self.pw_plotOptions_ln_6[self.plot_option_num].hide()
    self.pw_plotOptions_hl_5[self.plot_option_num].addWidget(self.pw_plotOptions_ln_6[self.plot_option_num])
    self.pw_plotOptions_hl_4[self.plot_option_num].addLayout(self.pw_plotOptions_hl_5[self.plot_option_num])
    self.pw_plotOptions_bt_2.append(QtWidgets.QToolButton())
    self.pw_plotOptions_bt_2[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_2[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_2[self.plot_option_num].setStyleSheet("QToolButton {\n"
                                                                 "    border: 1px solid transparent;\n"
                                                                 "    background-color: transparent;\n"
                                                                 "    width: 27px;\n"
                                                                 "    height: 27px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QToolButton:flat {\n"
                                                                 "    border: none;\n"
                                                                 "}")
    self.pw_plotOptions_bt_2[self.plot_option_num].setText("")
    self.pw_plotOptions_bt_2[self.plot_option_num].setIcon(icon)
    self.pw_plotOptions_bt_2[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_plotOptions_bt_2[self.plot_option_num].setAutoRaise(False)
    self.pw_plotOptions_bt_2[self.plot_option_num].setObjectName("pw_plotOptions_bt_2_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_4[self.plot_option_num].addWidget(self.pw_plotOptions_bt_2[self.plot_option_num])
    self.pw_plotOptions_hl_4[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_4[self.plot_option_num])
    self.pw_plotOptions_hl_6.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_6[self.plot_option_num].setObjectName("pw_plotOptions_hl_6_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_6[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_4.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_4[self.plot_option_num].setMinimumSize(QtCore.QSize(200, 27))
    self.pw_plotOptions_lb_4[self.plot_option_num].setMaximumSize(QtCore.QSize(200, 27))
    self.pw_plotOptions_lb_4[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_4[self.plot_option_num].setText("Line width / Marker size:")
    self.pw_plotOptions_lb_4[self.plot_option_num].setObjectName("pw_plotOptions_lb_4_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_4[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_6[self.plot_option_num].addWidget(self.pw_plotOptions_lb_4[self.plot_option_num])
    self.pw_plotOptions_ln_1.append(QtWidgets.QLineEdit())
    self.pw_plotOptions_ln_1[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_1[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_1[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_ln_1[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                                                                 "    border-radius: 3px;\n"
                                                                 "    padding: 1px 4px 1px 4px;\n"
                                                                 "    background-color:  rgb(240, 240, "
                                                                 "240);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_ln_1[self.plot_option_num].setObjectName("pw_plotOptions_ln_1_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_6[self.plot_option_num].addWidget(self.pw_plotOptions_ln_1[self.plot_option_num])
    self.pw_plotOptions_hl_6[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_bt_3.append(QtWidgets.QToolButton())
    self.pw_plotOptions_bt_3[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_3[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_3[self.plot_option_num].setStyleSheet("QToolButton {\n"
                                                                 "    border: 1px solid transparent;\n"
                                                                 "    background-color: transparent;\n"
                                                                 "    width: 27px;\n"
                                                                 "    height: 27px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QToolButton:flat {\n"
                                                                 "    border: none;\n"
                                                                 "}")
    self.pw_plotOptions_bt_3[self.plot_option_num].setText("")
    self.pw_plotOptions_bt_3[self.plot_option_num].setIcon(icon)
    self.pw_plotOptions_bt_3[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_plotOptions_bt_3[self.plot_option_num].setAutoRaise(False)
    self.pw_plotOptions_bt_3[self.plot_option_num].setObjectName("pw_plotOptions_bt_3_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_6[self.plot_option_num].addWidget(self.pw_plotOptions_bt_3[self.plot_option_num])
    self.pw_plotOptions_hl_6[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_6[self.plot_option_num])
    self.pw_plotOptions_hl_7.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_7[self.plot_option_num].setObjectName("pw_plotOptions_hl_7_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_7[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_5.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_5[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_5[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_5[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_5[self.plot_option_num].setText("Antialiased ?")
    self.pw_plotOptions_lb_5[self.plot_option_num].setObjectName("pw_plotOptions_lb_5_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_5[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_7[self.plot_option_num].addWidget(self.pw_plotOptions_lb_5[self.plot_option_num])
    self.pw_plotOptions_ck_1.append(QtWidgets.QCheckBox())
    self.pw_plotOptions_ck_1[self.plot_option_num].setMinimumSize(QtCore.QSize(25, 20))
    self.pw_plotOptions_ck_1[self.plot_option_num].setMaximumSize(QtCore.QSize(25, 20))
    self.pw_plotOptions_ck_1[self.plot_option_num].setText("")
    self.pw_plotOptions_ck_1[self.plot_option_num].setObjectName("pw_plotOptions_ck_1_" + str(self.plot_option_num))
    self.pw_plotOptions_ck_1[self.plot_option_num].setStyleSheet("QCheckBox {\n"
                                                                 "    spacing: 5px;\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_7[self.plot_option_num].addWidget(self.pw_plotOptions_ck_1[self.plot_option_num])
    self.pw_plotOptions_hl_7[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_bt_4.append(QtWidgets.QToolButton())
    self.pw_plotOptions_bt_4[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_4[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_4[self.plot_option_num].setStyleSheet("QToolButton {\n"
                                                                 "    border: 1px solid transparent;\n"
                                                                 "    background-color: transparent;\n"
                                                                 "    width: 27px;\n"
                                                                 "    height: 27px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QToolButton:flat {\n"
                                                                 "    border: none;\n"
                                                                 "}")
    self.pw_plotOptions_bt_4[self.plot_option_num].setText("")
    self.pw_plotOptions_bt_4[self.plot_option_num].setIcon(icon)
    self.pw_plotOptions_bt_4[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_plotOptions_bt_4[self.plot_option_num].setAutoRaise(False)
    self.pw_plotOptions_bt_4[self.plot_option_num].setObjectName("pw_plotOptions_bt_4_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_7[self.plot_option_num].addWidget(self.pw_plotOptions_bt_4[self.plot_option_num])
    self.pw_plotOptions_hl_7[self.plot_option_num].addItem(QtWidgets.QSpacerItem(18, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_7[self.plot_option_num])
    self.pw_plotOptions_hl_8.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_8[self.plot_option_num].setObjectName("pw_plotOptions_hl_8_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_6.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_6[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_6[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_6[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_6[self.plot_option_num].setText("Opacity ?")
    self.pw_plotOptions_lb_6[self.plot_option_num].setObjectName("pw_plotOptions_lb_6_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_6[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_lb_6[self.plot_option_num])
    self.pw_plotOptions_ck_2.append(QtWidgets.QCheckBox())
    self.pw_plotOptions_ck_2[self.plot_option_num].setMinimumSize(QtCore.QSize(25, 20))
    self.pw_plotOptions_ck_2[self.plot_option_num].setMaximumSize(QtCore.QSize(25, 20))
    self.pw_plotOptions_ck_2[self.plot_option_num].setText("")
    self.pw_plotOptions_ck_2[self.plot_option_num].setObjectName("pw_plotOptions_ck_2_" + str(self.plot_option_num))
    self.pw_plotOptions_ck_2[self.plot_option_num].setStyleSheet("QCheckBox {\n"
                                                                 "    spacing: 5px;\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_ck_2[self.plot_option_num])
    self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_7.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_7[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_7[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_7[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_7[self.plot_option_num].setText("Percentage:")
    self.pw_plotOptions_lb_7[self.plot_option_num].setObjectName("pw_plotOptions_lb_7_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_7[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "\n"
                                                                 "QLabel:disabled {\n"
                                                                 "    color: rgb(145,145,145);\n"
                                                                 "}")
    self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_lb_7[self.plot_option_num])
    self.pw_plotOptions_ln_2.append(QtWidgets.QLineEdit())
    self.pw_plotOptions_ln_2[self.plot_option_num].setEnabled(False)
    self.pw_plotOptions_ln_2[self.plot_option_num].setMinimumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_2[self.plot_option_num].setMaximumSize(QtCore.QSize(60, 27))
    self.pw_plotOptions_ln_2[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_ln_2[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                                                                 "    border-radius: 3px;\n"
                                                                 "    padding: 1px 4px 1px 4px;\n"
                                                                 "    background-color:  rgb(240, 240, "
                                                                 "240);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QLineEdit:disabled {\n"
                                                                 "    background-color:  rgb(200, 200, 200);\n"
                                                                 "    color: rgb(145,145,145);\n"
                                                                 "}")
    self.pw_plotOptions_ln_2[self.plot_option_num].setObjectName("pw_plotOptions_ln_2_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_ln_2[self.plot_option_num])
    self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_bt_5.append(QtWidgets.QToolButton())
    self.pw_plotOptions_bt_5[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_5[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_5[self.plot_option_num].setStyleSheet("QToolButton {\n"
                                                                 "    border: 1px solid transparent;\n"
                                                                 "    background-color: transparent;\n"
                                                                 "    width: 27px;\n"
                                                                 "    height: 27px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QToolButton:flat {\n"
                                                                 "    border: none;\n"
                                                                 "}")
    self.pw_plotOptions_bt_5[self.plot_option_num].setText("")
    self.pw_plotOptions_bt_5[self.plot_option_num].setIcon(icon)
    self.pw_plotOptions_bt_5[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_plotOptions_bt_5[self.plot_option_num].setAutoRaise(False)
    self.pw_plotOptions_bt_5[self.plot_option_num].setObjectName("pw_plotOptions_bt_5_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_8[self.plot_option_num].addWidget(self.pw_plotOptions_bt_5[self.plot_option_num])
    self.pw_plotOptions_hl_8[self.plot_option_num].addItem(QtWidgets.QSpacerItem(28, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_8[self.plot_option_num])
    self.pw_plotOptions_hl_9.append(QtWidgets.QHBoxLayout())
    self.pw_plotOptions_hl_9[self.plot_option_num].setObjectName("pw_plotOptions_hl_9_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_9[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_lb_9.append(QtWidgets.QLabel())
    self.pw_plotOptions_lb_9[self.plot_option_num].setMinimumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_9[self.plot_option_num].setMaximumSize(QtCore.QSize(100, 27))
    self.pw_plotOptions_lb_9[self.plot_option_num].setFont(font)
    self.pw_plotOptions_lb_9[self.plot_option_num].setText("Legend:")
    self.pw_plotOptions_lb_9[self.plot_option_num].setObjectName("pw_plotOptions_lb_9_" + str(self.plot_option_num))
    self.pw_plotOptions_lb_9[self.plot_option_num].setStyleSheet("QLabel {\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_hl_9[self.plot_option_num].addWidget(self.pw_plotOptions_lb_9[self.plot_option_num])
    self.pw_plotOptions_ln_4.append(QtWidgets.QLineEdit())
    self.pw_plotOptions_ln_4[self.plot_option_num].setMinimumSize(QtCore.QSize(250, 27))
    self.pw_plotOptions_ln_4[self.plot_option_num].setMaximumSize(QtCore.QSize(250, 27))
    self.pw_plotOptions_ln_4[self.plot_option_num].setFont(font3)
    self.pw_plotOptions_ln_4[self.plot_option_num].setStyleSheet("QLineEdit {\n"
                                                                 "    border-radius: 3px;\n"
                                                                 "    padding: 1px 4px 1px 4px;\n"
                                                                 "    background-color:  rgb(240, 240, "
                                                                 "240);\n"
                                                                 "    color: rgb(45,45,45);\n"
                                                                 "}")
    self.pw_plotOptions_ln_4[self.plot_option_num].setObjectName("pw_plotOptions_ln_4_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_9[self.plot_option_num].addWidget(self.pw_plotOptions_ln_4[self.plot_option_num])
    self.pw_plotOptions_hl_9[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_bt_6.append(QtWidgets.QToolButton())
    self.pw_plotOptions_bt_6[self.plot_option_num].setMinimumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_6[self.plot_option_num].setMaximumSize(QtCore.QSize(27, 27))
    self.pw_plotOptions_bt_6[self.plot_option_num].setStyleSheet("QToolButton {\n"
                                                                 "    border: 1px solid transparent;\n"
                                                                 "    background-color: transparent;\n"
                                                                 "    width: 27px;\n"
                                                                 "    height: 27px;\n"
                                                                 "}\n"
                                                                 "\n"
                                                                 "QToolButton:flat {\n"
                                                                 "    border: none;\n"
                                                                 "}")
    self.pw_plotOptions_bt_6[self.plot_option_num].setText("")
    self.pw_plotOptions_bt_6[self.plot_option_num].setIcon(icon)
    self.pw_plotOptions_bt_6[self.plot_option_num].setIconSize(QtCore.QSize(23, 23))
    self.pw_plotOptions_bt_6[self.plot_option_num].setAutoRaise(False)
    self.pw_plotOptions_bt_6[self.plot_option_num].setObjectName("pw_plotOptions_bt_6_" + str(self.plot_option_num))
    self.pw_plotOptions_hl_9[self.plot_option_num].addWidget(self.pw_plotOptions_bt_6[self.plot_option_num])
    self.pw_plotOptions_hl_9[self.plot_option_num].addItem(QtWidgets.QSpacerItem(28, 20,
                                                                                 QtWidgets.QSizePolicy.Expanding,
                                                                                 QtWidgets.QSizePolicy.Minimum))
    self.pw_plotOptions_vl_1[self.plot_option_num].addLayout(self.pw_plotOptions_hl_9[self.plot_option_num])
    self.pw_plotOptions_vl_1[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum,
                                                                                 QtWidgets.QSizePolicy.Fixed))
    self.pw_plotOptions_li_1.append(QtWidgets.QFrame())
    self.pw_plotOptions_li_1[self.plot_option_num].setFrameShape(QtWidgets.QFrame.HLine)
    self.pw_plotOptions_li_1[self.plot_option_num].setFrameShadow(QtWidgets.QFrame.Sunken)
    self.pw_plotOptions_li_1[self.plot_option_num].setStyleSheet("QFrame {\n"
                                                                 "    background: rgb(190,190,190);\n"
                                                                 "    height: 5px;\n"
                                                                 "    border: 0px solid black;\n"
                                                                 "}")
    self.pw_plotOptions_li_1[self.plot_option_num].setObjectName("pw_plotOptions_li_1_" + str(self.plot_option_num))
    self.pw_plotOptions_vl_1[self.plot_option_num].addWidget(self.pw_plotOptions_li_1[self.plot_option_num])
    self.pw_plotOptions_vl_1[self.plot_option_num].addItem(QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum,
                                                                                 QtWidgets.QSizePolicy.Fixed))
    self.pw_plotOptions_la.addLayout(self.pw_plotOptions_vl_1[self.plot_option_num])
    self.pw_plotOptions_la.setAlignment(QtCore.Qt.AlignTop)
    self.pw_plotOptions_cb_2[self.plot_option_num].currentIndexChanged.connect(lambda: activate_ts_line_color(self))
    color_list = ['HEX Color', 'RGB Color'] + sorted(list(colors_dict().keys()))
    if plot_options['line_color'] in color_list:
        item = plot_options['line_color']
    else:
        if '#' in plot_options['line_color']:
            item = 'HEX Color'
        else:
            item = 'RGB Color'
    populate_combobox(self.pw_plotOptions_cb_2[self.plot_option_num], color_list, False, item)
    self.pw_plotOptions_ln_3[self.plot_option_num].setText(str(plot_options['line_color']))
    self.pw_plotOptions_ck_2[self.plot_option_num].stateChanged.connect(lambda: activate_ts_opacity_options(self))
    self.pw_plotOptions_bg_1[self.plot_option_num].buttonClicked.connect(lambda val: activate_ts_line_style(self, val))
    self.pw_plotOptions_rb_1[self.plot_option_num].click()
    self.pw_plotOptions_ln_1[self.plot_option_num].setText(str(plot_options['line_width']))
    self.pw_plotOptions_ck_1[self.plot_option_num].setChecked(plot_options['line_antialiased'])
    self.pw_plotOptions_ck_2[self.plot_option_num].setChecked(plot_options['line_alpha'])
    self.pw_plotOptions_ln_4[self.plot_option_num].setText(plot_options['legend_label'])
    self.pw_plotOptions_bt_1[self.plot_option_num].clicked.connect(self.figure_button_information)
    self.pw_plotOptions_bt_2[self.plot_option_num].clicked.connect(self.figure_button_information)
    self.pw_plotOptions_bt_3[self.plot_option_num].clicked.connect(self.figure_button_information)
    self.pw_plotOptions_bt_4[self.plot_option_num].clicked.connect(self.figure_button_information)
    self.pw_plotOptions_bt_5[self.plot_option_num].clicked.connect(self.figure_button_information)
    self.pw_plotOptions_bt_6[self.plot_option_num].clicked.connect(self.figure_button_information)
    self.pw_plotOptions_ln_2[self.plot_option_num].setText('100')
    self.pw_plotOptions_lb_7[self.plot_option_num].setEnabled(False)
    self.plot_option_num += 1


def figure_options_sliders(self):
    logging.debug('gui - plot_ts_main_functions.py - figure_options_sliders')
    font3 = font_creation_function('small')
    font2 = font_creation_function('big')
    font = font_creation_function('normal')
    icon = icon_creation_function('info_icon.svg')
    self.pw_commonOptions_hl_1 = QtWidgets.QHBoxLayout()
    self.pw_commonOptions_hl_1.setObjectName("pw_commonOptions_hl_1")
    self.pw_commonOptions_lb_1 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_1.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_1.setFont(font2)
    self.pw_commonOptions_lb_1.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_1.setObjectName("pw_commonOptions_lb_1")
    self.pw_commonOptions_hl_1.addWidget(self.pw_commonOptions_lb_1)
    self.pw_commonOptions_hl_1.addItem(QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding,
                                                             QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_la.addLayout(self.pw_commonOptions_hl_1)
    self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
    self.horizontalLayout_2.setObjectName("horizontalLayout_2")
    self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.gridLayout_3 = QtWidgets.QGridLayout()
    self.gridLayout_3.setObjectName("gridLayout_3")
    self.pw_commonOptions_lb_2 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_2.setMinimumSize(QtCore.QSize(90, 0))
    self.pw_commonOptions_lb_2.setMaximumSize(QtCore.QSize(90, 16777215))
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.pw_commonOptions_lb_2.setFont(font)
    self.pw_commonOptions_lb_2.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_2.setWordWrap(True)
    self.pw_commonOptions_lb_2.setObjectName("pw_commonOptions_lb_2")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_2, 0, 0, 2, 1)
    self.pw_commonOptions_lb_3 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_3.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_3.setFont(font)
    self.pw_commonOptions_lb_3.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_3.setObjectName("pw_commonOptions_lb_3")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_3, 0, 1, 1, 1)
    self.pw_commonOptions_sl_1 = QtWidgets.QSlider()
    self.pw_commonOptions_sl_1.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_1.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_1.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 1px solid #999999;\n"
                                             "    height: 1px;\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
                                             "stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                             "    margin: 2px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                             "    border: 1px solid #5c5c5c;\n"
                                             "    width: 10px;\n"
                                             "    margin: -5px 0;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal:hover {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::add-page:horizontal {\n"
                                             "    background: rgb(200,200,200);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::sub-page:horizontal {\n"
                                             "    background: rgb(0,0,200);\n"
                                             "}")
    self.pw_commonOptions_sl_1.setMinimum(0)
    self.pw_commonOptions_sl_1.setMaximum(40)
    self.pw_commonOptions_sl_1.setSingleStep(1)
    self.pw_commonOptions_sl_1.setPageStep(1)
    self.pw_commonOptions_sl_1.setOrientation(QtCore.Qt.Horizontal)
    self.pw_commonOptions_sl_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_commonOptions_sl_1.setTickInterval(4)
    self.pw_commonOptions_sl_1.setObjectName("pw_commonOptions_sl_1")
    self.gridLayout_3.addWidget(self.pw_commonOptions_sl_1, 0, 2, 1, 1)
    self.pw_commonOptions_lb_5 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_5.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_5.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_5.setFont(font3)
    self.pw_commonOptions_lb_5.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_5.setObjectName("slider_lb_1")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_5, 0, 3, 1, 1)
    self.pw_commonOptions_lb_7 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_7.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_7.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_7.setFont(font)
    self.pw_commonOptions_lb_7.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_7.setObjectName("pw_commonOptions_lb_7")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_7, 0, 4, 1, 1)
    self.pw_commonOptions_sl_2 = QtWidgets.QSlider()
    self.pw_commonOptions_sl_2.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_2.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_2.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 1px solid #999999;\n"
                                             "    height: 1px;\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
                                             "stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                             "    margin: 2px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                             "    border: 1px solid #5c5c5c;\n"
                                             "    width: 10px;\n"
                                             "    margin: -5px 0;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal:hover {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::sub-page:horizontal {\n"
                                             "background: rgb(200,200,200);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::add-page:horizontal {\n"
                                             "background: rgb(0,0,200);\n"
                                             "}")
    self.pw_commonOptions_sl_2.setMinimum(0)
    self.pw_commonOptions_sl_2.setMaximum(40)
    self.pw_commonOptions_sl_2.setSingleStep(1)
    self.pw_commonOptions_sl_2.setPageStep(1)
    self.pw_commonOptions_sl_2.setProperty("value", 0)
    self.pw_commonOptions_sl_2.setSliderPosition(0)
    self.pw_commonOptions_sl_2.setOrientation(QtCore.Qt.Horizontal)
    self.pw_commonOptions_sl_2.setInvertedAppearance(True)
    self.pw_commonOptions_sl_2.setInvertedControls(False)
    self.pw_commonOptions_sl_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_commonOptions_sl_2.setTickInterval(4)
    self.pw_commonOptions_sl_2.setObjectName("pw_commonOptions_sl_2")
    self.gridLayout_3.addWidget(self.pw_commonOptions_sl_2, 0, 5, 1, 1)
    self.pw_commonOptions_lb_9 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_9.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_9.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_9.setFont(font3)
    self.pw_commonOptions_lb_9.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_9.setObjectName("slider_lb_2")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_9, 0, 6, 1, 1)
    self.pw_commonOptions_lb_11 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_11.setMinimumSize(QtCore.QSize(90, 0))
    self.pw_commonOptions_lb_11.setMaximumSize(QtCore.QSize(90, 16777215))
    self.pw_commonOptions_lb_11.setFont(font)
    self.pw_commonOptions_lb_11.setStyleSheet("QLabel {\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}")
    self.pw_commonOptions_lb_11.setWordWrap(True)
    self.pw_commonOptions_lb_11.setObjectName("pw_commonOptions_lb_11")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_11, 0, 7, 2, 1)
    self.pw_commonOptions_lb_14 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_14.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_14.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_14.setFont(font)
    self.pw_commonOptions_lb_14.setStyleSheet("QLabel {\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}")
    self.pw_commonOptions_lb_14.setObjectName("pw_commonOptions_lb_14")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_14, 1, 8, 1, 1)
    self.pw_commonOptions_lb_13 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_13.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_13.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_13.setFont(font)
    self.pw_commonOptions_lb_13.setStyleSheet("QLabel {\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}")
    self.pw_commonOptions_lb_13.setObjectName("pw_commonOptions_lb_13")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_13, 0, 8, 1, 1)
    self.pw_commonOptions_sl_5 = QtWidgets.QSlider()
    self.pw_commonOptions_sl_5.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_5.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_5.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 1px solid #999999;\n"
                                             "    height: 1px;\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
                                             "stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                             "    margin: 2px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                             "    border: 1px solid #5c5c5c;\n"
                                             "    width: 10px;\n"
                                             "    margin: -5px 0;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal:hover {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::add-page:horizontal {\n"
                                             "    background: rgb(200,200,200);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::sub-page:horizontal {\n"
                                             "    background: rgb(0,0,200);\n"
                                             "}")
    self.pw_commonOptions_sl_5.setMinimum(1)
    self.pw_commonOptions_sl_5.setMaximum(100)
    self.pw_commonOptions_sl_5.setSingleStep(1)
    self.pw_commonOptions_sl_5.setPageStep(1)
    self.pw_commonOptions_sl_5.setOrientation(QtCore.Qt.Horizontal)
    self.pw_commonOptions_sl_5.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_commonOptions_sl_5.setTickInterval(4)
    self.pw_commonOptions_sl_5.setObjectName("pw_commonOptions_sl_5")
    self.gridLayout_3.addWidget(self.pw_commonOptions_sl_5, 0, 9, 1, 1)
    self.pw_commonOptions_sl_6 = QtWidgets.QSlider()
    self.pw_commonOptions_sl_6.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_6.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_6.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 1px solid #999999;\n"
                                             "    height: 1px;\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
                                             "stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                             "    margin: 2px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                             "    border: 1px solid #5c5c5c;\n"
                                             "    width: 10px;\n"
                                             "    margin: -5px 0;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal:hover {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::add-page:horizontal {\n"
                                             "    background: rgb(200,200,200);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::sub-page:horizontal {\n"
                                             "    background: rgb(0,0,200);\n"
                                             "}")
    self.pw_commonOptions_sl_6.setMinimum(0)
    self.pw_commonOptions_sl_6.setMaximum(100)
    self.pw_commonOptions_sl_6.setSingleStep(1)
    self.pw_commonOptions_sl_6.setPageStep(1)
    self.pw_commonOptions_sl_6.setOrientation(QtCore.Qt.Horizontal)
    self.pw_commonOptions_sl_6.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_commonOptions_sl_6.setTickInterval(4)
    self.pw_commonOptions_sl_6.setObjectName("pw_commonOptions_sl_6")
    self.gridLayout_3.addWidget(self.pw_commonOptions_sl_6, 1, 9, 1, 1)
    self.pw_commonOptions_lb_12 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_12.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_12.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_12.setFont(font3)
    self.pw_commonOptions_lb_12.setStyleSheet("QLabel {\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}")
    self.pw_commonOptions_lb_12.setObjectName("slider_lb_5")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_12, 0, 10, 1, 1)
    self.pw_commonOptions_lb_15 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_15.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_15.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_15.setFont(font)
    self.pw_commonOptions_lb_15.setStyleSheet("QLabel {\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}")
    self.pw_commonOptions_lb_15.setObjectName("slider_lb_6")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_15, 1, 10, 1, 1)
    self.pw_commonOptions_lb_4 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_4.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_4.setFont(font)
    self.pw_commonOptions_lb_4.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_4.setObjectName("pw_commonOptions_lb_4")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_4, 1, 1, 1, 1)
    self.pw_commonOptions_sl_3 = QtWidgets.QSlider()
    self.pw_commonOptions_sl_3.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_3.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_3.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 1px solid #999999;\n"
                                             "    height: 1px;\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
                                             "stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                             "    margin: 2px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                             "    border: 1px solid #5c5c5c;\n"
                                             "    width: 10px;\n"
                                             "    margin: -5px 0;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal:hover {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::add-page:horizontal {\n"
                                             "    background: rgb(200,200,200);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::sub-page:horizontal {\n"
                                             "    background: rgb(0,0,200);\n"
                                             "}")
    self.pw_commonOptions_sl_3.setMinimum(0)
    self.pw_commonOptions_sl_3.setMaximum(40)
    self.pw_commonOptions_sl_3.setSingleStep(1)
    self.pw_commonOptions_sl_3.setPageStep(1)
    self.pw_commonOptions_sl_3.setOrientation(QtCore.Qt.Horizontal)
    self.pw_commonOptions_sl_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_commonOptions_sl_3.setTickInterval(4)
    self.pw_commonOptions_sl_3.setObjectName("pw_commonOptions_sl_3")
    self.gridLayout_3.addWidget(self.pw_commonOptions_sl_3, 1, 2, 1, 1)
    self.pw_commonOptions_lb_6 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_6.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_6.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_6.setFont(font3)
    self.pw_commonOptions_lb_6.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_6.setObjectName("slider_lb_3")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_6, 1, 3, 1, 1)
    self.pw_commonOptions_lb_8 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_8.setMinimumSize(QtCore.QSize(0, 27))
    self.pw_commonOptions_lb_8.setMaximumSize(QtCore.QSize(16777215, 27))
    self.pw_commonOptions_lb_8.setFont(font)
    self.pw_commonOptions_lb_8.setStyleSheet("QLabel {\n"
                                             "    color: rgb(45,45,45);\n"
                                             "}")
    self.pw_commonOptions_lb_8.setObjectName("pw_commonOptions_lb_8")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_8, 1, 4, 1, 1)
    self.pw_commonOptions_sl_4 = QtWidgets.QSlider()
    self.pw_commonOptions_sl_4.setMinimumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_4.setMaximumSize(QtCore.QSize(180, 27))
    self.pw_commonOptions_sl_4.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 1px solid #999999;\n"
                                             "    height: 1px;\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
                                             "stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                             "    margin: 2px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
                                             "    border: 1px solid #5c5c5c;\n"
                                             "    width: 10px;\n"
                                             "    margin: -5px 0;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal:hover {\n"
                                             "    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                                             "stop:0 #c7c7c7, stop:1 #a7a7a7);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::sub-page:horizontal {\n"
                                             "background: rgb(200,200,200);\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::add-page:horizontal {\n"
                                             "background: rgb(0,0,200);\n"
                                             "}")
    self.pw_commonOptions_sl_4.setMinimum(0)
    self.pw_commonOptions_sl_4.setMaximum(40)
    self.pw_commonOptions_sl_4.setSingleStep(1)
    self.pw_commonOptions_sl_4.setPageStep(1)
    self.pw_commonOptions_sl_4.setProperty("value", 0)
    self.pw_commonOptions_sl_4.setOrientation(QtCore.Qt.Horizontal)
    self.pw_commonOptions_sl_4.setInvertedAppearance(True)
    self.pw_commonOptions_sl_4.setInvertedControls(False)
    self.pw_commonOptions_sl_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
    self.pw_commonOptions_sl_4.setTickInterval(4)
    self.pw_commonOptions_sl_4.setObjectName("pw_commonOptions_sl_4")
    self.gridLayout_3.addWidget(self.pw_commonOptions_sl_4, 1, 5, 1, 1)
    self.pw_commonOptions_lb_10 = QtWidgets.QLabel()
    self.pw_commonOptions_lb_10.setMinimumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_10.setMaximumSize(QtCore.QSize(50, 27))
    self.pw_commonOptions_lb_10.setFont(font3)
    self.pw_commonOptions_lb_10.setStyleSheet("QLabel {\n"
                                              "    color: rgb(45,45,45);\n"
                                              "}")
    self.pw_commonOptions_lb_10.setObjectName("slider_lb_4")
    self.gridLayout_3.addWidget(self.pw_commonOptions_lb_10, 1, 6, 1, 1)
    self.horizontalLayout_2.addLayout(self.gridLayout_3)
    self.pw_commonOptions_bt_1 = QtWidgets.QToolButton()
    self.pw_commonOptions_bt_1.setMinimumSize(QtCore.QSize(27, 27))
    self.pw_commonOptions_bt_1.setMaximumSize(QtCore.QSize(27, 27))
    self.pw_commonOptions_bt_1.setStyleSheet("QToolButton {\n"
                                             "    border: 1px solid transparent;\n"
                                             "    background-color: transparent;\n"
                                             "    width: 27px;\n"
                                             "    height: 27px;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:flat {\n"
                                             "    border: none;\n"
                                             "}")
    self.pw_commonOptions_bt_1.setIcon(icon)
    self.pw_commonOptions_bt_1.setIconSize(QtCore.QSize(23, 23))
    self.pw_commonOptions_bt_1.setObjectName("pw_commonOptions_bt_1")
    self.horizontalLayout_2.addWidget(self.pw_commonOptions_bt_1)
    self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum))
    self.pw_figureOptions_la.addLayout(self.horizontalLayout_2)
    self.pw_figureOptions_la.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                           QtWidgets.QSizePolicy.Fixed))
    self.line = QtWidgets.QFrame()
    self.line.setStyleSheet("QFrame {\n"
                            "    background: rgb(190,190,190);\n"
                            "    height: 5px;\n"
                            "    border: 0px solid black;\n"
                            "}")
    self.line.setLineWidth(1)
    self.line.setFrameShape(QtWidgets.QFrame.HLine)
    self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line.setObjectName("line")
    self.pw_figureOptions_la.addWidget(self.line)
    self.pw_figureOptions_la.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                           QtWidgets.QSizePolicy.Fixed))
    self.pw_commonOptions_lb_1.setText("Common options:")
    self.pw_commonOptions_lb_2.setText("Set figure margins:")
    self.pw_commonOptions_lb_3.setText("Left:")
    self.pw_commonOptions_lb_5.setText("TMP")
    self.pw_commonOptions_lb_7.setText("Right:")
    self.pw_commonOptions_lb_9.setText("TMP")
    self.pw_commonOptions_lb_11.setText("Set subplot interval:")
    self.pw_commonOptions_lb_12.setText("TMP")
    self.pw_commonOptions_lb_4.setText("Bottom:")
    self.pw_commonOptions_lb_6.setText("TMP")
    self.pw_commonOptions_lb_8.setText("Top:")
    self.pw_commonOptions_lb_10.setText("TMP")
    self.pw_commonOptions_lb_14.setText("Vertical:")
    self.pw_commonOptions_lb_13.setText("Horizontal:")
    self.pw_commonOptions_lb_15.setText("TMP")
    self.pw_commonOptions_sl_1.valueChanged.connect(lambda val: update_ts_slider_value(self, val))
    self.pw_commonOptions_sl_2.valueChanged.connect(lambda val: update_ts_slider_value(self, val))
    self.pw_commonOptions_sl_3.valueChanged.connect(lambda val: update_ts_slider_value(self, val))
    self.pw_commonOptions_sl_4.valueChanged.connect(lambda val: update_ts_slider_value(self, val))
    self.pw_commonOptions_sl_5.valueChanged.connect(lambda val: update_ts_slider_value(self, val))
    self.pw_commonOptions_sl_6.valueChanged.connect(lambda val: update_ts_slider_value(self, val))
    self.pw_commonOptions_bt_1.clicked.connect(self.figure_button_information)
    self.pw_commonOptions_sl_1.setSliderPosition(10)
    self.pw_commonOptions_sl_2.setSliderPosition(5)
    self.pw_commonOptions_sl_3.setSliderPosition(10)
    self.pw_commonOptions_sl_4.setSliderPosition(10)
    self.pw_commonOptions_sl_5.setSliderPosition(40)
    self.pw_commonOptions_sl_6.setSliderPosition(40)
    self.pw_commonOptions_sl_1.setValue(10)
    self.pw_commonOptions_sl_2.setValue(5)
    self.pw_commonOptions_sl_3.setValue(10)
    self.pw_commonOptions_sl_4.setValue(10)
    self.pw_commonOptions_sl_5.setValue(40)
    self.pw_commonOptions_sl_6.setValue(40)
    if not self.subplot_ts_fig_list:
        self.pw_commonOptions_lb_11.setVisible(False)
        self.pw_commonOptions_sl_5.setVisible(False)
        self.pw_commonOptions_lb_12.setVisible(False)
        self.pw_commonOptions_sl_6.setVisible(False)
        self.pw_commonOptions_lb_13.setVisible(False)
        self.pw_commonOptions_lb_14.setVisible(False)
        self.pw_commonOptions_lb_15.setVisible(False)
