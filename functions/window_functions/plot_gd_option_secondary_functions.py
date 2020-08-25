import logging
import cartopy
from functions.window_functions.other_windows_functions import (MyWait, MyProjection, MyTicks, MyColorbarTicks,
                                                                MyExtent, MyLayer, MyInfo)
from functions.material_functions import cmap_default_fig_margins, grid_projection_parameters
from PyQt5 import QtCore


def update_gd_slider_value(self, val):
    logging.debug('gui - plot_gd_option_secondary_functions.py - update_gd_slider_value')
    if self.sender().objectName() == 'pw_grid_slider_1':
        self.pw_grid_label_5.setText(str(float(val) / 100))
    elif self.sender().objectName() == 'pw_grid_slider_2':
        self.pw_grid_label_6.setText(str(float(val) / 100))
    elif self.sender().objectName() == 'pw_grid_slider_3':
        self.pw_grid_label_9.setText(str(float(val) / 100))
    elif self.sender().objectName() == 'pw_grid_slider_4':
        self.pw_grid_label_10.setText(str(float(val) / 100))


def display_grid_projection_options(self, projection_options=None):
    logging.debug('gui - plot_gd_option_secondary_functions.py - display_grid_projection_options')
    if projection_options is None:
        projection_options = self.gd_projection_options
    text = 'Options: '
    non_options = ['default_ticks', 'default_extent', 'central_longitude_extent', 'zonal_label_display', 'zlb_defaults']
    for option in sorted(projection_options.keys()):
        if option not in non_options:
            text += option + '=' + str(projection_options[option]) + ' ; '
    text = text[: -3]
    self.pw_grid_label_13.setText(text)


def set_projection_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_projection_options')
    self.gd_projection_options = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]
    display_grid_projection_options(self, self.gd_projection_options)
    self.gd_ticks_options = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['default_ticks']
    self.gd_extent_options = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['default_extent']
    if self.gd_extent_options:
        cle = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['central_longitude_extent']
        self.gd_extent_options['central_longitude_extent'] = cle
    label_display = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['zonal_label_display']
    if self.gd_ticks_options:
        self.pw_grid_set_ticks.setEnabled(True)
        self.pw_grid_label_14.setEnabled(True)
        display_grid_ticks_options(self)
    else:
        self.pw_grid_set_ticks.setEnabled(False)
        self.pw_grid_label_14.setEnabled(False)
        self.pw_grid_label_14.setText('')

    if self.gd_extent_options:
        self.pw_grid_set_extent.setEnabled(True)
        self.pw_grid_label_15.setEnabled(True)
        display_grid_extent(self)
    else:
        self.pw_grid_set_extent.setEnabled(False)
        self.pw_grid_label_15.setEnabled(False)
        self.pw_grid_label_15.setText('')

    if label_display:
        label_dict = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['zlb_defaults']
        self.pw_grid_checkbox_11.setChecked(label_dict['top'])
        self.pw_grid_checkbox_12.setChecked(label_dict['bottom'])
        self.pw_grid_checkbox_13.setChecked(label_dict['right'])
        self.pw_grid_checkbox_14.setChecked(label_dict['left'])
        self.pw_grid_checkbox_11.setEnabled(True)
        self.pw_grid_checkbox_12.setEnabled(True)
        self.pw_grid_checkbox_13.setEnabled(True)
        self.pw_grid_checkbox_14.setEnabled(True)
    else:
        self.pw_grid_checkbox_11.setChecked(True)
        self.pw_grid_checkbox_12.setChecked(True)
        self.pw_grid_checkbox_13.setChecked(True)
        self.pw_grid_checkbox_14.setChecked(True)
        self.pw_grid_checkbox_11.setEnabled(False)
        self.pw_grid_checkbox_12.setEnabled(False)
        self.pw_grid_checkbox_13.setEnabled(False)
        self.pw_grid_checkbox_14.setEnabled(False)


def display_grid_ticks_options(self, ticks_options=None):
    logging.debug('gui - plot_gd_option_secondary_functions.py - display_grid_ticks_options')
    if ticks_options is None:
        ticks_options = self.gd_ticks_options
    self.pw_grid_label_14.setText('X: ' + str(ticks_options['xticks']) + ' | Y: ' + str(ticks_options['yticks']))


def display_grid_extent(self, extent_options=None):
    logging.debug('gui - plot_gd_option_secondary_functions.py - display_grid_extent')
    if extent_options is None:
        extent_options = self.gd_extent_options

    if extent_options['ymin'] is not None:
        self.pw_grid_label_15.setText('Y min: ' + str(extent_options['ymin'])
                                      + ' | Y max: ' + str(extent_options['ymax'])
                                      + ' | X min: ' + str(extent_options['xmin'])
                                      + ' | X max: ' + str(extent_options['xmax']))
    else:
        self.pw_grid_label_15.setText('Y min: -90 | Y max: 90 | X min: -180 | X max: 180')


def display_layer_order(self, layer_order=None):
    logging.debug('gui - plot_gd_option_secondary_functions.py - display_layer_order')
    if layer_order is None:
        layer_order = self.gd_layer_order
    layers = 'Bottom [ ' + ' > '.join([k for k, v in sorted(layer_order.items(), key=lambda item: item[1])]) + ' ] Top'
    self.pw_grid_label_47.setText(layers)


def activate_boundaries_hex_rgb_color(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_boundaries_hex_rgb_color')
    if self.sender().objectName() == 'pw_grid_combobox_13':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_13.setVisible(True)
            self.pw_grid_line_14.setVisible(False)
            self.pw_grid_line_15.setVisible(False)
            self.pw_grid_line_13.setEnabled(True)
            self.pw_grid_line_14.setEnabled(False)
            self.pw_grid_line_15.setEnabled(False)
            self.pw_grid_line_13.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_13.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_13.setText('')
            self.pw_grid_line_14.setText('')
            self.pw_grid_line_15.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_13.setVisible(True)
            self.pw_grid_line_14.setVisible(True)
            self.pw_grid_line_15.setVisible(True)
            self.pw_grid_line_13.setEnabled(True)
            self.pw_grid_line_14.setEnabled(True)
            self.pw_grid_line_15.setEnabled(True)
            self.pw_grid_line_13.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setText('')
            self.pw_grid_line_14.setText('')
            self.pw_grid_line_15.setText('')
        else:
            self.pw_grid_line_13.setVisible(False)
            self.pw_grid_line_14.setVisible(False)
            self.pw_grid_line_15.setVisible(False)
            self.pw_grid_line_13.setEnabled(False)
            self.pw_grid_line_14.setEnabled(False)
            self.pw_grid_line_15.setEnabled(False)
            self.pw_grid_line_13.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setText('')
            self.pw_grid_line_14.setText('')
            self.pw_grid_line_15.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_14':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_18.setVisible(True)
            self.pw_grid_line_16.setVisible(False)
            self.pw_grid_line_17.setVisible(False)
            self.pw_grid_line_18.setEnabled(True)
            self.pw_grid_line_16.setEnabled(False)
            self.pw_grid_line_17.setEnabled(False)
            self.pw_grid_line_18.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_18.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_18.setText('')
            self.pw_grid_line_16.setText('')
            self.pw_grid_line_17.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_18.setVisible(True)
            self.pw_grid_line_16.setVisible(True)
            self.pw_grid_line_17.setVisible(True)
            self.pw_grid_line_18.setEnabled(True)
            self.pw_grid_line_16.setEnabled(True)
            self.pw_grid_line_17.setEnabled(True)
            self.pw_grid_line_18.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setText('')
            self.pw_grid_line_16.setText('')
            self.pw_grid_line_17.setText('')
        else:
            self.pw_grid_line_18.setVisible(False)
            self.pw_grid_line_16.setVisible(False)
            self.pw_grid_line_17.setVisible(False)
            self.pw_grid_line_18.setEnabled(False)
            self.pw_grid_line_16.setEnabled(False)
            self.pw_grid_line_17.setEnabled(False)
            self.pw_grid_line_18.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setText('')
            self.pw_grid_line_16.setText('')
            self.pw_grid_line_17.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_16':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_20.setVisible(True)
            self.pw_grid_line_21.setVisible(False)
            self.pw_grid_line_22.setVisible(False)
            self.pw_grid_line_20.setEnabled(True)
            self.pw_grid_line_21.setEnabled(False)
            self.pw_grid_line_22.setEnabled(False)
            self.pw_grid_line_20.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_20.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_20.setText('')
            self.pw_grid_line_21.setText('')
            self.pw_grid_line_22.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_20.setVisible(True)
            self.pw_grid_line_21.setVisible(True)
            self.pw_grid_line_22.setVisible(True)
            self.pw_grid_line_20.setEnabled(True)
            self.pw_grid_line_21.setEnabled(True)
            self.pw_grid_line_22.setEnabled(True)
            self.pw_grid_line_20.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setText('')
            self.pw_grid_line_21.setText('')
            self.pw_grid_line_22.setText('')
        else:
            self.pw_grid_line_20.setVisible(False)
            self.pw_grid_line_21.setVisible(False)
            self.pw_grid_line_22.setVisible(False)
            self.pw_grid_line_20.setEnabled(False)
            self.pw_grid_line_21.setEnabled(False)
            self.pw_grid_line_22.setEnabled(False)
            self.pw_grid_line_20.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setText('')
            self.pw_grid_line_21.setText('')
            self.pw_grid_line_22.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_17':
        if self.sender().currentIndex() == 1:
            self.pw_grid_line_23.setVisible(True)
            self.pw_grid_line_24.setVisible(False)
            self.pw_grid_line_25.setVisible(False)
            self.pw_grid_line_23.setEnabled(True)
            self.pw_grid_line_24.setEnabled(False)
            self.pw_grid_line_25.setEnabled(False)
            self.pw_grid_line_23.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_23.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_23.setText('')
            self.pw_grid_line_24.setText('')
            self.pw_grid_line_25.setText('')
        elif self.sender().currentIndex() == 2:
            self.pw_grid_line_23.setVisible(True)
            self.pw_grid_line_24.setVisible(True)
            self.pw_grid_line_25.setVisible(True)
            self.pw_grid_line_23.setEnabled(True)
            self.pw_grid_line_24.setEnabled(True)
            self.pw_grid_line_25.setEnabled(True)
            self.pw_grid_line_23.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setText('')
            self.pw_grid_line_24.setText('')
            self.pw_grid_line_25.setText('')
        else:
            self.pw_grid_line_23.setVisible(False)
            self.pw_grid_line_24.setVisible(False)
            self.pw_grid_line_25.setVisible(False)
            self.pw_grid_line_23.setEnabled(False)
            self.pw_grid_line_24.setEnabled(False)
            self.pw_grid_line_25.setEnabled(False)
            self.pw_grid_line_23.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setText('')
            self.pw_grid_line_24.setText('')
            self.pw_grid_line_25.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_18':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_28.setVisible(True)
            self.pw_grid_line_27.setVisible(False)
            self.pw_grid_line_26.setVisible(False)
            self.pw_grid_line_28.setEnabled(True)
            self.pw_grid_line_27.setEnabled(False)
            self.pw_grid_line_26.setEnabled(False)
            self.pw_grid_line_28.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_28.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_28.setText('')
            self.pw_grid_line_27.setText('')
            self.pw_grid_line_26.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_28.setVisible(True)
            self.pw_grid_line_27.setVisible(True)
            self.pw_grid_line_26.setVisible(True)
            self.pw_grid_line_28.setEnabled(True)
            self.pw_grid_line_27.setEnabled(True)
            self.pw_grid_line_26.setEnabled(True)
            self.pw_grid_line_28.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setText('')
            self.pw_grid_line_27.setText('')
            self.pw_grid_line_26.setText('')
        else:
            self.pw_grid_line_28.setVisible(False)
            self.pw_grid_line_27.setVisible(False)
            self.pw_grid_line_26.setVisible(False)
            self.pw_grid_line_28.setEnabled(False)
            self.pw_grid_line_27.setEnabled(False)
            self.pw_grid_line_26.setEnabled(False)
            self.pw_grid_line_28.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setText('')
            self.pw_grid_line_27.setText('')
            self.pw_grid_line_26.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_19':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_30.setVisible(True)
            self.pw_grid_line_31.setVisible(False)
            self.pw_grid_line_32.setVisible(False)
            self.pw_grid_line_30.setEnabled(True)
            self.pw_grid_line_31.setEnabled(False)
            self.pw_grid_line_32.setEnabled(False)
            self.pw_grid_line_30.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_30.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_30.setText('')
            self.pw_grid_line_31.setText('')
            self.pw_grid_line_32.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_30.setVisible(True)
            self.pw_grid_line_31.setVisible(True)
            self.pw_grid_line_32.setVisible(True)
            self.pw_grid_line_30.setEnabled(True)
            self.pw_grid_line_31.setEnabled(True)
            self.pw_grid_line_32.setEnabled(True)
            self.pw_grid_line_30.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_30.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_30.setText('')
            self.pw_grid_line_31.setText('')
            self.pw_grid_line_32.setText('')
        else:
            self.pw_grid_line_30.setVisible(False)
            self.pw_grid_line_31.setVisible(False)
            self.pw_grid_line_32.setVisible(False)
            self.pw_grid_line_30.setEnabled(False)
            self.pw_grid_line_31.setEnabled(False)
            self.pw_grid_line_32.setEnabled(False)
            self.pw_grid_line_30.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_30.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_30.setText('')
            self.pw_grid_line_31.setText('')
            self.pw_grid_line_32.setText('')


def activate_coastlines_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_coastlines_options')
    self.pw_grid_label_27.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_label_29.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_label_30.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_combobox_12.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_line_12.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_combobox_13.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_line_12.setText('1')
    self.pw_grid_combobox_12.setCurrentIndex(2)
    self.pw_grid_combobox_13.setCurrentIndex(2)


def activate_land_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_land_options')
    self.pw_grid_label_40.setEnabled(self.pw_grid_checkbox_8.isChecked())
    self.pw_grid_combobox_14.setEnabled(self.pw_grid_checkbox_8.isChecked())
    self.pw_grid_line_18.setEnabled(self.pw_grid_checkbox_8.isChecked())
    self.pw_grid_combobox_14.setCurrentIndex(0)
    self.pw_grid_line_18.setText('#e6e6e6')


def activate_ocean_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_ocean_options')
    self.pw_grid_label_46.setEnabled(self.pw_grid_checkbox_9.isChecked())
    self.pw_grid_combobox_19.setEnabled(self.pw_grid_checkbox_9.isChecked())
    self.pw_grid_line_30.setEnabled(self.pw_grid_checkbox_9.isChecked())
    self.pw_grid_combobox_19.setCurrentIndex(0)
    self.pw_grid_line_30.setText('#e6f5ff')


def activate_lakes_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_lakes_options')
    self.pw_grid_label_28.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_label_41.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_label_42.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_label_43.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_combobox_15.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_line_19.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_combobox_16.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_combobox_17.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_line_19.setText('0.5')
    self.pw_grid_combobox_15.setCurrentIndex(2)
    self.pw_grid_combobox_16.setCurrentIndex(3)
    self.pw_grid_combobox_17.setCurrentIndex(4)


def activate_grid_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_grid_options')
    self.pw_grid_label_23.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_label_24.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_label_25.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_combobox_8.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_combobox_18.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_line_4.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_combobox_8.setCurrentIndex(3)
    self.pw_grid_combobox_18.setCurrentIndex(2)
    self.pw_grid_line_4.setText('0.5')


def activate_label_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_albel_options')
    self.pw_grid_checkbox_11.setEnabled(self.pw_grid_checkbox_10.isChecked())
    self.pw_grid_checkbox_12.setEnabled(self.pw_grid_checkbox_10.isChecked())
    self.pw_grid_checkbox_13.setEnabled(self.pw_grid_checkbox_10.isChecked())
    self.pw_grid_checkbox_14.setEnabled(self.pw_grid_checkbox_10.isChecked())
    self.pw_grid_checkbox_11.setChecked(True)
    self.pw_grid_checkbox_12.setChecked(False)
    self.pw_grid_checkbox_13.setChecked(False)
    self.pw_grid_checkbox_14.setChecked(True)


def activate_colormap_dimensions(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_colormap_dimensions')
    self.pw_grid_label_36.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_label_37.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_label_38.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_label_39.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_8.setText('')
    self.pw_grid_line_9.setText('')
    self.pw_grid_line_10.setText('')
    self.pw_grid_line_11.setText('')
    self.pw_grid_line_8.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_9.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_10.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_11.setEnabled(not self.pw_grid_checkbox_5.isChecked())


def activate_colormap_values(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_colormap_values')
    self.pw_grid_line_5.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_line_6.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_line_7.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_line_5.setText('')
    self.pw_grid_line_6.setText('')
    self.pw_grid_line_7.setText('')
    self.pw_grid_label_33.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_34.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_35.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_57.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_set_cmap_ticks.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_57.setText('')
    self.gd_cbar_ticks_options = []


def activate_colormap_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_colormap_options')
    self.pw_grid_label_31.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_label_32.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_label_45.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_line_29.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_info_button_5.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_combobox_10.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_combobox_11.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_combobox_10.setCurrentIndex(1)
    self.pw_grid_combobox_11.setCurrentIndex(3)
    self.pw_grid_checkbox_3.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_checkbox_4.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_checkbox_5.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_checkbox_3.setChecked(False)
    self.pw_grid_checkbox_4.setChecked(True)
    self.pw_grid_checkbox_5.setChecked(True)


def set_colormap_default_dimensions(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_colormap_default_dimensions')
    self.pw_grid_combobox_11.currentIndex()


def set_colormap_default_margins(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_colormap_default_margins')
    margins_dict = cmap_default_fig_margins()[int(self.pw_grid_combobox_11.currentIndex())]
    self.pw_grid_slider_1.setSliderPosition(margins_dict['margin_left'] * 100)
    self.pw_grid_slider_2.setSliderPosition(100 - margins_dict['margin_top'] * 100)
    self.pw_grid_slider_3.setSliderPosition(100 - margins_dict['margin_right'] * 100)
    self.pw_grid_slider_4.setSliderPosition(margins_dict['margin_bottom'] * 100)


def set_projection_function(proj, option_dict):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_projection_function')
    proj_result = None
    if proj == 'PlateCarree':
        proj_result = cartopy.crs.PlateCarree(central_longitude=option_dict['central_longitude'],
                                              globe=option_dict['globe'])
    elif proj == 'AlbersEqualArea':
        proj_result = cartopy.crs.AlbersEqualArea(central_longitude=option_dict['central_longitude'],
                                                  central_latitude=option_dict['central_latitude'],
                                                  false_easting=option_dict['false_easting'],
                                                  false_northing=option_dict['false_northing'],
                                                  standard_parallels=option_dict['standard_parallels'],
                                                  globe=option_dict['globe'])
    elif proj == 'AzimuthalEquidistant':
        proj_result = cartopy.crs.AzimuthalEquidistant(central_longitude=option_dict['central_longitude'],
                                                       central_latitude=option_dict['central_latitude'],
                                                       false_easting=option_dict['false_easting'],
                                                       false_northing=option_dict['false_northing'],
                                                       globe=option_dict['globe'])
    elif proj == 'EquidistantConic':
        proj_result = cartopy.crs.EquidistantConic(central_longitude=option_dict['central_longitude'],
                                                   central_latitude=option_dict['central_latitude'],
                                                   false_easting=option_dict['false_easting'],
                                                   false_northing=option_dict['false_northing'],
                                                   standard_parallels=option_dict['standard_parallels'],
                                                   globe=option_dict['globe'])
    elif proj == 'LambertConformal':
        proj_result = cartopy.crs.LambertConformal(central_longitude=option_dict['central_longitude'],
                                                   central_latitude=option_dict['central_latitude'],
                                                   false_easting=option_dict['false_easting'],
                                                   false_northing=option_dict['false_northing'],
                                                   secant_latitudes=option_dict['secant_latitudes'],
                                                   standard_parallels=option_dict['standard_parallels'],
                                                   globe=option_dict['globe'],
                                                   cutoff=option_dict['cutoff'])
    elif proj == 'Mollweide':
        proj_result = cartopy.crs.Mollweide(central_longitude=option_dict['central_longitude'],
                                            globe=option_dict['globe'],
                                            false_easting=option_dict['false_easting'],
                                            false_northing=option_dict['false_northing'])
    elif proj == 'Orthographic':
        proj_result = cartopy.crs.Orthographic(central_longitude=option_dict['central_longitude'],
                                               central_latitude=option_dict['central_latitude'],
                                               globe=option_dict['globe'])
    elif proj == 'LambertCylindrical':
        proj_result = cartopy.crs.LambertCylindrical(central_longitude=option_dict['central_longitude'])
    elif proj == 'Mercator':
        proj_result = cartopy.crs.Mercator(central_longitude=option_dict['central_longitude'],
                                           min_latitude=option_dict['min_latitude'],
                                           max_latitude=option_dict['max_latitude'],
                                           globe=option_dict['globe'],
                                           latitude_true_scale=option_dict['latitude_true_scale'],
                                           false_easting=option_dict['false_easting'],
                                           false_northing=option_dict['false_northing'],
                                           scale_factor=option_dict['scale_factor'])
    elif proj == 'Miller':
        proj_result = cartopy.crs.Miller(central_longitude=option_dict['central_longitude'],
                                         globe=option_dict['globe'])
    elif proj == 'Robinson':
        proj_result = cartopy.crs.Robinson(central_longitude=option_dict['central_longitude'],
                                           globe=option_dict['globe'],
                                           false_easting=option_dict['false_easting'],
                                           false_northing=option_dict['false_northing'])
    elif proj == 'Sinusoidal':
        proj_result = cartopy.crs.Sinusoidal(central_longitude=option_dict['central_longitude'],
                                             false_easting=option_dict['false_easting'],
                                             false_northing=option_dict['false_northing'],
                                             globe=option_dict['globe'])
    elif proj == 'Geostationary':
        proj_result = cartopy.crs.Geostationary(central_longitude=option_dict['central_longitude'],
                                                satellite_height=option_dict['satellite_height'],
                                                false_easting=option_dict['false_easting'],
                                                false_northing=option_dict['false_northing'],
                                                globe=option_dict['globe'],
                                                sweep_axis=option_dict['sweep_axis'])
    elif proj == 'EckertI':
        proj_result = cartopy.crs.EckertI(central_longitude=option_dict['central_longitude'],
                                          false_easting=option_dict['false_easting'],
                                          false_northing=option_dict['false_northing'],
                                          globe=option_dict['globe'])
    elif proj == 'EqualEarth':
        proj_result = cartopy.crs.EqualEarth(central_longitude=option_dict['central_longitude'],
                                             false_easting=option_dict['false_easting'],
                                             false_northing=option_dict['false_northing'],
                                             globe=option_dict['globe'])
    elif proj == 'NorthPolarStereo':
        proj_result = cartopy.crs.NorthPolarStereo(central_longitude=option_dict['central_longitude'],
                                                   true_scale_latitude=option_dict['true_scale_latitude'],
                                                   globe=option_dict['globe'])
    elif proj == 'SouthPolarStereo':
        proj_result = cartopy.crs.SouthPolarStereo(central_longitude=option_dict['central_longitude'],
                                                   true_scale_latitude=option_dict['true_scale_latitude'],
                                                   globe=option_dict['globe'])
    return proj_result


def wait_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - wait_window')
    info_text = 'Rendering figure, please wait...'
    self.mywait_window = MyWait(info_text)
    self.mywait_window.exec_()


def update_wait_window(self, text):
    logging.debug('gui - plot_gd_option_secondary_functions.py - update_wait_window')
    self.mywait_window.label.setText(text)


def close_wait_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - close_wait_window')
    self.mywait_window.close()


def close_wait_window_error(self, message):
    logging.debug('gui - plot_gd_option_secondary_functions.py - close_wait_window_error')
    self.mywait_window.close()
    exc_type = message[0]
    exc_value = message[1]
    error_message = ('An exception has been thrown and the rendering of the figure couldn\'t be achieved. Please try '
                     'again or select different options. Contact the developer if the same exception occurs again.'
                     '<br><br>Exception type: ' + exc_type + '<br><br>Exception value: ' + exc_value)
    info_window = MyInfo(error_message)
    info_window.exec_()


def projection_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - projection_option_window')
    option_window = MyProjection(self.gd_projection_options, str(self.pw_grid_combobox_7.currentText()))
    option_window.exec_()
    if option_window.new_option_dict is not None:
        self.gd_projection_options = option_window.new_option_dict
        display_grid_projection_options(self)


def tick_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - tick_option_window')
    default_tick_dict = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['default_ticks']
    ticks_window = MyTicks(self.gd_ticks_options, default_tick_dict)
    ticks_window.exec_()
    if ticks_window.new_option_dict is not None:
        self.gd_ticks_options = ticks_window.new_option_dict
        display_grid_ticks_options(self)


def extent_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - tick_option_window')
    default_extent_dict = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]['default_extent']
    extent_window = MyExtent(self.gd_extent_options, default_extent_dict)
    extent_window.exec_()
    if extent_window.new_option_dict is not None:
        self.gd_extent_options = extent_window.new_option_dict
        display_grid_extent(self)


def colorbar_tick_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - colorbar_tick_option_window')
    cbar_ticks_window = MyColorbarTicks(self.gd_cbar_ticks_options)
    cbar_ticks_window.exec_()
    if cbar_ticks_window.new_option_dict is not None:
        self.gd_cbar_ticks_options = cbar_ticks_window.new_option_dict
        self.pw_grid_line_5.setText('man')
        self.pw_grid_line_6.setText('man')
        self.pw_grid_line_7.setText('man')
        self.pw_grid_label_57.setText(str(self.gd_cbar_ticks_options))


def colorbar_tick_option_man_remove(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - colorbar_tick_option_man_remove')
    self.pw_grid_label_57.setText('')
    self.gd_cbar_ticks_options = []


def layer_order_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - layer_order_window')
    layer_window = MyLayer(self.gd_layer_order)
    layer_window.exec_()
    if layer_window.new_option_dict is not None:
        self.gd_layer_order = layer_window.new_option_dict
        display_layer_order(self)
