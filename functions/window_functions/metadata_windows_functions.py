import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_globalattributewindow import Ui_globalAttributeWindow
from ui.Ui_naglobalattributewindow import Ui_naglobalAttributeWindow
from ui.Ui_variableattributewindow import Ui_variableAttributeWindow
from ui.Ui_navariableattributewindow import Ui_naVariableAttributeWindow
from ui.Ui_groupattributewindow import Ui_groupAttributeWindow
from functions.utils import clear_layout, font_creation_function, icon_creation_function, stylesheet_creation_function
from functions.window_functions.other_windows_functions import MyExistingVariable


class MyNAGlobalAttributes(QtWidgets.QDialog, Ui_naglobalAttributeWindow):
    def __init__(self, global_attributes, open_file_ext):
        logging.debug('gui - metadata_windows_functions.py - MyNAGlobalAttributes - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.splitter.setSizes([177, 400])
        self.global_attributes = global_attributes
        self.open_file_ext = open_file_ext
        self.gw_showButton.clicked.connect(self.other_attribute)
        self.gw_okButton.clicked.connect(self.close_window_save)
        self.gw_cancelButton.clicked.connect(self.close_window)
        self.list_label = []
        self.list_line = []
        self.list_del = []
        self.attribute_num = 0
        self.na_metadata_not_for_user = ['NLHEAD', 'FFI', 'IVOL', 'NVOL', 'DX', 'NIV', 'NV', 'VSCAL', 'VMISS', 'VNAME',
                                         'NSCOML' 'NNCOML', 'ORG', 'SNAME', 'MNAME']
        self.populate_attribute_nasaames()
        logging.info('gui - metadata_windows_functions.py - MyNAGlobalAttributes - ready')

    def populate_attribute_nasaames(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAGlobalAttributes - populate_attribute_nasaames')
        try:
            self.gw_conventions_ln.setText('NASA Ames')
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAGlobalAttributes - populate_attribute_nasaames : '
                          'no Conventions key')
            pass
        try:
            self.gw_title_lb.setText('title - MNAME:')
            self.gw_title_ln.setText(self.global_attributes["MNAME"])
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAGlobalAttributes - populate_attribute_nasaames : '
                          'no title key')
            pass
        try:
            self.gw_institution_lb.setText('institution - ORG:')
            self.gw_institution_ln.setText(self.global_attributes["ORG"])
            self.gw_institution_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAGlobalAttributes - populate_attribute_nasaames : '
                          'no institution key')
            pass
        try:
            self.gw_source_lb.setText('source - SNAME:')
            self.gw_source_ln.setText(self.global_attributes["SNAME"])
            self.gw_source_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAGlobalAttributes - populate_attribute_nasaames : '
                          'no source key')
            pass

    def other_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAGlobalAttributes - other_attribute')
        if self.gw_showButton.text() == "Show other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            font1 = font_creation_function('normal')
            font2 = font_creation_function('small')
            for key, value in sorted(self.global_attributes.items()):
                if key not in self.na_metadata_not_for_user:
                    self.list_label.append(QtWidgets.QLabel())
                    self.list_label[self.attribute_num].setFont(font1)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                    self.list_label[self.attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                    self.other_attributes_layout.addWidget(self.list_label[self.attribute_num], self.attribute_num,
                                                           0, 1, 1)
                    if key == "SCOM" or key == "NCOM":
                        self.list_line.append(QtWidgets.QPlainTextEdit())
                        self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 100))
                        self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 100))
                        self.list_line[self.attribute_num].setFrameShape(QtWidgets.QFrame.NoFrame)
                        self.list_line[self.attribute_num].setPlainText(str(value))
                        self.list_line[self.attribute_num].setStyleSheet(stylesheet_creation_function('qplaintextedit'))
                    else:
                        self.list_line.append(QtWidgets.QLineEdit())
                        self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                        self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                        self.list_line[self.attribute_num].setFrame(False)
                        self.list_line[self.attribute_num].setText(str(value))
                        self.list_line[self.attribute_num].setCursorPosition(0)
                        self.list_line[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setFont(font2)
                    self.other_attributes_layout.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1,
                                                           1, 1)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    if self.attribute_num > 0:
                        self.setTabOrder(self.list_line[self.attribute_num - 1], self.list_line[self.attribute_num])
                    self.attribute_num += 1
            if self.attribute_num != 0:
                self.gw_showButton.setText("Hide other attributes")
            else:
                self.gw_showButton.setText("Hide other attributes")
                label = QtWidgets.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                label.setStyleSheet(stylesheet_creation_function('qlabel'))
                self.other_attributes_layout.addWidget(label, 0, 0, 1, 1)
            self.other_attributes_layout.setAlignment(QtCore.Qt.AlignTop)
        elif self.gw_showButton.text() == "Hide other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            clear_layout(self.other_attributes_layout)
            self.gw_showButton.setText("Show other attributes")

    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAGlobalAttributes - close_window_save')
        self.global_attributes["MNAME"] = str(self.gw_title_ln.text())
        self.global_attributes["ORG"] = str(self.gw_institution_ln.text())
        self.global_attributes["SNAME"] = str(self.gw_source_ln.text())
        for index, widget in enumerate(self.list_label):
            if widget is not None:
                try:
                    if isinstance(self.list_line[index], QtWidgets.QPlainTextEdit):
                        self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].toPlainText())
                    else:
                        self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                except ValueError:
                    if isinstance(self.list_line[index], QtWidgets.QPlainTextEdit):
                        self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].toPlainText())
                    else:
                        self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
        self.close()

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAGlobalAttributes - close_window')
        self.global_attributes = None
        self.close()


class MyGlobalAttributes(QtWidgets.QDialog, Ui_globalAttributeWindow):
    def __init__(self, global_attributes, open_file_ext):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.splitter.setSizes([170, 200, 125])
        self.gw_addAttribute_rl.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.global_attributes = global_attributes
        self.open_file_ext = open_file_ext
        self.gw_showButton.clicked.connect(self.other_attribute)
        self.gw_okButton.clicked.connect(self.close_window_save)
        self.gw_cancelButton.clicked.connect(self.close_window)
        self.gw_button_1.clicked.connect(self.add_attribute)
        self.populate_attribute_netcdf()
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.list_label = []
        self.list_line = []
        self.list_del = []
        self.add_attribute_num = 0
        self.attribute_num = 0
        self.deleted_attributes = []
        self.combobox_items = ["comment", "date_created", "geospatial_lat_min", "geospatial_lat_max",
                               "geospatial_lon_min", "geospatial_lon_max", "geospatial_vertical_min",
                               "geospatial_vertical_max", "geospatial_vertical_positive", "geospatial_vertical_units",
                               "history", "project", "references", "time_coverage_start", "time_coverage_end",
                               "time_coverage_duration"]
        self.populate_combobox()
        logging.info('gui - metadata_windows_functions.py - MyGlobalAttributes - ready')

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - close_window')
        self.global_attributes = None
        self.close()
        
    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - close_window_save')
        overwrite = False
        new_attr_list = [str(widget.text()) for widget in self.add_list_label if widget is not None]
        filtered_list = [string for string in new_attr_list if string in list(self.global_attributes.keys())]
        if filtered_list:
            text = 'The following metadata already exist in the global metadata dictionary:<ul>'
            for attr in filtered_list:
                text += '<li>' + attr + '</li>'
            text += ('</ul>Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on <b>Cancel</b> '
                     'to go back to the Metadata window.')
            existing_window = MyExistingVariable(text)
            existing_window.exec_()
            if not existing_window.overwrite:
                return
            else:
                overwrite = True
        self.global_attributes["Conventions"] = str(self.gw_conventions_ln.text())
        self.global_attributes["title"] = str(self.gw_title_ln.text())
        self.global_attributes["institution"] = str(self.gw_institution_ln.text())
        self.global_attributes["source"] = str(self.gw_source_ln.text())
        for index, widget in enumerate(self.list_label):
            if widget is not None:
                try:
                    if isinstance(self.list_line[index], QtWidgets.QPlainTextEdit):
                        self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].toPlainText())
                    else:
                        self.global_attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                except ValueError:
                    if isinstance(self.list_line[index], QtWidgets.QPlainTextEdit):
                        self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].toPlainText())
                    else:
                        self.global_attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
        if self.deleted_attributes:
            for attr in self.deleted_attributes:
                del self.global_attributes[attr]
        for index, widget in enumerate(self.add_list_label):
            if widget is not None:
                if str(widget.text()) in self.global_attributes:
                    if overwrite:
                        if isinstance(widget, QtWidgets.QLineEdit):
                            key = str(widget.text())
                        else:
                            key = str(widget.text()[:-1])
                        try:
                            self.global_attributes[key] = float(self.add_list_line[index].text())
                        except ValueError:
                            self.global_attributes[key] = str(self.add_list_line[index].text())
                else:
                    if isinstance(widget, QtWidgets.QLineEdit):
                        key = str(widget.text())
                    else:
                        key = str(widget.text()[:-1])
                    try:
                        self.global_attributes[key] = float(self.add_list_line[index].text())
                    except ValueError:
                        self.global_attributes[key] = str(self.add_list_line[index].text())
        self.close()

    def add_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - add_attribute: '
                      + str(self.gw_addAttribute_rl.currentText()))
        selected_attribute = str(self.gw_addAttribute_rl.currentText())
        if selected_attribute != "Make a choice...":
            if selected_attribute not in [str(label.text()[:-1]) for label in self.add_list_label if label is not None]:
                font1 = font_creation_function('normal')
                font2 = font_creation_function('small')
                icon1 = icon_creation_function('del_icon.svg')
                if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                    self.add_list_label.append(QtWidgets.QLineEdit())
                    self.add_list_label[self.add_attribute_num].setFrame(False)
                    self.add_list_label[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                    self.add_list_label[self.add_attribute_num].setFont(font2)
                    if selected_attribute == "long_name_<xx>":
                        self.add_list_label[self.add_attribute_num].setText("long_name_")
                else:
                    self.add_list_label.append(QtWidgets.QLabel())
                    self.add_list_label[self.add_attribute_num].setFont(font1)
                    self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                    self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                    self.add_list_label[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                    self.add_list_label[self.add_attribute_num].setAlignment(QtCore.Qt.AlignRight |
                                                                             QtCore.Qt.AlignTrailing
                                                                             | QtCore.Qt.AlignVCenter)
                self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
                self.add_attribute_layout.addWidget(self.add_list_label[self.add_attribute_num],
                                                    self.add_attribute_num, 0, 1, 1)
                self.add_list_line.append(QtWidgets.QLineEdit())
                self.add_list_line[self.add_attribute_num].setEnabled(True)
                self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_line[self.add_attribute_num].setFrame(False)
                self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
                self.add_list_line[self.add_attribute_num].setFocus(True)
                self.add_list_line[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                self.add_list_line[self.add_attribute_num].setFont(font2)
                self.add_attribute_layout.addWidget(self.add_list_line[self.add_attribute_num],
                                                    self.add_attribute_num, 1, 1, 1)
                self.add_list_del.append(QtWidgets.QToolButton())
                self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setText("")
                self.add_list_del[self.add_attribute_num].setIcon(icon1)
                self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
                self.add_list_del[self.add_attribute_num].setAutoRaise(True)
                self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
                self.add_list_del[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                self.add_attribute_layout.addWidget(self.add_list_del[self.add_attribute_num],
                                                    self.add_attribute_num, 2, 1, 1)
                self.add_attribute_layout.setAlignment(QtCore.Qt.AlignTop)
                self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
                self.add_attribute_num += 1
    
    def populate_attribute_netcdf(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf')
        try:
            self.gw_conventions_ln.setText(self.global_attributes["Conventions"])
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'Conventions key')
            pass
        try:
            self.gw_title_ln.setText(self.global_attributes["title"])
            self.gw_title_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'title key')
            pass
        try:
            self.gw_institution_ln.setText(self.global_attributes["institution"])
            self.gw_institution_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'institution key')
            pass
        try:
            self.gw_source_ln.setText(self.global_attributes["source"])
            self.gw_source_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_attribute_netcdf : no '
                          'source key')
            pass

    def other_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - other_attribute : '
                      'gw_showButton.text() ' + str(self.gw_showButton.text()))
        if self.gw_showButton.text() == "Show other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            font1 = font_creation_function('normal')
            font2 = font_creation_function('small')
            icon1 = icon_creation_function('del_icon.svg')
            for key, value in sorted(self.global_attributes.items()):
                if key != "Conventions" and key != "title" and key != "institution" and key != "source":
                    self.list_label.append(QtWidgets.QLabel()) 
                    self.list_label[self.attribute_num].setFont(font1)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                    self.list_label[self.attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                    self.other_attributes_layout.addWidget(self.list_label[self.attribute_num], self.attribute_num,
                                                           0, 1, 1)
                    self.list_line.append(QtWidgets.QLineEdit())
                    self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_line[self.attribute_num].setFrame(False)
                    self.list_line[self.attribute_num].setText(str(value))
                    self.list_line[self.attribute_num].setCursorPosition(0)
                    self.list_line[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setFont(font2)
                    self.other_attributes_layout.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1,
                                                           1, 1)
                    self.list_del.append(QtWidgets.QToolButton())
                    self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setText("")
                    self.list_del[self.attribute_num].setIcon(icon1)
                    self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
                    self.list_del[self.attribute_num].setAutoRaise(True)
                    self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
                    self.list_del[self.attribute_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                    self.other_attributes_layout.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2,
                                                           1, 1)
                    self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    if self.attribute_num > 0:
                        self.setTabOrder(self.list_line[self.attribute_num - 1], self.list_line[self.attribute_num])
                    self.attribute_num += 1   
            if self.attribute_num != 0:
                self.gw_showButton.setText("Hide other attributes")
            else:
                self.gw_showButton.setText("Hide other attributes")
                label = QtWidgets.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                label.setStyleSheet(stylesheet_creation_function('qlabel'))
                self.other_attributes_layout.addWidget(label, 0, 0, 1, 1)
            self.other_attributes_layout.setAlignment(QtCore.Qt.AlignTop)
        elif self.gw_showButton.text() == "Hide other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            clear_layout(self.other_attributes_layout)
            self.gw_showButton.setText("Show other attributes")

    def delete_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - delete_attribute : sender('
                      ').objectName() ' + str(self.sender().objectName()))
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            self.add_attribute_layout.removeWidget(self.add_list_label[index])
            self.add_attribute_layout.removeWidget(self.add_list_line[index])
            self.add_attribute_layout.removeWidget(self.add_list_del[index])
            self.add_list_label[index].deleteLater()
            self.add_list_label[index] = None
            self.add_list_line[index].deleteLater()
            self.add_list_line[index] = None
            self.add_list_del[index].deleteLater()
            self.add_list_del[index] = None
        else:
            index = int(self.sender().objectName()[9:])
            self.deleted_attributes.append(self.list_label[index].text()[:-1])
            self.list_label[index].deleteLater()
            self.list_label.pop(index)
            self.list_line[index].deleteLater()
            self.list_line.pop(index)
            self.list_del[index].deleteLater()
            self.list_del.pop(index)
            self.attribute_num -= 1
            if len(self.list_del) > 0:
                for i in range(0, len(self.list_del)):
                    self.list_line[i].setObjectName("line_" + str(i))
                    self.list_label[i].setObjectName("label_" + str(i))
                    self.list_del[i].setObjectName("list_del_" + str(i))
            self.populate_combobox()

    def populate_combobox(self):
        logging.debug('gui - metadata_windows_functions.py - MyGlobalAttributes - populate_combobox')
        current_text = ''
        if self.gw_addAttribute_rl.currentText():
            current_text = self.gw_addAttribute_rl.currentText()
        self.gw_addAttribute_rl.clear()
        self.gw_addAttribute_rl.addItem("Make a choice...")
        self.gw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            if item not in self.global_attributes.keys():
                self.gw_addAttribute_rl.addItem(item)
        if current_text:
            self.gw_addAttribute_rl.setCurrentIndex(self.gw_addAttribute_rl.findText(current_text))


class MyVariableAttributes(QtWidgets.QDialog, Ui_variableAttributeWindow):
    def __init__(self, var, variable_attributes):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - __init__ : var ' + str(var))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.splitter.setSizes([110, 190, 124])
        self.vw_addAttribute_rl.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.variable = var
        self.setWindowTitle('Variable attributes - ' + self.variable)
        self.attributes = variable_attributes
        self.vw_showButton.clicked.connect(self.other_attribute)
        self.vw_okButton.clicked.connect(self.close_window_save)
        self.vw_cancelButton.clicked.connect(self.close_window)
        self.vw_button_1.clicked.connect(self.add_attribute)
        self.combobox_items = ["ancillary_variables", "CalibrationCoefficients", "Category", "Comments",
                               "Dependencies", "flag_masks", "flag_meaning", "flag_values", "InstrumentCoordinates",
                               "InstrumentLocation", "long_name", "long_name_<xx>", "Processor", "SampledRate",
                               "standard_name", "valid_max", "valid_min", "valid_range"]
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.list_label = []
        self.list_line = []
        self.list_del = []
        self.attribute_num = 0
        self.add_attribute_num = 0
        self.deleted_attributes = []
        self.populate_attribute()
        self.populate_combobox()
        logging.info('gui - metadata_windows_functions.py - MyVariableAttributes - ready')

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - close_window')
        self.attributes = None
        self.close()

    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - close_window_save')
        new_attr_list = [str(widget.text()) for widget in self.add_list_label if widget is not None]
        filtered_list = [string for string in new_attr_list if string in list(self.attributes.keys())]
        overwrite = False
        if filtered_list:
            text = 'The following metadata already exist in the variable metadata dictionary:<ul>'
            for attr in filtered_list:
                text += '<li>' + attr + '</li>'
            text += ('</ul>Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on <b>Cancel</b> '
                     'to go back to the Metadata window.')
            existing_window = MyExistingVariable(text)
            existing_window.exec_()
            if not existing_window.overwrite:
                return
            else:
                overwrite = True
        try:
            for index, widget in enumerate(self.list_label):
                if widget is not None:
                    try:
                        self.attributes[str(widget.text()[:-1])] = float(self.list_line[index].text())
                    except ValueError:
                        self.attributes[str(widget.text()[:-1])] = str(self.list_line[index].text())
        except AttributeError:
            pass
        if self.deleted_attributes:
            for attr in self.deleted_attributes:
                del self.attributes[attr]
        for index, widget in enumerate(self.add_list_label):
            if widget is not None:
                if str(widget.text()) in self.attributes:
                    if overwrite:
                        if isinstance(widget, QtWidgets.QLineEdit):
                            key = str(widget.text())
                        else:
                            key = str(widget.text()[:-1])
                        try:
                            self.attributes[key] = float(self.add_list_line[index].text())
                        except ValueError:
                            self.attributes[key] = str(self.add_list_line[index].text())
                else:
                    if isinstance(widget, QtWidgets.QLineEdit):
                        key = str(widget.text())
                    else:
                        key = str(widget.text()[:-1])
                    try:
                        self.attributes[key] = float(self.add_list_line[index].text())
                    except ValueError:
                        self.attributes[key] = str(self.add_list_line[index].text())
        self.close()

    def populate_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - populate_attribute')
        try:
            self.vw_units_ln.setText(str(self.attributes["units"]))
            self.vw_units_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyVariableAttributes - populate_attribute :no Units '
                          'attribute')
            pass
        try:
            self.vw_fillValue_ln.setText(str(self.attributes["_FillValue"]))
            self.vw_fillValue_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyVariableAttributes - populate_attribute : no '
                          'FillValue attribute')
            pass

    def other_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - other_attribute : '
                      'vw_showButton.text() ' + str(self.vw_showButton.text()))
        if self.vw_showButton.text() == "Show other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            font1 = font_creation_function('normal')
            font2 = font_creation_function('small')
            icon1 = icon_creation_function('del_icon.svg')
            for key, value in sorted(self.attributes.items()):
                if key != "units" and key != "_FillValue":
                    if isinstance(value, list):
                        value_string = ""
                        for string in value:
                            value_string += string + ", "
                        value = value_string[:-2]
                    self.list_label.append(QtWidgets.QLabel()) 
                    self.list_label[self.attribute_num].setFont(font1)
                    self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
                    self.list_label[self.attribute_num].setText(key + ':')
                    self.list_label[self.attribute_num].setToolTip(key)
                    self.list_label[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                    self.list_label[self.attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                     QtCore.Qt.AlignVCenter)
                    self.other_attributes_layout.addWidget(self.list_label[self.attribute_num], self.attribute_num,
                                                           0, 1, 1)
                    self.list_line.append(QtWidgets.QLineEdit())
                    self.list_line[self.attribute_num].setEnabled(True)
                    self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                    self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                    self.list_line[self.attribute_num].setFrame(False)
                    self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
                    self.list_line[self.attribute_num].setText(str(value))
                    self.list_line[self.attribute_num].setCursorPosition(0)
                    self.list_line[self.attribute_num].setFocus(True)
                    self.list_line[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                    self.list_line[self.attribute_num].setFont(font2)
                    self.other_attributes_layout.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1,
                                                           1, 1)
                    self.list_del.append(QtWidgets.QToolButton())
                    self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                    self.list_del[self.attribute_num].setText("")
                    self.list_del[self.attribute_num].setIcon(icon1)
                    self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
                    self.list_del[self.attribute_num].setAutoRaise(True)
                    self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
                    self.list_del[self.attribute_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                    self.other_attributes_layout.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2,
                                                           1, 1)
                    self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
                    if key == "missing_value":
                        self.list_line[self.attribute_num].setEnabled(False)
                    if self.attribute_num > 0:
                        self.setTabOrder(self.list_line[self.attribute_num - 1], self.list_line[self.attribute_num])
                    self.attribute_num += 1     
            if self.attribute_num != 0:
                self.vw_showButton.setText("Hide other attributes")
            else:
                self.vw_showButton.setText("Hide other attributes")
                label = QtGui.QLabel()
                label.setMinimumSize(QtCore.QSize(200, 27))
                label.setMaximumSize(QtCore.QSize(200, 27))
                label.setObjectName("label")
                label.setText("No more attribute")
                label.setStyleSheet(stylesheet_creation_function('qlabel'))
                self.other_attributes_layout.addWidget(label, 0, 0, 1, 1)
        elif self.vw_showButton.text() == "Hide other attributes":
            self.list_label = []
            self.list_line = []
            self.list_del = []
            self.attribute_num = 0
            clear_layout(self.other_attributes_layout)
            self.vw_showButton.setText("Show other attributes")

    def add_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - add_attribute : vw_addAttribu'
                      + 'te_rl.currentText() ' + str(self.vw_addAttribute_rl.currentText()))
        selected_attribute = self.vw_addAttribute_rl.currentText()
        if selected_attribute != "Make a choice...":
            if selected_attribute not in [str(label.text()[:-1]) for label in self.add_list_label if label is not None]:
                font1 = font_creation_function('normal')
                font2 = font_creation_function('small')
                icon1 = icon_creation_function('del_icon.svg')
                if selected_attribute == "Other..." or selected_attribute == "long_name_<xx>":
                    self.add_list_label.append(QtWidgets.QLineEdit())
                    self.add_list_label[self.add_attribute_num].setFrame(False)
                    self.add_list_label[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                    self.add_list_label[self.add_attribute_num].setFont(font2)
                    if selected_attribute == "long_name_<xx>":
                        self.add_list_label[self.add_attribute_num].setText("long_name_")
                else:
                    self.add_list_label.append(QtWidgets.QLabel())
                    self.add_list_label[self.add_attribute_num].setFont(font1)
                    self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                    self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                    self.add_list_label[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                    self.add_list_label[self.add_attribute_num].setAlignment(QtCore.Qt.AlignRight |
                                                                             QtCore.Qt.AlignTrailing
                                                                             | QtCore.Qt.AlignVCenter)
                self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
                self.add_attribute_layout.addWidget(self.add_list_label[self.add_attribute_num], self.add_attribute_num,
                                                    0, 1, 1)
                self.add_list_line.append(QtWidgets.QLineEdit())
                self.add_list_line[self.add_attribute_num].setEnabled(True)
                self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_line[self.add_attribute_num].setFrame(False)
                self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
                self.add_list_line[self.add_attribute_num].setFocus(True)
                self.add_list_line[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                self.add_list_line[self.add_attribute_num].setFont(font2)
                self.add_attribute_layout.addWidget(self.add_list_line[self.add_attribute_num], self.add_attribute_num,
                                                    1, 1, 1)
                self.add_list_del.append(QtWidgets.QToolButton())
                self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setText("")
                self.add_list_del[self.add_attribute_num].setIcon(icon1)
                self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
                self.add_list_del[self.add_attribute_num].setAutoRaise(True)
                self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
                self.add_list_del[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                self.add_attribute_layout.addWidget(self.add_list_del[self.add_attribute_num],
                                                    self.add_attribute_num, 2, 1, 1)
                self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
                self.add_attribute_num += 1

    def delete_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - delete_attribute : sender('
                      ').objectName() ' + str(self.sender().objectName()))
        if "add" in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            self.add_attribute_layout.removeWidget(self.add_list_label[index])
            self.add_attribute_layout.removeWidget(self.add_list_line[index])
            self.add_attribute_layout.removeWidget(self.add_list_del[index])
            self.add_list_label[index].deleteLater()
            self.add_list_label[index] = None
            self.add_list_line[index].deleteLater()
            self.add_list_line[index] = None
            self.add_list_del[index].deleteLater()
            self.add_list_del[index] = None
        else:
            index = int(self.sender().objectName()[9:])
            self.deleted_attributes.append(self.list_label[index].text()[:-1])
            self.other_attributes_layout.removeWidget(self.list_label[index])
            self.other_attributes_layout.removeWidget(self.list_line[index])
            self.other_attributes_layout.removeWidget(self.list_del[index])
            self.list_label[index].deleteLater()
            self.list_label[index] = None
            self.list_line[index].deleteLater()
            self.list_line[index] = None
            self.list_del[index].deleteLater()
            self.list_del[index] = None
            self.populate_combobox()

    def populate_combobox(self):
        logging.debug('gui - metadata_windows_functions.py - MyVariableAttributes - populate_combobox')
        current_text = ''
        if self.vw_addAttribute_rl.currentText():
            current_text = self.vw_addAttribute_rl.currentText()
        self.vw_addAttribute_rl.clear()
        self.vw_addAttribute_rl.addItem("Make a choice...")
        self.vw_addAttribute_rl.addItem("Other...")
        for item in self.combobox_items:
            if item not in self.attributes.keys():
                self.vw_addAttribute_rl.addItem(item)
        if current_text:
            self.vw_addAttribute_rl.setCurrentIndex(self.vw_addAttribute_rl.findText(current_text))


class MyNAVariableAttributes(QtWidgets.QDialog, Ui_naVariableAttributeWindow):
    def __init__(self, var, variable_attributes):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - __init__ : var ' + str(var))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.variable = var
        self.setWindowTitle('Variable attributes - ' + self.variable)
        self.attributes = variable_attributes
        self.vw_okButton.clicked.connect(self.close_window_save)
        self.vw_cancelButton.clicked.connect(self.close_window)
        self.populate_attribute()
        logging.info('gui - metadata_windows_functions.py - MyNAVariableAttributes - ready')

    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - close_window_save')
        self.attributes['units'] = str(self.vw_units_ln.text())
        self.attributes['_FillValue'] = str(self.vw_fillValue_ln.text())
        self.attributes['scale_factor'] = str(self.vw_scalefactor_ln.text())
        self.close()

    def populate_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute')
        try:
            self.vw_units_ln.setText(str(self.attributes["units"]))
            self.vw_units_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute :no Units '
                          'attribute')
            pass
        try:
            self.vw_fillValue_ln.setText(str(self.attributes["_FillValue"]))
            self.vw_fillValue_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute : no '
                          'FillValue attribute')
            pass
        try:
            self.vw_scalefactor_ln.setText(str(self.attributes["scale_factor"]))
            self.vw_scalefactor_ln.setCursorPosition(0)
        except KeyError:
            logging.error('gui - metadata_windows_functions.py - MyNAVariableAttributes - populate_attribute : no '
                          'scale_factor attribute')
            pass

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyNAVariableAttributes - close_window')
        self.attributes = None
        self.close()


class MyGroupAttributes(QtWidgets.QDialog, Ui_groupAttributeWindow):
    def __init__(self, group, variable_attributes):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - __init__ : group ' + str(group))
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.splitter.setSizes([200, 171])
        self.gw_add_attribute_rl.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.group = group
        self.setWindowTitle('Variable attributes - ' + self.group)
        self.attributes = variable_attributes
        self.vw_save_bt.clicked.connect(self.close_window_save)
        self.vw_cancel_bt.clicked.connect(self.close_window)
        self.gw_add_attribute_bt.clicked.connect(self.add_attribute)
        self.combobox_items = ["author", "category", "comments", "date_created", "dependencies", "history", "institute",
                               "processor", "project"]
        self.add_list_label = []
        self.add_list_line = []
        self.add_list_del = []
        self.list_label = []
        self.list_line = []
        self.list_del = []
        self.attribute_num = 0
        self.add_attribute_num = 0
        self.other_attribute()
        self.populate_combobox()
        logging.info('gui - metadata_windows_functions.py - MyGroupAttributes - ready')

    def close_window(self):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - close_window')
        self.attributes = None
        self.close()

    def close_window_save(self):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - close_window_save')
        for i, widget in enumerate(self.list_label):
            if widget is not None:
                if self.list_line[i].text():
                    self.attributes[widget.text()[:-1]] = str(self.list_line[i].text())
        for i, widget in enumerate(self.add_list_label):
            if widget is not None:
                if isinstance(widget, QtWidgets.QLineEdit):
                    if widget.text() and self.add_list_line[i].text():
                        self.attributes[widget.text()] = str(self.add_list_line[i].text())
                else:
                    if self.add_list_line[i].text():
                        self.attributes[widget.text()[:-1]] = str(self.add_list_line[i].text())
        self.close()

    def populate_combobox(self):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - populate_combobox')
        current_text = ''
        if self.gw_add_attribute_rl.currentText():
            current_text = self.gw_add_attribute_rl.currentText()
        self.gw_add_attribute_rl.clear()
        self.gw_add_attribute_rl.addItem("Make a choice...")
        self.gw_add_attribute_rl.addItem("Other...")
        for item in self.combobox_items:
            if item not in self.attributes.keys():
                self.gw_add_attribute_rl.addItem(item)
        if current_text:
            self.gw_add_attribute_rl.setCurrentIndex(self.gw_add_attribute_rl.findText(current_text))

    def add_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - add_attribute : '
                      'vw_gw_add_attribute_rl.currentText() ' + str(self.gw_add_attribute_rl.currentText()))
        selected_attribute = self.gw_add_attribute_rl.currentText()
        if selected_attribute != "Make a choice...":
            if selected_attribute not in [str(label.text()[:-1]) for label in self.add_list_label if label is not None]:
                font1 = font_creation_function('normal')
                font2 = font_creation_function('small')
                icon1 = icon_creation_function('del_icon.svg')
                if selected_attribute == "Other...":
                    self.add_list_label.append(QtWidgets.QLineEdit())
                    self.add_list_label[self.add_attribute_num].setFrame(False)
                    self.add_list_label[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                    self.add_list_label[self.add_attribute_num].setFont(font2)
                else:
                    self.add_list_label.append(QtWidgets.QLabel())
                    self.add_list_label[self.add_attribute_num].setFont(font1)
                    self.add_list_label[self.add_attribute_num].setToolTip(selected_attribute)
                    self.add_list_label[self.add_attribute_num].setText(selected_attribute + ':')
                    self.add_list_label[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                    self.add_list_label[self.add_attribute_num].setAlignment(QtCore.Qt.AlignRight |
                                                                             QtCore.Qt.AlignTrailing
                                                                             | QtCore.Qt.AlignVCenter)
                self.add_list_label[self.add_attribute_num].setMinimumSize(QtCore.QSize(0, 27))
                self.add_list_label[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_label[self.add_attribute_num].setObjectName("add_label_" + str(self.add_attribute_num))
                self.add_attribute_layout.addWidget(self.add_list_label[self.add_attribute_num], self.add_attribute_num,
                                                    0, 1, 1)
                self.add_list_line.append(QtWidgets.QLineEdit())
                self.add_list_line[self.add_attribute_num].setEnabled(True)
                self.add_list_line[self.add_attribute_num].setMinimumSize(QtCore.QSize(400, 27))
                self.add_list_line[self.add_attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.add_list_line[self.add_attribute_num].setFrame(False)
                self.add_list_line[self.add_attribute_num].setObjectName("add_line_" + str(self.add_attribute_num))
                self.add_list_line[self.add_attribute_num].setFocus(True)
                self.add_list_line[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
                self.add_list_line[self.add_attribute_num].setFont(font2)
                self.add_attribute_layout.addWidget(self.add_list_line[self.add_attribute_num], self.add_attribute_num,
                                                    1, 1, 1)
                self.add_list_del.append(QtWidgets.QToolButton())
                self.add_list_del[self.add_attribute_num].setMinimumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setMaximumSize(QtCore.QSize(27, 27))
                self.add_list_del[self.add_attribute_num].setText("")
                self.add_list_del[self.add_attribute_num].setIcon(icon1)
                self.add_list_del[self.add_attribute_num].setIconSize(QtCore.QSize(23, 23))
                self.add_list_del[self.add_attribute_num].setAutoRaise(True)
                self.add_list_del[self.add_attribute_num].setObjectName("add_list_del_" + str(self.add_attribute_num))
                self.add_list_del[self.add_attribute_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                self.add_attribute_layout.addWidget(self.add_list_del[self.add_attribute_num],
                                                    self.add_attribute_num, 2, 1, 1)
                self.add_list_del[self.add_attribute_num].clicked.connect(self.delete_attribute)
                self.add_attribute_num += 1

    def other_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - other_attribute')
        font1 = font_creation_function('normal')
        font2 = font_creation_function('small')
        icon1 = icon_creation_function('del_icon.svg')
        for key, value in sorted(self.attributes.items()):
            self.list_label.append(QtWidgets.QLabel())
            self.list_label[self.attribute_num].setFont(font1)
            self.list_label[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
            self.list_label[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.list_label[self.attribute_num].setObjectName("label_" + str(self.attribute_num))
            self.list_label[self.attribute_num].setText(key + ':')
            self.list_label[self.attribute_num].setToolTip(key)
            self.list_label[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.list_label[self.attribute_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                             QtCore.Qt.AlignVCenter)
            self.other_attributes_layout.addWidget(self.list_label[self.attribute_num], self.attribute_num,
                                                   0, 1, 1)
            self.list_line.append(QtWidgets.QLineEdit())
            self.list_line[self.attribute_num].setMinimumSize(QtCore.QSize(0, 27))
            self.list_line[self.attribute_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.list_line[self.attribute_num].setFrame(False)
            self.list_line[self.attribute_num].setText(str(value))
            self.list_line[self.attribute_num].setCursorPosition(0)
            self.list_line[self.attribute_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.list_line[self.attribute_num].setEnabled(True)
            self.list_line[self.attribute_num].setObjectName("line_" + str(self.attribute_num))
            self.list_line[self.attribute_num].setFocus(True)
            self.list_line[self.attribute_num].setFont(font2)
            self.other_attributes_layout.addWidget(self.list_line[self.attribute_num], self.attribute_num, 1,
                                                   1, 1)
            self.list_del.append(QtWidgets.QToolButton())
            self.list_del[self.attribute_num].setMinimumSize(QtCore.QSize(27, 27))
            self.list_del[self.attribute_num].setMaximumSize(QtCore.QSize(27, 27))
            self.list_del[self.attribute_num].setText("")
            self.list_del[self.attribute_num].setIcon(icon1)
            self.list_del[self.attribute_num].setIconSize(QtCore.QSize(23, 23))
            self.list_del[self.attribute_num].setAutoRaise(True)
            self.list_del[self.attribute_num].setObjectName("list_del_" + str(self.attribute_num))
            self.list_del[self.attribute_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
            self.other_attributes_layout.addWidget(self.list_del[self.attribute_num], self.attribute_num, 2,
                                                   1, 1)

            self.list_del[self.attribute_num].clicked.connect(self.delete_attribute)
            if self.attribute_num > 0:
                self.setTabOrder(self.list_line[self.attribute_num - 1], self.list_line[self.attribute_num])
            self.attribute_num += 1

    def delete_attribute(self):
        logging.debug('gui - metadata_windows_functions.py - MyGroupAttributes - delete_attribute : sender('
                      ').objectName() ' + str(self.sender().objectName()))
        if 'add' in self.sender().objectName():
            index = int(self.sender().objectName()[13:])
            self.add_attribute_layout.removeWidget(self.add_list_label[index])
            self.add_attribute_layout.removeWidget(self.add_list_line[index])
            self.add_attribute_layout.removeWidget(self.add_list_del[index])
            self.add_list_label[index].deleteLater()
            self.add_list_line[index].deleteLater()
            self.add_list_del[index].deleteLater()
            self.add_list_label[index] = None
            self.add_list_line[index] = None
            self.add_list_del[index] = None
        else:
            index = int(self.sender().objectName()[9:])
            del self.attributes[str(self.list_label[index].text()[:-1])]
            self.other_attributes_layout.removeWidget(self.list_label[index])
            self.other_attributes_layout.removeWidget(self.list_line[index])
            self.other_attributes_layout.removeWidget(self.list_del[index])
            self.list_label[index].deleteLater()
            self.list_label[index] = None
            self.list_line[index].deleteLater()
            self.list_line[index] = None
            self.list_del[index].deleteLater()
            self.list_del[index] = None
            self.populate_combobox()
