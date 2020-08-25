import logging
import datetime
import os
import pathlib
import egads
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_batchprocessingwindow import Ui_batchProcessingWindow
from ui.Ui_waitbatchwindow import Ui_waitBatchWindow
from ui.Ui_batchinfowindow import Ui_batchInfoWindow
from functions.window_functions.other_windows_functions import MyInfo, MyCoeff
from functions.gui_functions.gui_widgets import QtWaitingSpinner
from functions.thread_functions.processing_functions import BatchProcessingThread
from functions.help_functions import batch_processing_information_text
from functions.utils import (humansize, clear_layout, font_creation_function, stylesheet_creation_function,
                             icon_creation_function)


class MyBatchProcessing(QtWidgets.QDialog, Ui_batchProcessingWindow):
    def __init__(self, list_of_algorithms, config_dict):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.information_text = batch_processing_information_text()
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_of_algorithms = list_of_algorithms
        self.config_dict = config_dict
        self.bw_label_10.setText('')
        self.options_layout.setAlignment(QtCore.Qt.AlignTop)
        self.processing_layout.setAlignment(QtCore.Qt.AlignTop)
        self.bw_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_7.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_8.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_combobox_9.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_checkbox_1.stateChanged.connect(self.activate_filename_creation)
        self.bw_checkbox_1.stateChanged.connect(self.activate_launch_processing_button)
        self.bw_button_cancel.clicked.connect(self.closeWindow)
        self.bw_combobox_1.currentIndexChanged.connect(self.process_selection)
        self.bw_combobox_1.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_5.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_6.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_7.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_8.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_9.currentIndexChanged.connect(self.set_filename_options)
        self.bw_combobox_5.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_6.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_7.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_8.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_combobox_9.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_5.textChanged.connect(self.set_filename_example)
        self.bw_edit_6.textChanged.connect(self.set_filename_example)
        self.bw_edit_7.textChanged.connect(self.set_filename_example)
        self.bw_edit_8.textChanged.connect(self.set_filename_example)
        self.bw_edit_9.textChanged.connect(self.set_filename_example)
        self.bw_edit_5.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_6.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_7.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_8.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_9.textChanged.connect(self.activate_launch_processing_button)
        self.bw_open_button_1.clicked.connect(self.get_folder_path)
        self.bw_open_button_2.clicked.connect(self.get_folder_path)

        self.bw_edit_2.textChanged.connect(self.populate_file_list_widget)
        self.bw_edit_2.textChanged.connect(self.activate_launch_processing_button)
        self.bw_edit_3.textChanged.connect(self.activate_launch_processing_button)
        self.buttonGroup.buttonClicked.connect(self.populate_file_list_widget)
        self.buttonGroup.buttonClicked.connect(self.activate_launch_processing_button)
        self.filename_combobox_list = [self.bw_combobox_5, self.bw_combobox_6, self.bw_combobox_7, self.bw_combobox_8,
                                       self.bw_combobox_9]
        self.filename_edit_list = [self.bw_edit_5, self.bw_edit_6, self.bw_edit_7, self.bw_edit_8, self.bw_edit_9]
        self.button_format_text = {'NetCDF': ('*.nc', '*.cdf'), 'NASA Ames': ('*.na',),
                                   'HDF5': ('*.h5', '*.hdf5', '*.he5'),
                                   'no button': ('*.nc', '*.cdf', '*.na', '*.h5', '*.hdf5', '*.he5')}
        self.listWidget.itemSelectionChanged.connect(self.activate_list_item_buttons)
        self.bw_up_button.clicked.connect(self.move_up_item)
        self.bw_down_button.clicked.connect(self.move_down_item)
        self.bw_plus_button.clicked.connect(self.add_new_item)
        self.bw_plus_button.clicked.connect(self.activate_launch_processing_button)
        self.bw_del_button.clicked.connect(self.delete_item)
        self.bw_del_button.clicked.connect(self.activate_launch_processing_button)
        self.bw_file_info.clicked.connect(self.info_item)
        self.bw_button_ok.clicked.connect(self.launch_processing)
        self.bw_info_1.clicked.connect(self.batch_button_info)
        self.bw_info_3.clicked.connect(self.batch_button_info)
        self.bw_info_4.clicked.connect(self.batch_button_info)
        self.bw_info_5.clicked.connect(self.batch_button_info)
        self.bw_info_6.clicked.connect(self.batch_button_info)
        self.bw_info_7.clicked.connect(self.filename_button_info)
        self.bw_info_8.clicked.connect(self.filename_button_info)
        self.bw_info_9.clicked.connect(self.filename_button_info)
        self.bw_info_10.clicked.connect(self.filename_button_info)
        self.bw_info_11.clicked.connect(self.filename_button_info)
        self.tabWidget.removeTab(2)
        self.bw_proc_combobox_1 = None
        self.bw_proc_combobox_1 = None
        self.bw_proc_combobox_2 = None
        self.bw_proc_info_1 = None
        self.bw_proc_label_3 = None
        self.bw_proc_label_4 = None
        self.bw_proc_edit_2 = None
        self.algorithm = None
        self.options_hl_1 = None
        self.options_hl_2 = None
        self.options_label_1 = None
        self.options_label_2 = None
        self.options_combobox_1 = None
        self.options_list_1 = None
        self.options_hl_5 = None
        self.options_gl_1 = None
        self.options_label_4 = None
        self.options_hl_4 = None
        self.options_combobox_2 = None
        self.options_hl_3 = None
        self.options_label_3 = None
        self.options_button_1 = None
        self.grid_layout_input_1 = None
        self.grid_layout_input_2 = None
        self.options_line_1 = None
        self.input_activate = 0
        self.list_of_inputs = []
        self.list_label_input = []
        self.list_combobox_input = []
        self.list_button_input = []
        self.input_num = 0
        self.list_label_output = []
        self.list_edit_output = []
        self.list_button_output = []
        self.output_num = 0
        self.output_activate = 0
        self.list_of_outputs = []
        self.coefficient_matrix_values = {}
        self.types_for_combobox = ["vector", "array", "vector_optional", "array_optional"]
        logging.info('gui - batch_processing_window_functions.py - MyBatchProcessing - ready')

    def process_selection(self, val):
        clear_layout(self.processing_layout)
        self.clear_option_layout()
        self.set_default_radiobutton()
        if val == 1 or val == 3 or val == 4:
            self.set_other_processing(val)
        elif val == 2:
            self.set_conversion_processing()
        elif val == 5:
            self.set_algorithm_processing()

    def activate_filename_creation(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - activate_filename_creation')
        self.bw_label_10.setText('')
        self.bw_label_10.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_combobox_5.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_combobox_6.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_combobox_7.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_combobox_8.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_combobox_9.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_info_7.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_info_8.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_info_9.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_info_10.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_info_11.setEnabled(not self.bw_checkbox_1.isChecked())
        self.bw_edit_5.setText('')
        self.bw_edit_6.setText('')
        self.bw_edit_7.setText('')
        self.bw_edit_8.setText('')
        self.bw_edit_9.setText('')
        self.bw_combobox_5.setCurrentIndex(0)
        self.bw_combobox_6.setCurrentIndex(0)
        self.bw_combobox_7.setCurrentIndex(0)
        self.bw_combobox_8.setCurrentIndex(0)
        self.bw_combobox_9.setCurrentIndex(0)

    def set_filename_options(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - set_filename_options')
        combobox = self.sender()
        index = int(combobox.objectName()[-1:])
        edit = getattr(self, 'bw_edit_' + str(index))
        if combobox.currentIndex() == 0:
            edit.setText('')
            edit.setEnabled(False)
        else:
            edit.setText('')
            edit.setEnabled(True)
            if combobox.currentIndex() == 1:
                edit.setText('%Y%m%dT%H%M%S')
            elif combobox.currentIndex() == 2:
                edit.setEnabled(False)
                edit.setText('original filename')
            elif combobox.currentIndex() == 3:
                edit.setText('001')
            elif combobox.currentIndex() == 4:
                edit.setText('')

    def set_filename_example(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - set_filename_example')
        self.bw_label_10.setText('standby...')
        filename_example_str = ''
        for i, combobox in enumerate(self.filename_combobox_list):
            edit = self.filename_edit_list[i]
            edit_str = ''
            if combobox.currentIndex() == 0:
                edit_str = ''
            elif combobox.currentIndex() == 1:
                try:
                    edit_str = datetime.datetime.now().strftime(str(edit.text()))
                except ValueError:
                    edit_str = ''
            elif combobox.currentIndex() == 2:
                try:
                    edit_str = self.listWidget.item(0).text()[:-3]
                except AttributeError:
                    edit_str = 'original_filename'
            elif combobox.currentIndex() == 3:
                try:
                    int(edit.text())
                    edit_str = str(edit.text())
                except ValueError:
                    edit_str = ''
            elif combobox.currentIndex() == 4:
                edit_str = str(edit.text())
            filename_example_str += edit_str
        self.bw_label_10.setText(filename_example_str)

    def get_folder_path(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            if self.sender().objectName() == 'bw_open_button_1':
                self.bw_edit_2.setText(str(pathlib.Path(folder_path)))
            elif self.sender().objectName() == 'bw_open_button_2':
                self.bw_edit_3.setText(str(pathlib.Path(folder_path)))

    def populate_file_list_widget(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - populate_file_list_widget')
        self.listWidget.clear()
        path = str(self.bw_edit_2.text())
        try:
            button_text = self.buttonGroup.checkedButton().text()
        except AttributeError:
            button_text = 'no button'
        if pathlib.Path(path).is_dir() and self.bw_edit_2.text():
            for ext in self.button_format_text[button_text]:
                for file in pathlib.Path(path).glob(ext):
                    item = QtWidgets.QListWidgetItem(file.name)
                    item.setToolTip(str(file))
                    self.listWidget.addItem(item)

        # self.listWidget.clear()
        # if (self.bw_combobox_1.currentText() == 'Delete one or more global metadata'
        #         or self.bw_combobox_1.currentText() == 'Delete one or more variables'):
        #     try:
        #         self.options_combobox_2.clear()
        #     except AttributeError:
        #         pass
        # elif self.bw_combobox_1.currentText() == 'Execute an algorithm':
        #     for widget in self.list_combobox_input:
        #         if isinstance(widget, QtWidgets.QComboBox):
        #             widget.clear()
        # path = str(self.bw_edit_2.text())
        # try:
        #     button_text = self.buttonGroup.checkedButton().text()
        # except AttributeError:
        #     button_text = 'no button'
        # if pathlib.Path(path).is_dir() and self.bw_edit_2.text():
        #     for ext in self.button_format_text[button_text]:
        #         for file in pathlib.Path(path).glob(ext):
        #             item = QtWidgets.QListWidgetItem(file.name)
        #             item.setToolTip(str(file))
        #             self.listWidget.addItem(item)
        #     self.populate_options_file_combobox()
        #     self.populate_algorithm_input_combobox()

    def activate_list_item_buttons(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - activate_list_item_buttons')
        current_items = self.listWidget.selectedItems()
        if current_items:
            if len(current_items) == 1:
                self.bw_up_button.setEnabled(True)
                self.bw_down_button.setEnabled(True)
                self.bw_del_button.setEnabled(True)
                self.bw_file_info.setEnabled(True)
            else:
                self.bw_file_info.setEnabled(False)
                self.bw_up_button.setEnabled(False)
                self.bw_down_button.setEnabled(False)
                self.bw_del_button.setEnabled(True)
        else:
            self.bw_up_button.setEnabled(False)
            self.bw_down_button.setEnabled(False)
            self.bw_del_button.setEnabled(False)
            self.bw_file_info.setEnabled(False)

    def move_up_item(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - move_up_item')
        current_row = self.listWidget.currentRow()
        current_item = self.listWidget.takeItem(current_row)
        self.listWidget.insertItem(current_row - 1, current_item)
        self.listWidget.setCurrentItem(current_item)
        if current_row - 1 == 0:
            self.populate_algorithm_input_combobox()

    def move_down_item(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - move_down_item')
        current_row = self.listWidget.currentRow()
        current_item = self.listWidget.takeItem(current_row)
        self.listWidget.insertItem(current_row + 1, current_item)
        self.listWidget.setCurrentItem(current_item)
        if current_row == 0:
            self.populate_algorithm_input_combobox()

    def add_new_item(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - add_new_item')
        file_dialog = QtWidgets.QFileDialog()
        try:
            button_text = self.buttonGroup.checkedButton().text()
        except AttributeError:
            button_text = 'no button'
        if button_text == 'no button':
            filter_types = 'NetCDF Files (*.nc);;NASA Ames Files (*.na)'
        else:
            if self.button_format_text[button_text] == '.nc':
                filter_types = 'NetCDF Files (*.nc)'
            else:
                filter_types = 'NASA Ames Files (*.na)'
        file_path, _ = file_dialog.getOpenFileName(self, 'Select file', '', filter_types)
        path, file = os.path.split(file_path)
        item = QtWidgets.QListWidgetItem(file)
        item.setToolTip(str(pathlib.Path(path).joinpath(file)))
        self.listWidget.addItem(item)
        self.populate_options_file_combobox()

    def delete_item(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - delete_item')
        current_items = self.listWidget.selectedItems()
        for item in current_items:
            index = self.listWidget.row(item)
            self.listWidget.takeItem(index)
        self.populate_options_file_combobox()

    def info_item(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - info_item')
        batch_info_window = MyBatchInfo(self.listWidget.currentItem().toolTip())
        batch_info_window.exec_()

    def set_other_processing(self, val):
        font1 = font_creation_function('normal')
        font2 = font_creation_function('small')
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setObjectName("horizontalLayout")
        bw_proc_label_1 = QtWidgets.QLabel()
        bw_proc_label_1.setEnabled(True)
        bw_proc_label_1.setMinimumSize(QtCore.QSize(0, 27))
        bw_proc_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        bw_proc_label_1.setFont(font1)
        bw_proc_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
        bw_proc_label_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        bw_proc_label_1.setObjectName("bw_proc_label_1")
        horizontal_layout.addWidget(bw_proc_label_1)
        bw_proc_edit_1 = QtWidgets.QTextEdit()
        bw_proc_edit_1.setEnabled(True)
        bw_proc_edit_1.setMinimumSize(QtCore.QSize(300, 110))
        bw_proc_edit_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        bw_proc_edit_1.setFont(font2)
        bw_proc_edit_1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        bw_proc_edit_1.setStyleSheet(stylesheet_creation_function('qtextedit'))
        bw_proc_edit_1.setReadOnly(True)
        bw_proc_edit_1.setObjectName("bw_proc_edit_1")
        horizontal_layout.addWidget(bw_proc_edit_1)
        self.processing_layout.addLayout(horizontal_layout)
        bw_proc_label_1.setText("Description:")
        if val == 1:
            bw_proc_edit_1.setText('<p align="justify">This function is useful for those who wants to concatenate '
                                   'multiple files into one file. All metadata, variables, dimensions coming from '
                                   'each file are stored into one file. An option tab is available to let the '
                                   'user decide what to do with global attributes.<br><br>Please take note of few '
                                   'limitations:<ul><li>if different dimensions or variables have the same name, '
                                   'they will be overwritten in the destination file.</li><li>it is expected to '
                                   'have the same behaviour with metadata displaying the same name.</li><li>of '
                                   'course, it is not possible to concatenate NetCDF files AND HDF5 files AND NASA '
                                   'Ames file '
                                   'into the same file.</li><li>do not forget that EGADS only handles NASA Ames '
                                   'file with an FFI equal to 1001.</li></ul></p>')
            self.populate_file_list_widget()
        elif val == 3:
            bw_proc_edit_1.setText('<p align="justify">Use this function to delete global metadata from a '
                                   'list of NetCDF or HDF5 files. If the metadata to be deleted are not found in '
                                   'one or more files, those files are simply ignored, but still saved with others.')
            self.bw_radiobox_2.setEnabled(False)
            if self.bw_radiobox_2.isChecked():
                self.bw_radiobox_1.setChecked(True)
            self.add_options_tab('Options')
            self.populate_file_list_widget()
            self.set_delete_metadata_options()
        else:
            bw_proc_edit_1.setText('<p align="justify">Use this function to delete variables from a '
                                   'list of NetCDF, HDF5 or NASA Ames files. If the variable to be deleted is not '
                                   'found or is a dimension in one or more files, this variable is not deleted '
                                   'and simply ignored.')
            self.populate_file_list_widget()

    def set_conversion_processing(self):
        font1 = font_creation_function('normal')
        font2 = font_creation_function('small')
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setObjectName("gridLayout")
        bw_proc_label_1 = QtWidgets.QLabel()
        bw_proc_label_1.setEnabled(True)
        bw_proc_label_1.setMinimumSize(QtCore.QSize(0, 27))
        bw_proc_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        bw_proc_label_1.setFont(font1)
        bw_proc_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
        bw_proc_label_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        bw_proc_label_1.setObjectName("bw_proc_label_1")
        grid_layout.addWidget(bw_proc_label_1, 0, 0, 1, 1)
        bw_proc_hl_1 = QtWidgets.QHBoxLayout()
        bw_proc_hl_1.setObjectName("bw_proc_hl_1")
        self.bw_proc_combobox_1 = QtWidgets.QComboBox()
        self.bw_proc_combobox_1.setEnabled(True)
        self.bw_proc_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.bw_proc_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.bw_proc_combobox_1.setFont(font2)
        self.bw_proc_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.bw_proc_combobox_1.setFrame(False)
        self.bw_proc_combobox_1.setObjectName("bw_proc_combobox_1")
        self.bw_proc_combobox_1.addItem("")
        self.bw_proc_combobox_1.addItem("")
        self.bw_proc_combobox_1.addItem("")
        self.bw_proc_combobox_1.addItem("")
        self.bw_proc_combobox_1.addItem("")
        self.bw_proc_combobox_1.addItem("")
        self.bw_proc_combobox_1.addItem("")
        bw_proc_hl_1.addWidget(self.bw_proc_combobox_1)
        bw_proc_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Minimum))
        grid_layout.addLayout(bw_proc_hl_1, 1, 1, 1, 1)
        bw_proc_label_2 = QtWidgets.QLabel()
        bw_proc_label_2.setEnabled(True)
        bw_proc_label_2.setMinimumSize(QtCore.QSize(0, 27))
        bw_proc_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        bw_proc_label_2.setFont(font1)
        bw_proc_label_2.setStyleSheet(stylesheet_creation_function('qlabel'))
        bw_proc_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        bw_proc_label_2.setObjectName("bw_proc_label_2")
        grid_layout.addWidget(bw_proc_label_2, 1, 0, 1, 1)
        bw_proc_edit_1 = QtWidgets.QTextEdit()
        bw_proc_edit_1.setEnabled(True)
        bw_proc_edit_1.setMinimumSize(QtCore.QSize(300, 110))
        bw_proc_edit_1.setMaximumSize(QtCore.QSize(16777215, 110))
        bw_proc_edit_1.setFont(font2)
        bw_proc_edit_1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        bw_proc_edit_1.setStyleSheet(stylesheet_creation_function('qtextedit'))
        bw_proc_edit_1.setReadOnly(True)
        bw_proc_edit_1.setObjectName("bw_proc_edit_1")
        grid_layout.addWidget(bw_proc_edit_1, 0, 1, 1, 1)
        bw_proc_label_1.setText("Description:")
        self.bw_proc_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_proc_combobox_1.setItemText(0, "Make a choice...")
        self.bw_proc_combobox_1.setItemText(1, "HDF5 -> NASA Ames")
        self.bw_proc_combobox_1.setItemText(2, "HDF5 -> NetCDF")
        self.bw_proc_combobox_1.setItemText(3, "NASA Ames -> HDF5")
        self.bw_proc_combobox_1.setItemText(4, "NASA Ames -> NetCDF")
        self.bw_proc_combobox_1.setItemText(5, "NetCDF -> HDF5")
        self.bw_proc_combobox_1.setItemText(6, "NetCDF -> NASA Ames")
        bw_proc_label_2.setText("Conversion:")
        bw_proc_edit_1.setText('<p align="justify">This function allows the user to convert multiple files from a '
                               'specified format to another specified format.</p>')
        self.processing_layout.addLayout(grid_layout)
        self.bw_proc_combobox_1.currentIndexChanged.connect(self.set_format_radiobutton)
        self.bw_proc_combobox_1.currentIndexChanged.connect(self.activate_launch_processing_button)

    def set_algorithm_processing(self):
        font1 = font_creation_function('normal')
        font2 = font_creation_function('small')
        icon1 = icon_creation_function('info_icon.svg')
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setObjectName("gridLayout")
        bw_proc_label_1 = QtWidgets.QLabel()
        bw_proc_label_1.setEnabled(True)
        bw_proc_label_1.setMinimumSize(QtCore.QSize(0, 27))
        bw_proc_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        bw_proc_label_1.setFont(font1)
        bw_proc_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
        bw_proc_label_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        bw_proc_label_1.setObjectName("bw_proc_label_1")
        grid_layout.addWidget(bw_proc_label_1, 0, 0, 1, 1)
        bw_proc_edit_1 = QtWidgets.QTextEdit()
        bw_proc_edit_1.setEnabled(True)
        bw_proc_edit_1.setMinimumSize(QtCore.QSize(300, 110))
        bw_proc_edit_1.setMaximumSize(QtCore.QSize(16777215, 110))
        bw_proc_edit_1.setFont(font2)
        bw_proc_edit_1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        bw_proc_edit_1.setStyleSheet(stylesheet_creation_function('qtextedit'))
        bw_proc_edit_1.setReadOnly(True)
        bw_proc_edit_1.setObjectName("bw_proc_edit_1")
        grid_layout.addWidget(bw_proc_edit_1, 0, 1, 1, 1)
        bw_proc_label_2 = QtWidgets.QLabel()
        bw_proc_label_2.setEnabled(True)
        bw_proc_label_2.setMinimumSize(QtCore.QSize(0, 27))
        bw_proc_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        bw_proc_label_2.setFont(font1)
        bw_proc_label_2.setStyleSheet(stylesheet_creation_function('qlabel'))
        bw_proc_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        bw_proc_label_2.setObjectName("bw_proc_label_2")
        grid_layout.addWidget(bw_proc_label_2, 1, 0, 1, 1)
        bw_proc_hl_1 = QtWidgets.QHBoxLayout()
        bw_proc_hl_1.setObjectName("bw_proc_hl_1")
        self.bw_proc_combobox_1 = QtWidgets.QComboBox()
        self.bw_proc_combobox_1.setEnabled(True)
        self.bw_proc_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.bw_proc_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.bw_proc_combobox_1.setFont(font2)
        self.bw_proc_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.bw_proc_combobox_1.setFrame(False)
        self.bw_proc_combobox_1.setObjectName("bw_proc_combobox_1")
        bw_proc_hl_1.addWidget(self.bw_proc_combobox_1)
        bw_proc_hl_1.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.bw_proc_info_1 = QtWidgets.QToolButton()
        self.bw_proc_info_1.setEnabled(True)
        self.bw_proc_info_1.setMinimumSize(QtCore.QSize(27, 27))
        self.bw_proc_info_1.setMaximumSize(QtCore.QSize(27, 27))
        self.bw_proc_info_1.setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.bw_proc_info_1.setIcon(icon1)
        self.bw_proc_info_1.setIconSize(QtCore.QSize(23, 23))
        self.bw_proc_info_1.setObjectName("bw_proc_info_1")
        bw_proc_hl_1.addWidget(self.bw_proc_info_1)
        bw_proc_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Minimum))
        grid_layout.addLayout(bw_proc_hl_1, 1, 1, 1, 1)
        self.bw_proc_label_3 = QtWidgets.QLabel()
        self.bw_proc_label_3.setEnabled(False)
        self.bw_proc_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_proc_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.bw_proc_label_3.setFont(font1)
        self.bw_proc_label_3.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.bw_proc_label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bw_proc_label_3.setObjectName("bw_proc_label_3")
        grid_layout.addWidget(self.bw_proc_label_3, 2, 0, 1, 1)
        bw_proc_hl_2 = QtWidgets.QHBoxLayout()
        bw_proc_hl_2.setObjectName("bw_proc_hl_2")
        self.bw_proc_combobox_2 = QtWidgets.QComboBox()
        self.bw_proc_combobox_2.setEnabled(False)
        self.bw_proc_combobox_2.setMinimumSize(QtCore.QSize(250, 27))
        self.bw_proc_combobox_2.setMaximumSize(QtCore.QSize(250, 27))
        self.bw_proc_combobox_2.setFont(font2)
        self.bw_proc_combobox_2.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.bw_proc_combobox_2.setFrame(False)
        self.bw_proc_combobox_2.setObjectName("bw_proc_combobox_2")
        bw_proc_hl_2.addWidget(self.bw_proc_combobox_2)
        bw_proc_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Minimum))
        grid_layout.addLayout(bw_proc_hl_2, 2, 1, 1, 1)
        self.bw_proc_label_4 = QtWidgets.QLabel()
        self.bw_proc_label_4.setEnabled(False)
        self.bw_proc_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.bw_proc_label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bw_proc_label_4.setFont(font1)
        self.bw_proc_label_4.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.bw_proc_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.bw_proc_label_4.setObjectName("bw_proc_label_4")
        grid_layout.addWidget(self.bw_proc_label_4, 3, 0, 1, 1)
        self.bw_proc_edit_2 = QtWidgets.QTextEdit()
        self.bw_proc_edit_2.setEnabled(False)
        self.bw_proc_edit_2.setMinimumSize(QtCore.QSize(300, 110))
        self.bw_proc_edit_2.setMaximumSize(QtCore.QSize(16777215, 110))
        self.bw_proc_edit_2.setFont(font2)
        self.bw_proc_edit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bw_proc_edit_2.setStyleSheet(stylesheet_creation_function('qtextedit'))
        self.bw_proc_edit_2.setReadOnly(True)
        self.bw_proc_edit_2.setObjectName("bw_proc_edit_2")
        grid_layout.addWidget(self.bw_proc_edit_2, 3, 1, 1, 1)
        self.processing_layout.addLayout(grid_layout)
        self.bw_proc_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.bw_proc_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        bw_proc_label_1.setText("Description:")
        bw_proc_label_2.setText("Category:")
        self.bw_proc_label_3.setText("Algorithm:")
        self.bw_proc_label_4.setText("Information:")
        bw_proc_edit_1.setText('<p align="justify">All EGADS algorithms are available in the batch processing '
                               'window. Please select one of them to display information about it. An '
                               'Algorithm options tab is then displayed to handle inputs and outputs for '
                               'the algorithm. Please take note that the list of variables displayed in the '
                               'Algorithm options tab are retrieve from the first file in the Source tab.</p>')
        self.populate_combobox_category()
        self.bw_proc_info_1.clicked.connect(self.batch_button_info)
        self.bw_proc_combobox_1.currentIndexChanged.connect(self.populate_combobox_algorithms)
        self.bw_proc_combobox_2.currentIndexChanged.connect(self.set_algorithm_options)
        self.bw_proc_combobox_1.currentIndexChanged.connect(self.activate_launch_processing_button)
        self.bw_proc_combobox_2.currentIndexChanged.connect(self.activate_launch_processing_button)

    def populate_combobox_category(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - populate_combobox_1')
        self.bw_proc_combobox_1.addItem("Make a choice...")
        folder_list = []
        for key in self.list_of_algorithms.keys():
            folder_list.append(key[:key.find(' - ')].title())
        self.bw_proc_combobox_1.addItems(sorted(list(dict.fromkeys(folder_list))))

    def populate_combobox_algorithms(self, val):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - populate_combobox_2')
        self.clear_option_layout()
        self.bw_proc_combobox_2.clear()
        self.bw_proc_edit_2.setText('')
        if val == 0:
            enabled = False
        else:
            enabled = True
            self.bw_proc_combobox_2.addItem("Make a choice...")
            algo_list = []
            for key in self.list_of_algorithms.keys():
                if str(self.bw_proc_combobox_1.currentText()).lower() in key:
                    idx = key.find(' - ')
                    algo_list.append(key[idx + 3:])
            self.bw_proc_combobox_2.addItems(sorted(algo_list))
        self.bw_proc_label_3.setEnabled(enabled)
        self.bw_proc_label_4.setEnabled(enabled)
        self.bw_proc_edit_2.setEnabled(enabled)
        self.bw_proc_combobox_2.setEnabled(enabled)

    def set_format_radiobutton(self, val):
        if val == 0:
            self.set_default_radiobutton()
        elif val in [1, 2]:
            self.bw_radiobox_1.setEnabled(False)
            self.bw_radiobox_2.setEnabled(False)
            self.bw_radiobox_3.setEnabled(True)
            self.bw_radiobox_3.setChecked(True)
        elif val in [3, 4]:
            self.bw_radiobox_1.setEnabled(False)
            self.bw_radiobox_2.setEnabled(True)
            self.bw_radiobox_3.setEnabled(False)
            self.bw_radiobox_2.setChecked(True)
        else:
            self.bw_radiobox_1.setEnabled(True)
            self.bw_radiobox_2.setEnabled(False)
            self.bw_radiobox_3.setEnabled(False)
            self.bw_radiobox_1.setChecked(True)
        self.populate_file_list_widget()

    def set_default_radiobutton(self):
        self.bw_radiobox_1.setEnabled(True)
        self.bw_radiobox_2.setEnabled(True)
        self.bw_radiobox_3.setEnabled(True)
        self.bw_radiobox_1.setChecked(True)

    def set_algorithm_options(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - set_algorithm_options')
        self.clear_option_layout()
        self.bw_proc_edit_2.setText('')
        if self.bw_proc_combobox_2.currentText() == 'Make a choice...' or self.bw_proc_combobox_2.currentText() == '':
            return
        self.algorithm = self.list_of_algorithms[str(self.bw_proc_combobox_1.currentText()).lower() + ' - '
                                                 + str(self.bw_proc_combobox_2.currentText())]['method']
        font1 = font_creation_function('big')
        font2 = font_creation_function('normal')
        font3 = font_creation_function('small')
        icon1 = icon_creation_function('info_icon.svg')
        self.add_options_tab('Algorithm options')
        if self.algorithm is not None:
            self.bw_proc_edit_2.setText(self.algorithm().metadata['Description'])
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
            self.list_of_outputs = []
            self.input_num = 0
            self.coefficient_matrix_values = {}
            self.options_hl_1 = QtWidgets.QHBoxLayout()
            self.options_hl_1.setObjectName("options_hl_1")
            self.options_label_1 = QtWidgets.QLabel()
            self.options_label_1.setEnabled(True)
            self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
            self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
            self.options_label_1.setFont(font1)
            self.options_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
            self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.options_label_1.setObjectName("options_label_1")
            self.options_label_1.setText("Input(s)")
            self.options_hl_1.addWidget(self.options_label_1)
            self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Minimum))
            self.options_layout.addLayout(self.options_hl_1)
            self.grid_layout_input_1 = QtWidgets.QGridLayout()
            self.grid_layout_input_1.setObjectName("grid_layout_input_1")
            self.options_layout.addLayout(self.grid_layout_input_1)
            for index, item in enumerate(self.algorithm().metadata["Inputs"]):
                self.list_label_input.append(QtWidgets.QLabel())
                self.list_label_input[self.input_num].setFont(font2)
                self.list_label_input[self.input_num].setText(item + ':')
                self.list_label_input[self.input_num].setMinimumSize(QtCore.QSize(0, 27))
                self.list_label_input[self.input_num].setMaximumSize(QtCore.QSize(16777215, 27))
                self.list_label_input[self.input_num].setObjectName("list_label_input_" + str(self.input_num))
                self.list_label_input[self.input_num].setStyleSheet(stylesheet_creation_function('qlabel'))
                self.list_label_input[self.input_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                   QtCore.Qt.AlignVCenter)
                self.grid_layout_input_1.addWidget(self.list_label_input[self.input_num], self.input_num, 0, 1, 1)
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
                    self.list_combobox_input[self.input_num].setFont(font3)
                    self.list_combobox_input[self.input_num].setStyleSheet(stylesheet_creation_function('qcombobox'))
                    self.list_combobox_input[self.input_num].setObjectName("list_combobox_input_" + str(self.input_num))
                    self.list_combobox_input[self.input_num].addItem("Make a choice...")
                    self.list_combobox_input[self.input_num].activated.connect(self.activate_launch_processing_button)
                    self.grid_layout_input_1.addWidget(self.list_combobox_input[self.input_num], self.input_num, 2,
                                                       1, 1)
                else:
                    if ("coeff.[" in self.algorithm().metadata["InputTypes"][index]
                            or "coeff[" in self.algorithm().metadata["InputTypes"][index]):
                        self.list_combobox_input.append(QtWidgets.QHBoxLayout())
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_tmp_layout")
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("tmp_layout")
                        tmp_button = QtWidgets.QToolButton()
                        tmp_button.setMinimumSize(QtCore.QSize(150, 27))
                        tmp_button.setMaximumSize(QtCore.QSize(150, 27))
                        tmp_button.setFont(font2)
                        tmp_button.setStyleSheet(stylesheet_creation_function('qtoolbutton_win'))
                        tmp_button.setObjectName("coeff_set_button_" + str(index))
                        tmp_button.setText('Set coefficient')
                        tmp_button.clicked.connect(self.launch_coeff_window)
                        self.list_combobox_input[self.input_num].addWidget(tmp_button)
                        tmp_label = QtWidgets.QLabel()
                        tmp_label.setFont(font1)
                        tmp_label.setText('')
                        tmp_label.setMinimumSize(QtCore.QSize(0, 27))
                        tmp_label.setMaximumSize(QtCore.QSize(16777215, 27))
                        tmp_label.setObjectName("coeff_set_label" + str(index))
                        tmp_label.setStyleSheet(stylesheet_creation_function('qlabel'))
                        self.list_combobox_input[self.input_num].addWidget(tmp_label)
                        self.grid_layout_input_1.addLayout(self.list_combobox_input[self.input_num], self.input_num, 2,
                                                           1, 1)
                    else:
                        self.list_combobox_input.append(QtWidgets.QLineEdit())
                        self.list_combobox_input[self.input_num].setEnabled(True)
                        self.list_combobox_input[self.input_num].setMinimumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setMaximumSize(QtCore.QSize(300, 27))
                        self.list_combobox_input[self.input_num].setFrame(False)
                        self.list_combobox_input[self.input_num].setFont(font3)
                        self.list_combobox_input[self.input_num].setStyleSheet(stylesheet_creation_function(
                            'qlineedit'))
                        self.list_combobox_input[self.input_num].textChanged.connect(
                            self.activate_launch_processing_button)
                        if "optional" in self.algorithm().metadata["InputTypes"][index]:
                            self.list_combobox_input[self.input_num].setObjectName("optional_list_lineedit_input_" +
                                                                                   str(self.input_num))
                        else:
                            self.list_combobox_input[self.input_num].setObjectName("list_edit_input_" +
                                                                                   str(self.input_num))
                        self.grid_layout_input_1.addWidget(self.list_combobox_input[self.input_num],
                                                           self.input_num, 2, 1, 1)
                self.list_button_input.append(QtWidgets.QToolButton())
                self.list_button_input[self.input_num].setMinimumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setMaximumSize(QtCore.QSize(27, 27))
                self.list_button_input[self.input_num].setText("")
                self.list_button_input[self.input_num].setIcon(icon1)
                self.list_button_input[self.input_num].setIconSize(QtCore.QSize(23, 23))
                self.list_button_input[self.input_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                if "optional" in self.algorithm().metadata["InputTypes"][index]:
                    self.list_button_input[self.input_num].setObjectName("optional_list_button_input_"
                                                                         + str(self.input_num))
                else:
                    self.list_button_input[self.input_num].setObjectName("list_button_input_" + str(self.input_num))
                self.grid_layout_input_1.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                       QtWidgets.QSizePolicy.Minimum),
                                                 self.input_num, 3, 1, 1)
                self.list_button_input[self.input_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
                self.list_button_input[self.input_num].clicked.connect(self.algorithm_information_button)
                self.grid_layout_input_1.addWidget(self.list_button_input[self.input_num], self.input_num, 4, 1, 1)
                self.grid_layout_input_1.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                                       QtWidgets.QSizePolicy.Minimum),
                                                 self.input_num, 5, 1, 1)
                self.input_num += 1
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_line_1 = QtWidgets.QFrame()
        self.options_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.options_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.options_line_1.setObjectName("options_line_1")
        self.options_line_1.setStyleSheet(stylesheet_creation_function('qframe_algo'))
        self.options_layout.addWidget(self.options_line_1)
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_1")
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font1)
        self.options_label_2.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_2.setObjectName("options_label_2")
        self.options_label_2.setText("Output(s)")
        self.options_hl_2.addWidget(self.options_label_2)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_2)
        self.grid_layout_input_2 = QtWidgets.QGridLayout()
        self.grid_layout_input_2.setObjectName("grid_layout_input_2")
        self.options_layout.addLayout(self.grid_layout_input_2)
        for item in self.algorithm().metadata["Outputs"]:
            self.list_label_output.append(QtWidgets.QLabel())
            self.list_label_output[self.output_num].setText(item + ':')
            self.list_label_output[self.output_num].setFont(font2)
            self.list_label_output[self.output_num].setMinimumSize(QtCore.QSize(0, 27))
            self.list_label_output[self.output_num].setMaximumSize(QtCore.QSize(16777215, 27))
            self.list_label_output[self.output_num].setObjectName("list_label_output_" + str(self.output_num))
            self.list_label_output[self.output_num].setStyleSheet(stylesheet_creation_function('qlabel'))
            self.list_label_output[self.output_num].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing |
                                                                 QtCore.Qt.AlignVCenter)
            self.grid_layout_input_2.addWidget(self.list_label_output[self.output_num], self.output_num, 0, 1, 1)
            self.list_edit_output.append(QtWidgets.QLineEdit())
            self.list_edit_output[self.output_num].setEnabled(True)
            self.list_edit_output[self.output_num].setFont(font3)
            self.list_edit_output[self.output_num].setMinimumSize(QtCore.QSize(300, 27))
            self.list_edit_output[self.output_num].setMaximumSize(QtCore.QSize(300, 27))
            self.list_edit_output[self.output_num].setFrame(False)
            self.list_edit_output[self.output_num].setStyleSheet(stylesheet_creation_function('qlineedit'))
            self.list_edit_output[self.output_num].setObjectName("list_edit_output_" + str(self.output_num))
            self.list_edit_output[self.output_num].textChanged.connect(self.activate_launch_processing_button)
            self.grid_layout_input_2.addWidget(self.list_edit_output[self.output_num], self.output_num, 2, 1, 1)
            self.list_button_output.append(QtWidgets.QToolButton())
            self.list_button_output[self.output_num].setMinimumSize(QtCore.QSize(27, 27))
            self.list_button_output[self.output_num].setMaximumSize(QtCore.QSize(27, 27))
            self.list_button_output[self.output_num].setText("")
            self.list_button_output[self.output_num].setIcon(icon1)
            self.list_button_output[self.output_num].setIconSize(QtCore.QSize(23, 23))
            self.list_button_output[self.output_num].setPopupMode(QtWidgets.QToolButton.InstantPopup)
            self.list_button_output[self.output_num].setObjectName("list_button_output_" + str(self.output_num))
            self.grid_layout_input_2.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed,
                                                                   QtWidgets.QSizePolicy.Minimum),
                                             self.output_num, 3, 1, 1)
            self.list_button_output[self.output_num].setStyleSheet(stylesheet_creation_function('qtoolbutton'))
            self.list_button_output[self.output_num].clicked.connect(self.algorithm_information_button)
            self.grid_layout_input_2.addWidget(self.list_button_output[self.output_num], self.output_num, 4, 1, 1)
            self.grid_layout_input_2.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                                   QtWidgets.QSizePolicy.Minimum),
                                             self.output_num, 5, 1, 1)
            self.output_num += 1
            self.populate_algorithm_input_combobox()

    def launch_coeff_window(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - launch_coeff_window')
        if self.listWidget.item(0) is not None:
            index = int(self.sender().objectName()[17:])
            matrix_nbr_idx = self.algorithm().metadata["InputTypes"][index].index('[')
            matrix_nbr_str = self.algorithm().metadata["InputTypes"][index][matrix_nbr_idx + 1:-1]
            matrix_nbr_str = matrix_nbr_str.split(',')
            try:
                coefficient_data = self.coefficient_matrix_values[self.sender().objectName()]
            except KeyError:
                coefficient_data = None
            coef_window = MyCoeff(matrix_nbr_str, coefficient_data, self.listWidget.item(0).toolTip())
            coef_window.exec_()
            if coef_window.coef_array is not None:
                self.coefficient_matrix_values[self.sender().objectName()] = coef_window.coef_array
            self.activate_launch_processing_button()

    def set_delete_metadata_options(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - set_delete_metadata_options')
        font1 = font_creation_function('big')
        font2 = font_creation_function('normal')
        font3 = font_creation_function('small')
        icon1 = icon_creation_function('continue_icon.svg')
        self.options_hl_1 = QtWidgets.QHBoxLayout()
        self.options_hl_1.setObjectName("options_hl_1")
        self.options_label_1 = QtWidgets.QLabel()
        self.options_label_1.setEnabled(True)
        self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_1.setFont(font1)
        self.options_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_1.setObjectName("options_label_1")
        self.options_hl_1.addWidget(self.options_label_1)
        self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_1)
        self.options_hl_5 = QtWidgets.QHBoxLayout()
        self.options_hl_5.setObjectName("options_hl_5")
        self.options_hl_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1 = QtWidgets.QGridLayout()
        self.options_gl_1.setObjectName("options_gl_1")
        self.options_label_4 = QtWidgets.QLabel()
        self.options_label_4.setEnabled(True)
        self.options_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_4.setFont(font2)
        self.options_label_4.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_4.setIndent(-1)
        self.options_label_4.setObjectName("options_label_4")
        self.options_gl_1.addWidget(self.options_label_4, 0, 0, 1, 1)
        self.options_hl_4 = QtWidgets.QHBoxLayout()
        self.options_hl_4.setObjectName("options_hl_4")
        self.options_combobox_2 = QtWidgets.QComboBox()
        self.options_combobox_2.setMinimumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setMaximumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setFont(font3)
        self.options_combobox_2.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.options_combobox_2.setFrame(False)
        self.options_combobox_2.setObjectName("options_combobox_2")
        self.options_hl_4.addWidget(self.options_combobox_2)
        self.options_hl_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_4, 0, 1, 1, 1)
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font2)
        self.options_label_2.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_2.setIndent(-1)
        self.options_label_2.setObjectName("options_label_2")
        self.options_gl_1.addWidget(self.options_label_2, 1, 0, 1, 1)
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_2")
        self.options_combobox_1 = QtWidgets.QComboBox()
        self.options_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setFont(font3)
        self.options_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.options_combobox_1.setFrame(False)
        self.options_combobox_1.setObjectName("options_combobox_1")
        self.options_hl_2.addWidget(self.options_combobox_1)
        self.options_button_1 = QtWidgets.QToolButton()
        self.options_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.options_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.options_button_1.setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.options_button_1.setIcon(icon1)
        self.options_button_1.setIconSize(QtCore.QSize(23, 23))
        self.options_button_1.setObjectName("options_button_1")
        self.options_hl_2.addWidget(self.options_button_1)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_2, 1, 1, 1, 1)
        self.options_hl_5.addLayout(self.options_gl_1)
        self.options_layout.addLayout(self.options_hl_5)
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_hl_3 = QtWidgets.QHBoxLayout()
        self.options_hl_3.setObjectName("options_hl_3")
        self.options_hl_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_label_3 = QtWidgets.QLabel()
        self.options_label_3.setEnabled(True)
        self.options_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.options_label_3.setFont(font2)
        self.options_label_3.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.options_label_3.setIndent(-1)
        self.options_label_3.setObjectName("options_label_3")
        self.options_hl_3.addWidget(self.options_label_3)
        self.options_list_1 = QtWidgets.QListWidget()
        self.options_list_1.setEnabled(True)
        self.options_list_1.setFont(font3)
        self.options_list_1.setMinimumSize(QtCore.QSize(0, 150))
        self.options_list_1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.options_list_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.options_list_1.setStyleSheet(stylesheet_creation_function('qlistwidget'))
        self.options_list_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.options_list_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.options_list_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.options_list_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.options_list_1.setObjectName("options_list_1")
        self.options_hl_3.addWidget(self.options_list_1)
        self.options_layout.addLayout(self.options_hl_3)
        self.options_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_label_1.setText("Delete global metadata")
        self.options_label_4.setText("Global metadata from:")
        self.options_label_2.setText("Global metadata:")
        self.options_label_3.setText("The following metadata will be deleted:")
        self.options_button_1.clicked.connect(self.add_metadata_variable_to_list)
        self.options_combobox_2.currentTextChanged.connect(self.populate_options_metvar_combobox)
        self.options_list_1.itemDoubleClicked.connect(self.remove_metadata_variable_from_list)
        if self.listWidget.count() > 0:
            self.options_combobox_2.clear()
            item_list = []
            for i in range(self.listWidget.count()):
                item_list.append(self.listWidget.item(i).text())
            self.options_combobox_2.addItems(item_list)

    def set_delete_variable_options(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - set_delete_variable_options')
        font1 = font_creation_function('big')
        font2 = font_creation_function('normal')
        font3 = font_creation_function('small')
        icon1 = icon_creation_function('continue_icon.svg')
        self.options_hl_1 = QtWidgets.QHBoxLayout()
        self.options_hl_1.setObjectName("options_hl_1")
        self.options_label_1 = QtWidgets.QLabel()
        self.options_label_1.setEnabled(True)
        self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_1.setFont(font1)
        self.options_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_1.setObjectName("options_label_1")
        self.options_hl_1.addWidget(self.options_label_1)
        self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_1)
        self.options_hl_5 = QtWidgets.QHBoxLayout()
        self.options_hl_5.setObjectName("options_hl_5")
        self.options_hl_5.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1 = QtWidgets.QGridLayout()
        self.options_gl_1.setObjectName("options_gl_1")
        self.options_label_4 = QtWidgets.QLabel()
        self.options_label_4.setEnabled(True)
        self.options_label_4.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_4.setFont(font2)
        self.options_label_4.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_4.setIndent(-1)
        self.options_label_4.setObjectName("options_label_4")
        self.options_gl_1.addWidget(self.options_label_4, 0, 0, 1, 1)
        self.options_hl_4 = QtWidgets.QHBoxLayout()
        self.options_hl_4.setObjectName("options_hl_4")
        self.options_combobox_2 = QtWidgets.QComboBox()
        self.options_combobox_2.setMinimumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setMaximumSize(QtCore.QSize(400, 27))
        self.options_combobox_2.setFont(font3)
        self.options_combobox_2.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.options_combobox_2.setFrame(False)
        self.options_combobox_2.setObjectName("options_combobox_2")
        self.options_hl_4.addWidget(self.options_combobox_2)
        self.options_hl_4.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_4, 0, 1, 1, 1)
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font2)
        self.options_label_2.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.options_label_2.setIndent(-1)
        self.options_label_2.setObjectName("options_label_2")
        self.options_gl_1.addWidget(self.options_label_2, 1, 0, 1, 1)
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_2")
        self.options_combobox_1 = QtWidgets.QComboBox()
        self.options_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setFont(font3)
        self.options_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.options_combobox_1.setFrame(False)
        self.options_combobox_1.setObjectName("options_combobox_1")
        self.options_hl_2.addWidget(self.options_combobox_1)
        self.options_button_1 = QtWidgets.QToolButton()
        self.options_button_1.setMinimumSize(QtCore.QSize(27, 27))
        self.options_button_1.setMaximumSize(QtCore.QSize(27, 27))
        self.options_button_1.setStyleSheet(stylesheet_creation_function('qtoolbutton'))
        self.options_button_1.setIcon(icon1)
        self.options_button_1.setIconSize(QtCore.QSize(23, 23))
        self.options_button_1.setObjectName("options_button_1")
        self.options_hl_2.addWidget(self.options_button_1)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_gl_1.addLayout(self.options_hl_2, 1, 1, 1, 1)
        self.options_hl_5.addLayout(self.options_gl_1)
        self.options_layout.addLayout(self.options_hl_5)
        self.options_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Fixed))
        self.options_hl_3 = QtWidgets.QHBoxLayout()
        self.options_hl_3.setObjectName("options_hl_3")
        self.options_hl_3.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_label_3 = QtWidgets.QLabel()
        self.options_label_3.setEnabled(True)
        self.options_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.options_label_3.setFont(font2)
        self.options_label_3.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.options_label_3.setIndent(-1)
        self.options_label_3.setObjectName("options_label_3")
        self.options_hl_3.addWidget(self.options_label_3)
        self.options_list_1 = QtWidgets.QListWidget()
        self.options_list_1.setEnabled(True)
        self.options_list_1.setFont(font3)
        self.options_list_1.setMinimumSize(QtCore.QSize(0, 150))
        self.options_list_1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.options_list_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.options_list_1.setStyleSheet(stylesheet_creation_function('qlistwidget'))
        self.options_list_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.options_list_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.options_list_1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.options_list_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.options_list_1.setObjectName("options_list_1")
        self.options_hl_3.addWidget(self.options_list_1)
        self.options_layout.addLayout(self.options_hl_3)
        self.options_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_label_1.setText("Delete variable(s)")
        self.options_label_4.setText("Variables from:")
        self.options_label_2.setText("Variables:")
        self.options_label_3.setText("The following variables will be deleted:")
        self.options_button_1.clicked.connect(self.add_metadata_variable_to_list)
        self.options_list_1.itemDoubleClicked.connect(self.remove_metadata_variable_from_list)
        self.options_combobox_2.currentTextChanged.connect(self.populate_options_metvar_combobox)
        if self.listWidget.count() > 0:
            self.options_combobox_2.clear()
            item_list = []
            for i in range(self.listWidget.count()):
                item_list.append(self.listWidget.item(i).text())
            self.options_combobox_2.addItems(item_list)

    def set_concatenation_options(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - set_concatenation_options')
        font1 = font_creation_function('big')
        font2 = font_creation_function('normal')
        font3 = font_creation_function('small')
        self.options_hl_1 = QtWidgets.QHBoxLayout()
        self.options_hl_1.setObjectName("options_hl_1")
        self.options_label_1 = QtWidgets.QLabel()
        self.options_label_1.setEnabled(True)
        self.options_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_1.setFont(font1)
        self.options_label_1.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_1.setObjectName("options_label_1")
        self.options_hl_1.addWidget(self.options_label_1)
        self.options_hl_1.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_1)
        self.options_hl_2 = QtWidgets.QHBoxLayout()
        self.options_hl_2.setObjectName("options_hl_2")
        self.options_label_2 = QtWidgets.QLabel()
        self.options_label_2.setEnabled(True)
        self.options_label_2.setMinimumSize(QtCore.QSize(0, 27))
        self.options_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.options_label_2.setFont(font2)
        self.options_label_2.setStyleSheet(stylesheet_creation_function('qlabel'))
        self.options_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.options_label_2.setIndent(20)
        self.options_label_2.setObjectName("options_label_2")
        self.options_hl_2.addWidget(self.options_label_2)
        self.options_combobox_1 = QtWidgets.QComboBox()
        self.options_combobox_1.setMinimumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setMaximumSize(QtCore.QSize(250, 27))
        self.options_combobox_1.setFont(font3)
        self.options_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.options_combobox_1.setFrame(False)
        self.options_combobox_1.setObjectName("options_combobox_1")
        self.options_combobox_1.addItem("")
        self.options_combobox_1.addItem("")
        self.options_combobox_1.addItem("")
        self.options_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.options_hl_2.addWidget(self.options_combobox_1)
        self.options_hl_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum))
        self.options_layout.addLayout(self.options_hl_2)
        self.options_label_1.setText("Global metadata")
        self.options_label_2.setText("Global metadata will be:")
        self.options_combobox_1.setItemText(0, "copied from the first file")
        self.options_combobox_1.setItemText(1, "concatenated from all files")
        self.options_combobox_1.setItemText(2, "deleted (no global metadata)")

    def populate_algorithm_input_combobox(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - '
                      'populate_algorithm_input_combobox')
        if self.bw_combobox_1.currentText() == 'Execute an algorithm':
            if self.algorithm is not None:
                if self.bw_radiobox_1.isChecked():
                    input_class = egads.input.EgadsNetCdf
                elif self.bw_radiobox_2.isChecked():
                    input_class = egads.input.NasaAmes
                else:
                    input_class = egads.input.EgadsHdf
                if self.listWidget.count() > 0:
                    f = input_class(self.listWidget.item(0).toolTip(), 'r')
                    variable_list = f.get_variable_list()
                    f.close()
                    for widget in self.list_combobox_input:
                        if isinstance(widget, QtWidgets.QComboBox):
                            widget.clear()
                            widget.addItem('Make a choice...')
                            widget.addItems(sorted(variable_list))

    def populate_options_file_combobox(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - '
                      'populate_options_file_combobox')
        if self.bw_combobox_1.currentText() == 'Delete one or more global metadata' or \
                self.bw_combobox_1.currentText() == 'Delete one or more variables':
            try:
                self.options_combobox_2.clear()
                for i in range(self.listWidget.count()):
                    self.options_combobox_2.addItem(self.listWidget.item(i).text())
            except AttributeError:
                pass

    def populate_options_metvar_combobox(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - '
                      'populate_options_metvar_combobox')
        if (self.bw_combobox_1.currentText() == 'Delete one or more global metadata' and
                self.options_combobox_2.currentText() != ''):
            item = self.listWidget.findItems(self.options_combobox_2.currentText(), QtCore.Qt.MatchExactly)[0]
            if self.bw_radiobox_1.isChecked():
                f = egads.input.EgadsNetCdf(item.toolTip(), 'r')
            else:
                f = egads.input.EgadsHdf(item.toolTip(), 'r')
            self.options_combobox_1.clear()
            self.options_combobox_1.addItems(f.get_attribute_list())
            f.close()
        elif (self.bw_combobox_1.currentText() == 'Delete one or more variables' and
              self.options_combobox_2.currentText() != ''):
            item = self.listWidget.findItems(self.options_combobox_2.currentText(), QtCore.Qt.MatchExactly)[0]
            dim_list = None
            if self.bw_radiobox_1.isChecked():
                f = egads.input.EgadsNetCdf(item.toolTip(), 'r')
                dim_list = f.get_dimension_list()
            elif self.bw_radiobox_2.isChecked():
                f = egads.input.NasaAmes(item.toolTip(), 'r')
            else:
                f = egads.input.EgadsHdf(item.toolTip(), 'r')
            self.options_combobox_1.clear()
            var_list = f.get_variable_list()
            if dim_list is not None:
                for var in var_list:
                    if var in dim_list.keys():
                        var_list.remove(var)
            self.options_combobox_1.addItems(var_list)
            f.close()

    def add_metadata_variable_to_list(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - '
                      'add_metadata_variable_to_list')
        in_list = False
        for i in range(self.options_list_1.count()):
            if self.options_combobox_1.currentText() == str(self.options_list_1.item(i).text()):
                in_list = True
                break
        if not in_list:
            self.options_list_1.addItem(self.options_combobox_1.currentText())

    def remove_metadata_variable_from_list(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - '
                      'remove_metadata_variable_from_list')
        self.options_list_1.takeItem(self.options_list_1.currentRow())

    def algorithm_information_button(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - algorithm_information_button : '
                      + 'sender().objectName() ' + str(self.sender().objectName()))
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

    def activate_launch_processing_button(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - '
                      'activate_launch_processing_button')
        processing = True
        algorithm = True
        category = True
        conversion = True
        file_in_list = True
        destination_folder = True
        file_naming = True
        options_metvar_list = True
        options_input = True
        options_output = True
        if self.bw_combobox_1.currentText() == 'Make a choice...':
            processing = False
        if self.listWidget.count() == 0:
            file_in_list = False
        if not self.bw_edit_3.text():
            destination_folder = False
        if not self.bw_checkbox_1.isChecked():
            if not self.bw_label_10.text():
                file_naming = False
        if (self.bw_combobox_1.currentText() == 'Delete one or more global metadata' or
                self.bw_combobox_1.currentText() == 'Delete one or more variables'):
            try:
                if self.options_list_1.count() == 0:
                    options_metvar_list = False
            except AttributeError:
                options_metvar_list = False

        if self.bw_combobox_1.currentText() == 'Convert between different file formats':
            if self.bw_proc_combobox_1.currentText() == 'Make a choice...':
                conversion = False

        if self.bw_combobox_1.currentText() == 'Execute an algorithm':
            if self.bw_proc_combobox_1.currentText() == 'Make a choice...':
                algorithm = False
            if (self.bw_proc_combobox_2.currentText() == 'Make a choice...'
                    or self.bw_proc_combobox_2.currentText() == ''):
                category = False
        for widget in self.list_combobox_input:
            if "optional" not in widget.objectName():
                if isinstance(widget, QtWidgets.QComboBox):
                    if widget.currentText() == "Make a choice...":
                        options_input = False
                elif isinstance(widget, QtWidgets.QLineEdit):
                    if widget.text() == '':
                        options_input = False
                elif isinstance(widget, QtWidgets.QHBoxLayout):
                    if widget.itemAt(0).widget().objectName()not in self.coefficient_matrix_values:
                        options_input = False
        for widget in self.list_edit_output:
            if widget.text() == '':
                options_output = False
        if (processing and algorithm and category and file_in_list and destination_folder and file_naming and
                options_metvar_list and options_input and options_output and conversion):
            self.bw_button_ok.setEnabled(True)
        else:
            self.bw_button_ok.setEnabled(False)

    def launch_processing(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - launch_processing')
        filename_options = None
        if not self.bw_checkbox_1.isChecked():
            filename_options = []
            widgets_dict = [[self.bw_edit_5, self.bw_combobox_5], [self.bw_edit_6, self.bw_combobox_6],
                            [self.bw_edit_7, self.bw_combobox_7], [self.bw_edit_8, self.bw_combobox_8],
                            [self.bw_edit_9, self.bw_combobox_9]]
            for couple in widgets_dict:
                line, combobox = couple
                if combobox.currentIndex() == 0:
                    filename_options.append('')
                elif combobox.currentIndex() == 1:
                    filename_options.append('date' + str(line.text()))
                elif combobox.currentIndex() == 2:
                    filename_options.append('original_filename')
                elif combobox.currentIndex() == 3:
                    filename_options.append('ndigit' + str(line.text()))
                elif combobox.currentIndex() == 4:
                    filename_options.append(str(line.text()))

        processing_options = None
        if self.bw_combobox_1.currentIndex() == 1:
            processing_options = int(self.options_combobox_1.currentIndex())
        elif self.bw_combobox_1.currentIndex() == 4 or self.bw_combobox_1.currentIndex() == 5:
            processing_options = [str(self.options_list_1.item(i).text()) for i in
                                  range(self.options_list_1.count())]
        elif self.bw_combobox_1.currentIndex() == 6:
            if self.algorithm is not None:
                input_list = []
                output_list = []
                for widget in self.list_combobox_input:
                    if isinstance(widget, QtWidgets.QComboBox):
                        input_list.append(str(widget.currentText()))
                    elif isinstance(widget, QtWidgets.QLineEdit):
                        try:
                            input_list.append(float(widget.text()))
                        except ValueError:
                            input_list.append(str(widget.text()))

                    elif isinstance(widget, QtWidgets.QHBoxLayout):
                        input_list.append(self.coefficient_matrix_values[widget.itemAt(0).widget().objectName()])
                for widget in self.list_edit_output:
                    output_list.append(str(widget.text()))
                processing_options = {'inputs': input_list, 'outputs': output_list}

        if self.bw_combobox_4.currentIndex() == 0:
            stop_processing = True
        else:
            stop_processing = False
        batch_dict = {'process': int(self.bw_combobox_1.currentIndex()),
                      'algorithm': self.algorithm,
                      'file_list': [str(self.listWidget.item(i).toolTip()) for i in range(self.listWidget.count())],
                      'destination_folder': str(self.bw_edit_3.text()),
                      'filename_options': filename_options,
                      'stop_processing': stop_processing,
                      'processing_options': processing_options,
                      'out_format': str(self.buttonGroup.checkedButton().text())
                      }
        processing_window = MyWaitProcessing(batch_dict, self.config_dict)
        processing_window.exec_()
        error_occurred = processing_window.error_occurred
        success = processing_window.success
        if error_occurred:
            info_str = ('An important error occurred during the batch processing. The GUI decided to stop the '
                        'processing based on the choice of the user (cf. first tab and error option). Please read the '
                        'log file to check which kind or error occurred.')
            info_indow = MyInfo(info_str)
            info_indow.exec_()
        if success:
            info_indow = MyInfo('The batch processing has been well executed.')
            info_indow.exec_()

    def batch_button_info(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - batch_button_info')
        info_window = MyInfo(self.information_text[self.sender().objectName()])
        info_window.exec_()

    def filename_button_info(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - filename_button_info')
        widget = self.information_text[self.sender().objectName()]
        info_window = MyInfo(self.information_text[getattr(self, widget).currentText()])
        info_window.exec_()

    def clear_option_layout(self):
        clear_layout(self.options_layout)
        if self.tabWidget.count() > 3:
            self.tabWidget.removeTab(2)

    def add_options_tab(self, text):
        if self.tabWidget.count() == 3:
            self.tabWidget.insertTab(2, self.tab_3, text)

    def closeWindow(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchProcessing - closeWindow')
        self.close()


class MyWaitProcessing(QtWidgets.QDialog, Ui_waitBatchWindow):
    def __init__(self, batch_dict, config_dict):
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.batch_dict = batch_dict
        self.config_dict = config_dict
        self.spinner = None
        self.batch_thread = None
        self.error_occurred = False
        self.success = True
        self.setup_spinner()
        self.launch_processing_thread()
        logging.info('gui - batch_processing_window_functions.py - MyWaitProcessing - ready')

    def update_progress(self, val):
        progress_str, progress_nbr = val[0], val[1]
        if len(progress_str) > 65:
            progress_str = progress_str[:32] + '...' + progress_str[-32:0]
        self.progress_label.setText(progress_str)
        self.progress_bar.setValue(progress_nbr)

    def launch_processing_thread(self):
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - launch_processing_thread')
        self.batch_thread = BatchProcessingThread(self.batch_dict, self.config_dict)
        self.batch_thread.start()
        self.batch_thread.progress.connect(self.update_progress)
        self.batch_thread.finished.connect(self.processing_finished)
        self.batch_thread.error.connect(self.processing_failed)

    def processing_finished(self):
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - processing_finished')
        self.close()

    def processing_failed(self):
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - processing_failed')
        self.error_occurred = True
        self.success = False
        self.close()

    def setup_spinner(self):
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - setup_spinner')
        self.spinner = QtWaitingSpinner(self, centerOnParent=False)
        self.spinner_layout.addWidget(self.spinner)
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
        logging.debug('gui - batch_processing_window_functions.py - MyWaitProcessing - closeWindow')
        self.close()


class MyBatchInfo(QtWidgets.QDialog, Ui_batchInfoWindow):
    def __init__(self, file_path):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchInfo - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.file_path = file_path
        self.extension = os.path.splitext(file_path)[1]
        self.biw_ok_button.clicked.connect(self.close)
        self.met_label = []
        self.met_line = []
        self.var_label = []
        self.var_line = []
        self.horizontalLayout_4.removeItem(self.horizontalLayout_4.itemAt(1))
        self.splitter_1.setSizes([170, 200, 230])
        self.splitter_2.setSizes([216, 430])
        self.variable_list.currentTextChanged.connect(self.parse_variable_info)
        if self.extension == '.nc':
            self.file = egads.input.EgadsNetCdf(self.file_path, 'r')
        elif self.extension == '.na':
            self.file = egads.input.NasaAmes(self.file_path, 'r')
        self.parse_file_info()
        logging.info('gui - batch_processing_window_functions.py - MyBatchInfo - ready')

    def parse_file_info(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchInfo - parse_file_info')
        self.biw_line_1.setText(str(pathlib.Path(self.file_path).name))
        self.biw_line_2.setText(str(pathlib.Path(self.file_path).parent))
        self.biw_line_3.setText(humansize(pathlib.Path(self.file_path).stat().st_size))
        glob_attr = self.file.get_attribute_list()
        var_list = self.file.get_variable_list()
        if self.extension == '.na':
            var_list += self.file.get_variable_list(vartype='independant')
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
        i = 0
        for key, value in glob_attr.items():
            self.met_label.append(QtWidgets.QLabel())
            self.met_label[i].setFont(font)
            self.met_label[i].setMinimumSize(QtCore.QSize(0, 27))
            self.met_label[i].setMaximumSize(QtCore.QSize(16777215, 27))
            self.met_label[i].setObjectName("met_label_" + str(i))
            self.met_label[i].setText(key + ':')
            self.met_label[i].setStyleSheet("QLabel {\n"
                                            "   color: rgb(45,45,45);\n"
                                            "}")
            self.met_label[i].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.global_attributes_layout.addWidget(self.met_label[i], i, 0, 1, 1)
            if key == "SCOM" or key == "NCOM":
                self.met_line.append(QtWidgets.QPlainTextEdit())
                self.met_line[i].setMinimumSize(QtCore.QSize(0, 100))
                self.met_line[i].setMaximumSize(QtCore.QSize(16777215, 100))
                self.met_line[i].setFrameShape(QtWidgets.QFrame.NoFrame)
                self.met_line[i].setPlainText(str(value))
                self.met_line[i].setStyleSheet("QPlainTextEdit {\n"
                                               "    border-radius: 3px;\n"
                                               "    padding: 1px 0px 1px 4px;\n"
                                               "    background-color:  rgb(240, 240, 240);\n"
                                               "    color: rgb(45,45,45);\n"
                                               "}\n"
                                               "    \n"
                                               "QPlainTextEdit:disabled {\n"
                                               "    background-color:  rgb(240, 240, 240);\n"
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
                                               "  border-bottom-right-radius: 3px;\n"
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
                                               "  border-bottom: 1px solid rgb(240,240,"
                                               "240);\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  height: 20px;\n"
                                               "  subcontrol-position: top;\n"
                                               "  subcontrol-origin: margin;\n"
                                               "  border-top-right-radius: 3px;\n"
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
                                               "  border-bottom-right-radius: 3px;\n"
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
                                               "border-bottom-left-radius: 3px;\n"
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
                                               "QScrollBar::right-arrow:horizontal:pressed "
                                               "{\n"
                                               "  right: -1px;\n"
                                               "  bottom: -1px;\n"
                                               "}")
            else:
                self.met_line.append(QtWidgets.QLineEdit())
                self.met_line[i].setMinimumSize(QtCore.QSize(0, 27))
                self.met_line[i].setMaximumSize(QtCore.QSize(16777215, 27))
                self.met_line[i].setFrame(False)
                self.met_line[i].setText(str(value))
                self.met_line[i].setCursorPosition(0)
                self.met_line[i].setStyleSheet("QLineEdit {\n"
                                               "  border-radius: 3px;\n"
                                               "  padding: 1px 4px 1px 4px;\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "  color: rgb(45,45,45);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:disabled {\n"
                                               "  background-color: rgb(240, 240, 240);\n"
                                               "}")
            self.met_line[i].setEnabled(True)
            self.met_line[i].setReadOnly(True)
            self.met_line[i].setObjectName("met_line_" + str(i))
            self.met_line[i].setFocus(True)
            self.met_line[i].setFont(font2)
            self.global_attributes_layout.addWidget(self.met_line[i], i, 1, 1, 1)
            i += 1
        self.horizontalLayout_4.addLayout(self.global_attributes_layout)
        self.variable_list.addItems(var_list)

    def parse_variable_info(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchInfo - parse_variable_info')
        var_attr = self.file.get_attribute_list(self.variable_list.currentItem().text())
        clear_layout(self.variables_layout)
        self.var_label.clear()
        self.var_line.clear()
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
        i = 0
        for key, value in var_attr.items():
            self.var_label.append(QtWidgets.QLabel())
            self.var_label[i].setFont(font)
            self.var_label[i].setMinimumSize(QtCore.QSize(0, 27))
            self.var_label[i].setMaximumSize(QtCore.QSize(16777215, 27))
            self.var_label[i].setObjectName("var_label_" + str(i))
            self.var_label[i].setText(key + ':')

            self.var_label[i].setStyleSheet("QLabel {\n"
                                            "   color: rgb(45,45,45);\n"
                                            "}")
            self.var_label[i].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            self.variables_layout.addWidget(self.var_label[i], i, 0, 1, 1)
            self.var_line.append(QtWidgets.QLineEdit())
            self.var_line[i].setMinimumSize(QtCore.QSize(0, 27))
            self.var_line[i].setMaximumSize(QtCore.QSize(16777215, 27))
            self.var_line[i].setFrame(False)
            self.var_line[i].setText(str(value))
            self.var_line[i].setCursorPosition(0)
            self.var_line[i].setStyleSheet("QLineEdit {\n"
                                           "  border-radius: 3px;\n"
                                           "  padding: 1px 4px 1px 4px;\n"
                                           "  background-color: rgb(240, 240, 240);\n"
                                           "  color: rgb(45,45,45);\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:disabled {\n"
                                           "  background-color: rgb(240, 240, 240);\n"
                                           "}")
            self.var_line[i].setEnabled(True)
            self.var_line[i].setReadOnly(True)
            self.var_line[i].setObjectName("met_line_" + str(i))
            self.var_line[i].setFocus(True)
            self.var_line[i].setFont(font2)
            self.variables_layout.addWidget(self.var_line[i], i, 1, 1, 1)
            i += 1

    def closeWindow(self):
        logging.debug('gui - batch_processing_window_functions.py - MyBatchInfo - closeWindow')
        self.file.close()
        self.close()
