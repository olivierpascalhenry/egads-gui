import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_plotwindow import Ui_plotWindow
from ui.Ui_plottypewindow import Ui_plottypeWindow
from ui.Ui_tickslabelswindow import Ui_tickslabelsWindow
from functions.utils import icon_creation_function, font_creation_function, clear_layout
from functions.window_functions.other_windows_functions import MyInfo, MySubplot
from functions.thread_functions.plot_functions import ProvideWidthHeight
from functions.material_functions import setup_plot_material
from functions.help_functions import plot_information_text
from functions.window_functions.plot_ts_main_functions import (plot_ts_single, update_single_ts_fig_options,
                                                               update_single_ts_plt_options, plot_ts_multiple,
                                                               update_multiple_ts_plt_options,
                                                               update_multiple_ts_fig_options)
from functions.window_functions.plot_gd_main_functions import (prepare_plot_gd_single, plot_single_grid_start,
                                                               update_gd_fig_plt_options)
from functions.printing_functions import plot_save
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class PlotWindow(QtWidgets.QDialog, Ui_plotWindow):
    def __init__(self, variables, dimensions, font_list, default_font, config_dict, gui_path):
        logging.debug('gui - plot_window_functions.py - PlotWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.resize(1250, 750)
        self.pw_saveOptions_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.pw_saveOptions_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.pw_plotWindow_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.variables = variables
        self.dimensions = dimensions
        self.font_list = font_list
        self.default_font = default_font
        self.config_dict = config_dict
        self.gui_path = gui_path
        setup_plot_material(self)
        self.information_text = plot_information_text()
        self.figure = None
        self.canvas = None
        self.tool_bar = None
        self.action_save_as = None
        self.action_close = None
        self.action_zoom = None
        self.action_pan = None
        self.action_origin = None
        self.navigation_toolbar = None
        self.mywait_window = None
        self.thread_set_width_height = None
        self.draw_map_thread = None
        self.var_name = ''

        self.ts_plot = None

        self.plot_type = ''
        self.plot_dict = {}
        self.ts_figure_options = {}
        self.ts_plot_options = {}
        self.gd_figure_options = {}
        self.gd_plot_options = {}
        self.gd_ticks_options = {}
        self.gd_extent_options = {}
        self.gd_layer_order = {}
        self.gd_cbar_ticks_options = []
        self.gd_projection_options = {}
        self.subplot_ts_fig_list = []
        self.subplot_ts_plt_list = []
        self.setup_toolbar()
        self.setup_plot_area()
        self.action_close.triggered.connect(self.close_window)
        self.action_save_as.triggered.connect(lambda: plot_save(self))
        self.action_pan.triggered.connect(self.plot_pan)
        self.action_zoom.triggered.connect(self.plot_zoom)
        self.action_origin.triggered.connect(self.plot_home)
        self.pw_lock_bt_1.clicked.connect(self.unlock_size_edit)
        self.pw_saveOptions_cb_1.currentIndexChanged.connect(self.convert_inch_cm)
        self.pw_saveOptions_cb_2.currentIndexChanged.connect(self.convert_inch_cm)
        self.pw_saveOptions_sl_1.valueChanged.connect(self.update_quality_value)
        self.pw_saveOptions_ln_3.setText('100')
        self.pw_saveOptions_lb_7.setText('95')
        self.pw_info_bt_1.clicked.connect(self.save_button_information)
        self.pw_info_bt_2.clicked.connect(self.save_button_information)
        self.pw_info_bt_3.clicked.connect(self.save_button_information)
        self.pw_info_bt_4.clicked.connect(self.save_button_information)
        self.pw_navigate_bt_1.clicked.connect(self.navigate_layers_left)
        self.pw_navigate_bt_2.clicked.connect(self.navigate_layers_right)
        self.pw_update_bt_1.clicked.connect(self.update_options)
        self.pw_update_bt_2.clicked.connect(self.update_options)
        # self.set_window_size_thread()
        self.select_plot_type()
        logging.info('gui - plot_window_functions.py - PlotWindow - ready')

    def select_plot_type(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - select_plot_type')
        if len(self.variables) == 1:
            logging.debug('gui - plot_window_functions.py - PlotWindow - select_plot_type - only one variable has '
                          'been found.')
            dim_num = len(self.variables[list(self.variables.keys())[0]]['dimensions'])
            if dim_num == 1:
                self.remove_layer_navigation()
                plot_ts_single(self)
            elif 1 < dim_num < 4:
                self.tab_view.setTabText(1, 'Global options')
                if dim_num < 3:
                    self.remove_layer_navigation()
                try:
                    import cartopy
                    cartopy_module = True
                except ImportError:
                    cartopy_module = False
                if cartopy_module:
                    prepare_plot_gd_single(self)
                else:
                    text = ('Cartopy is not installed. Thus it is not possible to draw maps or multidimensional data. '
                            'You can install Cartopy from:<ul><li>source: https://github.com/SciTools/cartopy</li>'
                            '<li>pip: https://pypi.org/project/Cartopy/</li><li>conda: https://anaconda.org/conda-'
                            'forge/cartopy</li><li>and https://www.lfd.uci.edu/~gohlke/pythonlibs/ for '
                            'Windows</li></ul>')

                    info_window = MyInfo(text)
                    info_window.exec_()
            else:
                logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - EGADS GUI can\'t plot '
                             'variables with more than 3 dimensions.')
                text = 'Actually, EGADS Lineage GUI can\'t plot variables with more than three dimensions.'
                info_window = MyInfo(text)
                info_window.exec_()

        elif len(self.variables) > 1:
            logging.debug('gui - plot_window_functions.py - PlotWindow - select_plot_type - more than one variable '
                          'have been found, ' + str(len(self.variables)))
            dim_num = []
            units = []
            dim_name = []

            for _, value in self.variables.items():
                dim_num.append(len(value['dimensions']))
                dim_name.append(value['dimensions'])
                units.append(value['egads_units'])
            if dim_num.count(dim_num[0]) == len(dim_num):
                if dim_num[0] == 1:
                    if dim_name.count(dim_name[0]) == len(dim_name):
                        if units.count(units[0]) == len(units):
                            result = ''
                            pos_dict = None
                            if int(self.config_dict.get('PLOTS', 'same_unit_plot')) == 2:
                                plot_type_window = PlotTypeWindow()
                                plot_type_window.exec_()
                                result = plot_type_window.result
                            elif int(self.config_dict.get('PLOTS', 'same_unit_plot')) == 0:
                                result = 'plot'
                            elif int(self.config_dict.get('PLOTS', 'same_unit_plot')) == 1:
                                result = 'subplot'
                            if result == 'subplot':
                                if int(self.config_dict.get('PLOTS', 'subplot_disposition')) == 1:
                                    subplot_window = MySubplot(sorted(self.variables.keys()))
                                    subplot_window.exec_()
                                    if subplot_window.subplot_layout:
                                        pos_dict = subplot_window.subplot_layout
                            self.remove_layer_navigation()
                            plot_ts_multiple(self, result, pos_dict)
                        else:
                            pos_dict = None
                            if int(self.config_dict.get('PLOTS', 'subplot_disposition')) == 1:
                                subplot_window = MySubplot(sorted(self.variables.keys()))
                                subplot_window.exec_()
                                if subplot_window.subplot_layout:
                                    pos_dict = subplot_window.subplot_layout
                            self.remove_layer_navigation()
                            plot_ts_multiple(self, 'subplot', pos_dict)
                    else:
                        pos_dict = None
                        if int(self.config_dict.get('PLOTS', 'subplot_disposition')) == 1:
                            subplot_window = MySubplot(sorted(self.variables.keys()))
                            subplot_window.exec_()
                            if subplot_window.subplot_layout:
                                pos_dict = subplot_window.subplot_layout
                        self.remove_layer_navigation()
                        plot_ts_multiple(self, 'subplot', pos_dict)
                else:
                    logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - EGADS GUI can\'t '
                                 'plot more than 1 variable with more than 1 dimensions')

                    text = ('Actually, EGADS Lineage GUI can\'t plot more than one variable with more than one '
                            'dimension each.')
                    info_window = MyInfo(text)
                    info_window.exec_()
            else:
                logging.info('gui - plot_window_functions.py - PlotWindow - select_plot_type - Each variable has a '
                             'different number of dimensions, this is not yet supported')
                text = ('Each variable has a different number of dimensions, this is not yet supported by EGADS '
                        'Lineage GUI')
                info_window = MyInfo(text)
                info_window.exec_()

    def plot_pan(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_pan')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_zoom.setIcon(icon_creation_function('zoom_icon.svg'))
        self.action_zoom.setObjectName("action_zoom")
        if 'activated' in self.action_pan.objectName():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/pan_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action_pan.setIcon(icon_creation_function('pan_icon.svg'))
            self.action_pan.setObjectName("action_pan")
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/pan_icon_activated.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action_pan.setIcon(icon_creation_function('pan_icon_activated.svg'))
            self.action_pan.setObjectName("activated_action_pan")
        self.navigation_toolbar.pan()

    def plot_zoom(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_zoom')
        self.action_pan.setIcon(icon_creation_function('pan_icon.svg'))
        self.action_pan.setObjectName("action_pan")
        if "activated" in self.action_zoom.objectName():
            self.action_zoom.setIcon(icon_creation_function('zoom_icon.svg'))
            self.action_zoom.setObjectName("action_zoom")
        else:
            self.action_zoom.setIcon(icon_creation_function('zoom_icon_activated.svg'))
            self.action_zoom.setObjectName("activated_action_zoom")
        self.navigation_toolbar.zoom()

    def setup_toolbar(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - setup_toolbar')
        self.tool_bar = QtWidgets.QToolBar()
        self.tool_bar.setMinimumSize(QtCore.QSize(0, 0))
        self.tool_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tool_bar.setObjectName("tool_bar")
        self.tool_bar.setFont(font_creation_function('normal'))
        self.tool_bar.setMovable(False)
        self.tool_bar.setIconSize(QtCore.QSize(35, 35))
        self.action_save_as = QtWidgets.QAction(self)
        self.action_save_as.setIcon(icon_creation_function('save_as_icon.svg'))
        self.action_save_as.setObjectName("action_save_as")
        self.action_save_as.setEnabled(True)
        self.action_close = QtWidgets.QAction(self)
        self.action_close.setIcon(icon_creation_function('exit_icon.svg'))
        self.action_close.setObjectName("action_close")
        self.action_zoom = QtWidgets.QAction(self)
        self.action_zoom.setIcon(icon_creation_function('zoom_icon.svg'))
        self.action_zoom.setObjectName("action_zoom")
        self.action_zoom.setEnabled(True)
        self.action_pan = QtWidgets.QAction(self)
        self.action_pan.setIcon(icon_creation_function('pan_icon.svg'))
        self.action_pan.setObjectName("action_pan")
        self.action_pan.setEnabled(True)
        self.action_origin = QtWidgets.QAction(self)
        self.action_origin.setIcon(icon_creation_function('origin_icon.svg'))
        self.action_origin.setObjectName("action_origin")
        self.action_origin.setEnabled(True)
        separator1 = QtWidgets.QAction(self)
        separator1.setEnabled(False)
        separator1.setIcon(icon_creation_function('separator_icon.png'))
        separator1.setObjectName("separator1")
        separator2 = QtWidgets.QAction(self)
        separator2.setEnabled(False)
        separator2.setIcon(icon_creation_function('separator_icon.png'))
        separator2.setObjectName("separator2")
        self.tool_bar.addAction(self.action_save_as)
        self.tool_bar.addAction(separator1)
        self.tool_bar.addAction(self.action_pan)
        self.tool_bar.addAction(self.action_zoom)
        self.tool_bar.addAction(self.action_origin)
        self.tool_bar.addAction(separator2)
        self.tool_bar.addAction(self.action_close)
        self.pw_toolbar_fr.addWidget(self.tool_bar)
        self.tool_bar.setWindowTitle("tool_bar")
        self.action_save_as.setText("Save as...")
        self.action_save_as.setToolTip("Save to a graphic file")
        self.action_close.setText("Close...")
        self.action_close.setToolTip("Close the plot window")
        self.action_zoom.setText("Zoom")
        self.action_zoom.setToolTip("Zoom to rectangle")
        self.action_pan.setText("Pan")
        self.action_pan.setToolTip("Pan axes")
        self.action_origin.setText("Origin")
        self.action_origin.setToolTip("Reset to original view")

    def setup_plot_area(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - setup_plot_area')
        self.figure = plt.figure(facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect('resize_event', self.on_resize)
        self.pw_plot_fr.addWidget(self.canvas)
        self.navigation_toolbar = NavigationToolbar(self.canvas, self)
        self.navigation_toolbar.hide()

    def on_resize(self, _):
        fig_size = plt.gcf().get_size_inches()
        if self.pw_saveOptions_cb_1.currentText() == 'Centimeters':
            h = round((fig_size[1] * 2.54) * 100.) / 100.
            w = round((fig_size[0] * 2.54) * 100.) / 100.
        else:
            h = fig_size[1]
            w = fig_size[0]
        self.pw_saveOptions_ln_1.setText(str(h))
        self.pw_saveOptions_ln_2.setText(str(w))

    def plot_home(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - plot_home')
        self.navigation_toolbar.home()

    def unlock_size_edit(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - unlock_size_edit')
        if not self.pw_saveOptions_ln_1.isEnabled():
            self.pw_lock_bt_1.setIcon(icon_creation_function('unlock_icon.svg'))
            activate = True
        else:
            self.pw_lock_bt_1.setIcon(icon_creation_function('lock_icon.svg'))
            activate = False
        self.pw_saveOptions_ln_1.setEnabled(activate)
        self.pw_saveOptions_ln_2.setEnabled(activate)
        self.pw_saveOptions_cb_1.setEnabled(activate)
        self.pw_saveOptions_cb_2.setEnabled(activate)

    def convert_inch_cm(self, index):
        logging.debug('gui - plot_window_functions.py - PlotWindow - convert_inch_cm')
        if self.sender().objectName() == 'pw_saveOptions_cb_1':
            if index == 0:
                value = round((float(self.pw_saveOptions_ln_1.text()) * 2.54) * 100) / 100
                self.pw_saveOptions_ln_1.setText(str(value))
            else:
                value = round((float(self.pw_saveOptions_ln_1.text()) / 2.54) * 100) / 100
                self.pw_saveOptions_ln_1.setText(str(value))
        else:
            if index == 0:
                value = round((float(self.pw_saveOptions_ln_2.text()) * 2.54) * 100) / 100
                self.pw_saveOptions_ln_2.setText(str(value))
            else:
                value = round((float(self.pw_saveOptions_ln_2.text()) / 2.54) * 100) / 100
                self.pw_saveOptions_ln_2.setText(str(value))

    def update_quality_value(self, val):
        logging.debug('gui - plot_window_functions.py - PlotWindow - update_quality_value')
        self.pw_saveOptions_lb_7.setText(str(val))

    def save_button_information(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - save_button_information')
        info_window = MyInfo(self.information_text[self.sender().objectName()])
        info_window.exec_()

    def figure_button_information(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - figure_button_information')
        if 'pw_grid_info_button' in self.sender().objectName():
            name = self.sender().objectName()
        elif self.sender().objectName() != 'pw_commonOptions_bt_1':
            name = self.sender().objectName()[:-1 * (int(''.join(reversed(self.sender().objectName())).find('_')) + 1)]
        else:
            name = self.sender().objectName()
        info_window = MyInfo(self.information_text[name])
        info_window.exec_()

    def navigate_layers_left(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - navigate_layers_left')
        if self.layer_idx > 0:
            plt.clf()
            self.canvas.draw()
            self.layer_idx -= 1
            self.pw_plotWindow_cb_1.currentIndexChanged.disconnect(self.navigate_into_layers)
            self.pw_plotWindow_cb_1.setCurrentIndex(self.layer_idx)
            self.pw_plotWindow_cb_1.currentIndexChanged.connect(self.navigate_into_layers)
            self.plot_single_grid_start()

    def navigate_layers_right(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - navigate_layers_right')
        if self.plot_dict['layer_idx'] < len(self.plot_dict['layer_values']):
            plt.clf()
            self.canvas.draw()
            self.plot_dict['layer_idx'] += 1
            self.pw_plotWindow_cb_1.currentIndexChanged.disconnect(self.navigate_into_layers)
            self.pw_plotWindow_cb_1.setCurrentIndex(self.plot_dict['layer_idx'])
            self.pw_plotWindow_cb_1.currentIndexChanged.connect(self.navigate_into_layers)
            plot_single_grid_start(self)

    def navigate_into_layers(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - navigate_into_layers')
        self.plot_dict['layer_idx'] = int(self.pw_plotWindow_cb_1.currentIndex())
        plt.clf()
        self.canvas.draw()
        plot_single_grid_start(self)

    def remove_layer_navigation(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - remove_layer_navigation')
        clear_layout(self.horizontalLayout_6)

    def update_options(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - update_options')
        if self.sender().objectName() == 'pw_update_bt_1':
            if self.plot_type == 'single_timeseries' or self.plot_type == 'multiple_timeseries_single_fig':
                update_single_ts_fig_options(self)
            elif self.plot_type == 'multiple_timeseries':
                update_multiple_ts_fig_options(self)
            elif self.plot_type == 'grid':
                update_gd_fig_plt_options(self)
        elif self.sender().objectName() == 'pw_update_bt_2':
            if self.plot_type == 'single_timeseries':
                update_single_ts_plt_options(self)
            elif self.plot_type == 'multiple_timeseries' or self.plot_type == 'multiple_timeseries_single_fig':
                update_multiple_ts_plt_options(self)
            elif self.plot_type == 'grid':
                update_gd_fig_plt_options(self)

    def get_file_name(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        try:
            import PIL
            filter_types = "EPS Files (*.eps);;JPEG Files (*.jpg *.jpeg *.jpe);;PDF Files (*.pdf);;PNG Files (*.png " \
                           "*.pns);;TIFF Files (*.tif *.tiff)"
        except ImportError:
            filter_types = "EPS Files (*.eps);;PDF Files (*.pdf);;PNG Files (*.png *.pns);;TIFF Files (*.tif *.tiff)"
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, "Save File", "", filter_types)
        return str(out_file_name), str(out_file_ext)

    def close_window(self):
        logging.debug('gui - plot_window_functions.py - PlotWindow - close_window')
        self.close()


class PlotTypeWindow(QtWidgets.QDialog, Ui_plottypeWindow):
    def __init__(self):
        logging.debug('gui - plot_window_functions.py - PlotTypeWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.button.clicked.connect(self.close_window)
        self.result = None
        logging.info('gui - plot_window_functions.py - PlotTypeWindow - ready')

    def close_window(self):
        logging.debug('gui - plot_window_functions.py - PlotTypeWindow - close_window')
        if self.radio_button_1.isChecked():
            self.result = 'plot'
        else:
            self.result = 'subplot'
        self.close()


class TicksLabelsWindow(QtWidgets.QDialog, Ui_tickslabelsWindow):
    def __init__(self, text):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - __init__')
        QtWidgets.QDialog.__init__(self, parent=None)
        self.setupUi(self)
        self.ticks_labels = ''
        self.label.setText(text)
        self.ok_button.clicked.connect(self.set_ticks)
        self.cancel_button.clicked.connect(self.close_window)
        self.add_button.clicked.connect(self.add_cell)
        self.del_button.clicked.connect(self.del_cell)
        logging.info('gui - plot_window_functions.py - TicksLabelsWindow - ready')

    def add_cell(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - add_cell')
        self.table.insertColumn(self.table.columnCount())

    def del_cell(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - del_cell')
        self.table.removeColumn(self.table.columnCount() - 1)

    def set_ticks(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - set_ticks')
        for i in range(self.table.columnCount()):
            if self.table.item(0, i).text():
                self.ticks_labels += self.table.item(0, i).text() + '|'
        self.ticks_labels = self.ticks_labels[:-1]
        self.close_window()

    def close_window(self):
        logging.debug('gui - plot_window_functions.py - TicksLabelsWindow - close_window')
        self.close()
