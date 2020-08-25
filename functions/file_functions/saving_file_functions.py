import logging
import pathlib
from PyQt5 import QtWidgets, QtGui
from ui.Ui_waitbatchwindow import Ui_waitBatchWindow
from functions.gui_functions.gui_widgets import QtWaitingSpinner
from functions.thread_functions.file_functions import SaveFileThread
from functions.window_functions.other_windows_functions import MyInfo


def saving_file(self, save_file_name, save_file_ext, open_file_ext):
    logging.debug('gui - saving_file_functions.py - saving_file - save_file_name ' + save_file_name)
    self.saving_window = MyWaitSaving(save_file_name, save_file_ext, open_file_ext, self.list_of_global_attributes,
                                      self.list_of_variables_and_attributes)
    self.saving_window.exec_()
    if self.saving_window.error_occurred:
        if self.saving_window.error_reason:
            exc_type = self.saving_window.error_reason[0]
            exc_value = self.saving_window.error_reason[1]
            info_str = ('An exception occurred during the saving of the file. Thus the GUI decided to stop the '
                        'process. Please read the log file to have more details about the exception. Contact the '
                        'developer if the same exception occurs again.<br><br>Exception type: ' + exc_type +
                        '<br><br>Exception value: ' + exc_value)
        else:
            info_str = ('An unexpected error occurred during the saving of the file, thus the GUI decided to stop the '
                        'process. Please read the log file to check which kind of error occurred.')
        self.info_window = MyInfo(info_str)
        self.info_window.exec_()
    if self.saving_window.success:
        self.modified = False
        self.make_window_title()
        self.start_status_bar_msg_thread('The file ' + pathlib.PurePath(save_file_name).name + ' has been saved...')
        logging.info('gui - saving_file_functions.py - saving_file - the file has been saved - save_file_name ' +
                     save_file_name)


class MyWaitSaving(QtWidgets.QDialog, Ui_waitBatchWindow):
    def __init__(self, file_name, file_ext, open_file_ext, glob_attr, var_dict):
        logging.debug('gui - saving_file_functions.py - MyWaitSaving - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.file_name = file_name
        self.file_ext = file_ext
        self.open_file_ext = open_file_ext
        self.glob_attr = glob_attr
        self.var_dict = var_dict
        self.spinner = None
        self.save_thread = None
        self.error_occurred = False
        self.error_reason = ''
        self.success = True
        self.final_dict = None
        self.setup_spinner()
        self.launch_saving_thread()
        logging.info('gui - saving_file_functions.py - MyWaitSaving - ready')

    def update_progress(self, val):
        progress_str, progress_nbr = val[0], val[1]
        if len(progress_str) > 65:
            progress_str = progress_str[:32] + '...' + progress_str[-32:0]
        self.progress_label.setText(progress_str)
        self.progress_bar.setValue(progress_nbr)

    def launch_saving_thread(self):
        logging.debug('gui - saving_file_functions.py - MyWaitSaving - launch_saving_thread')
        self.save_thread = SaveFileThread(self.file_name, self.file_ext, self.open_file_ext, self.glob_attr,
                                          self.var_dict)
        self.save_thread.start()
        self.save_thread.progress.connect(self.update_progress)
        self.save_thread.finished.connect(self.saving_finished)
        self.save_thread.error.connect(self.saving_failed)

    def saving_finished(self):
        logging.debug('gui - saving_file_functions.py - MyWaitSaving - saving_finished')
        self.close()

    def saving_failed(self, val):
        logging.debug('gui - saving_file_functions.py - MyWaitSaving - saving_failed')
        self.error_occurred = True
        self.success = False
        self.error_reason = val
        self.close()

    def setup_spinner(self):
        logging.debug('gui - saving_file_functions.py - MyWaitSaving - setup_spinner')
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
        logging.debug('gui - saving_file_functions.py - MyWaitSaving - closeWindow')
        self.close()
