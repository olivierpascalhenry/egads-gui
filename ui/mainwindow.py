import logging
import time
import os
import pathlib
import io
import configparser
import numpy
import webbrowser
import egads
import shutil
import tempfile
import xml
import datetime
import collections
from ui._version import _gui_version
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from functions.window_functions.option_window_functions import MyOptions
from functions.window_functions.plot_window_functions import PlotWindow
from functions.file_functions.reading_file_functions import reading_file
from functions.material_functions import setup_fonts, extension_filetype_dict_function
from functions.thread_functions.other_functions import StatusbarMsgThread
from functions.thread_functions.update_functions import CheckEGADSGuiUpdateOnline, CheckEGADSVersion
from functions.window_functions.algorithm_windows_functions import MyProcessing, MyAlgorithm
from functions.window_functions.batch_processing_window_functions import MyBatchProcessing
from functions.window_functions.export_window_functions import MyExport
from functions.gui_functions.gui_menu_functions import algorithm_menu_initialization
from functions.gui_functions.gui_support_functions import add_variable_to_widget_tree
from functions.file_functions.saving_file_functions import saving_file
from functions.window_functions.other_windows_functions import (MyAbout, MyDisplay, MyInfo, MyUpdate, MyAsk,
                                                                MyUpdateAvailable, MyExistingVariable,
                                                                MyWarningUpdate)
from functions.window_functions.metadata_windows_functions import (MyGlobalAttributes, MyVariableAttributes,
                                                                   MyNAVariableAttributes, MyGroupAttributes)
from functions.gui_functions.gui_global_functions import (gui_reset_function, file_drop_layout, status_bar_update,
                                                          clear_var_metadata_layout, update_icons_state,
                                                          create_quick_access_menu, create_recent_file_menu)
from functions.gui_functions.gui_netcdf_functions import (update_nc_global_attribute_gui, nc_tree_var_reading,
                                                          update_nc_variable_attribute_gui)
from functions.gui_functions.gui_newvariable_functions import (add_new_variable_tab, populate_newvariable_tree_widget,
                                                               new_tree_var_reading)
from functions.gui_functions.gui_nasaames_functions import (na_tree_var_reading, update_na_global_attribute_gui,
                                                            update_na_variable_attribute_gui)
from functions.utils import (prepare_algorithm_categories, prepare_output_categories, create_algorithm_dict,
                             add_element, get_element_value, full_path_name_from_treewidget, icon_creation_function,
                             multi_full_path_name_from_treewidget, clear_layout)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, user_path, config_dict, frozen, system, installed, parent=None):
        logging.info('gui - egads version: ' + egads.__version__)
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.gui_path = path
        self.user_path = user_path
        self.egads_path = egads.user_path
        self.config_dict = config_dict
        self.frozen_app = frozen
        self.system = system
        self.installed_app = installed
        self.egads_config_dict = egads.config_dict

        QtGui.QFontDatabase.addApplicationFont('fonts/SourceSansPro-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont('fonts/SourceSansPro-SemiBold.ttf')


        self.setupUi(self)
        self.font_list, self.default_font = setup_fonts()
        self.list_of_algorithms = create_algorithm_dict()
        self.modified = False
        self.opened_file = None
        self.file_name = ''
        self.file_ext = ''
        self.default_message = ''
        self.file_is_opened = False
        gui_reset_function(self)
        file_drop_layout(self)
        algorithm_menu_initialization(self)
        self.list_of_dimensions = {}
        self.list_of_global_attributes = {}
        self.list_of_variables_and_attributes = {}
        self.list_of_new_variables_and_attributes = {}
        self.list_of_unread_variables = {}
        self.x_axis_variable_set = False
        self.x_axis_variable_name = None
        self.new_variables = False
        self.x_variable = None
        self.first_time_x_variable = True
        self.gui_update_url = None
        self.statusbar_msg_thread = None
        self.min_egads_version = '1.2.7'
        self.min_egads_branch = 'Lineage'
        self.variable_menu = None
        self.check_egads_version_thread = None
        self.check_gui_update_thread = None
        self.make_window_title()
        self.opened_file_list = []
        self.create_quick_access()
        self.create_recent_access()
        self.check_egads_version()
        self.check_egads_gui_update()
        self.actionCreateVariableBar.setVisible(False)
        self.actionCreate_group.setVisible(False)
        self.start_status_bar_msg_thread('Welcome to the EGADS Lineage GUI !')
        logging.info('gui - mainwindow.py - MainWindow ready')

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

    @QtCore.pyqtSlot()
    def on_actionHelp_triggered(self):
        self.open_help()

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
    def on_actionExport_triggered(self):
        self.export_variables()

    @QtCore.pyqtSlot()
    def on_actionBatch_processing_triggered(self):
        self.batch_processing()

    @QtCore.pyqtSlot()
    def on_actionCloseBar_triggered(self):
        self.before_close_file()

    @QtCore.pyqtSlot()
    def on_actionGlobalAttributesBar_triggered(self):
        self.global_attributes()

    @QtCore.pyqtSlot()
    def on_actionVariableAttributesBar_triggered(self):
        self.variable_attributes()

    @QtCore.pyqtSlot()
    def on_actionCreate_group_triggered(self):
        self.create_group()

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
    def on_actionUpdate_triggered(self):
        self.gui_update_info()

    def right_click_menu(self, relative_position):
        logging.debug('gui - mainwindow.py - MainWindow - right_click_menu')
        if self.tab_view.currentIndex() == 1:
            if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
                nc_tree_var_reading(self)
            else:
                na_tree_var_reading(self)
        elif self.tab_view.currentIndex() == 2:
            new_tree_var_reading(self)
        self.variable_menu = QtWidgets.QMenu()
        if 'dataset' in self.variable_list.selectedItems()[0].toolTip(0):
            display_variable = self.variable_menu.addAction("Display variable")
            plot_variable = self.variable_menu.addAction("Plot variable")
            self.x_variable = self.variable_menu.addAction("Use variable as X axis in plot window")
            if self.x_axis_variable_name is not None:
                if self.x_axis_variable_name[0] == full_path_name_from_treewidget(self.variable_list)[0]:
                    self.x_variable.setIcon(icon_creation_function('activated_icon.svg'))
                else:
                    self.x_variable.setIcon(icon_creation_function('none_icon.svg'))
            else:
                self.x_variable.setIcon(icon_creation_function('none_icon.svg'))
            display_variable.setIcon(icon_creation_function('data_icon.svg'))
            plot_variable.setIcon(icon_creation_function('plot_icon.svg'))
            display_variable.triggered.connect(self.display_variable)
            plot_variable.triggered.connect(self.plot_variable)
            self.x_variable.triggered.connect(self.set_x_variable)
            delete_variable = self.variable_menu.addAction("Delete variable")
        else:
            delete_variable = self.variable_menu.addAction("Delete group")
        delete_variable.setIcon(icon_creation_function('del_icon.svg'))
        delete_variable.triggered.connect(self.delete_variable)
        parent_position = self.variable_list.mapToGlobal(QtCore.QPoint(0, 0))
        self.variable_menu.popup(parent_position + relative_position)

    def open_file(self, file_path=None):
        logging.debug('gui - mainwindow.py - MainWindow - open_file')
        if file_path is None:
            file_name, file_ext = self.get_file_name('open')
            if file_name:
                if self.file_name:
                    self.before_close_file()
                self.file_name = file_name
                self.file_ext = file_ext
            else:
                return
        else:
            if pathlib.Path(file_path).is_file():
                if self.file_name:
                    self.before_close_file()
                self.file_name = file_path
                self.file_ext = extension_filetype_dict_function()[os.path.splitext(file_path)[1]]
            else:
                text = ('EGADS can\'t find the following file:\n\n\t\t\t' + file_path + '\n\nPlease check that the file'
                        + ' exists before trying to open it.')
                info_window = MyInfo(text)
                info_window.exec_()
                return
        if self.file_name:
            self.add_file_to_opened_file_list()
            if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'NASA Ames Files (*.na)',
                                 'Hdf Files (*.h5 *.hdf5 *.he5)']:
                reading_file(self)
            else:
                info_window = MyInfo('This format ' + self.file_ext + ' is not supported actually.')
                info_window.exec_()
            if self.list_of_unread_variables:
                info_text = 'The following variable(s) couldn\'t be loaded:<ul>'
                for var, reason in self.list_of_unread_variables.items():
                    info_text += '<li><b>' + var + '</b> &rarr; ' + reason + '</li>'
                info_text += '</ul><p>Please read the GUI log file to have more details on previous issues.'
                info_window = MyInfo(info_text)
                info_window.exec_()

    def save_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - save_file')
        if self.new_variables:
            text = ('New variables exist in the New variables workspace. If they are not migrated into the '
                    'Variables workspace, they won\'t be saved in the new file.')
            info_window = MyInfo(text)
            info_window.exec_()
        save_file_name, save_file_ext = self.get_file_name('save')
        if save_file_name:
            supported_formats = ['NetCDF Files (*.nc *.cdf)', 'NASA Ames Files (*.na)', 'Hdf Files (*.h5 *.hdf5 *.he5)']
            unsupported_formats = ['CSV Files (*.csv *.dat *.txt)']
            if save_file_ext in supported_formats:
                if save_file_ext == 'NASA Ames Files (*.na)':
                    if not self.check_nasaames_compatibility():
                        info_text = ('The actual NASA Ames file class can only handle FFI equal to 1001. Thus it is '
                                     'not possible at this time to save file with more than one dimension or '
                                     'including groups.')
                        info_window = MyInfo(info_text)
                        info_window.exec_()
                        return
                saving_file(self, save_file_name, save_file_ext, self.file_ext)
            elif save_file_ext in unsupported_formats:
                info_window = MyInfo('This format ' + save_file_ext + ' is not supported actually.')
                info_window.exec_()

    def check_nasaames_compatibility(self):
        na_pass = True
        dim_nbr = 0
        groups = False
        for key, val in self.list_of_variables_and_attributes.items():
            if not isinstance(val[0], egads.EgadsData):
                groups = True
            if val[2]:
                dim_nbr += 1
        if dim_nbr > 1 or groups:
            na_pass = False
        return na_pass

    def export_variables(self):
        logging.debug('gui - mainwindow.py - MainWindow - export_variables')
        export_window = MyExport(self.list_of_variables_and_attributes)
        export_window.exec_()

    def global_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - global_attributes')
        glob_attr_window = MyGlobalAttributes(self.list_of_global_attributes, self.file_ext)
        glob_attr_window.exec_()
        if glob_attr_window.global_attributes is not None:
            self.list_of_global_attributes = glob_attr_window.global_attributes
            if self.file_ext == 'NetCDF Files (*.nc *.cdf)':
                update_nc_global_attribute_gui(self)

            elif self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
                update_nc_global_attribute_gui(self)

            elif self.file_ext == 'NASA Ames Files (*.na)':
                update_na_global_attribute_gui(self)
            self.modified = True
            self.make_window_title()
            self.start_status_bar_msg_thread('Global attributes have been modified...')

    def variable_attributes(self):
        logging.debug('gui - mainwindow.py - MainWindow - variable_attributes')
        dataset = False
        if self.tab_view.currentIndex() == 1:
            variable_tree = self.variable_list
            variable_list = self.list_of_variables_and_attributes
        else:
            variable_tree = self.new_variable_list
            variable_list = self.list_of_new_variables_and_attributes
        path, name = full_path_name_from_treewidget(variable_tree)
        if isinstance(variable_list[path][0], egads.EgadsData):
            dataset = True
        if dataset:
            variable_attributes = variable_list[path][0].metadata
        else:
            variable_attributes = variable_list[path][1]
        if self.file_ext == 'NASA Ames Files (*.na)':
            var_attr_window = MyNAVariableAttributes(path, variable_attributes)
        else:
            if dataset:
                var_attr_window = MyVariableAttributes(path, variable_attributes)
            else:
                var_attr_window = MyGroupAttributes(path, variable_attributes)
        var_attr_window.exec_()
        if var_attr_window.attributes is not None:
            if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
                update_nc_variable_attribute_gui(self)
            else:
                update_na_variable_attribute_gui(self)
            self.modified = True
            self.make_window_title()
            self.start_status_bar_msg_thread('Variable attributes have been modified...')
    
    def display_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_variable')
        var_object = None
        var_path = None
        var_name = None
        if self.tab_view.currentIndex() == 1:
            var_path, var_name = full_path_name_from_treewidget(self.variable_list)
            var_object = self.list_of_variables_and_attributes[var_path]
        elif self.tab_view.currentIndex() == 2:
            var_path, var_name = full_path_name_from_treewidget(self.new_variable_list)
            var_object = self.list_of_new_variables_and_attributes[var_path]
        var_units = var_object[0].metadata['units']
        fill_value = None
        try:
            fill_value = var_object[0].metadata['_FillValue']
        except KeyError:
            try:
                fill_value = var_object[0].metadata['missing_value']
            except KeyError:
                pass
        var_values = var_object[0].value
        dimensions = collections.OrderedDict()
        i = 0
        for key, value in var_object[1].items():
            dimensions[key] = {'length': value, 'axis': i,
                               'values': self.list_of_variables_and_attributes[key][0].value,
                               'units': self.list_of_variables_and_attributes[key][0].metadata['units']}
            i += 1
        logging.debug('gui - mainwindow.py - MainWindow - display_variable : tab index '
                      + str(self.tab_view.currentIndex()) + ', variable ' + var_path)
        display_window = MyDisplay(var_path, var_units, fill_value, var_values, dimensions)
        display_window.exec_()

    def plot_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_variable')
        list_of_variables_and_attributes = None
        varible_tree = None
        if self.tab_view.currentIndex() == 1:
            varible_tree = self.variable_list
            list_of_variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            varible_tree = self.new_variable_list
            list_of_variables_and_attributes = self.list_of_new_variables_and_attributes
        variable_list = multi_full_path_name_from_treewidget(varible_tree)
        variables = collections.OrderedDict()
        dimensions = {}
        for sublist in variable_list:
            var_path, var_name = sublist[0], sublist[1]
            var_units = list_of_variables_and_attributes[var_path][0].metadata['units']
            egads_units = list_of_variables_and_attributes[var_path][0].units
            var = list_of_variables_and_attributes[var_path][0].value
            try:
                fill_value = list_of_variables_and_attributes[var_path][0].metadata['_FillValue']
                try:
                    var[var == fill_value] = numpy.nan
                except ValueError:
                    logging.error('gui - mainwindow.py - MainWindow - plot_variable - impossible to replace missing '
                                  'values by NaN, check variable type for integers')
            except KeyError:
                try:
                    fill_value = list_of_variables_and_attributes[var_path][0].metadata['missing_value']
                    try:
                        var[var == fill_value] = numpy.nan
                    except ValueError:
                        logging.error('gui - mainwindow.py - MainWindow - plot_variable - impossible to replace '
                                      'missing values by NaN, check variable type for integers')
                except KeyError:
                    logging.error('gui - mainwindow.py - MainWindow - plot_variable - no missing value found, '
                                  'impossible to replace missing values by NaN')
            var_dimensions = []
            i = 0
            orig_var_list = self.list_of_variables_and_attributes
            if self.x_axis_variable_name is None:
                for key in list_of_variables_and_attributes[var_path][1]:
                    var_dimensions.append(key)
                    try:
                        dimensions[key]
                    except KeyError:
                        dimensions[key] = {'units': orig_var_list[key][0].metadata['units'], 'axis': i,
                                           'values': orig_var_list[key][0].value, 'name': key}
                    i += 1
            else:
                var_dimensions.append(self.x_axis_variable_name[0])
                try:
                    dimensions[self.x_axis_variable_name[0]]
                except KeyError:
                    dimensions[self.x_axis_variable_name[0]] = {
                        'units': orig_var_list[self.x_axis_variable_name[0]][0].metadata['units'], 'axis': i,
                        'values': orig_var_list[self.x_axis_variable_name[0]][0].value,
                        'name': self.x_axis_variable_name[1]}
                i += 1
            variables[var_path] = {'units': var_units, 'egads_units': egads_units, 'values': var,
                                   'dimensions': var_dimensions, 'name': var_name}

        plot_window = PlotWindow(variables, dimensions, self.x_axis_variable_name, self.font_list, self.default_font,
                                 self.config_dict, self.gui_path)
        plot_window.setModal(True)
        plot_window.exec_()

    def process_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - process_variable')
        processing_window = MyProcessing(self.list_of_algorithms, self.list_of_variables_and_attributes,
                                         self.list_of_new_variables_and_attributes)
        processing_window.exec_()
        if processing_window.new_var_list is not None:
            self.list_of_new_variables_and_attributes.update(processing_window.new_var_list)
            if not self.new_variables:
                self.new_variables = True
                add_new_variable_tab(self)
            populate_newvariable_tree_widget(self)
            self.modified = True
            self.make_window_title()
            self.start_status_bar_msg_thread('New variables have been created...')

    def create_group(self):
        pass

    def create_algorithm(self):
        logging.debug('gui - mainwindow.py - MainWindow - create_algorithm')
        new_algorithm_window = MyAlgorithm(prepare_algorithm_categories(self.list_of_algorithms),
                                           prepare_output_categories(self.list_of_algorithms))
        new_algorithm_window.exec_()
        if not new_algorithm_window.cancel:
            try:
                algorithm_filename = new_algorithm_window.algorithm_filename
                algorithm_category = new_algorithm_window.algorithm_category
                algorithm_name = new_algorithm_window.algorithm_name
                success = new_algorithm_window.success
                if success is True:
                    info_text = ('<p>The algorithm has been successfully created with the following details:'
                                 + '<ul><li>File name: ' + algorithm_filename + '.py</li>'
                                 + '<li>Folder: .egads_lineage/user_algorithms/' + algorithm_category.lower() + '</li>'
                                 + '<li>Algorithm name: ' + algorithm_name + '</li></ul></p>')
                    self.start_status_bar_msg_thread('A new algorithm has been created and saved...')
                else:
                    info_text = ('A critical exception occured during algorithm creation and the \'.py\' file'
                                 + ' couldn\'t be written.')
                info_window = MyInfo(info_text)
                info_window.exec_()
                egads._reload_user_algorithms()
                self.list_of_algorithms = create_algorithm_dict()
                algorithm_menu_initialization(self)
            except AttributeError:
                logging.exception('gui - mainwindow.py - MainWindow - create_algorithm: an exception occurred during '
                                  'the initialization of the algorithm information window.')

    def migrate_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - migrate_variable')
        var_list = list(self.list_of_variables_and_attributes.keys())
        selected_items = self.new_variable_list.selectedItems()
        filtered_list = []
        for item in selected_items:
            var = self.list_of_new_variables_and_attributes['/' + item.text(0)][2] + item.text(0)
            if var in var_list:
                filtered_list.append(var)
        if filtered_list:
            if len(filtered_list) > 1:
                text = 'The following variables already exist in the Variables workspace:<ul>'
                for var in filtered_list:
                    text += '<li>' + var + '</li>'
                text += ('</ul>Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on <b>Cancel</b> '
                         'to cancel the processing.')
            else:
                text = ('The following variable, ' + filtered_list[0] + ', already exists in the Variables '
                        'workspace. Please confirm the overwriting by clicking on <b>Overwrite</b>. Click on '
                        '<b>Cancel</b> to cancel the processing.')
            existing_window = MyExistingVariable(text)
            existing_window.exec_()
            if not existing_window.overwrite:
                return
        for item in selected_items:
            var_name = str(item.text(0))
            sublist = self.list_of_new_variables_and_attributes['/' + var_name]
            self.list_of_variables_and_attributes[sublist[2] + var_name] = sublist[:2]
            self.list_of_new_variables_and_attributes.pop('/' + var_name, 0)
            add_variable_to_widget_tree(self.variable_list, var_name, sublist[2])
            self.new_variable_list.takeTopLevelItem(self.new_variable_list.indexOfTopLevelItem(item))
            self.modified = True
            self.make_window_title()
        self.start_status_bar_msg_thread('The selected variables have been migrated to the main workspace...')
        if self.new_variable_list.topLevelItemCount() == 0:
            clear_layout(self.newvariable_widget_container)
            self.tab_view.removeTab(2)
            self.new_variables = False

    def delete_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - delete_variable - tab index ' + str(
            self.tab_view.currentIndex()))
        variables_and_attributes = None
        list_object = None
        new_tab = False
        if self.tab_view.currentIndex() == 1:
            new_tab = False
            list_object = self.variable_list
            variables_and_attributes = self.list_of_variables_and_attributes
        elif self.tab_view.currentIndex() == 2:
            new_tab = True
            list_object = self.new_variable_list
            variables_and_attributes = self.list_of_new_variables_and_attributes
        undeleted_list = []
        for var in list_object.selectedItems():
            var_path, var_name = full_path_name_from_treewidget(list_object, var)
            if self.file_ext == 'NASA Ames Files (*.na)':
                var_comp_dim = var_name
            else:
                var_comp_dim = var_name + ' (' + var_path[: - len(var_name) - 1] + ')'
            if var_comp_dim not in self.list_of_dimensions:
                if not isinstance(variables_and_attributes[var_path][0], egads.EgadsData):
                    for key in list(variables_and_attributes.keys()):
                        if key.find(var_path) == 0:
                            del variables_and_attributes[key]
                    var.takeChildren()
                    parent = var.parent()
                    if parent is None:
                        list_object.takeTopLevelItem(list_object.indexFromItem(var).row())
                    else:
                        var.parent().removeChild(var)
                else:
                    try:
                        del variables_and_attributes[var_path]
                        parent = var.parent()
                        if parent is None:
                            list_object.takeTopLevelItem(list_object.indexFromItem(var).row())
                        else:
                            var.parent().removeChild(var)
                    except TypeError:
                        logging.exception('gui - mainwindow.py - MainWindow - delete_variable: an exception occured '
                                          'during the deletion of the variable ' + var_name)
                self.modified = True
            else:
                undeleted_list.append(var_name)
        clear_var_metadata_layout(self)
        if new_tab:
            if list_object.topLevelItemCount() == 0:
                clear_layout(self.newvariable_widget_container)
                self.tab_view.removeTab(2)
                self.new_variables = False
        self.make_window_title()
        update_icons_state(self)
        self.start_status_bar_msg_thread('The selected variables/groups have been deleted...')
        if undeleted_list:
            if len(undeleted_list) > 1:
                text = 'Because they are considered as dimensions, the following variables couldn\'t be deleted:<ul>'
                for var in undeleted_list:
                    text += '<li>' + var + '</li>'
            else:
                text = ('Because it is considered as a dimension, the following variable couldn\'t be '
                        'deleted:<ul>''<li>' + undeleted_list[0] + '</li>')
            undeleted_window = MyInfo(text)
            undeleted_window.exec_()

    @staticmethod
    def about_egads():
        logging.debug('gui - mainwindow.py - MainWindow - about_egads')
        egads_version = egads.__version__
        text = ('<p align=\"justify\">EGADS (EUFAR General Airborne Data-processing Software, v' + egads_version
                + ') and its GUI (v' + _gui_version + ') are both Python-based toolboxes for processing airborne '
                + 'atmospheric data and data visualization. <p align=\"justify\">Based on Python 3.5.4 '
                + ' and PyQt 5.11.3, EGADS and its GUI provide a framework for researchers to apply '
                + 'expert-contributed algorithms to data files, and acts as a platform for data intercomparison. '
                + 'Algorithms in EGADS will be contributed by members of the EUFAR Expert Working Group if they are '
                + 'found to be mature and well-established in the scientific community.</p><p align=\"justify\">EGADS '
                + 'and its GUI are under development by EUFAR (European Facility for Airborne Research), an Integrating'
                + ' Activity funded by the European Commission. Specifically, the networking activity Standards & '
                + 'Protocols within EUFAR is responsible for development of toolbox, in addition to developing standar'
                + 'ds for use within the EUFAR community. A compilation of these standards and other Standards & Protoc'
                + 'ols products is available on the EUFAR website: <a http://www.eufar.net/tools><span style=\" text-de'
                + 'coration: underline; color:#0000ff;\">http://www.eufar.net/tools/</a></p>')
        about_window = MyAbout(text)
        about_window.exec_()
    
    def show_options(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_options')
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0)
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        config_string = io.StringIO()
        self.egads_config_dict.write(config_string)
        config_string.seek(0)
        egads_config_dict_copy = configparser.ConfigParser()
        egads_config_dict_copy.read_file(config_string)
        option_window = MyOptions(config_dict_copy, egads_config_dict_copy, self.frozen_app, self.system,
                                  self.installed_app, self.user_path)
        option_window.available_update.connect(self.display_gui_update_button)
        option_window.exec_()
        if not option_window.cancel:
            self.config_dict = option_window.config_dict
            self.egads_config_dict = option_window.egads_config_dict
            ini_file = open(str(pathlib.Path(self.user_path, 'egads_gui.ini')), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            egads_ini_file = open(str(pathlib.Path(self.egads_path, 'egads.ini')), 'w')
            self.egads_config_dict.write(egads_ini_file)
            egads_ini_file.close()
            self.start_status_bar_msg_thread('Options have been modified and saved...')
            if self.config_dict['FILES_FOLDERS'].getboolean('enable_user_folders'):
                create_quick_access_menu(self)
            else:
                self.menuQuick_access.clear()
                self.menuQuick_access.setEnabled(False)
            if self.config_dict['FILES_FOLDERS'].getboolean('keep_opened_files'):
                self.menuOpen_recent.clear()
                self.menuOpen_recent.setEnabled(True)
            else:
                self.menuOpen_recent.clear()
                self.menuOpen_recent.setEnabled(False)
    
    def check_egads_version(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_egads_version')
        if not self.frozen_app:
            egads_version = egads.__version__
            try:
                egads_branch = egads.__branch__
            except KeyError:
                egads_branch = 'master'
            self.check_egads_version_thread = CheckEGADSVersion(egads_version, egads_branch, self.min_egads_version,
                                                                self.min_egads_branch)
            self.check_egads_version_thread.start()
            self.check_egads_version_thread.version_issue.connect(self.parse_egads_version)

    @staticmethod
    def parse_egads_version(version_issue):
        logging.debug('gui - mainwindow.py - MainWindow - parse_egads_version - version_issue ' + str(version_issue))
        egads_version = egads.__version__
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
            info_window = MyInfo(info_text)
            info_window.exec_()

    def check_egads_gui_update(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_egads_gui_updates')
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            try:
                import requests
                self.check_gui_update_thread = CheckEGADSGuiUpdateOnline(_gui_version, self.frozen_app, self.system,
                                                                         self.installed_app)
                self.check_gui_update_thread.start()
                self.check_gui_update_thread.finished.connect(self.display_gui_update_button)
            except ImportError:
                logging.info('gui - mainwindow.py - check_egads_gui_updates - requests is not installed, '
                             'no update check')
        else:
            logging.info('gui - mainwindow.py - check_egads_gui_updates - from options, no update check')

    def display_gui_update_button(self, val):
        logging.debug('gui - mainwindow.py - MainWindow - display_gui_update_button - val ' + str(val))
        if val != 'no new version':
            self.gui_update_url = val
            self.actionSeparator5.setVisible(True)
            self.actionUpdate.setVisible(True)
            self.start_status_bar_msg_thread('An update is available...')

    def gui_update_info(self):
        logging.debug('gui - mainwindow.py - MainWindow - gui_update_info')
        if self.frozen_app:
            if self.system == 'Windows':
                if self.installed_app:
                    warning_update_window = MyWarningUpdate()
                    warning_update_window.exec_()
                    if warning_update_window.update:
                        temp_folder = tempfile.gettempdir()
                        download_window = MyUpdate(self.gui_update_url, temp_folder)
                        download_window.exec_()
                        filename = self.gui_update_url[self.gui_update_url.rfind('/') + 1:]
                        os.startfile(temp_folder + '\\' + filename)
                        time.sleep(0.1)
                        self.close()
                else:
                    updade_window = MyUpdateAvailable(self.gui_update_url)
                    updade_window.exec_()
            elif self.system == 'Linux':
                warning_update_window = MyWarningUpdate()
                warning_update_window.exec_()
                if warning_update_window.update:
                    temp_folder = tempfile.gettempdir()
                    download_window = MyUpdate(self.gui_update_url, temp_folder)
                    download_window.exec_()
                    filename = self.gui_update_url[self.gui_update_url.rfind('/') + 1:]
                    shutil.copy('functions/unzip_update.py', temp_folder)
                    install_folder = self.gui_path + '/'
                    command = ('python3 ' + temp_folder + '/unzip_update.py ' + temp_folder
                               + '/' + filename + ' ' + install_folder)
                    os.system('x-terminal-emulator -e ' + command)
                    time.sleep(1.5)
                    self.close()
        else:
            updade_window = MyUpdateAvailable(self.gui_update_url)
            updade_window.exec_()

    def batch_processing(self):
        logging.debug('gui - mainwindow.py - Mainwindow - batch_processing')
        batch_processing_window = MyBatchProcessing(self.list_of_algorithms, self.config_dict)
        batch_processing_window.exec_()

    def get_file_name(self, action, folder=None):
        logging.debug('gui - mainwindow.py - MainWindow - get_file_name : action ' + str(action))
        if folder is not None:
            file_dialog = QtWidgets.QFileDialog(directory=folder)
        else:
            file_dialog = QtWidgets.QFileDialog()
        filter_types = 'NetCDF Files (*.nc *.cdf);;NASA Ames Files (*.na);;Hdf Files (*.h5 *.hdf5 *.he5)'
        out_file_name, out_file_ext = None, None
        if action == 'save':
            out_file_name, out_file_ext = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
        elif action == 'open':
            out_file_name, out_file_ext = file_dialog.getOpenFileName(self, 'Open File', '', filter_types)
        return str(out_file_name), str(out_file_ext)
    
    def before_close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - before_close_file')
        if self.modified:
            ask_save_window = MyAsk('Close')
            ask_save_window.exec_()
            if ask_save_window.choice == 'save':
                self.save_file()
                self.close_file()
            elif ask_save_window.choice == 'cancel':
                pass
            elif ask_save_window.choice == 'close':
                self.close_file()
        else:
            self.close_file()

    def close_file(self):
        logging.debug('gui - mainwindow.py - MainWindow - close_file')
        self.opened_file.close()
        filename = self.file_name
        self.modified = False
        self.opened_file = None
        self.file_name = ''
        self.file_ext = ''
        self.default_message = ''
        self.file_is_opened = False
        self.list_of_dimensions = {}
        self.list_of_global_attributes = {}
        self.list_of_variables_and_attributes = {}
        self.list_of_new_variables_and_attributes = {}
        self.list_of_unread_variables = {}
        self.x_axis_variable_set = False
        self.x_axis_variable_name = None
        self.new_variables = False
        self.x_variable = None
        self.first_time_x_variable = True
        status_bar_update(self)
        gui_reset_function(self)
        file_drop_layout(self)
        self.make_window_title()
        self.start_status_bar_msg_thread('The file ' + pathlib.PurePath(filename).name + ' has been closed...')

    def set_x_variable(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_x_variable')
        if self.x_axis_variable_set:
            self.x_axis_variable_set = False
            self.x_axis_variable_name = None
            self.start_status_bar_msg_thread('No variable set as a temporary dimension...')
        else:
            self.x_axis_variable_set = True
            self.x_axis_variable_name = full_path_name_from_treewidget(self.variable_list)
            if self.first_time_x_variable:
                self.first_time_x_variable = False
                if not self.config_dict['PLOTS'].getboolean('x_info_disabled'):
                    info_text = ('You have replaced the default dimension by another variable for the first time. '
                                 'Please note that this option only works for time series (one dimension) and not for '
                                 + 'gridded data (two or more dimensions).')
                    info_window = MyInfo(info_text)
                    info_window.exec_()
            msg = 'The variable ' + self.x_axis_variable_name[0] + ' has been set as a temporary dimension...'
            self.start_status_bar_msg_thread(msg)

    def make_window_title(self):
        logging.debug('gui - mainwindow.py - MainWindow - make_window_title : modified ' + str(self.modified))
        if self.modified:
            title_string = 'EUFAR General Airborne Data-processing Software - GUI' + ' - modified'
        else:
            title_string = 'EUFAR General Airborne Data-processing Software - GUI'
        self.setWindowTitle(title_string)

    def start_status_bar_msg_thread(self, message):
        if self.statusbar_msg_thread is not None:
            self.statusbar_msg_thread.stop()
        self.statusbar_msg_thread = StatusbarMsgThread(self.default_message, message)
        self.statusbar_msg_thread.display_msg.connect(self.display_status_bar_msg)
        self.statusbar_msg_thread.start()

    def display_status_bar_msg(self, string):
        self.statusBar.showMessage(string)

    @staticmethod
    def open_help():
        logging.debug('gui - mainwindow.py - MainWindow - open_help')
        webbrowser.open('https://egads-gui.readthedocs.io/en/lineage/')

    def create_quick_access(self):
        if self.config_dict['FILES_FOLDERS'].getboolean('enable_user_folders'):
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')).exists():
                create_quick_access_menu(self)
            else:
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                add_element(doc, "Folders", doc_root)
                f = open(str(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()

    def create_recent_access(self):
        if self.config_dict['FILES_FOLDERS'].getboolean('keep_opened_files'):
            if pathlib.Path(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')).exists():
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'r')
                doc = xml.dom.minidom.parse(f)
                folders = doc.getElementsByTagName('Files')[0]
                nodes = folders.getElementsByTagName('File')
                for node in nodes:
                    self.opened_file_list.append(get_element_value(node, 'Path'))
                f.close()
            else:
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                add_element(doc, "Files", doc_root)
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()
            create_recent_file_menu(self)

    def add_file_to_opened_file_list(self):
        if self.file_name in self.opened_file_list:
            self.opened_file_list.remove(self.file_name)
            self.opened_file_list.insert(0, self.file_name)
        else:
            if len(self.opened_file_list) == 10:
                self.opened_file_list.pop(-1)
            self.opened_file_list.insert(0, self.file_name)
        create_recent_file_menu(self)

    def closeEvent(self, event):
        logging.debug('gui - mainwindow.py - MainWindow - closeEvent')
        if self.config_dict['FILES_FOLDERS'].getboolean('keep_opened_files'):
            if self.opened_file_list:
                doc = xml.dom.minidom.Document()
                doc_root = add_element(doc, "EGADSLineageGui", doc)
                add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
                files = add_element(doc, "Files", doc_root)
                for recent_file in self.opened_file_list:
                    file = add_element(doc, "File", files)
                    add_element(doc, "Path", file, recent_file)
                f = open(str(pathlib.Path(self.user_path).joinpath('opened_file_list.xml')), 'w')
                f.write(doc.toprettyxml())
                f.close()
        if self.modified:
            ask_save_window = MyAsk('Quit')
            ask_save_window.exec_()
            if ask_save_window.choice == 'save':
                self.save_file()
                if self.file_is_opened:
                    self.opened_file.close()
                event.accept()
                logging.info('**********************************')
                logging.info('EGADS GUI ' + _gui_version + ' is closing ...')
                logging.info('**********************************')
            elif ask_save_window.choice == 'cancel':
                event.ignore()
            elif ask_save_window.choice == 'close':
                if self.file_is_opened:
                    self.opened_file.close()
                event.accept()
                logging.info('**********************************')
                logging.info('EGADS GUI ' + _gui_version + ' is closing ...')
                logging.info('**********************************')
        else:
            if self.file_is_opened:
                self.opened_file.close()
            event.accept()
            logging.info('**********************************')
            logging.info('EGADS GUI ' + _gui_version + ' is closing ...')
            logging.info('**********************************')
