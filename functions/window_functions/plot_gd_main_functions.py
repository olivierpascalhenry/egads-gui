import logging
import numpy
import cartopy
import re
import pathlib
from functions.window_functions.plot_gd_option_gui_functions import add_figure_options, add_plot_options
from functions.window_functions.plot_gd_option_secondary_functions import (set_projection_function, wait_window,
                                                                           close_wait_window, update_wait_window,
                                                                           close_wait_window_error)
from functions.thread_functions.plot_functions import DrawGriddedMap
from functions.material_functions import cmap_default_fig_margins, grid_projection_parameters, cmap_dict
import matplotlib.pyplot as plt
import cartopy.util


def prepare_plot_gd_single(self):
    logging.debug('gui - plot_gd_main_functions.py - prepare_plot_gd_single')
    self.plot_type = 'grid'
    lon_dim, lat_dim = False, False
    lon_name, lat_name = None, None
    lon_num, lat_num = None, None
    self.var_name = list(self.variables.keys())[0]
    self.plot_dict = {'var_units': self.variables[self.var_name]['units'],
                      'var_dims': self.variables[self.var_name]['dimensions']}
    dim_list = self.variables[list(self.variables.keys())[0]]['dimensions']
    if not self.config_dict.getboolean('PLOTS', 'geo_as_standard'):
        for i, dim in enumerate(dim_list):
            if str(pathlib.Path(dim).name).lower() in ['longitude', 'long', 'lon']:
                lon_dim = True
                lon_name = dim
                lon_num = i
            if str(pathlib.Path(dim).name).lower() in ['latitude', 'lat']:
                lat_dim = True
                lat_name = dim
                lat_num = i
        if lon_dim and lat_dim:
            geo_dict = {'lon_name': lon_name, 'lat_name': lat_name, 'lon_num': lon_num, 'lat_num': lat_num,
                        'dim_list': dim_list}
            prepare_default_grid_dictionary(self, geo_dict)
        else:
            if self.config_dict.getboolean('PLOTS', 'manual_axis_distribution'):
                if self.config_dict.get('PLOTS', 'first_dimension_axis') == 0:
                    prepare_default_grid_dictionary(self)
                else:
                    pass
            else:
                prepare_default_grid_dictionary(self)
    else:
        if self.config_dict.getboolean('PLOTS', 'manual_axis_distribution'):
            if self.config_dict.get('PLOTS', 'first_dimension_axis') == 0:
                prepare_default_grid_dictionary(self)
            else:
                pass
        else:
            prepare_default_grid_dictionary(self)
    set_single_gd_plt_options(self)
    set_single_gd_fig_options(self)
    add_figure_options(self)
    add_plot_options(self)
    plot_single_grid_start(self)


def prepare_default_grid_dictionary(self, geo_dict=None):
    logging.debug('gui - plot_gd_main_functions.py - prepare_default_grid_dictionary')
    if geo_dict is not None:
        lon_name = geo_dict['lon_name']
        lat_name = geo_dict['lat_name']
        lon_num = geo_dict['lon_num']
        lat_num = geo_dict['lat_num']
        dim_list = geo_dict['dim_list']
        self.plot_dict['georeferenced'] = True
        self.plot_dict['lon_name'] = lon_name
        self.plot_dict['lon_values'] = self.dimensions[lon_name]['values']
        self.plot_dict['lon_units'] = self.dimensions[lon_name]['units']
        self.plot_dict['lon_num'] = lon_num
        self.plot_dict['lat_name'] = lat_name
        self.plot_dict['lat_values'] = self.dimensions[lat_name]['values']
        self.plot_dict['lat_units'] = self.dimensions[lat_name]['units']
        self.plot_dict['lat_num'] = lat_num
        dim_list.remove(lon_name)
        dim_list.remove(lat_name)
        if dim_list:
            self.plot_dict['layer_idx'] = 0
            self.plot_dict['layer_name'] = dim_list[0]
            self.plot_dict['layer_values'] = self.dimensions[dim_list[0]]['values']
            self.plot_dict['layer_units'] = self.dimensions[dim_list[0]]['units']
            self.plot_dict['layer_num'] = self.variables[list(self.variables.keys())[0]]['dimensions'].index(
                dim_list[0])
            self.pw_plotWindow_lb_1.setText(dim_list[0])
            self.pw_plotWindow_cb_1.addItems([str(item) for item in self.dimensions[dim_list[0]]['values'].tolist()])
            self.pw_plotWindow_cb_1.currentIndexChanged.connect(self.navigate_into_layers)
    else:
        x_name = self.variables[list(self.variables.keys())[0]]['dimensions'][1]
        y_name = self.variables[list(self.variables.keys())[0]]['dimensions'][0]
        self.plot_dict['georeferenced'] = False
        self.plot_dict['projection'] = None
        self.plot_dict['lon_name'] = x_name
        self.plot_dict['lon_values'] = self.dimensions[x_name]['values']
        self.plot_dict['lon_units'] = self.dimensions[x_name]['units']
        self.plot_dict['lon_num'] = 0
        self.plot_dict['lat_name'] = y_name
        self.plot_dict['lat_values'] = self.dimensions[y_name]['values']
        self.plot_dict['lat_units'] = self.dimensions[y_name]['units']
        self.plot_dict['lat_nums'] = 1
        if len(self.variables[list(self.variables.keys())[0]]['dimensions']) > 2:
            z_name = self.variables[list(self.variables.keys())[0]]['dimensions'][2]
            self.plot_dict['layer_idx'] = 0
            self.plot_dict['layer_name'] = z_name
            self.plot_dict['layer_values'] = self.dimensions[z_name]['values']
            self.plot_dict['layer_units'] = self.dimensions[z_name]['units']
            self.plot_dict['layer_num'] = 2
            self.pw_plotWindow_lb_1.setText(z_name)
            self.pw_plotWindow_cb_1.addItems([str(item) for item in self.dimensions[z_name]['values'].tolist()])
            self.pw_plotWindow_cb_1.currentIndexChanged.connect(self.navigate_into_layers)


def set_single_gd_fig_options(self):
    logging.debug('gui - plot_gd_main_functions.py - set_single_gd_fig_options')
    self.gd_figure_options['title'] = ''
    self.gd_figure_options['title_font'] = self.default_font
    self.gd_figure_options['title_size'] = 10
    self.gd_figure_options['title_xpos'] = 0.5
    self.gd_figure_options['title_ypos'] = 1.08
    self.gd_figure_options['default_title_xpos'] = 0.5
    self.gd_figure_options['default_title_ypos'] = 1.08
    self.gd_figure_options['xlabel'] = self.plot_dict['lon_name']
    self.gd_figure_options['xlabel_font'] = self.default_font
    self.gd_figure_options['xlabel_size'] = 10
    self.gd_figure_options['xlabel_xpos'] = 0.5
    self.gd_figure_options['xlabel_ypos'] = -0.07
    self.gd_figure_options['default_xlabel_xpos'] = 0.5
    self.gd_figure_options['default_xlabel_ypos'] = -0.07
    self.gd_figure_options['ylabel'] = self.plot_dict['lat_name']
    self.gd_figure_options['ylabel_font'] = self.default_font
    self.gd_figure_options['ylabel_size'] = 10
    self.gd_figure_options['ylabel_xpos'] = -0.07
    self.gd_figure_options['ylabel_ypos'] = 0.5
    self.gd_figure_options['default_ylabel_xpos'] = -0.07
    self.gd_figure_options['default_ylabel_ypos'] = 0.5
    self.gd_figure_options['margin_left'] = cmap_default_fig_margins()[self.gd_plot_options['colorbar_position']][
        'margin_left']
    self.gd_figure_options['margin_right'] = cmap_default_fig_margins()[self.gd_plot_options['colorbar_position']][
        'margin_right']
    self.gd_figure_options['margin_bottom'] = cmap_default_fig_margins()[self.gd_plot_options['colorbar_position']][
        'margin_bottom']
    self.gd_figure_options['margin_top'] = cmap_default_fig_margins()[self.gd_plot_options['colorbar_position']][
        'margin_top']


def set_single_gd_plt_options(self):
    logging.debug('gui - plot_gd_main_functions.py - set_single_gd_plt_options')
    if self.plot_dict['georeferenced']:
        self.gd_plot_options['xticks'] = [-180., -120., -60., 0., 60., 120., 180.]
        self.gd_plot_options['yticks'] = [-100.,  -80., -60., -40., -20., 0., 20., 40., 60., 80., 100.]
        self.gd_ticks_options['xticks'] = [-180., -120., -60., 0., 60., 120., 180.]
        self.gd_ticks_options['yticks'] = [-100., -80., -60., -40., -20., 0., 20., 40., 60., 80., 100.]
        self.gd_extent_options['ymin'] = -90
        self.gd_extent_options['ymax'] = 90
        self.gd_extent_options['xmin'] = -180
        self.gd_extent_options['xmax'] = 180
        self.gd_extent_options['central_longitude_extent'] = True
        self.gd_plot_options['ymin'] = -90
        self.gd_plot_options['ymax'] = 90
        self.gd_plot_options['xmin'] = -180
        self.gd_plot_options['xmax'] = 180
        self.gd_plot_options['central_longitude_extent'] = True
        self.gd_layer_order = {'Background': 1, 'Data': 3, 'Coasts': 4, 'Lands': 2, 'Rivers': 5, 'Lakes': 6, 'Grid': 7}
        self.gd_plot_options['layer_order'] = {'Background': 1, 'Data': 3, 'Coasts': 4, 'Lands': 2, 'Rivers': 5,
                                               'Lakes': 6, 'Grid': 7}
        self.gd_plot_options['projection'] = 'PlateCarree'
        self.gd_plot_options['projection_options'] = grid_projection_parameters()['PlateCarree']
        self.gd_projection_options = grid_projection_parameters()['PlateCarree']
        self.gd_plot_options['coast'] = True
        self.gd_plot_options['coast_resolution'] = '110m'
        self.gd_plot_options['coast_line_width'] = 1
        self.gd_plot_options['coast_line_color'] = 'black'
        self.gd_plot_options['default_coast_line_width'] = 1
        self.gd_plot_options['default_coast_line_color'] = 'black'
        self.gd_plot_options['land'] = True
        self.gd_plot_options['land_color'] = '#e6e6e6'
        self.gd_plot_options['default_land_color'] = '#e6e6e6'
        self.gd_plot_options['ocean'] = True
        self.gd_plot_options['ocean_color'] = '#e6f5ff'
        self.gd_plot_options['default_ocean_color'] = '#e6f5ff'
        self.gd_plot_options['river'] = False
        self.gd_plot_options['river_resolution'] = '110m'
        self.gd_plot_options['river_line_width'] = 0.5
        self.gd_plot_options['river_line_color'] = 'blue'
        self.gd_plot_options['river_fill_color'] = 'blue'
        self.gd_plot_options['default_river_line_width'] = 0.5
        self.gd_plot_options['default_river_line_color'] = 'blue'
        self.gd_plot_options['default_river_fill_color'] = 'blue'
    self.gd_plot_options['grid'] = True
    self.gd_plot_options['grid_style'] = '-'
    self.gd_plot_options['grid_size'] = 0.5
    self.gd_plot_options['grid_color'] = 'black'
    self.gd_plot_options['default_grid_size'] = 0.5
    self.gd_plot_options['default_grid_color'] = 'black'
    self.gd_plot_options['labels'] = True
    self.gd_plot_options['labels_top'] = True
    self.gd_plot_options['labels_bottom'] = False
    self.gd_plot_options['labels_right'] = False
    self.gd_plot_options['labels_left'] = True
    self.gd_plot_options['colorbar'] = True
    self.gd_plot_options['colorbar_style'] = 'jet'
    self.gd_plot_options['colorbar_legend'] = self.plot_dict['var_units']
    self.gd_plot_options['colorbar_position'] = 3
    self.gd_plot_options['colorbar_reversed'] = False
    self.gd_plot_options['colorbar_automatic_values'] = True
    self.gd_plot_options['colorbar_automatic_dimensions'] = True
    self.gd_plot_options['colorbar_height'] = 0.7
    self.gd_plot_options['colorbar_width'] = 0.02
    self.gd_plot_options['colorbar_axis_xposition'] = 0.92
    self.gd_plot_options['colorbar_axis_yposition'] = 0.13
    self.gd_plot_options['default_colorbar_height'] = 0.7
    self.gd_plot_options['default_colorbar_width'] = 0.02
    self.gd_plot_options['default_colorbar_axis_xposition'] = 0.92
    self.gd_plot_options['default_colorbar_axis_yposition'] = 0.13
    self.gd_plot_options['colorbar_max_value'] = None
    self.gd_plot_options['colorbar_min_value'] = None
    self.gd_plot_options['colorbar_step_value'] = None
    self.gd_plot_options['colorbar_ticks'] = self.gd_cbar_ticks_options


def plot_single_grid_start(self):
    logging.debug('gui - plot_gd_main_functions.py - plot_single_grid_start')
    if self.plot_dict['georeferenced']:
        proj_instance = set_projection_function(self.gd_plot_options['projection'],
                                                self.gd_plot_options['projection_options'])
        self.plot_dict['projection_instance'] = proj_instance

    self.plot_dict['ax'] = plt.subplot(len(self.variables), 1, 1, projection=self.plot_dict['projection_instance'])
    self.plot_dict['ax'].set_global()
    self.draw_map_thread = DrawGriddedMap(self.canvas, self.variables, self.var_name, self.plot_dict,
                                          self.gd_figure_options, self.gd_plot_options, self.gui_path)
    self.draw_map_thread.started.connect(lambda: wait_window(self))
    self.draw_map_thread.update.connect(lambda val: update_wait_window(self, val))
    self.draw_map_thread.finished.connect(lambda: close_wait_window(self))
    self.draw_map_thread.error.connect(lambda val: close_wait_window_error(self, val))
    self.draw_map_thread.start()


def update_gd_fig_plt_options(self):
    logging.debug('gui - plot_gd_main_functions.py - update_gd_fig_plt_options')
    if "activated" in self.action_pan.objectName():
        self.plot_pan()
    if "activated" in self.action_zoom.objectName():
        self.plot_zoom()

    if self.plot_dict['georeferenced']:
        if self.gd_ticks_options:
            self.gd_plot_options['xticks'] = self.gd_ticks_options['xticks']
            self.gd_plot_options['yticks'] = self.gd_ticks_options['yticks']
        else:
            self.gd_plot_options['xticks'] = None
            self.gd_plot_options['yticks'] = None
        if self.gd_extent_options:
            self.gd_plot_options['ymin'] = self.gd_extent_options['ymin']
            self.gd_plot_options['ymax'] = self.gd_extent_options['ymax']
            self.gd_plot_options['xmin'] = self.gd_extent_options['xmin']
            self.gd_plot_options['xmax'] = self.gd_extent_options['xmax']
            if self.gd_extent_options:
                self.gd_plot_options['central_longitude_extent'] = self.gd_extent_options['central_longitude_extent']
        else:
            self.gd_plot_options['ymin'] = None
            self.gd_plot_options['ymax'] = None
            self.gd_plot_options['xmin'] = None
            self.gd_plot_options['xmax'] = None
            self.gd_plot_options['central_longitude_extent'] = None
        self.gd_plot_options['layer_order'] = self.gd_layer_order
        self.gd_plot_options['projection'] = str(self.pw_grid_combobox_7.currentText())
        self.gd_plot_options['projection_options'] = self.gd_projection_options
        self.gd_plot_options['coast'] = self.pw_grid_checkbox_6.isChecked()
        self.gd_plot_options['coast_resolution'] = str(self.pw_grid_combobox_12.currentText())
        self.gd_plot_options['coast_line_width'] = float(self.pw_grid_line_12.text())
        if str(self.pw_grid_combobox_13.currentText()) == 'HEX Color':
            if self.pw_grid_line_13.text():
                hex_code = str(self.pw_grid_line_13.text())
                if '#' not in hex_code:
                    hex_code = '#' + hex_code
                if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                    self.gd_plot_options['coast_line_color'] = hex_code
                else:
                    self.gd_plot_options['coast_line_color'] = self.gd_plot_options['default_coast_line_color']
            else:
                self.gd_plot_options['coast_line_color'] = self.gd_plot_options['default_coast_line_color']
        elif str(self.pw_grid_combobox_13.currentText()) == 'RGB Color':
            try:
                r = float(self.pw_grid_line_13.text()) / 255.
                g = float(self.pw_grid_line_14.text()) / 255.
                b = float(self.pw_grid_line_15.text()) / 255.
                self.gd_plot_options['coast_line_color'] = (r, g, b)
            except ValueError:
                self.gd_plot_options['coast_line_color'] = self.gd_plot_options['default_coast_line_color']
        else:
            self.gd_plot_options['coast_line_color'] = str(self.pw_grid_combobox_13.currentText()).lower()
        self.gd_plot_options['land'] = self.pw_grid_checkbox_8.isChecked()
        if str(self.pw_grid_combobox_14.currentText()) == 'HEX Color':
            if self.pw_grid_line_18.text():
                hex_code = str(self.pw_grid_line_18.text())
                if '#' not in hex_code:
                    hex_code = '#' + hex_code
                if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                    self.gd_plot_options['land_color'] = hex_code
                else:
                    self.gd_plot_options['land_color'] = self.gd_plot_options['default_land_color']
            else:
                self.gd_plot_options['land_color'] = self.gd_plot_options['default_land_color']
        elif str(self.pw_grid_combobox_14.currentText()) == 'RGB Color':
            try:
                r = float(self.pw_grid_line_18.text()) / 255.
                g = float(self.pw_grid_line_16.text()) / 255.
                b = float(self.pw_grid_line_17.text()) / 255.
                self.gd_plot_options['land_color'] = (r, g, b)
            except ValueError:
                self.gd_plot_options['land_color'] = self.gd_plot_options['default_land_color']
        else:
            self.gd_plot_options['land_color'] = str(self.pw_grid_combobox_14.currentText()).lower()
        self.gd_plot_options['ocean'] = self.pw_grid_checkbox_9.isChecked()
        if str(self.pw_grid_combobox_19.currentText()) == 'HEX Color':
            if self.pw_grid_line_30.text():
                hex_code = str(self.pw_grid_line_30.text())
                if '#' not in hex_code:
                    hex_code = '#' + hex_code
                if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                    self.gd_plot_options['ocean_color'] = hex_code
                else:
                    self.gd_plot_options['ocean_color'] = self.gd_plot_options['default_ocean_color']
            else:
                self.gd_plot_options['ocean_color'] = self.gd_plot_options['default_ocean_color']
        elif str(self.pw_grid_combobox_19.currentText()) == 'RGB Color':
            try:
                r = float(self.pw_grid_line_30.text())
                g = float(self.pw_grid_line_31.text())
                b = float(self.pw_grid_line_32.text())
                self.gd_plot_options['ocean_color'] = (r, g, b)
            except ValueError:
                self.gd_plot_options['ocean_color'] = self.gd_plot_options['default_ocean_color']
        else:
            self.gd_plot_options['ocean_color'] = str(self.pw_grid_combobox_19.currentText()).lower()
        self.gd_plot_options['river'] = self.pw_grid_checkbox_7.isChecked()
        self.gd_plot_options['river_resolution'] = str(self.pw_grid_combobox_15.currentText())
        self.gd_plot_options['river_line_width'] = float(self.pw_grid_line_19.text())
        if str(self.pw_grid_combobox_16.currentText()) == 'HEX Color':
            if self.pw_grid_line_20.text():
                hex_code = str(self.pw_grid_line_20.text())
                if '#' not in hex_code:
                    hex_code = '#' + hex_code
                if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                    self.gd_plot_options['river_line_color'] = hex_code
                else:
                    self.gd_plot_options['river_line_color'] = self.gd_plot_options['default_river_line_color']
            else:
                self.gd_plot_options['river_line_color'] = self.gd_plot_options['default_river_line_color']
        elif str(self.pw_grid_combobox_16.currentText()) == 'RGB Color':
            try:
                r = float(self.pw_grid_line_20.text()) / 255.
                g = float(self.pw_grid_line_21.text()) / 255.
                b = float(self.pw_grid_line_22.text()) / 255.
                self.gd_plot_options['river_line_color'] = (r, g, b)
            except ValueError:
                self.gd_plot_options['river_line_color'] = self.gd_plot_options['default_river_line_color']
        else:
            self.gd_plot_options['river_line_color'] = str(self.pw_grid_combobox_16.currentText()).lower()

        if str(self.pw_grid_combobox_17.currentText()) == 'HEX Color':
            if self.pw_grid_line_23.text():
                hex_code = str(self.pw_grid_line_23.text())
                if '#' not in hex_code:
                    hex_code = '#' + hex_code
                if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                    self.gd_plot_options['river_fill_color'] = hex_code
                else:
                    self.gd_plot_options['river_fill_color'] = self.gd_plot_options['default_river_fill_color']
            else:
                self.gd_plot_options['river_fill_color'] = self.gd_plot_options['default_river_fill_color']
        elif str(self.pw_grid_combobox_17.currentText()) == 'RGB Color':
            try:
                r = float(self.pw_grid_line_23.text()) / 255.
                g = float(self.pw_grid_line_24.text()) / 255.
                b = float(self.pw_grid_line_25.text()) / 255.
                self.gd_plot_options['river_fill_color'] = (r, g, b)
            except ValueError:
                self.gd_plot_options['river_fill_color'] = self.gd_plot_options['default_river_fill_color']
        else:
            self.gd_plot_options['river_fill_color'] = str(self.pw_grid_combobox_17.currentText()).lower()

    self.gd_plot_options['grid'] = self.pw_grid_checkbox_1.isChecked()
    self.gd_plot_options['grid_style'] = str(self.pw_grid_combobox_8.currentText()).lower()
    try:
        self.gd_plot_options['grid_size'] = float(self.pw_grid_line_4.text())
    except ValueError:
        self.gd_plot_options['grid_size'] = self.gd_plot_options['default_grid_size']

    if str(self.pw_grid_combobox_18.currentText()) == 'HEX Color':
        if self.pw_grid_line_28.text():
            hex_code = str(self.pw_grid_line_28.text())
            if '#' not in hex_code:
                hex_code = '#' + hex_code
            if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                self.gd_plot_options['grid_color'] = hex_code
            else:
                self.gd_plot_options['grid_color'] = self.gd_plot_options['default_grid_color']
        else:
            self.gd_plot_options['grid_color'] = self.gd_plot_options['default_grid_color']
    elif str(self.pw_grid_combobox_18.currentText()) == 'RGB Color':
        try:
            r = float(self.pw_grid_line_28.text()) / 255.
            g = float(self.pw_grid_line_27.text()) / 255.
            b = float(self.pw_grid_line_26.text()) / 255.
            self.gd_plot_options['grid_color'] = (r, g, b)
        except ValueError:
            self.gd_plot_options['grid_color'] = self.gd_plot_options['default_grid_color']
    else:
        self.gd_plot_options['grid_color'] = str(self.pw_grid_combobox_18.currentText()).lower()
    self.gd_plot_options['labels'] = self.pw_grid_checkbox_10.isChecked()
    self.gd_plot_options['labels_top'] = self.pw_grid_checkbox_11.isChecked()
    self.gd_plot_options['labels_bottom'] = self.pw_grid_checkbox_12.isChecked()
    self.gd_plot_options['labels_right'] = self.pw_grid_checkbox_13.isChecked()
    self.gd_plot_options['labels_left'] = self.pw_grid_checkbox_14.isChecked()
    self.gd_plot_options['colorbar'] = self.pw_grid_checkbox_2.isChecked()
    self.gd_plot_options['colorbar_style'] = cmap_dict()[int(self.pw_grid_combobox_10.currentIndex()) + 1]
    self.gd_plot_options['colorbar_legend'] = str(self.pw_grid_line_29.text())
    self.gd_plot_options['colorbar_position'] = int(self.pw_grid_combobox_11.currentIndex())
    self.gd_plot_options['colorbar_reversed'] = self.pw_grid_checkbox_3.isChecked()
    self.gd_plot_options['colorbar_automatic_values'] = self.pw_grid_checkbox_4.isChecked()
    self.gd_plot_options['colorbar_automatic_dimensions'] = self.pw_grid_checkbox_5.isChecked()
    try:
        self.gd_plot_options['colorbar_height'] = float(self.pw_grid_line_11.text())
    except ValueError:
        self.gd_plot_options['colorbar_height'] = self.gd_plot_options['default_colorbar_height']
    try:
        self.gd_plot_options['colorbar_width'] = float(self.pw_grid_line_10.text())
    except ValueError:
        self.gd_plot_options['colorbar_width'] = self.gd_plot_options['default_colorbar_width']
    try:
        self.gd_plot_options['colorbar_axis_xposition'] = float(self.pw_grid_line_8.text())
    except ValueError:
        self.gd_plot_options['colorbar_axis_xposition'] = self.gd_plot_options['default_colorbar_axis_xposition']
    try:
        self.gd_plot_options['colorbar_axis_yposition'] = float(self.pw_grid_line_9.text())
    except ValueError:
        self.gd_plot_options['colorbar_axis_yposition'] = self.gd_plot_options['default_colorbar_axis_yposition']

    try:
        self.gd_plot_options['colorbar_max_value'] = float(self.pw_grid_line_6.text())
    except ValueError:
        self.gd_plot_options['colorbar_max_value'] = None
    try:
        self.gd_plot_options['colorbar_min_value'] = float(self.pw_grid_line_5.text())
    except ValueError:
        self.gd_plot_options['colorbar_min_value'] = None
    try:
        self.gd_plot_options['colorbar_step_value'] = int(self.pw_grid_line_7.text())
    except ValueError:
        self.gd_plot_options['colorbar_step_value'] = None

    self.gd_plot_options['colorbar_ticks'] = self.gd_cbar_ticks_options
    self.gd_figure_options['title'] = str(self.pw_grid_line_1.text())
    self.gd_figure_options['title_font'] = str(self.pw_grid_combobox_1.currentText())
    self.gd_figure_options['title_size'] = int(self.pw_grid_combobox_4.currentText())
    try:
        self.gd_figure_options['title_xpos'] = float(self.pw_grid_line_30.text())
    except ValueError:
        self.gd_figure_options['title_xpos'] = self.gd_figure_options['default_title_xpos']
    try:
        self.gd_figure_options['title_ypos'] = float(self.pw_grid_line_31.text())
    except ValueError:
        self.gd_figure_options['title_ypos'] = self.gd_figure_options['default_title_ypos']
    self.gd_figure_options['xlabel'] = str(self.pw_grid_line_2.text())
    self.gd_figure_options['xlabel_font'] = str(self.pw_grid_combobox_2.currentText())
    self.gd_figure_options['xlabel_size'] = int(self.pw_grid_combobox_5.currentText())
    try:
        self.gd_figure_options['xlabel_xpos'] = float(self.pw_grid_line_32.text())
    except ValueError:
        self.gd_figure_options['xlabel_xpos'] = self.gd_figure_options['default_xlabel_xpos']
    try:
        self.gd_figure_options['xlabel_ypos'] = float(self.pw_grid_line_33.text())
    except ValueError:
        self.gd_figure_options['xlabel_ypos'] = self.gd_figure_options['default_xlabel_ypos']
    self.gd_figure_options['ylabel'] = str(self.pw_grid_line_3.text())
    self.gd_figure_options['ylabel_font'] = str(self.pw_grid_combobox_3.currentText())
    self.gd_figure_options['ylabel_size'] = int(self.pw_grid_combobox_6.currentText())
    try:
        self.gd_figure_options['ylabel_xpos'] = float(self.pw_grid_line_34.text())
    except ValueError:
        self.gd_figure_options['ylabel_xpos'] = self.gd_figure_options['default_ylabel_xpos']
    try:
        self.gd_figure_options['ylabel_ypos'] = float(self.pw_grid_line_35.text())
    except ValueError:
        self.gd_figure_options['ylabel_ypos'] = self.gd_figure_options['default_ylabel_ypos']
    self.gd_figure_options['margin_left'] = float(self.pw_grid_label_5.text())
    self.gd_figure_options['margin_right'] = 1 - float(self.pw_grid_label_9.text())
    self.gd_figure_options['margin_bottom'] = float(self.pw_grid_label_10.text())
    self.gd_figure_options['margin_top'] = 1 - float(self.pw_grid_label_6.text())
    plt.clf()
    plot_single_grid_start(self)
