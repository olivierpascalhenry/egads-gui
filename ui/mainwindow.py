import logging
import os
import copy
import collections
import numpy
import matplotlib
matplotlib.use('Qt5Agg')
from ui._version import _gui_version, _python_version, _qt_version
from egads import __version__ as egads_version
try:
    from egads import __branch__ as egads_branch
except ImportError:
    egads_branch = 'master'
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.other_windows_functions import MyAbout, MyOptions, MyDisplay, MyInfo, MyUpdate
from functions.plot_window_functions import PlotWindow
from functions.metadata_windows_functions import MyGlobalAttributes, MyVariableAttributes
from functions.algorithm_windows_functions import MyProcessing, MyAlgorithm
from functions.gui_functions import gui_initialization, algorithm_list_menu_initialization, clear_gui
from functions.gui_functions import netcdf_gui_initialization, update_icons_state, status_bar_update
from functions.gui_functions import update_global_attribute_gui, update_variable_attribute_gui
from functions.gui_functions import update_new_variable_list_gui
from functions.reading_functions import add_new_variable_gui, netcdf_reading, var_reading, new_var_reading
from functions.material_functions import objects_initialization
from functions.thread_functions import CheckEGADSGuiUpdateOnline, CheckEGADSVersion
from functions.material_functions import setup_fonts
from functions.utils import prepare_algorithm_categories, prepare_output_categories, reload_user_folders


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, parent=None):
        logging.info('gui - egads version: ' + egads_version)
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.config_dict = config_dict
        self.setupUi(self)
        self.font_list, self.default_font = setup_fonts()
        self.list_of_algorithms = dict()
        gui_initialization(self)
        objects_initialization(self)
        algorithm_list_menu_initialization(self)
        self.make_window_title()
        self.variable_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.variable_list.customContextMenuRequested.connect(self.right_click_menu)
        self.check_egads_version()
        self.check_egads_gui_update()
        logging.info('gui - mainwindow.py - MainWindow ready')
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

    @QtCore.pyqtSlot()
    def on_actionAbout_EGADS_triggered(self):
        self.about_egads()

    @QtCore.pyqtSlot()
    def on_actionOptions_triggered(self):
        self.show_options()

    @QtCore.pyqtSlot()
    def on_actionOpenBar_triggered(self):
        self.open_file()

    @QtCore.pyqtSlot()
    def on_actionSaveAsBar_triggered(self):
        self.save_file()

    @QtCore.pyqtSlot()
    def on_actionCloseBar_triggered(self):
        self.close_file()

    @QtCore.pyqtSlot()
    def on_actionGlobalAttributesBar_triggered(self):
        self.global_attributes()

    @QtCore.pyqtSlot()
    def on_actionVariableAttributesBar_triggered(self):
        self.variable_attributes()

    @QtCore.pyqtSlot()
    def on_actionCreateVariableBar_triggered(self):
        self.create_variable()

    @QtCore.pyqtSlot()
    def on_actionMigrateVariableBar_triggered(self):
        self.migrate_variable()

    @QtCore.pyqtSlot()
    def on_actionDeleteVariableBar_triggered(self):
        self.delete_variable()

    @QtCore.pyqtSlot()
    def on_actionAlgorithmsBar_triggered(self):
        self.process_variable()

    @QtCore.pyqtSlot()
    def on_actionCreatealgorithmBar_triggered(self):
        self.create_algorithm()

    @QtCore.pyqtSlot()
    def on_actionDisplayBar_triggered(self):
        self.display_variable()

    @QtCore.pyqtSlot()
    def on_actionPlotBar_triggered(self):
        self.plot_variable()

    @QtCore.pyqtSlot()
    def on_actionUpdateBar_triggered(self):
        self.gui_update_info()

    def right_click_menu(self, relative_position):
        if self.tab_view.currentIndex() == 1:
            var_reading(self)
        elif self.tab_view.currentIndex() == 2:
            new_var_reading(self)
        self.variable_menu = QtWidgets.QMenu()
        display_variable = self.variable_menu.addAction("Display variable")
        plot_variable = self.variable_menu.addAction("Plot variable")
        self.x_variable = self.variable_menu.addAction("Use variable as X axis in plot window")
        delete_variable = self.variable_menu.addAction("Delete variable")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/data_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/plot_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if self.x_axis_variable_name == str(self.variable_list.currentItem().text()):
            activated_icon = "icons/activated_icon.svg"
        else:
            activated_icon = "icons/none_icon.png"
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(activated_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        display_variable.setIcon(icon1)
        plot_variable.setIcon(icon2)
        self.x_variable.setIcon(icon3)
        delete_variable.setIcon(icon4)
        display_variable.triggered.connect(self.display_variable)
        plot_variable.triggered.connect(self.plot_variable)
        delete_variable.triggered.connect(self.delete_variable)
        self.x_variable.triggered.connect(self.set_x_variable)
        parent_position = self.variable_list.mapToGlobal(QtCore.QPoint(0, 0))
        self.variable_menu.move(parent_position + relative_position)
        self.variable_menu.exec_()

    def open_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - open_file')
        self.file_name, self.file_ext = self.get_file_name('open')
        if self.file_name:
            if self.file_ext == 'NetCDF Files (*.nc)' or self.file_ext == 'NASA Ames Files (*.na)':
                if self.file_ext == 'NetCDF Files (*.nc)':
                    netcdf_gui_initialization(self)
                    netcdf_reading(self)
                    update_icons_state(self, 'open_file')
                    status_bar_update(self)
                    self.file_is_opened = True
                else:
                    # elif self.file_ext == 'NASA Ames Files (*.na)':
                    #     nasaames_gui_initialization(self)
                    #     nasaames_reading(self)
                    info_text = 'This format ' + self.file_ext + ' is not supported yet actually.'
                    self.infoWindow = MyInfo(info_text)
                    self.infoWindow.exec_()
            else:
                info_text = 'This format ' + self.file_ext + ' is not supported actually.'
                self.infoWindow = MyInfo(info_text)
                self.infoWindow.exec_()
            if self.list_of_unread_variables:
                info_text = 'The following variable(s) couldn\'t be loaded:<ul>'
                for var, reason in self.list_of_unread_variables.items():
                    info_text += '<li><b>' + var + '</b> &rarr; ' + reason + '</li>'
                info_text += '</ul><p>Please read the GUI log file to have more details on the previous issues'
                self.infoWindow = MyInfo(info_text)
                self.infoWindow.exec_()

    def save_file(self):
        info_text = 'The GUI is still in an early stage of development. Thus it is not possible to save a file. It ' \
                    'will be available in the next version.'
        self.infoWindow = MyInfo(info_text)
        self.infoWindow.exec_()

    def global_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - global_attributes')
        self.globalAttributesWindow = MyGlobalAttributes(copy.deepcopy(self.list_of_global_attributes), self.file_ext)
        self.globalAttributesWindow.exec_()
        try:
            self.list_of_global_attributes = self.globalAttributesWindow.global_attributes
            if self.open_file_ext == 'NetCDF Files (*.nc)':
                update_global_attribute_gui(self, 'NetCDF')
            elif self.open_file_ext == 'NASA Ames Files (*.na)':
                update_global_attribute_gui(self, 'NASA Ames')
            self.modified = True
            self.make_window_title()
        except AttributeError:
            pass

    def variable_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - .variable_attributes')
        variable = None
        if self.tab_view.currentIndex() == 1:
            variable = str(self.variable_list.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_variables_and_attributes[variable][1])
            self.variableAttributesWindow = MyVariableAttributes(variable, variable_attributes, self.file_ext)
        elif self.tab_view.currentIndex() == 2:
            variable = str(self.new_variable_list.currentItem().text())
            variable_attributes = copy.deepcopy(self.list_of_new_variables_and_attributes[variable][1])
            self.variableAttributesWindow = MyVariableAttributes(variable, variable_attributes, self.file_ext)
        self.variableAttributesWindow.exec_()
        try:
            new_attributes = self.variableAttributesWindow.attributes
            if self.tab_view.currentIndex() == 1:
                if self.open_file_ext == 'NASA Ames Files (*.na)':
                    self.list_of_variables_and_attributes[variable][1] = new_attributes
                    self.list_of_variables_and_attributes[new_attributes['standard_name']] = \
                        self.list_of_variables_and_attributes.pop(str(self.variable_list.currentItem().text()))
                    self.variable_list.currentItem().setText(new_attributes['standard_name'])
                    new_attributes['var_name'] = new_attributes['standard_name']
                    
                else:
                    self.list_of_variables_and_attributes[variable][1] = new_attributes    
            elif self.tab_view.currentIndex() == 2:
                if self.open_file_ext == 'NASA Ames Files (*.na)':
                    self.list_of_new_variables_and_attributes[variable][1] = new_attributes
                    self.list_of_new_variables_and_attributes[new_attributes['standard_name']] = \
                        self.list_of_variables_and_attributes.pop(str(self.new_variable_list.currentItem().text()))
                    self.new_variable_list.currentItem().setText(new_attributes['standard_name'])
                    new_attributes['var_name'] = new_attributes['standard_name']
                self.list_of_new_variables_and_attributes[variable][1] = new_attributes    
            update_variable_attribute_gui(self)
            self.modified = True
            self.make_window_title()
        except AttributeError:
            pass
    
    def display_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_variable')
        variable = None
        if self.tab_view.currentIndex() == 1:
            variable = self.list_of_variables_and_attributes[str(self.variable_list.currentItem().text())]
        elif self.tab_view.currentIndex() == 2:
            variable = self.list_of_new_variables_and_attributes[str(self.new_variable_list.currentItem().text())]
        var_name = variable[1]['var_name']
        var_units = variable[1]['units']
        
        fill_value = None
        try:
            fill_value = variable[1]['_FillValue']
        except KeyError:
            try:
                fill_value = variable[1]['missing_value']
            except KeyError:
                pass
        var_values = variable[3].value
        dimensions = collections.OrderedDict()
        i = 0
        for key, value in variable[2].items():
            dimensions[key] = {'length': value,
                               'values': self.list_of_variables_and_attributes[key][3].value,
                               'axis': i,
                               'units': self.list_of_variables_and_attributes[key][1]['units']}
            i += 1
        logging.debug('gui - mainwindow.py - MainWindow - display_variable : tab index '
                      + str(self.tab_view.currentIndex()) + ', variable ' + str(variable[1]['var_name']))
        self.displayWindow = MyDisplay(var_name, var_units, fill_value, var_values, dimensions)
        self.displayWindow.exec_()

    def plot_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_variable')
        variable_list = None
        list_of_variables_and_attributes = None
        if self.tab_view.currentIndex() == 1:
            variable_list = [str(item.text()) for item in self.variable_list.selectedItems()]
            list_of_variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            variable_list = [str(item.text()) for item in self.new_variable_list.selectedItems()]
            list_of_variables_and_attributes = self.list_of_new_variables_and_attributes
        variables = collections.OrderedDict()
        dimensions = {}
        for variable in variable_list:
            var_name = list_of_variables_and_attributes[variable][1]['var_name']
            var_units = list_of_variables_and_attributes[variable][1]['units']
            var = list_of_variables_and_attributes[variable][3].value
            try:
                fill_value = list_of_variables_and_attributes[variable][1]['_FillValue']
                var[var == fill_value] = numpy.nan
            except KeyError:
                try:
                    fill_value = list_of_variables_and_attributes[variable][1]['missing_value']
                    var[var == fill_value] = numpy.nan
                except KeyError:
                    pass
            var_dimensions = []
            i = 0

            if self.x_axis_variable_name is None:
                for key in list_of_variables_and_attributes[variable][2]:
                    var_dimensions.append(key)
                    try:
                        dimensions[key]
                    except KeyError:
                        dimensions[key] = {'units': self.list_of_variables_and_attributes[key][1]['units'],
                                           'values': self.list_of_variables_and_attributes[key][3].value,
                                           'axis': i}
                    i += 1
            else:
                var_dimensions.append(self.x_axis_variable_name)
                try:
                    dimensions[self.x_axis_variable_name]
                except KeyError:
                    dimensions[self.x_axis_variable_name] = {'units': self.list_of_variables_and_attributes[
                        self.x_axis_variable_name][1]['units'],
                                       'values': self.list_of_variables_and_attributes[self.x_axis_variable_name][
                                           3].value,
                                       'axis': i}
                i += 1
            variables[var_name] = {'units': var_units,
                                   'values': var,
                                   'dimensions': var_dimensions}
        self.plotWindow = PlotWindow(variables, dimensions, self.x_axis_variable_name, self.font_list,
                                     self.default_font)
        self.plotWindow.setModal(True)
        self.plotWindow.exec_()

    def process_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - process_variable')
        self.processingWindow = MyProcessing(self.list_of_algorithms,
                                             self.list_of_variables_and_attributes,
                                             self.list_of_new_variables_and_attributes)
        self.processingWindow.exec_()
        try:
            self.list_of_new_variables_and_attributes = self.processingWindow.list_of_new_variables_and_attributes
            if not self.new_variables:
                self.new_variables = True
                add_new_variable_gui(self)
            update_new_variable_list_gui(self)
            self.modified = True
            self.make_window_title()
        except AttributeError:
            pass

    def create_algorithm(self):
        logging.debug('gui - mainwindow.py - MainWindow - create_algorithm')
        algorithm_categories = prepare_algorithm_categories(self.list_of_algorithms)
        output_categories = prepare_output_categories(self.list_of_algorithms)
        self.myAlgorithm = MyAlgorithm(algorithm_categories, output_categories)
        self.myAlgorithm.exec_()
        if not self.myAlgorithm.cancel:
            try:
                algorithm_filename = self.myAlgorithm.algorithm_filename
                algorithm_category = self.myAlgorithm.algorithm_category
                algorithm_name = self.myAlgorithm.algorithm_name
                success = self.myAlgorithm.success
                if success is True:
                    info_text = ('<p>The algorithm has been successfully created with the following details:'
                                 + '<ul><li>File name: ' + algorithm_filename + '.py</li>'
                                 + '<li>Folder: egads/algorithms/user/' + algorithm_category.lower() + '</li>'
                                 + '<li>Algorithm name: ' + algorithm_name + '</li></ul></p>')
                else:
                    info_text = ('A critical exception occured during algorithm creation and the \'.py\' file'
                                 + ' couldn\'t be written.')
                self.infoWindow = MyInfo(info_text)
                self.infoWindow.exec_()
                reload_user_folders()
                algorithm_list_menu_initialization(self)
            except AttributeError:
                logging.exception('gui - mainwindow.py - MainWindow - create_algorithm: an exception occurred during '
                                  'the initialization of the algorithm information window.')

    def migrate_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - migrate_variable : variable ' + str(
            self.new_variable_list.currentItem().text()))
        sublist = self.list_of_new_variables_and_attributes[str(self.new_variable_list.currentItem().text())]
        self.list_of_variables_and_attributes[str(self.new_variable_list.currentItem().text())] = sublist
        self.list_of_new_variables_and_attributes.pop(str(self.new_variable_list.currentItem().text()), 0)
        self.new_variable_list.takeItem(self.new_variable_list.currentRow())
        self.variable_list.addItem(sublist[1]["var_name"])
        self.modified = True
        self.make_window_title()
        try:
            if not self.new_variable_list:
                self.tab_view.removeTab(2)
                self.new_variables = False
        except AttributeError:
            logging.exception(
                'gui - mainwindow.py - MainWindow - migrate_variable: an exception occurred during the removal '
                + 'of the tab 2.')

    def delete_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - delete_variable')
        variables_and_attributes = None
        list_object = None
        if self.tab_view.currentIndex() == 1:
            list_object = self.variable_list
            variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            list_object = self.new_variable_list
            variables_and_attributes = self.list_of_new_variables_and_attributes
        logging.debug('gui - mainwindow.py - MainWindow - delete_variable :, tab index ' + str(
            self.tab_view.currentIndex()) + ', variable ' + str(list_object.currentItem().text()))
        variable = str(list_object.currentItem().text())
        sublist = variables_and_attributes[variable]
        try:
            sublist[1], sublist[2], sublist[3] = 'deleted', 'deleted', 'deleted'
            item = list_object.currentItem()
            list_object.takeItem(list_object.row(item))
            clear_gui(self, 'variable')
            self.modified = True
            self.make_window_title()
        except TypeError:
            logging.exception('gui - mainwindow.py - MainWindow - delete_variable: an exception occured during the '
                              'deletion of the variable ' + str(variable))
        try:
            if not self.new_variable_list:
                self.tab_view.removeTab(2)
                self.new_variables = False
        except AttributeError:
            logging.exception(
                'gui - mainwindow.py - MainWindow - delete_variable: an exception occured during the removal '
                + 'of the tab 2.')
        if not self.variable_list:
            self.actionAlgorithmsBar.setEnabled(False)
            self.actionDeleteVariableBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionPlotBar.setEnabled(False)
            self.actionDisplayBar.setEnabled(False)
            self.actionMigrateVariableBar.setEnabled(False)

    def create_variable(self):
        info_text = 'The GUI is still in an early stage of development. Thus it is not possible to create a new ' \
                    'variable. It will be available in the next version.'
        self.infoWindow = MyInfo(info_text)
        self.infoWindow.exec_()

    def about_egads(self):
        logging.debug('gui - mainwindow.py - MainWindow - about_egads')
        text = ('<p align=\"justify\">EGADS (EUFAR General Airborne Data-processing Software, v' + egads_version
                + ') and its GUI (v' + _gui_version + ') are both Python-based toolboxes for processing airborne '
                + 'atmospheric data and data visualization. <p align=\"justify\">Based on Python ' + _python_version
                + ' and PyQt ' + _qt_version + ', EGADS and its GUI provide a framework for researchers to apply '
                + 'expert-contributed algorithms to data files, and acts as a platform for data intercomparison. '
                + 'Algorithms in EGADS will be contributed by members of the EUFAR Expert Working Group if they are '
                + 'found to be mature and well-established in the scientific community.</p><p align=\"justify\">EGADS '
                + 'and its GUI are under development by EUFAR (European Facility for Airborne Research), an Integrating'
                + ' Activity funded by the European Commission. Specifically, the networking activity Standards & '
                + 'Protocols within EUFAR is responsible for development of toolbox, in addition to developing standar'
                + 'ds for use within the EUFAR community. A compilation of these standards and other Standards & Protoc'
                + 'ols products is available on the EUFAR website: <a http://www.eufar.net/tools><span style=\" text-de'
                + 'coration: underline; color:#0000ff;\">http://www.eufar.net/tools/</a></p>')
        self.aboutWindow = MyAbout(text)
        self.aboutWindow.exec_()
    
    def show_options(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_options')
        self.optionWindow = MyOptions(self.config_dict)
        self.optionWindow.exec_()
        if not self.optionWindow.cancel:
            self.config_dict = self.optionWindow.config_dict
            ini_file = open(os.path.join(self.gui_path, 'egads_gui.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()  
    
    def check_egads_version(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_egads_version')
        self.check_egads_version_thread = CheckEGADSVersion(egads_version, egads_branch, self.min_egads_version,
                                                            self.min_egads_branch)
        self.check_egads_version_thread.start()
        self.check_egads_version_thread.version_issue.connect(self.parse_egads_version)
    
    def parse_egads_version(self, version_issue):
        logging.debug('gui - mainwindow.py - MainWindow - parse_egads_version - version_issue ' + str(version_issue))
        if not version_issue['version'] or not version_issue['branch']:
            info_text = ''
            if not version_issue['version'] and not version_issue['branch']:
                info_text = ('<p>The GUI has detected a deprecated version of EGADS (v' + egads_version + ') and a non'
                             + ' Lineage EGADS branch (master). Please consider updating EGADS Lineage before using '
                             + 'the GUI. Malfunctions can occur with a deprecated version or a wrong branch of the '
                             + 'toolbox.</p>')
            else:
                if not version_issue['version']:
                    info_text = ('<p>The GUI has detected a deprecated version of EGADS (v' + egads_version + '). '
                                 + 'Please consider updating EGADS Lineage before using the GUI. Malfunctions can '
                                 + 'occur with a deprecated version of the toolbox.</p>')
                if not version_issue['branch']:
                    info_text = ('<p>The GUI has detected a a non Lineage EGADS branch (master) . Please consider '
                                 + 'updating EGADS Lineage before using the GUI. Malfunctions can occur with a wrong'
                                 + ' branch of the toolbox.</p>')
            self.infoWindow = MyInfo(info_text)
            self.infoWindow.exec_()

    def check_egads_gui_update(self):
        logging.debug('gui - mainwindow.py - check_egads_gui_updates')
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            self.check_gui_update_thread = CheckEGADSGuiUpdateOnline(_gui_version)
            self.check_gui_update_thread.start()
            self.check_gui_update_thread.finished.connect(self.display_gui_update_button)
        else:
            logging.info('gui - mainwindow.py - check_egads_gui_updates - from options, no update check')

    def display_gui_update_button(self, val):
        logging.debug('gui - mainwindow.py - MainWindow - display_gui_update_button - val ' + str(val))
        if val != 'no new version':
            self.gui_update_url = val
            self.actionSeparator5.setVisible(True)
            self.actionUpdateBar.setVisible(True)

    def gui_update_info(self):
        logging.debug('gui - mainwindow.py - gui_update_info')
        self.updade_window = MyUpdate(self.gui_update_url)
        self.updade_window.exec_()

    def get_file_name(self, action):
        logging.debug('gui - mainwindow.py - get_file_name : action ' + str(action))
        file_dialog = QtWidgets.QFileDialog()
        filter_types = 'NetCDF Files (*.nc);;CSV Files (*.csv *.dat *.txt);;NASA Ames Files (*.na)'
        out_file_name, out_file_ext = None, None
        if action == 'save':
            out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        elif action == 'open':
            out_file_name, out_file_ext = file_dialog.getOpenFileName(self, 'Open File', '', filter_types)
        return str(out_file_name), str(out_file_ext)
    
    def close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - close_file')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        all_buttons = self.tab_view.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            if 'none_button' not in widget.objectName() and widget.objectName():
                widget.setIcon(icon)
                value = self.buttons_lines_dict[str(widget.objectName())]
                linewidget = self.findChildren(QtWidgets.QLineEdit, value[0])
                if not linewidget:
                    linewidget = self.findChildren(QtWidgets.QPlainTextEdit, value[0])
                linewidget[0].setEnabled(False)
                widget.clicked.disconnect()
        self.opened_file.close()
        self.tab_view.setCurrentIndex(0)
        self.file_is_opened = False
        objects_initialization(self)
        status_bar_update(self)
        clear_gui(self)
        update_icons_state(self, 'close_file')
        self.tab_view.removeTab(2)
        self.tab_view.setEnabled(False)
        self.tab_view.setVisible(False)
        self.modified = False
        self.make_window_title()
        self.opened_file = None

    def set_x_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_x_variable')
        if self.x_axis_variable_set:
            self.x_axis_variable_set = False
            self.x_axis_variable_name = None
        else:
            self.x_axis_variable_set = True
            self.x_axis_variable_name = str(self.variable_list.currentItem().text())
            if self.first_time_x_variable:
                self.first_time_x_variable = False
                info_text = ('You have replaced the default dimension by another variable for the first time. Please '
                             + 'note that this option only works for time series (one dimension) and not for gridded '
                             + 'data (two or more dimensions).')
                self.infoWindow = MyInfo(info_text)
                self.infoWindow.exec_()

    def make_window_title(self):
        logging.debug('gui - mainwindow.py - MainWindow - make_window_title : modified ' + str(self.modified))
        if self.modified:
            title_string = "EGADS GUI v" + _gui_version + ' - modified'
        else:
            title_string = "EGADS GUI v" + _gui_version
        self.setWindowTitle(title_string)

    def closeEvent(self, event):
        logging.debug('gui - mainwindow.py - MainWindow - closeEvent')
        logging.info('**********************************')
        logging.info('EGADS GUI is closing ...')
        logging.info('**********************************')
        '''if self.modified == True and self.file_is_opened == True:
            result = self.make_onsave_msg_box('Close', 'Quit EGADS GUI')
            if result == "iw_saveButton":
                self.save_file()
                event.accept()
            elif result == "iw_nosaveButton":
                event.accept()
            else:
                event.ignore()
        if self.file_is_opened == True:
            self.opened_file.close()'''
