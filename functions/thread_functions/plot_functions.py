import logging
import sys
import time
import numpy
import pathlib
from PyQt5 import QtCore, QtWidgets
import cartopy
import matplotlib as mpl
from functions.material_functions import cmap_default_dimensions, grid_projection_parameters


class DrawGriddedMap(QtCore.QThread):
    started = QtCore.pyqtSignal()
    update = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(list)

    def __init__(self, canvas, variables, var_name, plot_dict, fig_options, plot_options, gui_path):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - DrawGriddedMap - __init__')
        self.canvas = canvas
        self.variables = variables
        self.var_name = var_name
        self.plot_dict = plot_dict
        self.fig_options = fig_options
        self.plot_options = plot_options
        self.gui_path = gui_path

    def run(self):
        logging.debug('gui - file_functions.py - DrawGriddedMap - run')
        self.started.emit()
        try:
            self.update.emit('Rendering data, please wait...')

            if self.plot_dict['georeferenced']:
                try:
                    layer_num = self.plot_dict['layer_num']
                    var_values = numpy.take(self.variables[self.var_name]['values'], self.plot_dict['layer_idx'],
                                            layer_num)
                    var_values, lon = cartopy.util.add_cyclic_point(var_values, coord=self.plot_dict['lon_values'],
                                                                    axis=self.plot_dict['lon_num'] - 1)
                except KeyError:
                    var_values = self.variables[self.var_name]['values']
                    var_values, lon = cartopy.util.add_cyclic_point(var_values, coord=self.plot_dict['lon_values'],
                                                                    axis=self.plot_dict['lon_num'])
                self.plot_dict['var_values'], self.plot_dict['lon_values_cyclic'] = var_values, lon

            else:
                try:
                    layer_num = self.plot_dict['layer_num']
                    var_values = numpy.take(self.variables[self.var_name]['values'], self.plot_dict['layer_idx'], layer_num)
                except KeyError:
                    var_values = self.variables[self.var_name]['values']
                self.plot_dict['var_values'] = var_values
                self.plot_dict['projection_instance'] = None

            drawing_order = self.plot_options['layer_order']
            cmap_name = self.plot_options['colorbar_style']
            if self.plot_options['colorbar_reversed']:
                cmap_name += '_r'
            max_val, min_val, steps, norm, ticks, ticks_lbl = None, None, None, None, None, None
            if not self.plot_options['colorbar_automatic_values']:
                if self.plot_options['colorbar_ticks']:
                    min_val = self.plot_options['colorbar_ticks'][0]
                    max_val = self.plot_options['colorbar_ticks'][-1]
                    # norm = mpl.colors.Normalize(vmin=min_val, vmax=max_val)
                else:
                    max_val = self.plot_options['colorbar_max_value']
                    min_val = self.plot_options['colorbar_min_value']
                    steps = self.plot_options['colorbar_step_value']
                    # norm = mpl.colors.Normalize(vmin=min_val, vmax=max_val)

            if self.plot_options['ocean']:
                if isinstance(self.plot_options['ocean_color'], tuple):
                    r, g, b = self.plot_options['ocean_color']
                elif '#' in self.plot_options['ocean_color']:
                    h = self.plot_options['ocean_color'].lstrip('#')
                    r, g, b = tuple(int(h[i: i + 2], 16) for i in (0, 2, 4))
                else:
                    r, g, b, _ = mpl.colors.to_rgba(self.plot_options['ocean_color'])
                    r = 255 * r
                    g = 255 * g
                    b = 255 * b
                self.plot_dict['ax'].imshow(numpy.tile(numpy.array([[[r, g, b]]], dtype=numpy.uint8), [2, 2, 1]),
                                            origin='upper', transform=cartopy.crs.PlateCarree(),
                                            extent=[-180, 180, -180, 180], zorder=drawing_order['Background'])

            if self.plot_dict['georeferenced']:
                lon_values = self.plot_dict['lon_values_cyclic']
                pcolormesh = self.plot_dict['ax'].pcolormesh(lon_values, self.plot_dict['lat_values'],
                                                             self.plot_dict['var_values'],
                                                             cmap=cmap_name,
                                                             transform=cartopy.crs.PlateCarree(),
                                                             vmin=min_val, vmax=max_val, zorder=drawing_order['Data'])
            else:
                lon_values = self.plot_dict['lon_values']
                pcolormesh = self.plot_dict['ax'].pcolormesh(lon_values, self.plot_dict['lat_values'],
                                                             self.plot_dict['var_values'],
                                                             cmap=cmap_name, zorder=drawing_order['Data'])
            self.plot_dict['pcolormesh'] = pcolormesh
            if self.plot_options['colorbar']:
                self.update.emit('Rendering colorbar, please wait...')
                if self.plot_options['colorbar_automatic_dimensions']:
                    cmap_height = cmap_default_dimensions()[self.plot_options['colorbar_position']]['colorbar_height']
                    cmap_width = cmap_default_dimensions()[self.plot_options['colorbar_position']]['colorbar_width']
                    cmap_xposition = cmap_default_dimensions()[self.plot_options['colorbar_position']][
                        'colorbar_axis_xposition']
                    cmap_yposition = cmap_default_dimensions()[self.plot_options['colorbar_position']][
                        'colorbar_axis_yposition']
                    cmap_orientation = cmap_default_dimensions()[self.plot_options['colorbar_position']]['orientation']
                else:
                    cmap_height = self.plot_options['colorbar_height']
                    cmap_width = self.plot_options['colorbar_width']
                    cmap_xposition = self.plot_options['colorbar_axis_xposition']
                    cmap_yposition = self.plot_options['colorbar_axis_yposition']
                    cmap_orientation = self.plot_options['colorbar_position']
                if steps is not None:
                    ticks = numpy.linspace(min_val, max_val, steps)
                    ticks_lbl = [str(item) for item in ticks]
                elif steps is None and self.plot_options['colorbar_ticks']:
                    ticks = self.plot_options['colorbar_ticks']
                    ticks_lbl = [str(item) for item in ticks]
                cax = mpl.pyplot.axes([cmap_xposition, cmap_yposition, cmap_width, cmap_height])
                cmap = mpl.pyplot.colorbar(pcolormesh, cax=cax, orientation=cmap_orientation, ticks=ticks)
                # cmap = mpl.pyplot.colorbar(pcolormesh, cax=cax, orientation=cmap_orientation, norm=norm, ticks=ticks)
                if cmap_orientation == 'vertical':
                    cmap.ax.set_ylabel(self.plot_options['colorbar_legend'])
                    if ticks_lbl is not None:
                        cmap.ax.set_yticklabels(ticks_lbl)
                else:
                    cmap.ax.set_xlabel(self.plot_options['colorbar_legend'])
                    if ticks_lbl is not None:
                        cmap.ax.set_xticklabels(ticks_lbl)
            if self.plot_dict['georeferenced']:
                self.update.emit('Rendering coasts and lands, please wait...')
                if self.plot_options['coast']:
                    coast_shp_path = ('graphic_materials/shape_files/ne_' + self.plot_options['coast_resolution']
                                      + '_coastline.shp')
                    coast_shp_file = str(pathlib.Path(self.gui_path).joinpath(coast_shp_path))
                    for coast in cartopy.io.shapereader.Reader(coast_shp_file).records():
                        self.plot_dict['ax'].add_geometries([coast.geometry], cartopy.crs.PlateCarree(), antialiased=True,
                                                            edgecolor=self.plot_options['coast_line_color'],
                                                            linewidth=self.plot_options['coast_line_width'],
                                                            facecolor='none', zorder=drawing_order['Coasts'])
                if self.plot_options['land']:
                    land_shp_path = ('graphic_materials/shape_files/ne_' + self.plot_options['coast_resolution']
                                     + '_land.shp')
                    land_shp_file = str(pathlib.Path(self.gui_path).joinpath(land_shp_path))
                    for land in cartopy.io.shapereader.Reader(land_shp_file).records():
                        self.plot_dict['ax'].add_geometries([land.geometry], cartopy.crs.PlateCarree(), antialiased=True,
                                                            edgecolor='none', linewidth=0.,
                                                            zorder=drawing_order['Lands'],
                                                            facecolor=self.plot_options['land_color'])
                self.update.emit('Rendering rivers and lakes, please wait...')
                if self.plot_options['river']:
                    riv_shp_path = ('graphic_materials/shape_files/ne_' + self.plot_options['river_resolution'] +
                                    '_rivers_lake_centerlines.shp')
                    riv_shp_file = str(pathlib.Path(self.gui_path).joinpath(riv_shp_path))
                    for river in cartopy.io.shapereader.Reader(riv_shp_file).records():
                        self.plot_dict['ax'].add_geometries([river.geometry], cartopy.crs.PlateCarree(), antialiased=True,
                                                            edgecolor=self.plot_options['river_line_color'],
                                                            linewidth=self.plot_options['river_line_width'],
                                                            facecolor='none', zorder=drawing_order['Rivers'])
                    lak_shp_path = ('graphic_materials/shape_files/ne_' + self.plot_options['river_resolution'] +
                                    '_lakes.shp')
                    lak_shp_file = str(pathlib.Path(self.gui_path).joinpath(lak_shp_path))
                    for lake in cartopy.io.shapereader.Reader(lak_shp_file).records():
                        self.plot_dict['ax'].add_geometries([lake.geometry], cartopy.crs.PlateCarree(), antialiased=True,
                                                            edgecolor='none', zorder=drawing_order['Lakes'],
                                                            facecolor=self.plot_options['river_fill_color'])
                self.update.emit('Rendering grid, please wait...')

                gl = self.plot_dict['ax'].gridlines(crs=cartopy.crs.PlateCarree(),
                                                    draw_labels=self.plot_options['labels'],
                                                    linewidth=self.plot_options['grid_size'],
                                                    color=self.plot_options['grid_color'], alpha=1,
                                                    linestyle=self.plot_options['grid_style'],
                                                    zorder=drawing_order['Grid'])
                gl.xlines = self.plot_options['grid']
                gl.ylines = self.plot_options['grid']
                gl.xformatter = cartopy.mpl.gridliner.LONGITUDE_FORMATTER
                gl.yformatter = cartopy.mpl.gridliner.LATITUDE_FORMATTER
                if self.plot_options['xticks'] is not None:
                    gl.xlocator = mpl.ticker.FixedLocator(self.plot_options['xticks'])
                    gl.ylocator = mpl.ticker.FixedLocator(self.plot_options['yticks'])
                if self.plot_options['labels']:
                    gl.top_labels = self.plot_options['labels_top']
                    gl.bottom_labels = self.plot_options['labels_bottom']
                    gl.right_labels = self.plot_options['labels_right']
                    gl.left_labels = self.plot_options['labels_left']
                else:
                    gl.top_labels = False
                    gl.bottom_labels = False
                    gl.right_labels = False
                    gl.left_labels = False

                if self.plot_options['ymin'] is not None:

                    y_min = self.plot_options['ymin']
                    y_max = self.plot_options['ymax']
                    x_min = self.plot_options['xmin']
                    x_max = self.plot_options['xmax']

                    if y_min is not None:

                        try:
                            min_latitude = self.plot_options['projection_options']['min_latitude']
                            max_latitude = self.plot_options['projection_options']['max_latitude']
                            if y_max > max_latitude:
                                y_max = max_latitude
                            if y_min < min_latitude:
                                y_min = min_latitude
                        except KeyError:
                            pass

                        if self.plot_options['central_longitude_extent'] is not None:
                            if self.plot_options['central_longitude_extent']:
                                cl = self.plot_options['projection_options']['central_longitude']
                                self.plot_dict['ax'].set_extent([x_min, x_max, y_min, y_max],
                                                                crs=cartopy.crs.PlateCarree(central_longitude=cl))
                            else:
                                self.plot_dict['ax'].set_extent([x_min, x_max, y_min, y_max],
                                                                crs=cartopy.crs.PlateCarree())
                        else:
                            self.plot_dict['ax'].set_extent([x_min, x_max, y_min, y_max], crs=cartopy.crs.PlateCarree())

            else:
                pass
                # subplot['ax'].grid(True)
                # if self.gd_plot_options['grid']:
                #     gl = subplot_dict['ax'].gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=False,
                #                                       linewidth=self.gd_plot_options['grid_size'],
                #                                       color=self.gd_plot_options['grid_color'], alpha=1,
                #                                       linestyle=self.gd_plot_options['grid_style'])

            self.update.emit('Rendering figure, please wait...')
            self.plot_dict['ax'].text(self.fig_options['ylabel_xpos'], self.fig_options['ylabel_ypos'],
                                      self.fig_options['ylabel'], va='center', ha='center', rotation='vertical',
                                      rotation_mode='anchor', transform=self.plot_dict['ax'].transAxes,
                                      fontsize=self.fig_options['ylabel_size'], fontfamily=self.fig_options['ylabel_font'])
            self.plot_dict['ax'].text(self.fig_options['xlabel_xpos'], self.fig_options['xlabel_ypos'],
                                      self.fig_options['xlabel'], va='center', ha='center', rotation='horizontal',
                                      rotation_mode='anchor', transform=self.plot_dict['ax'].transAxes,
                                      fontsize=self.fig_options['xlabel_size'], fontfamily=self.fig_options['xlabel_font'])
            self.plot_dict['ax'].text(self.fig_options['title_xpos'], self.fig_options['title_ypos'],
                                      self.fig_options['title'], va='center', ha='center', rotation='horizontal',
                                      rotation_mode='anchor', transform=self.plot_dict['ax'].transAxes,
                                      fontsize=self.fig_options['title_size'], fontfamily=self.fig_options['title_font'])
            mpl.pyplot.subplots_adjust(left=self.fig_options['margin_left'], right=self.fig_options['margin_right'],
                                       bottom=self.fig_options['margin_bottom'], top=self.fig_options['margin_top'])

            self.canvas.draw()
            self.finished.emit()
        except Exception:
            logging.exception('gui - plot_functions.py - DrawGriddedMap - An exception occured')
            etype, value, _ = sys.exc_info()
            self.error.emit([etype.__name__, str(value)])

    def stop(self):
        logging.debug('gui - file_functions.py - DrawGriddedMap - stop')
        self.terminate()


class ProvideWidthHeight(QtCore.QThread):
    finished = QtCore.pyqtSignal(list)

    def __init__(self):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - ProvideWidthHeight - __init__')

    def run(self):
        logging.debug('gui - file_functions.py - ProvideWidthHeight - run')
        time.sleep(1)
        self.finished.emit([str(6.2), str(12.02)])

    def stop(self):
        logging.debug('gui - file_functions.py - ProvideWidthHeight - stop')
        self.terminate()
