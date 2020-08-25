import logging
import pathlib
from PyQt5 import QtWidgets, QtGui
from functions.utils import clear_layout
from ui.Ui_waitbatchwindow import Ui_waitBatchWindow
from functions.gui_functions.gui_widgets import QtWaitingSpinner
from functions.thread_functions.file_functions import ReadFileThread
from functions.window_functions.other_windows_functions import MyInfo
from functions.gui_functions.gui_netcdf_functions import (netcdf_gui_initialization, update_nc_global_attribute_gui,
                                                          populate_netcdf_tree_widget)
from functions.gui_functions.gui_nasaames_functions import (nasaames_gui_initialization, update_na_global_attribute_gui,
                                                            populate_na_tree_widget)
from functions.gui_functions.gui_global_functions import status_bar_update, update_icons_state


def reading_file(self):
    logging.debug('gui - file_functions.py - reading_file - file_name ' + self.file_name)
    self.reading_window = MyWaitReading(self.file_name, self.file_ext, self.config_dict)
    self.reading_window.exec_()
    if self.reading_window.error_occurred:
        exc_type = self.reading_window.error_reason[0]
        exc_value = self.reading_window.error_reason[1]
        info_str = ('An exception occurred during the reading of the file. Thus the GUI decided to stop the '
                    'process. Please read the log file to have more details about the exception. Contact the '
                    'developer if the same exception occurs again.<br><br>Exception type: ' + exc_type +
                    '<br><br>Exception value: ' + exc_value)
        self.info_window = MyInfo(info_str)
        self.info_window.exec_()
    if self.reading_window.success:
        self.opened_file = self.reading_window.final_dict['opened_file']
        self.list_of_global_attributes = self.reading_window.final_dict['glob_attr_list']
        self.list_of_variables_and_attributes = self.reading_window.final_dict['var_attr_list']
        self.list_of_unread_variables = self.reading_window.final_dict['unread_var']
        self.opened_file.close()
        clear_layout(self.gridLayout)
        if self.file_ext == 'NetCDF Files (*.nc *.cdf)' or self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
            netcdf_gui_initialization(self)
            update_nc_global_attribute_gui(self)
            populate_netcdf_tree_widget(self)
        elif self.file_ext == 'NASA Ames Files (*.na)':
            nasaames_gui_initialization(self)
            update_na_global_attribute_gui(self)
            populate_na_tree_widget(self)
        self.file_is_opened = True
        update_icons_state(self)
        status_bar_update(self)
        self.start_status_bar_msg_thread('The file ' + pathlib.PurePath(self.file_name).name + ' has been opened...')
        logging.info('gui - old_reading_functions.py - reading_file: file loaded, file_ext ' + self.file_ext)


class MyWaitReading(QtWidgets.QDialog, Ui_waitBatchWindow):
    def __init__(self, file_name, file_ext, config_dict):
        logging.debug('gui - old_reading_functions.py - MyWaitReading - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.file_name = file_name
        self.file_ext = file_ext
        self.config_dict = config_dict
        self.spinner = None
        self.read_thread = None
        self.error_occurred = False
        self.success = True
        self.final_dict = None
        self.error_reason = None
        self.setup_spinner()
        self.launch_reading_thread()
        logging.info('gui - old_reading_functions.py - MyWaitReading - ready')

    def update_progress(self, val):
        progress_str, progress_nbr = val[0], val[1]
        if len(progress_str) > 65:
            progress_str = progress_str[:32] + '...' + progress_str[-32:0]
        self.progress_label.setText(progress_str)
        self.progress_bar.setValue(progress_nbr)

    def launch_reading_thread(self):
        logging.debug('gui - old_reading_functions.py - MyWaitReading - launch_reading_thread')
        self.read_thread = ReadFileThread(self.file_name, self.file_ext, self.config_dict)
        self.read_thread.start()
        self.read_thread.progress.connect(self.update_progress)
        self.read_thread.finished.connect(self.reading_finished)
        self.read_thread.error.connect(self.reading_failed)

    def reading_finished(self, final_dict):
        logging.debug('gui - old_reading_functions.py - MyWaitReading - reading_finished')
        self.final_dict = final_dict
        self.close()

    def reading_failed(self, val):
        logging.debug('gui - old_reading_functions.py - MyWaitReading - reading_failed')
        self.error_occurred = True
        self.success = False
        self.error_reason = val
        self.close()

    def setup_spinner(self):
        logging.debug('gui - old_reading_functions.py - MyWaitReading - setup_spinner')
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
        logging.debug('gui - old_reading_functions.py - MyWaitReading - closeWindow')
        self.close()
