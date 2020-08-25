import logging
import os
import matplotlib.pyplot as plt
from functions.thread_functions.file_functions import PrintingThread
from functions.window_functions.other_windows_functions import MyWait


def plot_save(self):
    logging.debug('gui - printing_functions.py - plot_save')
    save_file_name, save_file_ext = self.get_file_name()
    if save_file_name:
        out_file_ext = os.path.splitext(os.path.basename(save_file_name))[1]
        if not out_file_ext:
            save_file_name += images_extension_dict()[save_file_ext]
        out_file_ext = os.path.splitext(os.path.basename(save_file_name))[1]
        self.fig_size_proportions = {'real_width': plt.gcf().get_size_inches()[0],
                                     'real_height': plt.gcf().get_size_inches()[1],
                                     'set_height': None, 'set_width': None, 'user_size': False}
        if self.pw_saveOptions_ln_1.text():
            if self.pw_saveOptions_cb_1.currentText() == 'Centimeters':
                self.fig_size_proportions['set_height'] = round((self.fig_size_proportions['set_height']
                                                                 / 2.54) * 100) / 100
            else:
                self.fig_size_proportions['set_height'] = float(self.pw_saveOptions_ln_1.text())
        if self.pw_saveOptions_ln_2.text():
            if self.pw_saveOptions_cb_2.currentText() == 'Centimeters':
                self.fig_size_proportions['set_width'] = round((self.fig_size_proportions['set_width']
                                                                / 2.54) * 100) / 100
            else:
                self.fig_size_proportions['set_width'] = float(self.pw_saveOptions_ln_2.text())
        if self.fig_size_proportions['set_height'] is not None and self.fig_size_proportions['set_width'] is not None:
            if ((self.fig_size_proportions['real_height'] - 0.1) <= self.fig_size_proportions['set_height']
                    <= (self.fig_size_proportions['real_height'] + 0.1)
                    and (self.fig_size_proportions['real_width'] - 0.1) <= self.fig_size_proportions['set_width']
                    <= (self.fig_size_proportions['real_width'] + 0.1)):
                pass
            else:
                self.fig_size_proportions['user_size'] = True
                plt.gcf().set_size_inches(self.fig_size_proportions['set_width'],
                                          self.fig_size_proportions['set_height'])
        kwargs = {'orientation': 'landscape', 'format': None, 'bbox_inches': None, 'pad_inches': 0.1, 'dpi': 100}
        try:
            kwargs['dpi'] = int(self.pw_saveOptions_ln_3.text())
        except ValueError:
            pass
        if out_file_ext == '.jpg':
            pil_kwargs = {'quality': self.pw_saveOptions_sl_1.value()}
        else:
            pil_kwargs = {}
        kwargs['pil_kwargs'] = pil_kwargs
        kwargs['transparent'] = self.pw_saveOptions_ck_1.isChecked()
        self.print_thread = PrintingThread(save_file_name, kwargs)
        self.print_thread.started.connect(lambda: wait_window(self))
        self.print_thread.end.connect(lambda: close_wait_window(self))
        self.print_thread.start()


def wait_window(self):
    logging.debug('gui - printing_functions.py - wait_window')
    info_text = 'Saving figure, please wait...'
    self.mywait_window = MyWait(info_text)
    self.mywait_window.exec_()


def close_wait_window(self):
    logging.debug('gui - printing_functions.py - close_wait_window')
    self.mywait_window.close()
    if self.fig_size_proportions['user_size']:
        plt.gcf().set_size_inches(self.fig_size_proportions['real_width'], self.fig_size_proportions['real_height'])
        self.canvas.draw()
