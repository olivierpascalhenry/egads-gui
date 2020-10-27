import logging
from egads import EgadsData
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_exportwindow import Ui_exportWindow
from ui.Ui_waitwindow import Ui_waitWindow
from functions.gui_functions.gui_widgets import QtWaitingSpinner
from functions.thread_functions.file_functions import ExportThread
from functions.window_functions.other_windows_functions import MyInfo, MyColorbarTicks
from functions.help_functions import export_information_text
from functions.material_functions import cmap_dict
from functions.utils import stylesheet_creation_function


class MyExport(QtWidgets.QDialog, Ui_exportWindow):
    def __init__(self, var_dict):
        logging.debug('gui - export_window_functions.py - MyExport - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.var_dict = var_dict
        self.ew_splitter.setSizes([140, 608])  # 748
        self.ew_vertical_layout_1.setAlignment(QtCore.Qt.AlignTop)
        self.ew_vertical_layout_2.setAlignment(QtCore.Qt.AlignTop)
        self.ew_vertical_layout_3.setAlignment(QtCore.Qt.AlignTop)
        self.ew_vertical_layout_4.setAlignment(QtCore.Qt.AlignTop)
        # self.ew_combobox_1.setStyleSheet(stylesheet_creation_function('qcombobox'))
        self.ew_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_5.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_7.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_8.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.export_information_text = export_information_text()
        self.ew_combobox_1.currentIndexChanged.connect(self.populate_export_options)
        self.ew_option_list.currentRowChanged.connect(self.display_export_options)
        self.ew_cancel_button.clicked.connect(self.closeWindow)
        self.ew_export_button.clicked.connect(self.export_function)
        self.info_button_1.clicked.connect(self.export_button_info)
        self.info_button_2.clicked.connect(self.export_button_info)
        self.info_button_3.clicked.connect(self.export_button_info)
        self.info_button_4.clicked.connect(self.export_button_info)
        self.info_button_5.clicked.connect(self.export_button_info)
        self.info_button_6.clicked.connect(self.export_button_info)
        self.info_button_7.clicked.connect(self.export_button_info)
        self.info_button_8.clicked.connect(self.export_button_info)
        self.info_button_9.clicked.connect(self.export_button_info)
        self.info_button_10.clicked.connect(self.export_button_info)
        self.info_button_11.clicked.connect(self.export_button_info)
        self.ew_ticks_button.clicked.connect(self.colorbar_tick_option_window)
        self.ew_combobox_2.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_3.currentIndexChanged.connect(self.activate_export_button)
        self.ew_combobox_4.currentIndexChanged.connect(self.activate_export_button)
        self.ew_add_button.clicked.connect(self.add_var_to_list)
        self.ew_varlist_1.itemDoubleClicked.connect(self.remove_var_from_list)
        self.ew_add_button.clicked.connect(self.activate_export_button)
        self.ew_varlist_1.itemDoubleClicked.connect(self.activate_export_button)
        self.ew_checkbox_1.clicked.connect(self.activate_transparency_checkbox)
        self.ew_checkbox_2.clicked.connect(self.activate_transparency_slider)
        self.ew_checkbox_3.clicked.connect(self.activate_reduce_value)
        self.ew_slider_1.valueChanged.connect(self.update_slider_value)
        self.ew_slider_2.valueChanged.connect(self.update_slider_value)
        self.ew_combobox_6.currentIndexChanged.connect(self.activate_colormap_options)
        self.ew_combobox_6.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ew_combobox_6.currentIndexChanged.connect(self.activate_export_button)
        self.ew_checkbox_5.clicked.connect(self.activate_colormap_values)
        self.ew_checkbox_6.clicked.connect(self.activate_colormap_dimensions)
        self.ew_line_2.textEdited.connect(self.colorbar_tick_option_man_remove)
        self.ew_line_3.textEdited.connect(self.colorbar_tick_option_man_remove)
        self.ew_line_4.textEdited.connect(self.colorbar_tick_option_man_remove)
        self.idx_base = 0
        self.export_format = None
        self.export_dict = {}
        self.var_list = []
        self.cbar_ticks_options = []
        self.ew_combobox_1.removeItem(2)
        self.ew_label_24.setVisible(False)
        self.ew_combobox_9.setVisible(False)
        logging.info('gui - export_window_functions.py - MyExport - ready')

    def populate_export_options(self):
        logging.debug('gui - export_window_functions.py - MyExport - populate_export_options')
        self.clear_all_var_comboboxes()
        if self.ew_combobox_1.currentIndex() == 0:
            self.setWindowTitle('Export to')
            self.export_format = None
            self.ew_option_list.clear()
            self.ew_stacked_widget.setCurrentIndex(0)
            self.idx_base = 0
        elif self.ew_combobox_1.currentIndex() == 1:
            self.setWindowTitle('Export to Google Earth - Time Series')
            self.export_format = 'GE-TS'
            self.ew_option_list.clear()
            self.ew_option_list.addItems(['Coordinates', 'Variables', 'Options', 'Colormap'])
            self.idx_base = 1
            self.prepare_var_list()
            self.populate_ge_ts_var_comboboxes()
        else:
            self.setWindowTitle('Export to')
            self.export_format = None
            self.ew_option_list.clear()
            self.ew_stacked_widget.setCurrentIndex(0)
            self.idx_base = 0

    def display_export_options(self, idx):
        self.ew_stacked_widget.setCurrentIndex(self.idx_base + idx)

    def clear_all_var_comboboxes(self):
        self.ew_combobox_2.clear()
        self.ew_combobox_3.clear()
        self.ew_combobox_4.clear()
        self.ew_combobox_5.clear()

    def populate_ge_ts_var_comboboxes(self):
        self.ew_combobox_2.addItems(['Make a choice...'] + self.var_list)
        self.ew_combobox_3.addItems(['Make a choice...'] + self.var_list)
        self.ew_combobox_4.addItems(['Make a choice...', 'Stick path to ground'] + self.var_list)
        self.ew_combobox_5.addItems(['Make a choice...'] + self.var_list)

    def prepare_var_list(self):
        logging.debug('gui - export_window_functions.py - MyExport - prepare_var_list')
        if self.export_format == 'GE-TS':
            for key, val in self.var_dict.items():
                if isinstance(val[0], EgadsData):
                    if len(val[0].value.shape) == 1:
                        self.var_list.append(key)
        self.var_list = sorted(self.var_list)

    def activate_colormap_dimensions(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_colormap_dimensions')
        self.ew_line_5.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_line_6.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_line_7.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_line_8.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_line_9.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_line_10.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_line_5.setText('')
        self.ew_line_6.setText('')
        self.ew_line_7.setText('')
        self.ew_line_8.setText('')
        self.ew_line_9.setText('')
        self.ew_line_10.setText('')
        self.ew_label_17.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_label_18.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_label_19.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_label_20.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_label_21.setEnabled(not self.ew_checkbox_6.isChecked())
        self.ew_label_22.setEnabled(not self.ew_checkbox_6.isChecked())

    def activate_colormap_options(self, val):
        logging.debug('gui - export_window_functions.py - MyExport - activate_colormap_options')
        enable = False
        if val != 0:
            enable = True
        self.ew_label_12.setEnabled(enable)
        self.ew_label_13.setEnabled(enable)
        self.info_button_9.setEnabled(enable)
        self.info_button_10.setEnabled(enable)
        self.info_button_11.setEnabled(enable)
        self.info_button_12.setEnabled(enable)
        self.info_button_13.setEnabled(enable)
        self.ew_combobox_7.setEnabled(enable)
        self.ew_combobox_8.setEnabled(enable)
        self.ew_combobox_7.setCurrentIndex(0)
        self.ew_combobox_8.setCurrentIndex(0)
        self.ew_checkbox_4.setEnabled(enable)
        self.ew_checkbox_5.setEnabled(enable)
        self.ew_checkbox_6.setEnabled(enable)
        self.ew_checkbox_4.setChecked(False)
        self.ew_checkbox_5.setChecked(True)
        self.ew_checkbox_6.setChecked(True)
        self.activate_colormap_values()
        self.activate_colormap_dimensions()

    def activate_colormap_values(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_colormap_values')
        self.ew_line_2.setEnabled(not self.ew_checkbox_5.isChecked())
        self.ew_line_3.setEnabled(not self.ew_checkbox_5.isChecked())
        self.ew_line_4.setEnabled(not self.ew_checkbox_5.isChecked())
        self.ew_line_2.setText('')
        self.ew_line_3.setText('')
        self.ew_line_4.setText('')
        self.ew_label_14.setEnabled(not self.ew_checkbox_5.isChecked())
        self.ew_label_15.setEnabled(not self.ew_checkbox_5.isChecked())
        self.ew_label_16.setEnabled(not self.ew_checkbox_5.isChecked())
        self.ew_ticks_button.setEnabled(not self.ew_checkbox_5.isChecked())
        self.pw_grid_label_57.setEnabled(not self.ew_checkbox_5.isChecked())
        self.pw_grid_label_57.setText('')

    def colorbar_tick_option_man_remove(self):
        logging.debug('gui - export_window_functions.py - MyExport - colorbar_tick_option_man_remove')
        self.pw_grid_label_57.setText('')
        self.cbar_ticks_options = []

    def activate_transparency_checkbox(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_transparency_checkbox')
        self.ew_checkbox_2.setEnabled(self.ew_checkbox_1.isChecked())
        self.info_button_6.setEnabled(self.ew_checkbox_1.isChecked())
        self.ew_checkbox_2.setChecked(False)
        self.activate_transparency_slider()

    def activate_transparency_slider(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_transparency_slider')
        self.ew_label_9.setEnabled(self.ew_checkbox_2.isChecked())
        self.ew_label_23.setEnabled(self.ew_checkbox_2.isChecked())
        self.ew_slider_2.setEnabled(self.ew_checkbox_2.isChecked())
        self.ew_label_23.setText('0 %')
        self.ew_slider_2.setValue(0)

    def update_slider_value(self, val):
        logging.debug('gui - export_window_functions.py - MyExport - update_slider_value')
        if self.sender().objectName() == 'ew_slider_2':
            self.ew_label_23.setText(str(val) + ' %')
        elif self.sender().objectName() == 'ew_slider_1':
            self.ew_label_8.setText(str(val) + ' px')

    def activate_reduce_value(self):
        logging.debug('gui - export_window_functions.py - MyExport - activate_reduce_value')
        self.ew_label_10.setEnabled(self.ew_checkbox_3.isChecked())
        self.ew_line_1.setEnabled(self.ew_checkbox_3.isChecked())
        self.ew_line_1.setText('')

    def remove_var_from_list(self, item):
        logging.debug('gui - export_window_functions.py - MyExport - remove_variable_from_list')
        self.ew_varlist_1.takeItem(self.ew_varlist_1.row(item))

    def add_var_to_list(self):
        logging.debug('gui - export_window_functions.py - MyExport - set_button_options')
        if self.export_format == 'GE-TS' and self.sender().objectName() == 'ew_add_button':
            if self.ew_combobox_5.currentText() != 'Make a choice...':
                if self.ew_varlist_1.count() < 1:  # MODIFY ONCE WINDOW IS READY
                    var_exist = False
                    for i in range(0, self.ew_varlist_1.count()):
                        if self.ew_combobox_5.currentText() == self.ew_varlist_1.item(i).text():
                            var_exist = True
                            break
                    if not var_exist:
                        self.ew_varlist_1.addItem(self.ew_combobox_5.currentText())

    def activate_export_button(self):
        if self.export_format == 'GE-TS':
            coordinate, variables, colormap = True, True, True
            if self.ew_combobox_2.currentIndex() == 0:
                coordinate = False
            if self.ew_combobox_3.currentIndex() == 0:
                coordinate = False
            if self.ew_combobox_4.currentIndex() == 0:
                coordinate = False
            if self.ew_varlist_1.count() == 0:
                variables = False
            if self.ew_combobox_6.currentIndex() == 0:
                colormap = False
            if coordinate and variables and colormap:
                self.ew_export_button.setEnabled(True)
            else:
                self.ew_export_button.setEnabled(False)

    def export_function(self):
        logging.debug('gui - export_window_functions.py - MyExport - export_function')
        file_name, file_ext = self.get_file_name()
        if file_name:
            if self.export_format == 'GE-TS':
                export_dict = self.export_ge_ts_function()
            else:
                export_dict = None
            export_window = MyWaitExport(self.export_format, export_dict, self.var_dict, file_name, file_ext)
            export_window.exec_()
            error_occurred = export_window.error_occurred
            success = export_window.success
            if error_occurred:
                info_str = ('An important error occurred during the process. Please read the log file to check which '
                            'kind or error occurred.')
                info_window = MyInfo(info_str)
                info_window.exec_()
            if success:
                info_window = MyInfo('The file has been well exported.')
                info_window.exec_()

    def export_ge_ts_function(self):
        logging.debug('gui - export_window_functions.py - MyExport - export_ge_ts_function')
        export_dict = {'Coordinates': {}, 'Variables': [], 'Options': {}, 'Colormap': {}}
        for i in range(0, self.ew_varlist_1.count()):
            export_dict['Variables'].append(self.ew_varlist_1.item(i).text())
        export_dict['Coordinates']['lon'] = self.ew_combobox_2.currentText()
        export_dict['Coordinates']['lat'] = self.ew_combobox_3.currentText()
        export_dict['Coordinates']['alt'] = self.ew_combobox_4.currentText()
        export_dict['Colormap']['colormap'] = cmap_dict()[self.ew_combobox_6.currentIndex()]
        export_dict['Colormap']['position'] = int(self.ew_combobox_7.currentIndex())
        export_dict['Colormap']['color_value'] = int(self.ew_combobox_8.currentIndex())
        export_dict['Options']['wall'] = self.ew_checkbox_1.isChecked()
        export_dict['Options']['wall_transparency'] = self.ew_checkbox_2.isChecked()
        export_dict['Options']['reduce_samples'] = self.ew_checkbox_3.isChecked()
        export_dict['Colormap']['reversed'] = self.ew_checkbox_4.isChecked()
        export_dict['Colormap']['automatic'] = self.ew_checkbox_5.isChecked()
        export_dict['Colormap']['auto_dimension'] = self.ew_checkbox_6.isChecked()
        export_dict['Options']['transparency'] = int(self.ew_slider_2.value())
        export_dict['Options']['path_width'] = int(self.ew_slider_1.value())
        try:
            export_dict['Options']['reduce_value'] = int(self.ew_line_1.text())
        except ValueError:
            export_dict['Options']['reduce_value'] = None
        try:
            export_dict['Colormap']['min'] = float(self.ew_line_4.text())
        except ValueError:
            export_dict['Colormap']['min'] = None
        try:
            export_dict['Colormap']['max'] = float(self.ew_line_2.text())
        except ValueError:
            export_dict['Colormap']['max'] = None
        try:
            export_dict['Colormap']['steps'] = float(self.ew_line_3.text())
        except ValueError:
            export_dict['Colormap']['steps'] = None
        export_dict['Colormap']['ticks_list'] = self.cbar_ticks_options
        try:
            export_dict['Colormap']['fig_width'] = float(self.ew_line_5.text())
        except ValueError:
            export_dict['Colormap']['fig_width'] = None
        try:
            export_dict['Colormap']['fig_height'] = float(self.ew_line_6.text())
        except ValueError:
            export_dict['Colormap']['fig_height'] = None
        try:
            export_dict['Colormap']['pos_left'] = float(self.ew_line_7.text())
        except ValueError:
            export_dict['Colormap']['pos_left'] = None
        try:
            export_dict['Colormap']['pos_bottom'] = float(self.ew_line_8.text())
        except ValueError:
            export_dict['Colormap']['pos_bottom'] = None
        try:
            export_dict['Colormap']['width'] = float(self.ew_line_9.text())
        except ValueError:
            export_dict['Colormap']['width'] = None
        try:
            export_dict['Colormap']['height'] = float(self.ew_line_10.text())
        except ValueError:
            export_dict['Colormap']['height'] = None
        return export_dict

    def get_file_name(self):
        logging.debug('gui - export_window_functions.py - MyExport - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        if self.export_format == 'GE-TS':
            filter_types = 'Google Earth KML (*.kml);;Google Earth KMZ (*.kmz)'
        else:
            filter_types = ''
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        return str(out_file_name), str(out_file_ext)

    def export_button_info(self):
        logging.debug('gui - export_window_functions.py - MyExport - export_button_info')
        info_window = MyInfo(self.export_information_text[self.sender().objectName()])
        info_window.exec_()

    def colorbar_tick_option_window(self):
        logging.debug('gui - export_window_functions.py - MyExport - colorbar_tick_option_window')
        cbar_ticks_window = MyColorbarTicks(self.cbar_ticks_options)
        cbar_ticks_window.exec_()
        if cbar_ticks_window.new_option_dict is not None:
            self.cbar_ticks_options = cbar_ticks_window.new_option_dict
            self.ew_line_2.setText('man')
            self.ew_line_3.setText('man')
            self.ew_line_4.setText('man')
            self.pw_grid_label_57.setText(str(self.cbar_ticks_options))

    def closeWindow(self):
        logging.debug('gui - export_window_functions.py - MyExport - closeWindow')
        self.close()


class MyWaitExport(QtWidgets.QDialog, Ui_waitWindow):
    def __init__(self, export_format, export_dict, var_dict, file_name, file_ext):
        logging.debug('gui - export_window_functions.py - MyWaitExport - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.export_format = export_format
        self.export_dict = export_dict
        self.var_dict = var_dict
        self.file_name = file_name
        self.file_ext = file_ext
        self.label.setText('Please wait...')
        self.spinner = None
        self.export_thread = None
        self.error_occurred = False
        self.success = True
        self.setup_spinner()
        self.launch_export_thread()
        logging.info('gui - export_window_functions.py - MyWaitExport - ready')

    def launch_export_thread(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - launch_export_thread')
        self.export_thread = ExportThread(self.export_format, self.export_dict, self.var_dict, self.file_name,
                                          self.file_ext)
        self.export_thread.start()
        self.export_thread.finished.connect(self.export_finished)
        self.export_thread.error.connect(self.export_failed)

    def export_finished(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - export_finished')
        self.close()

    def export_failed(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - export_failed')
        self.error_occurred = True
        self.success = False
        self.close()

    def setup_spinner(self):
        logging.debug('gui - export_window_functions.py - MyWaitExport - setup_spinner')
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
        logging.debug('gui - export_window_functions.py - MyWaitExport - closeWindow')
        self.close()
