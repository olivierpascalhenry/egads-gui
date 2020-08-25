import logging
import numpy
import datetime
import webbrowser
import egads
import textwrap
import platform
import time
import os
import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_displaywindow import Ui_displayWindow
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_addcategorywindow import Ui_Addcategory
from ui.Ui_fillwindow import Ui_fillWindow
from ui.Ui_filenamewindow import Ui_Addfilename
from ui.Ui_unitwindow import Ui_unitWindow
from ui.Ui_waitwindow import Ui_waitWindow
from ui.Ui_downloadwindow import Ui_downloadWindow
from ui.Ui_coefwindow import Ui_coefWindow
from ui.Ui_asksavewindow import Ui_asksaveWindow
from ui.Ui_subplotwindow import Ui_subplotWindow
from ui.Ui_updatewindow import Ui_updateWindow
from ui.Ui_updateavailablewindow import Ui_updateAvailableWindow
from ui.Ui_existingvarwindow import Ui_existingvarWindow
from ui.Ui_projectionwindow import Ui_projectionWindow
from ui.Ui_tickslabelswindow import Ui_tickslabelsWindow
from ui.Ui_tickscolorbarwindow import Ui_tickscolorbarWindow
from ui.Ui_mapextentwindow import Ui_mapextentWindow
from ui.Ui_layerorderwindow import Ui_layerorderWindow
from functions.gui_functions.gui_widgets import QtWaitingSpinner
from functions.utils import font_creation_function, icon_creation_function, stylesheet_creation_function
from functions.thread_functions.update_functions import DownloadFile
from functions.material_functions import grid_projection_option_help


class MyExistingVariable(QtWidgets.QDialog, Ui_existingvarWindow):
    def __init__(self, text):
        logging.debug('gui - other_windows_functions.py - MyExistingVariable - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.label.setText(text)
        self.overwrite = False
        self.overwrite_button.clicked.connect(self.set_overwrite)
        self.cancel_button.clicked.connect(self.close_window)
        logging.info('gui - other_windows_functions.py - MyExistingVariable - ready')

    def set_overwrite(self):
        logging.debug('gui - other_windows_functions.py - MyExistingVariable - set_overwrite')
        self.overwrite = True
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyExistingVariable - close_window')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, url, folder):
        logging.debug('gui - other_windows_functions.py - MyUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.temp_folder = folder
        self.url = url
        if platform.system() == 'Windows':
            self.update_file = self.temp_folder + '\\' + self.url[self.url.rfind('/') + 1:]
        elif platform.system() == 'Linux':
            self.update_file = self.temp_folder + '/' + self.url[self.url.rfind('/') + 1:]
        self.dw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.thread = None
        self.download_update()
        logging.info('gui - other_windows_functions.py - MyUpdate - ready')

    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.dw_progress_bar.setValue(val[0])
            self.dw_label.setText(val[1])
        else:
            self.dw_progress_bar.setValue(val)

    def download_update(self):
        logging.debug('gui - other_windows_functions.py - MyUpdate - download_update')
        self.thread = DownloadFile(self.url, self.update_file)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.close)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()

    def cancel_download(self):
        logging.debug('gui - other_windows_functions.py - MyUpdate - cancel_download')
        if self.thread is not None:
            self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close()

    def download_failed(self):
        logging.debug('gui - other_windows_functions.py - MyUpdate - download_failed')
        self.update_progress_bar(0)
        self.dw_label.setText('Download failed')
        self.cancel_download()

    def closeEvent(self, event):
        logging.info('gui - other_windows_functions.py - MyUpdate - closeEvent')
        if self.cancel:
            try:
                os.remove(self.update_file)
            except PermissionError:
                pass


class MyWarningUpdate(QtWidgets.QDialog, Ui_updateWindow):
    def __init__(self):
        logging.debug('gui - other_windows_functions.py - MyWarningUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.uw_update_button.clicked.connect(self.agree_update)
        self.uw_cancel_button.clicked.connect(self.close_window)
        self.update = False
        logging.info('gui - other_windows_functions.py - MyWarningUpdate - ready')

    def agree_update(self):
        logging.debug('gui - other_windows_functions.py - MyWarningUpdate - agree_update')
        self.update = True
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyWarningUpdate - close_window')
        self.close()


class MySubplot(QtWidgets.QDialog, Ui_subplotWindow):
    def __init__(self, var_list):
        logging.debug('gui - other_windows_functions.py - MyTest - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.var_list = var_list
        self.sw_ok_button.clicked.connect(self.create_layout)
        self.sw_cancel_button.clicked.connect(self.closeWindow)
        self.add_column.clicked.connect(self.add_table_column)
        self.add_row.clicked.connect(self.add_table_row)
        self.subplot_layout = {}
        self.parse_var_list()
        logging.info('gui - other_windows_functions.py - MyTest - ready')

    def parse_var_list(self):
        k = 0
        for i in range(0, 3):
            for j in range(0, 3):
                try:
                    var = ''
                    if len(textwrap.wrap(self.var_list[k], 10)) > 1:
                        for text in textwrap.wrap(self.var_list[k], 10):
                            var += text + '\n'
                        var = var[:-1]
                    else:
                        var = textwrap.wrap(self.var_list[k], 10)[0]
                    self.sw_table.setItem(j, i, QtWidgets.QTableWidgetItem(var))
                except IndexError:
                    self.sw_table.setItem(j, i, QtWidgets.QTableWidgetItem(''))
                k += 1

    def add_table_column(self):
        idx = int(self.sw_table.columnCount())
        self.sw_table.insertColumn(idx)
        for i in range(0, int(self.sw_table.rowCount())):
            self.sw_table.setItem(i, idx, QtWidgets.QTableWidgetItem(''))

    def add_table_row(self):
        idx = int(self.sw_table.rowCount())
        self.sw_table.insertRow(idx)
        for i in range(0, int(self.sw_table.columnCount())):
            self.sw_table.setItem(idx, i, QtWidgets.QTableWidgetItem(''))

    def create_layout(self):
        self.remove_empty_row()
        self.remove_empty_column()
        k = 1
        self.subplot_layout['mpl_nrow'] = int(self.sw_table.rowCount())
        self.subplot_layout['mpl_ncol'] = int(self.sw_table.columnCount())
        for i in range(0, self.sw_table.rowCount()):
            for j in range(0, self.sw_table.columnCount()):
                if self.sw_table.item(i, j).text():
                    self.subplot_layout[str(self.sw_table.item(i, j).text()).replace('\n', '')] = k
                k += 1
        self.close()

    def remove_empty_row(self):
        empty_row = []
        for i in range(0, int(self.sw_table.rowCount())):
            empty = True
            for j in range(0, int(self.sw_table.columnCount())):
                if self.sw_table.item(i, j).text():
                    empty = False
            if empty:
                empty_row.append(i)
        for i in reversed(empty_row):
            self.sw_table.removeRow(i)

    def remove_empty_column(self):
        empty_col = []
        for i in range(0, int(self.sw_table.columnCount())):
            empty = True
            for j in range(0, int(self.sw_table.rowCount())):
                if self.sw_table.item(j, i).text():
                    empty = False
            if empty:
                empty_col.append(i)
        for i in reversed(empty_col):
            self.sw_table.removeColumn(i)

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyInfo - closeWindow')
        self.close()


class MyAsk(QtWidgets.QDialog, Ui_asksaveWindow):
    def __init__(self, text):
        logging.debug('gui - other_windows_functions.py - MyAsk - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.choice = None
        self.cancel_button.clicked.connect(self.cancel_choice)
        self.save_button.clicked.connect(self.save_choice)
        self.close_button.clicked.connect(self.close_choice)
        self.close_button.setText(text + ' without saving')
        logging.info('gui - other_windows_functions.py - MyAsk - ready')

    def save_choice(self):
        logging.info('gui - other_windows_functions.py - MyAsk - save_choice')
        self.choice = 'save'
        self.closeWindow()

    def close_choice(self):
        logging.info('gui - other_windows_functions.py - MyAsk - close_choice')
        self.choice = 'close'
        self.closeWindow()

    def cancel_choice(self):
        logging.info('gui - other_windows_functions.py - MyAsk - cancel_choice')
        self.choice = 'cancel'
        self.closeWindow()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyAsk - closeWindow')
        self.close()


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, info_text):
        logging.debug('gui - other_windows_functions.py - MyInfo - __init__ : infoText ' + str(info_text))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(info_text)
        self.iw_okButton.clicked.connect(self.closeWindow)
        logging.info('gui - other_windows_functions.py - MyInfo - ready')

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyInfo - closeWindow')
        self.close()


class MyDisplay(QtWidgets.QDialog, Ui_displayWindow):
    def __init__(self, var_name, var_units, fill_value, var_values, dimensions):
        logging.debug('gui - other_windows_functions.py - MyDisplay - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fill_value = fill_value
        self.var = var_values
        self.dimensions = dimensions
        self.splitter.setSizes([107, 282])  # 389
        self.dw_line_1.setText(var_name)
        self.dw_line_2.setText(var_units)
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.current_row = 0
        self.current_col = 0
        self.current_lay = 0
        self.lay_count = None
        self.row_count = None
        self.col_count = None
        self.shape_length = len(self.var.shape)
        self.scroll_connect = False
        self.dw_label_4.setVisible(False)
        self.dw_label_5.setText('')
        self.dw_label_5.setVisible(False)
        self.gridLayout_2.removeWidget(self.dw_label_5)
        self.dw_label_5.deleteLater()
        self.dw_label_7.setVisible(False)
        self.dw_label_8.setVisible(False)
        self.horizontalLayout_4 = None
        self.dw_label_6 = None
        self.dw_slider_1 = None
        self.dw_navigate_1 = None
        self.dw_navigate_2 = None
        self.dw_combobox_1 = None
        self.populate_dimensions()
        self.populate_table()
        logging.info('gui - other_windows_functions.py - MyDisplay - ready')

    def populate_dimensions(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - populate_dimensions')
        dimensions_str = ''
        for key, value in self.dimensions.items():
            dimensions_str = dimensions_str + str(value['length']) + ' (' + key + '), '
        self.dw_line_3.setText(dimensions_str[:-2])

    def populate_table(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - populate_table')
        if self.shape_length > 3:
            text = 'It is not possible to display data with more than 3 dimensions.'
            info_window = MyInfo(text)
            info_window.exec_()
        else:
            if self.fill_value is not None:
                try:
                    self.var[self.var == self.fill_value] = numpy.nan
                except ValueError:
                    pass
            self.lay_count, self.row_count, self.col_count = self.populate_headers()
            if self.shape_length == 1:
                for x in range(self.col_count):
                    self.dw_table.setItem(0, x, QtWidgets.QTableWidgetItem(str(self.var[x])))
            elif self.shape_length == 2:
                self.scroll_connect = False
                if self.var.shape[0] > 50:
                    self.row_count = 50
                    self.scroll_connect = True
                if self.var.shape[1] > 50:
                    self.col_count = 50
                    self.scroll_connect = True
                if self.scroll_connect:
                    self.connect_scrollbars()
                for x in range(self.col_count):
                    for y in range(self.row_count):
                        self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[y, x])))
            elif self.shape_length == 3:
                if self.var.shape[1] > 50:
                    self.row_count = 50
                    self.scroll_connect = True
                if self.var.shape[2] > 50:
                    self.col_count = 50
                    self.scroll_connect = True
                if self.scroll_connect:
                    self.connect_scrollbars()
                for x in range(self.col_count):
                    for y in range(self.row_count):
                        self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[0, y, x])))

    def connect_scrollbars(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - connect_scrollbars')
        h_scrollbar = self.dw_table.horizontalScrollBar()
        v_scrollbar = self.dw_table.verticalScrollBar()
        h_scrollbar.valueChanged.connect(lambda val: self.load_more_data(val, col=True))
        v_scrollbar.valueChanged.connect(lambda val: self.load_more_data(val, row=True))
        
    def load_more_data(self, val, row=False, col=False):
        logging.debug('gui - other_windows_functions.py - MyDisplay - load_more_data')
        if row:
            self.current_row = val
        elif col:
            self.current_col = val
        for x in range(self.current_col - 20, self.current_col + 20):
            for y in range(self.current_row - 20, self.current_row + 20):
                try:     
                    if not self.dw_table.item(y, x):
                        if self.shape_length == 2:
                            self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[y, x])))
                        else:
                            self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[self.current_lay, y,
                                                                                                x])))
                except IndexError:
                    pass

    def load_new_layer_data(self):
        self.dw_table.clearContents()
        if self.scroll_connect:
            for x in range(self.current_col - 20, self.current_col + 20):
                for y in range(self.current_row - 20, self.current_row + 20):
                    try:
                        if not self.dw_table.item(y, x):
                            self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[self.current_lay, y,
                                                                                                x])))
                    except IndexError:
                        pass
        else:
            for x in range(self.col_count):
                for y in range(self.row_count):
                    self.dw_table.setItem(y, x, QtWidgets.QTableWidgetItem(str(self.var[self.current_lay, y, x])))

    def populate_headers(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - populate_headers')
        lay_size, row_size, col_size = None, None, None
        if self.shape_length == 1:
            lay_size, col_size, row_size = 1, self.var.shape[0], 1
            self.dw_table.setColumnCount(col_size)
            self.dw_table.setRowCount(row_size) 
            for dim, value in self.dimensions.items():
                self.dw_label_4.setVisible(True)
                if 'time' in dim.lower():
                    self.dw_label_4.setText('Time')
                    units = value['units']
                    if 'since' in units:
                        if 'days' in units or 'day' in units:
                            date = units[units.index('since') + 6:]
                            value['values'] = [str((datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:10]),
                                                                      0, 0) + datetime.timedelta(i - 1)).strftime(
                                "%Y-%m-%d")) for i in value['values']]
                elif dim.lower() in ['longitude', 'lon', 'long']:
                    self.dw_label_4.setText('Longitude')
                elif dim.lower() in ['latitude', 'lat']:
                    self.dw_label_4.setText('Latitude')
                val_list = [str(i) for i in value['values']]
                self.dw_table.setHorizontalHeaderLabels(val_list)
        elif self.shape_length == 2:
            lay_size = 1
            time_in, lon_in, lat_in = False, False, False
            time_name = None
            lon_name = None
            for dim, value in self.dimensions.items():
                if 'time' in dim.lower():
                    time_in = True
                    time_name = dim
                if dim.lower() in ['longitude', 'lon', 'long']:
                    lon_in = True
                    lon_name = dim
            if time_in:
                if self.dimensions[time_name]['axis'] == 0:
                    self.var = numpy.transpose(self.var)
                row_size, col_size = self.var.shape
                self.dw_table.setColumnCount(col_size)
                self.dw_table.setRowCount(row_size)
                val_list = [str(i) for i in self.dimensions[time_name]['values']]
                self.dw_label_4.setVisible(True)
                self.dw_label_4.setText('Time')
                self.dw_table.setHorizontalHeaderLabels(val_list)
                self.dimensions.pop(time_name)
                for key, value in self.dimensions.items():
                    val_list = [str(i) for i in value['values']]
                    self.dw_table.setVerticalHeaderLabels(val_list)
                    self.set_row_label(key.title())
            else:
                if lon_in:
                    if self.dimensions[lon_name]['axis'] == 0:
                        self.var = numpy.transpose(self.var)
                    row_size, col_size = self.var.shape
                    self.dw_table.setColumnCount(col_size)
                    self.dw_table.setRowCount(row_size)
                    val_list = [str(i) for i in self.dimensions[lon_name]['values']]
                    self.dw_label_4.setVisible(True)
                    self.dw_label_4.setText('Longitude')
                    self.dw_table.setHorizontalHeaderLabels(val_list)
                    self.dimensions.pop(lon_name)
                    for key, value in self.dimensions.items():
                        val_list = [str(i) for i in value['values']]
                        self.dw_table.setVerticalHeaderLabels(val_list)
                        self.set_row_label(key.title())
                else:
                    row_size, col_size = self.var.shape
                    self.dw_table.setColumnCount(col_size)
                    self.dw_table.setRowCount(row_size)
        elif self.shape_length == 3:
            time_in, lon_in, lat_in = False, False, False
            dim_list = list(self.dimensions.keys())
            if 'time' in dim_list[0]:
                time_in = True
            if 'longitude' in dim_list[2] or 'long' in dim_list[2] or 'lon' in dim_list[2]:
                lon_in = True
            if 'latitude' in dim_list[1] or 'lati' in dim_list[1] or 'lat' in dim_list[1]:
                lat_in = True
            lay = self.dimensions[dim_list[0]]
            row = self.dimensions[dim_list[1]]
            col = self.dimensions[dim_list[2]]
            lay_size = lay['length']
            row_size = row['length']
            col_size = col['length']
            self.dw_table.setColumnCount(col_size)
            self.dw_table.setRowCount(row_size)
            self.dw_table.setHorizontalHeaderLabels([str(i) for i in col['values']])
            self.dw_table.setVerticalHeaderLabels([str(i) for i in row['values']])
            self.dw_label_4.setVisible(True)
            if lon_in:
                self.dw_label_4.setText('Longitude')
            else:
                self.dw_label_4.setText(dim_list[2])
            if lat_in:
                self.set_row_label('Latitude')
            else:
                self.set_row_label(dim_list[1])
            if time_in:
                self.set_layer_options([str(i) for i in lay['values']], str(lay['values'][0]), lay_size - 1, 'Time:',
                                       'Time:')
            else:
                self.set_layer_options([str(i) for i in lay['values']], str(lay['values'][0]), lay_size - 1)

        return lay_size, row_size, col_size
            
    def set_row_label(self, text):
        logging.debug('gui - other_windows_functions.py - MyDisplay - set_row_label')
        text_str = ''
        for i in text:
            text_str += i + '<br>'
        dw_label_5 = QtWidgets.QLabel()
        dw_label_5.setFont(font_creation_function('small'))
        dw_label_5.setStyleSheet("QLabel {\n"
                                 "    color: rgb(45,45,45);\n"
                                 "    margin-bottom: 5px;\n"
                                 "    margin-right: 10px;\n"
                                 "}")
        dw_label_5.setText(text_str[:-4])
        dw_label_5.setAlignment(QtCore.Qt.AlignCenter)
        dw_label_5.setObjectName("dw_label_5")
        self.gridLayout_2.addWidget(dw_label_5, 1, 0, 1, 1)

    def set_layer_options(self, cb_values, lb8_value, sl_value, lb6_value='Layer:', lb7_value='Layer:'):
        logging.debug('gui - other_windows_functions.py - MyDisplay - set_layer_options')
        font1 = font_creation_function('normal')
        font2 = font_creation_function('small')
        icon1 = icon_creation_function('left_arrow_icon.svg')
        icon2 = icon_creation_function('right_arrow_icon.svg')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dw_label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.dw_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.dw_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.dw_label_6.setFont(font1)
        self.dw_label_6.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.dw_label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dw_label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dw_label_6.setLineWidth(0)
        self.dw_label_6.setMidLineWidth(0)
        self.dw_label_6.setTextFormat(QtCore.Qt.AutoText)
        self.dw_label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.dw_label_6.setWordWrap(False)
        self.dw_label_6.setObjectName("dw_label_6")
        self.horizontalLayout_4.addWidget(self.dw_label_6)
        self.dw_slider_1 = QtWidgets.QSlider(self.layoutWidget1)
        self.dw_slider_1.setMinimumSize(QtCore.QSize(250, 27))
        self.dw_slider_1.setMaximumSize(QtCore.QSize(250, 27))
        self.dw_slider_1.setStyleSheet(stylesheet_creation_function('qslider'))
        self.dw_slider_1.setMinimum(1)
        self.dw_slider_1.setMaximum(100)
        self.dw_slider_1.setSingleStep(1)
        self.dw_slider_1.setPageStep(1)
        self.dw_slider_1.setProperty("value", 1)
        self.dw_slider_1.setSliderPosition(1)
        self.dw_slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.dw_slider_1.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.dw_slider_1.setObjectName("dw_slider_1")
        self.horizontalLayout_4.addWidget(self.dw_slider_1)
        self.dw_navigate_1 = QtWidgets.QToolButton(self.layoutWidget1)
        self.dw_navigate_1.setMaximumSize(QtCore.QSize(23, 23))
        self.dw_navigate_1.setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.dw_navigate_1.setText("")
        self.dw_navigate_1.setIcon(icon1)
        self.dw_navigate_1.setIconSize(QtCore.QSize(19, 19))
        self.dw_navigate_1.setAutoRaise(False)
        self.dw_navigate_1.setObjectName("dw_navigate_1")
        self.horizontalLayout_4.addWidget(self.dw_navigate_1)
        self.dw_navigate_2 = QtWidgets.QToolButton(self.layoutWidget1)
        self.dw_navigate_2.setMaximumSize(QtCore.QSize(23, 23))
        self.dw_navigate_2.setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.dw_navigate_2.setText("")
        self.dw_navigate_2.setIcon(icon2)
        self.dw_navigate_2.setIconSize(QtCore.QSize(19, 19))
        self.dw_navigate_2.setAutoRaise(False)
        self.dw_navigate_2.setObjectName("dw_navigate_2")
        self.horizontalLayout_4.addWidget(self.dw_navigate_2)
        self.horizontalLayout_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                              QtWidgets.QSizePolicy.Minimum))
        self.dw_combobox_1 = QtWidgets.QComboBox(self.layoutWidget1)
        self.dw_combobox_1.setMinimumSize(QtCore.QSize(180, 27))
        self.dw_combobox_1.setMaximumSize(QtCore.QSize(180, 27))
        self.dw_combobox_1.setFont(font2)
        self.dw_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.dw_combobox_1.setFrame(False)
        self.dw_combobox_1.setObjectName("dw_combobox_1")
        self.dw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout_4.addWidget(self.dw_combobox_1)
        self.verticalLayout.insertLayout(1, self.horizontalLayout_4)
        self.dw_combobox_1.addItems(cb_values)
        self.dw_slider_1.setMinimum(0)
        self.dw_slider_1.setMaximum(sl_value)
        self.dw_slider_1.setSingleStep(1)
        self.dw_slider_1.setPageStep(1)
        self.dw_label_7.setVisible(True)
        self.dw_label_8.setVisible(True)
        self.dw_label_6.setText(lb6_value)
        self.dw_label_7.setText(lb7_value)
        self.dw_label_8.setText(lb8_value)
        self.dw_slider_1.valueChanged.connect(self.update_layer)
        self.dw_navigate_1.clicked.connect(self.update_layer)
        self.dw_navigate_2.clicked.connect(self.update_layer)
        self.dw_combobox_1.currentIndexChanged.connect(self.update_layer)

    def update_layer(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - update_layer')
        if self.sender().objectName() == 'dw_slider_1':
            self.dw_combobox_1.currentIndexChanged.disconnect(self.update_layer)
            val = int(self.dw_slider_1.value())
            self.dw_combobox_1.setCurrentIndex(val)
            self.dw_label_8.setText(self.dw_combobox_1.currentText())
            self.current_lay = val
            self.dw_combobox_1.currentIndexChanged.connect(self.update_layer)
        elif self.sender().objectName() == 'dw_navigate_1':
            if self.current_lay > 0:
                self.dw_slider_1.valueChanged.disconnect(self.update_layer)
                self.dw_combobox_1.currentIndexChanged.disconnect(self.update_layer)
                self.current_lay -= 1
                self.dw_combobox_1.setCurrentIndex(self.current_lay)
                self.dw_label_8.setText(self.dw_combobox_1.currentText())
                self.dw_slider_1.setValue(self.current_lay)
                self.dw_slider_1.valueChanged.connect(self.update_layer)
                self.dw_combobox_1.currentIndexChanged.connect(self.update_layer)
        elif self.sender().objectName() == 'dw_navigate_2':
            if self.current_lay < self.dw_combobox_1.count() - 1:
                self.dw_slider_1.valueChanged.disconnect(self.update_layer)
                self.dw_combobox_1.currentIndexChanged.disconnect(self.update_layer)
                self.current_lay += 1
                self.dw_combobox_1.setCurrentIndex(self.current_lay)
                self.dw_label_8.setText(self.dw_combobox_1.currentText())
                self.dw_slider_1.setValue(self.current_lay)
                self.dw_slider_1.valueChanged.connect(self.update_layer)
                self.dw_combobox_1.currentIndexChanged.connect(self.update_layer)
        elif self.sender().objectName() == 'dw_combobox_1':
            self.dw_slider_1.valueChanged.disconnect(self.update_layer)
            val = self.dw_combobox_1.currentIndex()
            self.dw_label_8.setText(self.dw_combobox_1.currentText())
            self.dw_slider_1.setValue(val)
            self.current_lay = val
            self.dw_slider_1.valueChanged.connect(self.update_layer)
        self.load_new_layer_data()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyDisplay - closeWindow')
        self.close()
    
    
class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, text):
        logging.debug('gui - other_windows_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.browser_1.setHtml(text)
        self.button.clicked.connect(self.closeWindow)
        self.splitter.setSizes([170, 130])
        self.read_markdown_file()
        logging.info('gui - other_windows_functions.py - MyAbout - ready')

    def read_markdown_file(self):
        changelog = open('documentation/changelog.txt').read()
        try:
            import markdown
            self.browser_2.setHtml(markdown.markdown(changelog))
        except ImportError:
            self.browser_2.setPlainText(changelog)

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyAbout - closeWindow')
        self.close()


class MyCategory(QtWidgets.QDialog, Ui_Addcategory):
    def __init__(self):
        logging.debug('gui - other_windows_functions.py - MyCategory - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.close_window)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyCategory - ready')

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyCategory - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyCategory - submitBox')
        self.accept()
        
        
class MyFilename(QtWidgets.QDialog, Ui_Addfilename):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        logging.debug('gui - other_windows_functions.py - MyFilename - __init__')
        self.setupUi(self)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyFilename - ready')

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyFilename - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyFilename - submitBox')
        self.accept()


class MyOverwriteFilename(QtWidgets.QDialog, Ui_Addfilename):
    def __init__(self, old_filename, category):
        QtWidgets.QWidget.__init__(self)
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - __init__')
        self.setupUi(self)
        self.old_filename = old_filename
        self.ac_label.setText('A file with the same name already exists in the ' + category + ' folder. You can '
                              + 'overwrite the file, or choose another name.')
        self.ac_submitButton.setText('Overwrite')
        self.ac_line.setText(self.old_filename)
        self.ac_line.textChanged.connect(self.check_filename)
        self.ac_cancelButton.clicked.connect(self.closeWindow)
        self.ac_submitButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyOverwriteFilename - ready')

    def check_filename(self):
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - check_filename')
        new_filename = str(self.ac_line.text())
        if self.old_filename == new_filename or self.old_filename == new_filename + '.py':
            self.ac_submitButton.setText('Overwrite')
        else:
            self.ac_submitButton.setText('Submit')

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyOverwriteFilename - submitBox')
        self.accept()
        
        
class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self):
        logging.debug('gui - other_windows_functions.py - MyFill - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fw_cancelButton.clicked.connect(self.cancel_window)
        self.fw_okButton.clicked.connect(self.closeWindow)
        self.cancel = False
        self.fw_cancelButton.setFocus(True)
        logging.info('gui - other_windows_functions.py - MyFill - ready')

    def cancel_window(self):
        logging.debug('gui - other_windows_functions.py - MyFill - cancel_window')
        self.cancel = True
        self.closeWindow()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyFill - closeWindow')
        self.close()
        
        
class MyUnit(QtWidgets.QDialog, Ui_unitWindow):
    def __init__(self, units_list):
        logging.debug('gui - other_windows_functions.py - MyUnit - __init__ : unit_list ' + str(units_list))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.units_list = units_list
        self.uw_label.setText(self.prepare_text())
        self.uw_cancelButton.clicked.connect(self.closeWindow)
        self.uw_okButton.clicked.connect(self.submitBox)
        logging.info('gui - other_windows_functions.py - MyUnit - ready')
    
    def prepare_text(self):
        logging.debug('gui - other_windows_functions.py - MyUnit - prepare_text')
        if len(self.units_list) > 1:
            text = ('<p>Too handle units properly, EGADS must validate and, probably, rewrite input and out'
                    + 'put units. Please check the <b>proposals</b> made by EGADS, and click Continue if you '
                    + 'agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><ul><li><u>Inputs:</u><ul>')
            for sublist in self.units_list:
                if sublist[3] == 'input':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;' \
                                                                                       '&nbsp;&nbsp;<b>' + sublist[2]\
                            + '</b></li>'
            text += '</ul></li><br><li><u>Outputs:</u><ul>'
            for sublist in self.units_list:
                if sublist[3] == 'output':
                    text += '<li>' + sublist[0] + ':&nbsp;&nbsp;&nbsp;' + sublist[1] + '&nbsp;&nbsp;&nbsp;->&nbsp;' \
                                                                                       '&nbsp;&nbsp;<b>' + sublist[2]\
                            + '</b></li>'
            text += '</ul></li></ul>'
        else:
            text = ('<p>Too handle units properly, EGADS must validate units in the current window. '
                    + 'Please check the <b>proposal</b> made by EGADS, and click Continue if you '
                    + 'are agree with the results. if <i>dimensionless</i> is proposed, then EGADS coul'
                    + 'dn\'t validate the unit. In that case, try to modify it to make it understandable '
                    + 'by EGADS.</p><p><u>Proposal:</u><br>')
            if len(self.units_list[0]) > 2:
                text += ('&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][0] + ':&nbsp;&nbsp;&nbsp;&nbsp;' +
                         self.units_list[0][1] + '&nbsp;&nbsp;&nbsp;&nbsp;->&nbsp;&nbsp;&nbsp;&nbsp;<b>' +
                         self.units_list[0][2] + '</b></p>')
            else:
                text += ('&nbsp;&nbsp;&nbsp;&nbsp;' + self.units_list[0][0] + '&nbsp;&nbsp;&nbsp;&nbsp;-> '
                         + '&nbsp;&nbsp;&nbsp;&nbsp;<b>' + self.units_list[0][1] + '</b></p>')
        return text
    
    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyUnit - closeWindow')
        self.close()

    def submitBox(self):
        logging.debug('gui - other_windows_functions.py - MyUnit - submitBox')
        self.accept()


class MyUpdateAvailable(QtWidgets.QDialog, Ui_updateAvailableWindow):
    def __init__(self, url, gui=False):
        logging.debug('gui - other_windows_functions.py - MyUpdateAvailable - __init__ ')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.url = url
        if not gui:
            self.dw_label_1.setText('A new version of EGADS is available on GitHub. Click on Download update to '
                                    'download it, or click on Visit GitHub to have a look at the EGADS repository on '
                                    'GitHub.')
        self.dw_okButton.clicked.connect(self.closeWindow)
        self.dw_downloadButton.clicked.connect(self.download_file)
        self.dw_downloadButton_2.clicked.connect(self.visit_github)
        logging.info('gui - other_windows_functions.py - MyUpdateAvailable - ready')

    @staticmethod
    def visit_github():
        webbrowser.open('https://github.com/EUFAR/egads-gui/tree/Lineage')

    def download_file(self):
        logging.debug('gui - other_windows_functions.py - MyUpdateAvailable - download_file')
        webbrowser.open(self.url)

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyUpdateAvailable - closeWindow')
        self.close()


class MyWait(QtWidgets.QDialog, Ui_waitWindow):
    def __init__(self, info_text):
        logging.debug('gui - other_windows_functions.py - MyWait - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.label.setText(info_text)
        self.spinner = None
        self.setup_spinner()
        logging.info('gui - other_windows_functions.py - MyWait - ready')
        
    def setup_spinner(self):
        logging.debug('gui - other_windows_functions.py - MyWait - setup_spinner')
        self.spinner = QtWaitingSpinner(self, centerOnParent=False)
        self.verticalLayout.addWidget(self.spinner)
        self.spinner.setRoundness(70.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(12)
        self.spinner.setLineLength(10)
        self.spinner.setLineWidth(5)
        self.spinner.setInnerRadius(10)
        self.spinner.setRevolutionsPerSecond(1)
        self.spinner.setColor(QtGui.QColor(45, 45, 45))
        self.spinner.start()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyWait - closeWindow')
        self.close()


class MyCoeff(QtWidgets.QDialog, Ui_coefWindow):
    def __init__(self, matrix_nbr_str, coefficient_data, variable_list):
        logging.debug('gui - other_windows_functions.py - MyCoeff - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.combobox.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.coefficient_data = coefficient_data
        self.matrix_nbr_str = matrix_nbr_str
        self.variable_list = variable_list
        self.ok_button.setEnabled(False)
        self.ok_button.clicked.connect(self.set_coef)
        self.cancel_button.clicked.connect(self.closeWindow)
        self.combobox.currentTextChanged.connect(self.populate_table)
        self.row = 0
        self.col = 0
        self.coef_array = None
        self.populate_variable_combobox()
        self.set_table()
        self.table.cellChanged.connect(self.activate_ok_button)
        logging.info('gui - other_windows_functions.py - MyCoeff - ready')

    def populate_table(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - populate_table')
        self.table.clear()
        if self.combobox.currentIndex() != 0:
            if isinstance(self.variable_list, str):
                f = egads.input.EgadsNetCdf(self.variable_list, 'r')
                self.parse_data(f.read_variable(str(self.combobox.currentText())).value)
                f.close()
            elif isinstance(self.variable_list, dict):
                self.parse_data(self.variable_list[str(self.combobox.currentText())][3].value)

    def parse_data(self, data):
        logging.debug('gui - other_windows_functions.py - MyCoeff - parse_data')
        try:
            row, col = data.shape
            if row == self.row and col == self.col:
                for i in range(row):
                    for j in range(col):
                        self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i, j])))
        except ValueError:
            var_len = data.shape
            if self.row == 1:
                if var_len == self.col:
                    for i in range(var_len):
                        self.table.setItem(0, i, QtWidgets.QTableWidgetItem(str(data[i])))
            if self.col == 1:
                if var_len == self.row:
                    for i in range(var_len):
                        self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i])))

    def populate_variable_combobox(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - populate_variable_combobox')
        variable_list = []
        if isinstance(self.variable_list, str):
            f = egads.input.EgadsNetCdf(self.variable_list, 'r')
            variable_list = f.get_variable_list()
            f.close()
        elif isinstance(self.variable_list, dict):
            variable_list = sorted(self.variable_list.keys())
        self.combobox.addItem('Make a choice...')
        self.combobox.addItems(sorted(variable_list))

    def set_table(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - set_table')
        self.row = int(self.matrix_nbr_str[0])
        self.col = int(self.matrix_nbr_str[1])
        self.table.setColumnCount(self.col)
        self.table.setRowCount(self.row)
        x = self.table.verticalHeader().size().width()
        for i in range(self.table.columnCount()):
            x += self.table.columnWidth(i)
        y = self.table.horizontalHeader().size().height()
        for i in range(self.table.rowCount()):
            y += self.table.rowHeight(i)
        w, h = self.size().width(), self.size().height()
        if x + 30 > w:
            w = x + 30
        if y + 187 > h:
            h = y + 187
        self.resize(w, h)
        if self.coefficient_data is not None:
            self.parse_data(self.coefficient_data)
            self.activate_ok_button()

    def activate_ok_button(self):
        table_filled = True
        for i in range(0, self.table.rowCount()):
            for j in range(0, self.table.columnCount()):
                if self.table.item(i, j) is not None:
                    if not self.table.item(i, j).text():
                        table_filled = False
                else:
                    table_filled = False
        if table_filled:
            self.ok_button.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)

    def set_coef(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - set_coef')
        self.coef_array = numpy.zeros((self.table.rowCount(), self.table.columnCount()))
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.coef_array[i, j] = float(self.table.item(i, j).text())
        self.close()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyCoeff - closeWindow')
        self.close()


class MyProjection(QtWidgets.QDialog, Ui_projectionWindow):
    def __init__(self, option_dict, projection_name):
        logging.debug('gui - other_windows_functions.py - MyProjection - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.option_dict = option_dict
        self.new_option_dict = copy.deepcopy(self.option_dict)
        self.cancel = True
        self.option_ok.clicked.connect(self.prepare_new_dict)
        self.option_cancel.clicked.connect(self.closeWindow)
        self.setWindowTitle('Projection: ' + projection_name)
        self.label_list, self.line_list, self.button_list = [], [], []
        self.parse_option_dict()
        logging.info('gui - other_windows_functions.py - MyProjection - ready')

    def parse_option_dict(self):
        logging.debug('gui - other_windows_functions.py - MyProjection - parse_option_dict')
        option_nbr = 0
        non_options = ['default_ticks', 'default_extent', 'central_longitude_extent', 'zonal_label_display',
                       'zlb_defaults']
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setObjectName('grid_layout')
        self.option_layout.addLayout(grid_layout)
        self.option_layout.setAlignment(QtCore.Qt.AlignTop)
        for option in sorted(self.option_dict):
            if option not in non_options:
                self.label_list.append(QtWidgets.QLabel())
                self.label_list[option_nbr].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop |
                                                         QtCore.Qt.AlignTrailing)
                self.label_list[option_nbr].setMinimumSize(QtCore.QSize(0, 27))
                self.label_list[option_nbr].setMaximumSize(QtCore.QSize(16777215, 27))
                self.label_list[option_nbr].setFont(font_creation_function('normal'))
                self.label_list[option_nbr].setText(option + ':')
                self.label_list[option_nbr].setStyleSheet("QLabel {\n"
                                                          "    color: rgb(45,45,45);\n"
                                                          "}")
                self.label_list[option_nbr].setObjectName(option + '_lb')
                grid_layout.addWidget(self.label_list[option_nbr], option_nbr, 0, 1, 1)
                self.line_list.append(QtWidgets.QLineEdit())
                self.line_list[option_nbr].setMinimumSize(QtCore.QSize(100, 27))
                self.line_list[option_nbr].setMaximumSize(QtCore.QSize(16777215, 27))
                self.line_list[option_nbr].setFont(font_creation_function('small'))
                self.line_list[option_nbr].setText(str(self.option_dict[option]))
                self.line_list[option_nbr].setStyleSheet("QLineEdit {\n"
                                                         "    border-radius: 3px;\n"
                                                         "    padding: 1px 4px 1px 4px;\n"
                                                         "    background-color:  rgb(240, 240, 240);\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QLineEdit:disabled {\n"
                                                         "    background-color:  rgb(200,200,200);\n"
                                                         "    color: rgb(45,45,45);\n"
                                                         "}")
                self.line_list[option_nbr].setObjectName(option + '_ln')
                grid_layout.addWidget(self.line_list[option_nbr], option_nbr, 1, 1, 1)
                if option == 'globe':
                    self.line_list[option_nbr].setEnabled(False)
                self.button_list.append(QtWidgets.QToolButton())
                self.button_list[option_nbr].setMinimumSize(QtCore.QSize(27, 27))
                self.button_list[option_nbr].setMaximumSize(QtCore.QSize(27, 27))
                self.button_list[option_nbr].setStyleSheet("QToolButton {\n"
                                                           "    border: 1px solid transparent;\n"
                                                           "    background-color: transparent;\n"
                                                           "    width: 27px;\n"
                                                           "    height: 27px;\n"
                                                           "}\n"
                                                           "\n"
                                                           "QToolButton:flat {\n"
                                                           "    border: none;\n"
                                                           "}")
                self.button_list[option_nbr].setIcon(icon_creation_function('info_icon.svg'))
                self.button_list[option_nbr].setIconSize(QtCore.QSize(23, 23))
                self.button_list[option_nbr].setObjectName(option + '_bt')
                grid_layout.addWidget(self.button_list[option_nbr], option_nbr, 2, 1, 1)
                self.button_list[option_nbr].clicked.connect(self.option_information)
                option_nbr += 1

    def prepare_new_dict(self):
        logging.debug('gui - other_windows_functions.py - MyProjection - prepare_new_dict')
        for i, widget in enumerate(self.label_list):
            option = str(widget.text())[:-1]
            if str(self.option_dict[option]) != str(self.line_list[i].text()):
                value = str(self.line_list[i].text())
                try:
                    if value == 'None':
                        value = None
                    elif '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                    self.new_option_dict[option] = value
                except ValueError:
                    text = ('The option <i>' + option + '</i> can\'t be understand by Cartopy. Please correct it. ' 
                            '<br><br>For your information, most options require numbers and not text.')
                    info_window = MyInfo(text)
                    info_window.exec_()
                    return
        self.cancel = False
        self.closeWindow()

    def option_information(self):
        logging.debug('gui - other_windows_functions.py - MyProjection - option_information')
        text = grid_projection_option_help()[self.sender().objectName()[:-3]]
        info_window = MyInfo(text)
        info_window.exec_()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyProjection - closeWindow')
        if self.cancel:
            self.new_option_dict = None
        self.close()


class MyTicks(QtWidgets.QDialog, Ui_tickslabelsWindow):
    def __init__(self, option_dict, default_tick_dict):
        logging.debug('gui - other_windows_functions.py - MyTicks - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.option_dict = option_dict
        self.default_tick_dict = default_tick_dict
        self.new_option_dict = copy.deepcopy(self.option_dict)
        self.cancel = True
        self.ok_button.clicked.connect(self.prepare_new_dict)
        self.cancel_button.clicked.connect(self.close)
        self.info_button.clicked.connect(self.display_information)
        self.default_button.clicked.connect(self.set_default_values)
        self.x_add_button.clicked.connect(self.add_col)
        self.y_add_button.clicked.connect(self.add_col)
        self.x_del_button.clicked.connect(self.remove_col)
        self.y_del_button.clicked.connect(self.remove_col)
        self.parse_option_dict()
        logging.info('gui - other_windows_functions.py - MyTicks - ready')

    def set_default_values(self):
        self.new_option_dict['xticks'] = self.default_tick_dict['xticks']
        self.new_option_dict['yticks'] = self.default_tick_dict['xticks']
        self.cancel = False
        self.close()

    def parse_option_dict(self):
        logging.debug('gui - other_windows_functions.py - MyTicks - parse_option_dict')
        x_ticks = self.option_dict['xticks']
        y_ticks = self.option_dict['yticks']
        self.x_table.setColumnCount(len(x_ticks))
        self.y_table.setColumnCount(len(y_ticks))
        for i, tick in enumerate(x_ticks):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(tick))
            self.x_table.setItem(0, i, item)
        for i, tick in enumerate(y_ticks):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(tick))
            self.y_table.setItem(0, i, item)

    def add_col(self):
        logging.debug('gui - other_windows_functions.py - MyTicks - add_col')
        x_y = self.sender().objectName()[:1]
        if x_y == 'x':
            table = self.x_table
        else:
            table = self.y_table
        cells = table.selectedItems()
        if cells:
            table.insertColumn(table.indexFromItem(cells[0]).column() + 1)
        else:
            table.insertColumn(table.columnCount())

    def remove_col(self):
        logging.debug('gui - other_windows_functions.py - MyTicks - remove_col')
        x_y = self.sender().objectName()[:1]
        if x_y == 'x':
            table = self.x_table
        else:
            table = self.y_table
        cells = table.selectedItems()
        if cells:
            table.removeColumn(table.indexFromItem(cells[0]).column())
        else:
            table.removeColumn(table.columnCount() - 1)

    def prepare_new_dict(self):
        logging.debug('gui - other_windows_functions.py - MyTicks - prepare_new_dict')
        x_list, y_list = [], []
        if self.x_table.columnCount() == 0 or self.y_table.columnCount() == 0:
            text = 'Ticks for one or both axis can\'t be empty. Please make a correction.'
            info_window = MyInfo(text)
            info_window.exec_()
            return
        for i in range(self.x_table.columnCount()):
            try:
                x_list.append(float(self.x_table.item(0, i).text()))
            except ValueError:
                text = ('One or more values for the X axis can\'t be understand by Cartopy. Please correct them.'
                        + '<br><br>For your information, Cartopy requires numbers, floats or integers, for ticks, not'
                        + 'text.')
                info_window = MyInfo(text)
                info_window.exec_()
                return
        for i in range(self.y_table.columnCount()):
            try:
                y_list.append(float(self.y_table.item(0, i).text()))
            except ValueError:
                text = ('One or more values for the Y axis can\'t be understand by Cartopy. Please correct them.'
                        + '<br><br>For your information, Cartopy requires numbers, floats or integers, for ticks, not'
                        + 'text.')
                info_window = MyInfo(text)
                info_window.exec_()
                return
        if x_list and y_list:
            self.new_option_dict['xticks'] = x_list
            self.new_option_dict['yticks'] = y_list
            self.cancel = False
            self.close()

    @staticmethod
    def display_information():
        text = ('From this window, ticks and labels can be modified.<br><br>Buttons \'+\' and \'x\' control the cell '
                'addition and deletion. If no cell is selected, the \'+\' button will add a cell at the end of the '
                'row, and the \'x\' button will delete the last cell ; if a cell is selected, the \'+\' button will '
                'add a cell after the selected one, and the \'x\' button will delete the selected cell.<br><br>To '
                'validate an input, the \'ENTER\' key must be hit or another cell must be selected.<br><br> To '
                'deselect a cell, click on it with the \'CTRL\' key pressed.')
        info_window = MyInfo(text)
        info_window.exec_()

    def closeEvent(self, event):
        logging.debug('gui - other_windows_functions.py - MyTicks - closeEvent')
        if self.cancel:
            self.new_option_dict = None
        self.close()


class MyExtent(QtWidgets.QDialog, Ui_mapextentWindow):
    def __init__(self, option_dict, default_extent_dict):
        logging.debug('gui - other_windows_functions.py - MyExtent - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.option_dict = option_dict
        self.default_extent_dict = default_extent_dict
        self.new_option_dict = copy.deepcopy(self.option_dict)
        self.cancel = True
        self.ok_button.clicked.connect(self.prepare_new_dict)
        self.default_button.clicked.connect(self.set_default_values)
        self.cancel_button.clicked.connect(self.close)
        self.parse_option_dict()
        logging.info('gui - other_windows_functions.py - MyExtent - ready')

    def set_default_values(self):
        self.new_option_dict['ymax'] = self.default_extent_dict['ymax']
        self.new_option_dict['ymin'] = self.default_extent_dict['ymin']
        self.new_option_dict['xmax'] = self.default_extent_dict['xmax']
        self.new_option_dict['xmin'] = self.default_extent_dict['xmin']
        self.new_option_dict['central_longitude_extent'] = self.default_extent_dict['central_longitude_extent']
        self.cancel = False
        self.close()

    def parse_option_dict(self):
        logging.debug('gui - other_windows_functions.py - MyExtent - prepare_new_dict')
        self.y_max_edit.setText(str(self.option_dict['ymax']))
        self.y_min_edit.setText(str(self.option_dict['ymin']))
        self.x_max_edit.setText(str(self.option_dict['xmax']))
        self.x_min_edit.setText(str(self.option_dict['xmin']))
        if self.option_dict['central_longitude_extent'] is not None:
            self.x_relative_ck.setChecked(self.option_dict['central_longitude_extent'])
        else:
            self.x_relative_ck.setEnabled(False)

    def prepare_new_dict(self):
        logging.debug('gui - other_windows_functions.py - MyExtent - prepare_new_dict')
        error = False
        y_max, y_min, x_max, x_min = None, None, None, None
        if (self.y_max_edit.text() != 'None' or self.x_max_edit.text() != 'None' or self.y_min_edit.text() != 'None'
                or self.x_min_edit.text() != 'None'):
            try:
                y_max = float(self.y_max_edit.text())
            except ValueError:
                error = True
            try:
                y_min = float(self.y_min_edit.text())
            except ValueError:
                error = True
            try:
                x_max = float(self.x_max_edit.text())
            except ValueError:
                error = True
            try:
                x_min = float(self.x_min_edit.text())
            except ValueError:
                error = True
        if error:
            text = ('One or more values can\'t be understand by Cartopy. Please correct them.'
                    + '<br><br>For your information, Cartopy requires numbers, floats or integers, for extent, not'
                    + 'text.')
            info_window = MyInfo(text)
            info_window.exec_()
            return
        else:
            self.new_option_dict['ymax'] = y_max
            self.new_option_dict['ymin'] = y_min
            self.new_option_dict['xmax'] = x_max
            self.new_option_dict['xmin'] = x_min

            if self.x_relative_ck.isEnabled():
                self.new_option_dict['central_longitude_extent'] = self.x_relative_ck.isChecked()

            self.cancel = False
            self.close()

    def closeEvent(self, event):
        logging.debug('gui - other_windows_functions.py - MyExtent - closeEvent')
        if self.cancel:
            self.new_option_dict = None
        self.close()


class MyColorbarTicks(QtWidgets.QDialog, Ui_tickscolorbarWindow):
    def __init__(self, option_dict):
        logging.debug('gui - other_windows_functions.py - MyColorbarTicks - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.option_dict = option_dict
        self.new_option_dict = copy.deepcopy(option_dict)
        self.cancel = True
        self.ok_button.clicked.connect(self.prepare_new_dict)
        self.cancel_button.clicked.connect(self.close)
        self.info_button.clicked.connect(self.display_information)
        self.add_button.clicked.connect(self.add_col)
        self.del_button.clicked.connect(self.remove_col)
        self.parse_option_dict()
        logging.info('gui - other_windows_functions.py - MyColorbarTicks - ready')

    def parse_option_dict(self):
        logging.debug('gui - other_windows_functions.py - MyColorbarTicks - parse_option_dict')
        if self.option_dict:
            self.table.setColumnCount(len(self.option_dict))
            for i, tick in enumerate(self.option_dict):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(tick))
                self.table.setItem(0, i, item)

    def add_col(self):
        logging.debug('gui - other_windows_functions.py - MyColorbarTicks - add_col')
        cells = self.table.selectedItems()
        if cells:
            self.table.insertColumn(self.table.indexFromItem(cells[0]).column() + 1)
        else:
            self.table.insertColumn(self.table.columnCount())

    def remove_col(self):
        logging.debug('gui - other_windows_functions.py - MyColorbarTicks - remove_col')
        cells = self.table.selectedItems()
        if cells:
            self.table.removeColumn(self.table.indexFromItem(cells[0]).column())
        else:
            self.table.removeColumn(self.table.columnCount() - 1)

    def prepare_new_dict(self):
        logging.debug('gui - other_windows_functions.py - MyColorbarTicks - prepare_new_dict')
        tick_list = []
        if self.table.columnCount() == 0:
            text = 'Ticks for the colorbar can\'t be empty. Please make a correction.'
            info_window = MyInfo(text)
            info_window.exec_()
            return
        for i in range(self.table.columnCount()):
            try:
                tick_list.append(float(self.table.item(0, i).text()))
            except ValueError:
                text = ('One or more values can\'t be understand by Cartopy. Please correct them.'
                        + '<br><br>For your information, Cartopy requires numbers, floats or integers, for ticks, not'
                        + 'text.')
                info_window = MyInfo(text)
                info_window.exec_()
                return
        if tick_list:
            self.new_option_dict = tick_list
            self.cancel = False
            self.close()

    @staticmethod
    def display_information():
        text = ('From this window, colorbar ticks can be modified.<br><br>Buttons \'+\' and \'x\' control '
                'the cell '
                'addition and deletion. If no cell is selected, the \'+\' button will add a cell at the end of the '
                'row, and the \'x\' button will delete the last cell ; if a cell is selected, the \'+\' button will '
                'add a cell after the selected one, and the \'x\' button will delete the selected cell.<br><br>To '
                'validate an input, the \'ENTER\' key must be hit or another cell must be selected.<br><br> To '
                'deselect a cell, click on it with the \'CTRL\' key pressed.')
        info_window = MyInfo(text)
        info_window.exec_()

    def closeEvent(self, event):
        logging.debug('gui - other_windows_functions.py - MyColorbarTicks - closeEvent')
        if self.cancel:
            self.new_option_dict = None
        self.close()


class MyLayer(QtWidgets.QDialog, Ui_layerorderWindow):
    def __init__(self, option_dict):
        logging.debug('gui - other_windows_functions.py - MyLayer - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.option_dict = option_dict
        self.new_option_dict = copy.deepcopy(self.option_dict)
        self.cancel = True
        self.ok_button.clicked.connect(self.prepare_new_dict)
        self.cancel_button.clicked.connect(self.close)
        self.parse_option_dict()
        logging.info('gui - other_windows_functions.py - MyLayer - ready')

    def parse_option_dict(self):
        logging.debug('gui - other_windows_functions.py - MyLayer - prepare_new_dict')
        self.layer_list.clear()
        for text in [k for k, _ in reversed(sorted(self.option_dict.items(), key=lambda item: item[1]))]:
            widget = QtWidgets.QListWidgetItem()
            widget.setText(text)
            widget.setTextAlignment(QtCore.Qt.AlignCenter)
            self.layer_list.addItem(widget)

    def prepare_new_dict(self):
        logging.debug('gui - other_windows_functions.py - MyLayer - prepare_new_dict')
        for j, layer in enumerate(reversed([self.layer_list.item(i).text() for i in range(self.layer_list.count())])):
            self.new_option_dict[layer] = j
        self.cancel = False
        self.close()

    def closeEvent(self, event):
        logging.debug('gui - other_windows_functions.py - MyLayer - closeEvent')
        if self.cancel:
            self.new_option_dict = None
        self.close()
