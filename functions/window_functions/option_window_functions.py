import logging
import egads
import pathlib
import xml
import datetime
import numpy
from PyQt5 import QtCore, QtWidgets
from ui.Ui_optionwindow import Ui_optionWindow
from functions.help_functions import option_information_text
from functions.window_functions.other_windows_functions import MyInfo, MyUpdateAvailable
from functions.thread_functions.update_functions import CheckEGADSGuiUpdateOnline, CheckEGADSUpdateOnline
from functions.utils import add_element, get_element_value, icon_creation_function
from ui._version import _gui_version


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    available_update = QtCore.pyqtSignal(str)

    def __init__(self, config_dict, egads_config_dict, frozen, system, installed, user_path):
        logging.debug('gui - option_window_functions.py - MyOptions - __init__ ')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.egads_config_dict = egads_config_dict
        self.frozen = frozen
        self.system = system
        self.installed = installed
        self.user_path = user_path
        self.ow_splitter.setSizes([130, 570])
        self.information_text = option_information_text()
        self.cancel = True
        self.check_egads_update_thread = None
        self.check_gui_update_thread = None
        self.ow_section_list.setCurrentRow(0)
        self.read_config_dict()
        self.ow_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_2.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_3.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_4.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_5.setAlignment(QtCore.Qt.AlignTop)
        self.ow_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_combobox_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_combobox_7.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_ok_button.clicked.connect(self.save_config_dict)
        self.ow_cancel_button.clicked.connect(self.closeWindow)
        self.ow_section_list.currentRowChanged.connect(self.display_options)
        self.ow_checkbox_2.stateChanged.connect(self.activate_checkbox_3)
        self.ow_checkbox_8.stateChanged.connect(self.activate_folder_registration)
        self.ow_checkbox_9.stateChanged.connect(self.activate_dimension_distribution)
        self.ow_check_button_1.clicked.connect(self.check_gui_update)
        self.ow_check_button_2.clicked.connect(self.check_egads_update)
        self.ow_openButton_1.clicked.connect(self.get_folder_path)
        self.ow_openButton_2.clicked.connect(self.get_folder_path)
        self.ow_openButton_3.clicked.connect(self.get_folder_path)
        self.ow_addButton_1.clicked.connect(self.add_folder_list)
        self.ow_folderList_1.itemSelectionChanged.connect(self.activate_folder_deletion)
        self.bw_del_button.clicked.connect(self.remove_list_folder)
        self.info_button_1.clicked.connect(self.button_info)
        self.info_button_2.clicked.connect(self.button_info)
        self.info_button_3.clicked.connect(self.button_info)
        self.info_button_4.clicked.connect(self.button_info)
        self.info_button_5.clicked.connect(self.button_info)
        self.info_button_6.clicked.connect(self.button_info)
        self.info_button_7.clicked.connect(self.button_info)
        self.info_button_8.clicked.connect(self.button_info)
        self.info_button_9.clicked.connect(self.button_info)
        self.info_button_10.clicked.connect(self.button_info)
        self.info_button_11.clicked.connect(self.button_info)
        self.info_button_13.clicked.connect(self.button_info)
        self.info_button_14.clicked.connect(self.button_info)
        self.info_button_15.clicked.connect(self.button_info)
        self.info_button_16.clicked.connect(self.button_info)
        self.info_button_17.clicked.connect(self.button_info)
        if self.frozen:
            self.ow_checkbox_5.setEnabled(False)
            self.ow_checkbox_5.setVisible(False)
            self.info_button_11.setEnabled(False)
            self.info_button_11.setVisible(False)
            self.ow_check_button_2.setEnabled(False)
            self.ow_check_button_2.setVisible(False)
        try:
            import requests
        except ImportError:
            logging.info('gui - option_window_functions.py - MyOptions - requests is not installed, no update check')
            self.ow_check_button_1.setEnabled(False)
            self.ow_check_button_2.setEnabled(False)
            self.ow_checkbox_4.setEnabled(False)
            self.ow_checkbox_5.setEnabled(False)
            self.ow_checkbox_4.setChecked(False)
            self.ow_checkbox_5.setChecked(False)

        self.ow_checkbox_9.setEnabled(False)  # for now the function has been disabled until a good solution is found

        logging.info('gui - option_window_functions.py - MyOptions - ready ')

    def display_options(self, idx):
        self.ow_stacked_widget.setCurrentIndex(idx)

    def activate_dimension_distribution(self):
        if self.ow_checkbox_9.isChecked():
            self.ow_label_12.setEnabled(True)
            self.ow_label_13.setEnabled(True)
            self.ow_label_14.setEnabled(True)
            self.ow_combobox_5.setEnabled(True)
            self.ow_combobox_6.setEnabled(True)
            self.ow_combobox_7.setEnabled(True)
        else:
            self.ow_label_12.setEnabled(False)
            self.ow_label_13.setEnabled(False)
            self.ow_label_14.setEnabled(False)
            self.ow_combobox_5.setEnabled(False)
            self.ow_combobox_6.setEnabled(False)
            self.ow_combobox_7.setEnabled(False)
            self.ow_combobox_5.setCurrentIndex(0)
            self.ow_combobox_6.setCurrentIndex(0)
            self.ow_combobox_7.setCurrentIndex(0)

    def activate_checkbox_3(self):
        logging.debug('gui - option_window_functions.py - MyOptions - activate_checkbox_4')
        if self.ow_checkbox_2.isChecked():
            self.ow_checkbox_3.setEnabled(True)
        else:
            self.ow_checkbox_3.setChecked(False)
            self.ow_checkbox_3.setEnabled(False)
            self.config_dict.set('SYSTEM', 'switch_fill_value', str(False))

    def activate_folder_registration(self):
        if self.ow_checkbox_8.isChecked():
            self.ow_label_9.setEnabled(True)
            self.ow_label_10.setEnabled(True)
            self.ow_line_3.setEnabled(True)
            self.ow_folderList_1.setEnabled(True)
            self.ow_openButton_3.setEnabled(True)
            self.ow_addButton_1.setEnabled(True)
            self.ow_line_3.setText('')
            self.ow_folderList_1.clear()
        else:
            self.ow_label_9.setEnabled(False)
            self.ow_label_10.setEnabled(False)
            self.ow_line_3.setEnabled(False)
            self.ow_folderList_1.setEnabled(False)
            self.ow_openButton_3.setEnabled(False)
            self.ow_addButton_1.setEnabled(False)
            self.ow_line_3.setText('')
            self.ow_folderList_1.clear()

    def activate_folder_deletion(self):
        if self.ow_folderList_1.selectedItems():
            self.bw_del_button.setEnabled(True)
        else:
            self.bw_del_button.setEnabled(False)

    def add_folder_list(self):
        if self.ow_line_3.text():
            if pathlib.Path(str(self.ow_line_1.text())).exists():
                existing_folder = self.ow_folderList_1.findItems(self.ow_line_3.text(), QtCore.Qt.MatchExactly)
                if not existing_folder:
                    self.ow_folderList_1.addItem(self.ow_line_3.text())

    def remove_list_folder(self):
        item_list = self.ow_folderList_1.selectedItems()
        for item in item_list:
            self.ow_folderList_1.takeItem(self.ow_folderList_1.row(item))

    def read_config_dict(self):
        logging.debug('gui - option_window_functions.py - MyOptions - read_config_dict')
        self.ow_checkbox_1.setChecked(self.config_dict.getboolean('SYSTEM', 'read_as_float'))
        self.ow_checkbox_2.setChecked(self.config_dict.getboolean('SYSTEM', 'replace_fill_value'))
        self.ow_checkbox_3.setChecked(self.config_dict.getboolean('SYSTEM', 'switch_fill_value'))
        self.activate_checkbox_3()
        self.ow_combobox_1.setCurrentIndex(self.ow_combobox_1.findText(self.config_dict.get('LOG', 'level')))
        self.ow_line_1.setText(self.config_dict.get('LOG', 'path'))
        self.ow_combobox_2.setCurrentIndex(self.ow_combobox_1.findText(self.egads_config_dict.get('LOG', 'level')))
        self.ow_line_2.setText(self.egads_config_dict.get('LOG', 'path'))
        self.ow_combobox_3.setCurrentIndex(int(self.config_dict.get('PLOTS', 'same_unit_plot')))
        self.ow_combobox_4.setCurrentIndex(int(self.config_dict.get('PLOTS', 'subplot_disposition')))
        # self.ow_checkbox_6.setChecked(self.config_dict.getboolean('PLOTS', 'x_info_disabled'))
        self.ow_checkbox_4.setChecked(self.config_dict.getboolean('OPTIONS', 'check_update'))
        self.ow_checkbox_5.setChecked(self.egads_config_dict.getboolean('OPTIONS', 'check_update'))
        self.ow_checkbox_7.setChecked(self.config_dict.getboolean('FILES_FOLDERS', 'keep_opened_files'))
        self.ow_checkbox_8.setChecked(self.config_dict.getboolean('FILES_FOLDERS', 'enable_user_folders'))
        self.ow_checkbox_9.setChecked(self.config_dict.getboolean('PLOTS', 'manual_axis_distribution'))
        self.ow_checkbox_10.setChecked(self.config_dict.getboolean('PLOTS', 'geo_as_standard'))
        self.activate_dimension_distribution()
        self.ow_combobox_5.setCurrentIndex(int(self.config_dict.get('PLOTS', 'first_dimension_axis')))
        self.ow_combobox_6.setCurrentIndex(int(self.config_dict.get('PLOTS', 'second_dimension_axis')))
        self.ow_combobox_7.setCurrentIndex(int(self.config_dict.get('PLOTS', 'third_dimension_axis')))
        self.ow_checkbox_11.setChecked(self.config_dict.getboolean('GENERAL', 'dimension_warning'))
        self.activate_folder_registration()
        self.read_folder_list_quick_access()
        self.ow_line_1.setCursorPosition(0)
        self.ow_line_2.setCursorPosition(0)

    def check_gui_update(self):
        logging.debug('gui - option_window_functions.py - MyOptions - check_gui_update')
        self.check_gui_update_thread = CheckEGADSGuiUpdateOnline(_gui_version, self.frozen, self.system, self.installed)
        self.check_gui_update_thread.start()
        self.check_gui_update_thread.finished.connect(self.parse_gui_update)

    def parse_gui_update(self, val):
        logging.debug('gui - option_window_functions.py - MyOptions - parse_gui_update - val ' + str(val))
        if val != 'no new version':
            self.available_update.emit(val)
            if self.frozen:
                if self.system == 'Windows':
                    if self.installed:
                        text = ('A new update for EGADS Lineage GUI is available on GitHub. Please exit the option '
                                'window and click on the Update button to launch the update process.')
                        info_window = MyInfo(text)
                        info_window.exec_()
                    else:
                        update_window = MyUpdateAvailable(val, gui=True)
                        update_window.exec_()
                elif self.system == 'Linux':
                    text = ('A new update for EGADS Lineage GUI is available on GitHub. Please exit the option '
                            'window and click on the Update button to launch the update process.')
                    info_window = MyInfo(text)
                    info_window.exec_()
            else:
                update_window = MyUpdateAvailable(val, gui=True)
                update_window.exec_()
        else:
            info_window = MyInfo('No new update available on GitHub for the GUI.')
            info_window.exec_()

    def check_egads_update(self):
        logging.debug('gui - option_window_functions.py - MyOptions - check_egads_update')
        self.check_egads_update_thread = CheckEGADSUpdateOnline(egads.__version__)
        self.check_egads_update_thread.start()
        self.check_egads_update_thread.finished.connect(self.parse_egads_update)

    def parse_egads_update(self, val):
        logging.debug('gui - option_window_functions.py - MyOptions - parse_egads_update - val ' + str(val))
        if val != 'no new version':
            update_window = MyUpdateAvailable(val)
            update_window.exec_()
        else:
            info_window = MyInfo('No new update available on GitHub for EGADS.')
            info_window.exec_()

    def save_config_dict(self):
        logging.debug('gui - option_window_functions.py - MyOptions - save_config_dict')
        egads_log_path, gui_log_path = False, False
        if pathlib.Path(str(self.ow_line_1.text())).exists():
            gui_log_path = True
        if pathlib.Path(str(self.ow_line_2.text())).exists():
            egads_log_path = True
        text = ''
        if not gui_log_path or not egads_log_path:
            if not gui_log_path and not egads_log_path:
                text = ('After checking, it appears that the paths for EGADS and its GUI log files are not valid. Thus '
                        + 'it is not possible to save the new configuration. Please correct them and try again.')
            else:
                if not gui_log_path:
                    text = ('After checking, it appears that the path for the GUI log file is not valid. Thus it is '
                            'not possible to save the new configuration. Please correct it and try again.')
                elif not egads_log_path:
                    text = ('After checking, it appears that the path for EGADS log file is not valid. Thus it is '
                            'not possible to save the new configuration. Please correct it and try again.')
            info_window = MyInfo(text)
            info_window.exec_()
        else:

            if self.check_manual_axis_distribution():
                self.config_dict.set('LOG', 'level', str(self.ow_combobox_1.currentText()))
                self.egads_config_dict.set('LOG', 'level', str(self.ow_combobox_2.currentText()))
                self.config_dict.set('PLOTS', 'same_unit_plot', str(self.ow_combobox_3.currentIndex()))
                self.config_dict.set('PLOTS', 'subplot_disposition', str(self.ow_combobox_4.currentIndex()))
                self.config_dict.set('LOG', 'path', str(self.ow_line_1.text()))
                self.egads_config_dict.set('LOG', 'path', str(self.ow_line_2.text()))
                self.config_dict.set('OPTIONS', 'check_update', str(self.ow_checkbox_4.isChecked()))
                self.egads_config_dict.set('OPTIONS', 'check_update', str(self.ow_checkbox_5.isChecked()))
                # self.config_dict.set('PLOTS', 'x_info_disabled', str(self.ow_checkbox_6.isChecked()))
                self.config_dict.set('PLOTS', 'manual_axis_distribution', str(self.ow_checkbox_9.isChecked()))
                self.config_dict.set('PLOTS', 'first_dimension_axis', str(self.ow_combobox_5.currentIndex()))
                self.config_dict.set('PLOTS', 'second_dimension_axis', str(self.ow_combobox_6.currentIndex()))
                self.config_dict.set('PLOTS', 'third_dimension_axis', str(self.ow_combobox_7.currentIndex()))
                self.config_dict.set('PLOTS', 'geo_as_standard', str(self.ow_checkbox_10.isChecked()))
                self.config_dict.set('SYSTEM', 'read_as_float', str(self.ow_checkbox_1.isChecked()))
                self.config_dict.set('SYSTEM', 'replace_fill_value', str(self.ow_checkbox_2.isChecked()))
                self.config_dict.set('SYSTEM', 'switch_fill_value', str(self.ow_checkbox_3.isChecked()))
                self.config_dict.set('FILES_FOLDERS', 'keep_opened_files', str(self.ow_checkbox_7.isChecked()))
                self.config_dict.set('FILES_FOLDERS', 'enable_user_folders', str(self.ow_checkbox_8.isChecked()))
                self.config_dict.set('GENERAL', 'dimension_warning', str(self.ow_checkbox_11.isChecked()))
                self.save_folder_list_quick_access()
                self.activate_recent_files_access()
                self.cancel = False
                self.closeWindow()
            else:
                self.ow_section_list.setCurrentRow(3)

    def check_manual_axis_distribution(self):
        if self.ow_checkbox_9.isChecked():
            idx_1 = self.ow_combobox_5.currentIndex()
            idx_2 = self.ow_combobox_6.currentIndex()
            idx_3 = self.ow_combobox_7.currentIndex()
            if idx_1 == 0 and idx_2 == 0 and idx_3 == 0:
                return True
            else:
                if idx_1 == 0 or idx_2 == 0 or idx_3 == 0:
                    self.check_failed_message()
                    return False
                else:
                    test = numpy.unique([idx_1, idx_2, idx_3])
                    if len(test) == 3:
                        return True
                    else:
                        self.check_failed_message()
                        return False
        else:
            return True

    def check_failed_message(self):
        text = ('When the manual axis distribution for 2D and 3D standard data is ON, the item selected in all three '
                'comboboxes should be on Automatic or on one of the three other items. In that last case, do not use '
                'the same item in more than one combobox.')
        info_window = MyInfo(text)
        info_window.exec_()

    def activate_recent_files_access(self):
        if self.ow_checkbox_7.isChecked():
            if not pathlib.Path(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')).exists():
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                add_element(doc, "Files", doc_root)
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()
        else:
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')).exists():
                file_to_rem = pathlib.Path(pathlib.Path(self.user_path).joinpath('opened_file_list.xml'))
                file_to_rem.unlink()

    def save_folder_list_quick_access(self):
        if self.ow_checkbox_8.isChecked():
            doc = xml.dom.minidom.Document()
            doc_root = add_element(doc, "EGADSLineageGui", doc)
            add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
            folders = add_element(doc, "Folders", doc_root)
            for i in range(self.ow_folderList_1.count()):
                folder = add_element(doc, "Folder", folders)
                add_element(doc, "Path", folder, str(self.ow_folderList_1.item(i).text()))
                add_element(doc, "Name", folder, str(pathlib.Path(str(self.ow_folderList_1.item(i).text())).stem))
            f = open(str(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')), 'w')
            f.write(doc.toprettyxml())
            f.close()
        else:
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')).exists():
                file_to_rem = pathlib.Path(pathlib.Path(self.user_path).joinpath('user_folder_list.xml'))
                file_to_rem.unlink()

    def read_folder_list_quick_access(self):
        if self.ow_checkbox_8.isChecked():
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')).exists():
                icon = icon_creation_function('small_warning_icon.svg')
                f = open(str(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')), 'r')
                doc = xml.dom.minidom.parse(f)
                f.close()
                folders = doc.getElementsByTagName('Folders')[0]
                nodes = folders.getElementsByTagName('Folder')
                for node in nodes:
                    path = get_element_value(node, 'Path')
                    item = QtWidgets.QListWidgetItem()
                    item.setText(str(path))
                    if not pathlib.Path(str(path)).exists():
                        item.setIcon(icon)
                        item.setToolTip('The path is not valid')
                    self.ow_folderList_1.addItem(item)

    def button_info(self):
        logging.debug('gui - option_window_functions.py - MyOptions - button_info')
        info_window = MyInfo(self.information_text[self.sender().objectName()])
        info_window.exec_()

    def get_folder_path(self):
        logging.debug('gui - option_window_functions.py - MyOptions - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            if self.sender().objectName() == 'ow_openButton_1':
                self.ow_line_1.setText(str(pathlib.Path(folder_path)))
                self.ow_line_1.setCursorPosition(0)
            elif self.sender().objectName() == 'ow_openButton_2':
                self.ow_line_2.setText(str(pathlib.Path(folder_path)))
                self.ow_line_2.setCursorPosition(0)
            elif self.sender().objectName() == 'ow_openButton_3':
                self.ow_line_3.setText(str(pathlib.Path(folder_path)))
                self.ow_line_3.setCursorPosition(0)

    def closeWindow(self):
        logging.debug('gui - option_window_functions.py - MyOptions - closeWindow')
        self.close()
