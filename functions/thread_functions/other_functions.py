import logging
import time
from PyQt5 import QtCore


class StatusbarMsgThread(QtCore.QThread):
    display_msg = QtCore.pyqtSignal(str)

    def __init__(self, default_msg, new_msg):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - StatusbarMsgThread - __init__')
        self.default_msg = default_msg
        self.new_msg = new_msg

    def run(self):
        logging.debug('gui - file_functions.py - StatusbarMsgThread - run')
        self.display_msg.emit(self.new_msg)
        time.sleep(5)
        self.display_msg.emit(self.default_msg)

    def stop(self):
        logging.debug('gui - file_functions.py - StatusbarMsgThread - stop')
        self.terminate()
