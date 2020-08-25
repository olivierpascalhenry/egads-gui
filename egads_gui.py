import logging
import platform
import sys
import os
import pathlib
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow
from ui._version import _gui_version
from functions.utils import create_option_file, create_logging_handlers, update_config_file
import configparser
from PyQt5.QtCore import QT_VERSION_STR as qt_version
from matplotlib import __version__ as mpl_version
try:
    from cartopy import __version__ as cy_version
except ImportError:
    cy_version = None
from simplekml import __version__ as km_version
try:
    from markdown import __version__ as mk_version
except ImportError:
    mk_version = None


def launch_egads_gui(gui_path, user_path):
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('icons/egads_gui_splashscreen.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()
    if getattr(sys, 'frozen', False):
        frozen = True
    else:
        frozen = False
    if not pathlib.Path(pathlib.Path(user_path).joinpath('egads_gui.ini')).is_file():
        if not pathlib.Path(user_path).is_dir():
            pathlib.Path(user_path).mkdir()
        create_option_file(user_path)
    update_config_file(user_path)
    config_dict = configparser.ConfigParser()
    config_dict.read(str(pathlib.Path(user_path).joinpath('egads_gui.ini')))
    create_logging_handlers(config_dict, 'egads_gui.log', user_path)
    logging.info('**********************************')
    logging.info('EGADS GUI ' + _gui_version + ' is starting ...')
    logging.info('**********************************')
    system, release, version = platform.system_alias(platform.system(), platform.release(), platform.version())
    logging.info('gui - operating system: ' + system + ' ' + release + ' (' + version + ')')
    logging.info('gui - gui frozen ? ' + str(frozen))
    installed = None
    if system == 'Windows':
        try:
            import winreg
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            winreg.OpenKey(reg, r'Software\EUFAR\EGADS Lineage GUI')
            if frozen:
                installed = True
            else:
                installed = False
        except FileNotFoundError:
            installed = False
    logging.info('gui - gui installed ? ' + str(installed))
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.info('gui - python version: ' + python_version)
    logging.info('gui - pyqt5 version: ' + qt_version)
    logging.info('gui - matplotlib version: ' + mpl_version)
    logging.info('gui - cartopy version: ' + cy_version)
    logging.info('gui - simplekml version: ' + km_version)
    logging.info('gui - markdown version: ' + mk_version)
    ui = MainWindow(gui_path, user_path, config_dict, frozen, system, installed)
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    user_path = str(pathlib.Path.home().joinpath('.egads_lineage_gui'))
    main_path = os.path.abspath(os.path.dirname(__file__))
    launch_egads_gui(main_path, user_path)
