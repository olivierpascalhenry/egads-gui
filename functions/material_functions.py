import logging
import platform
import matplotlib


def setup_fonts():
    logging.debug('gui - material_functions.py - setup_fonts')
    if platform.system() == 'Linux':
        font_list = ([str(f.name) for f in matplotlib.font_manager.fontManager.ttflist] + 
                     [str(f.name) for f in matplotlib.font_manager.fontManager.afmlist])
    elif platform.system() == 'Windows':
        font_list = []
        for fname in matplotlib.font_manager.win32InstalledFonts(fontext='ttf'):
            try:
                font_list.append(matplotlib.font_manager.FontProperties(fname=fname).get_name())
            except FileNotFoundError:
                pass
        for fname in matplotlib.font_manager.win32InstalledFonts(fontext='afm'):
            try:
                font_list.append(matplotlib.font_manager.FontProperties(fname=fname).get_name())
            except FileNotFoundError:
                pass
    else:
        raise Exception('EGADS Lineage GUI couldn\'t determined which os is installed')
    for index, item in enumerate(font_list):
        font_list[index] = str(item)
    default_font = matplotlib.font_manager.FontProperties(family=[str(matplotlib.rcParams['font.family'][
                                                                          0])]).get_name()
    if default_font not in font_list:
        font_list.append(default_font)
    return sorted(set(font_list)), default_font


def grid_projection_list():
    object_list = ['AlbersEqualArea', 'PlateCarree', 'AzimuthalEquidistant', 'EquidistantConic', 'LambertConformal',
                   'LambertCylindrical', 'Mercator', 'Miller', 'Mollweide', 'Orthographic', 'Robinson', 'Sinusoidal',
                   'Geostationary', 'EckertI', 'EqualEarth', 'NorthPolarStereo', 'SouthPolarStereo']
    return sorted(object_list)


def grid_projection_parameters():
    object_dict = {'AlbersEqualArea': {'central_longitude': 0.0,
                                       'central_latitude': 0.0,
                                       'false_easting': 0.0,
                                       'false_northing': 0.0,
                                       'standard_parallels': (20.0, 50.0),
                                       'globe': None,
                                       'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                         'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                       'default_extent': {'ymin': -89.5, 'ymax': 90, 'xmin': -180, 'xmax': 180},
                                       'central_longitude_extent': None,
                                       'zonal_label_display': False},
                   'PlateCarree': {'central_longitude': 0.0,
                                   'globe': None,
                                   'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                     'yticks': [-100., -80., -60., -40., -20., 0., 20., 40., 60., 80.,
                                                                100.]},
                                   'default_extent': {'ymin': -90, 'ymax': 90, 'xmin': -180, 'xmax': 180},
                                   'central_longitude_extent': True,
                                   'zonal_label_display': {'top': True, 'bottom': True, 'left': True, 'right': True},
                                   'zlb_defaults': {'top': True, 'bottom': False, 'left': True, 'right': False}},
                   'AzimuthalEquidistant': {'central_longitude': 0.0,
                                            'central_latitude': 0.0,
                                            'false_easting': 0.0,
                                            'false_northing': 0.0,
                                            'globe': None,
                                            'default_ticks': False,
                                            'default_extent': False,
                                            'central_longitude_extent': None,
                                            'zonal_label_display': False},
                   'EquidistantConic': {'central_longitude': 0.0,
                                        'central_latitude': 0.0,
                                        'false_easting': 0.0,
                                        'false_northing': 0.0,
                                        'standard_parallels': (20.0, 50.0),
                                        'globe': None,
                                        'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                          'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                        'default_extent': {'ymin': -89.99, 'ymax': 89.99, 'xmin': -180., 'xmax': 180.},
                                        'central_longitude_extent': None,
                                        'zonal_label_display': False},
                   'LambertConformal': {'central_longitude': -96.0,
                                        'central_latitude': 39.0,
                                        'false_easting': 0.0,
                                        'false_northing': 0.0,
                                        'secant_latitudes': None,
                                        'standard_parallels': None,
                                        'globe': None, 'cutoff': -30,
                                        'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                          'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                        'default_extent': {'ymin': -29.99, 'ymax': 90., 'xmin': -180., 'xmax': 180.},
                                        'central_longitude_extent': False,
                                        'zonal_label_display': False},
                   'LambertCylindrical': {'central_longitude': 0.0,
                                          'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                            'yticks': [-60.0, -40.0, -20.0, 0.0, 20.0, 40.0, 60.0]},
                                          'default_extent': {'ymin': -90., 'ymax': 90., 'xmin': -180., 'xmax': 180.},
                                          'central_longitude_extent': False,
                                          'zonal_label_display': {'top': True, 'bottom': True, 'left': True,
                                                                  'right': True},
                                          'zlb_defaults': {'top': True, 'bottom': False, 'left': True, 'right': False}},
                   'Mercator': {'central_longitude': 0.0,
                                'min_latitude': -80.0,
                                'max_latitude': 84.0,
                                'globe': None,
                                'latitude_true_scale': None,
                                'false_easting': 0.0,
                                'false_northing': 0.0,
                                'scale_factor': None,
                                'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                  'yticks': [-90., -60., -30., 0., 30., 60., 90.]},
                                'default_extent': {'ymin': -80, 'ymax': 84, 'xmin': -180, 'xmax': 180},
                                'central_longitude_extent': False,
                                'zonal_label_display': {'top': True, 'bottom': True, 'left': True, 'right': True},
                                'zlb_defaults': {'top': True, 'bottom': True, 'left': True, 'right': True}},
                   'Miller': {'central_longitude': 0.0,
                              'globe': None,
                              'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                              'default_extent': {'ymin': -90, 'ymax': 90, 'xmin': -180, 'xmax': 180},
                              'central_longitude_extent': False,
                              'zonal_label_display': {'top': True, 'bottom': True, 'left': True, 'right': True},
                              'zlb_defaults': {'top': True, 'bottom': True, 'left': True, 'right': True}},
                   'Mollweide': {'central_longitude': 0,
                                 'globe': None,
                                 'false_easting': None,
                                 'false_northing': None,
                                 'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                   'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                 'default_extent': False,
                                 'central_longitude_extent': False,
                                 'zonal_label_display': False},
                   'Orthographic': {'central_longitude': 0.0,
                                    'central_latitude': 0.0,
                                    'globe': None,
                                    'default_ticks': {'xticks': [-80., -60.0, -30., 0., 30., 60., 80.],
                                                      'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                    'default_extent': {'ymin': -88.68, 'ymax': 88.68, 'xmin': -89.36, 'xmax': 89.36},
                                    'central_longitude_extent': False,
                                    'zonal_label_display': {'top': True, 'bottom': True, 'left': True, 'right': True},
                                    'zlb_defaults': {'top': True, 'bottom': True, 'left': True, 'right': True}},
                   'Robinson': {'central_longitude': 0,
                                'globe': None,
                                'false_easting': None,
                                'false_northing': None,
                                'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                  'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                'default_extent': {'ymin': -90., 'ymax': 90., 'xmin': -179.9, 'xmax': 179.9},
                                'central_longitude_extent': True,
                                'zonal_label_display': False},
                   'Sinusoidal': {'central_longitude': 0.0,
                                  'false_easting': 0.0,
                                  'false_northing': 0.0,
                                  'globe': None,
                                  'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                    'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                  'default_extent': {'ymin': -90., 'ymax': 90., 'xmin': -179.999, 'xmax': 179.999},
                                  'central_longitude_extent': True,
                                  'zonal_label_display': False},
                   'Geostationary': {'central_longitude': 0.0,
                                     'satellite_height': 35785831,
                                     'false_easting': 0,
                                     'false_northing': 0,
                                     'globe': None,
                                     'sweep_axis': 'y',
                                     'default_ticks': {'xticks': [-60., -40.0, -20., 0., 20., 40., 60.],
                                                       'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                     'default_extent': False,
                                     'central_longitude_extent': None,
                                     'zonal_label_display': {'top': True, 'bottom': True, 'left': True, 'right': True},
                                     'zlb_defaults': {'top': True, 'bottom': True, 'left': True, 'right': True}},
                   'EckertI': {'central_longitude': 0,
                               'false_easting': None,
                               'false_northing': None,
                               'globe': None,
                               'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                 'yticks': [-100., -80., -60., -40., -20., 0., 20., 40., 60., 80.,
                                                            100.]},
                               'default_extent': {'ymin': -90, 'ymax': 90, 'xmin': -180, 'xmax': 180},
                               'central_longitude_extent': False,
                               'zonal_label_display': False},
                   'EqualEarth': {'central_longitude': 0,
                                  'false_easting': None,
                                  'false_northing': None,
                                  'globe': None,
                                  'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                    'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                  'default_extent': {'ymin': -90., 'ymax': 90., 'xmin': -179.97, 'xmax': 179.97},
                                  'central_longitude_extent': False,
                                  'zonal_label_display': False},
                   'NorthPolarStereo': {'central_longitude': 0.0,
                                        'true_scale_latitude': None,
                                        'globe': None,
                                        'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                          'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                        'default_extent': {'ymin': -61.6283, 'ymax': 90, 'xmin': -180, 'xmax': 180},
                                        'central_longitude_extent': None,
                                        'zonal_label_display': False},
                   'SouthPolarStereo': {'central_longitude': 0.0,
                                        'true_scale_latitude': None,
                                        'globe': None,
                                        'default_ticks': {'xticks': [-180., -120., -60., 0., 60., 120., 180.],
                                                          'yticks': [-90.0, -60.0, -30.0, 0.0, 30.0, 60.0, 90.0]},
                                        'default_extent': {'ymin': -90, 'ymax': 61.6283, 'xmin': -180, 'xmax': 180},
                                        'central_longitude_extent': None,
                                        'zonal_label_display': False}}
    return object_dict


def grid_projection_option_help():
    object_dict = {'central_longitude': 'The central longitude. Optional, defaults to 0.',
                   'central_latitude': 'The central latitude. Optional, defaults to 0.',
                   'false_easting': 'X offset from planar origin in metres. Optional, defaults to 0.',
                   'false_northing': 'Y offset from planar origin in metres. Optional, defaults to 0.',
                   'standard_parallels': 'The one or two latitudes of correct scale. Optional, defaults to (20, 50).',
                   'globe': 'A cartopy.crs.Globe. If omitted, a default globe is created. It is not possible to '
                            'modify this option in the GUI.',
                   'secant_latitudes': 'This keyword is deprecated in v0.12 of Cartopy and directly replaced by '
                                       'standard parallels. Optional, defaults to None.',
                   'cutoff': 'Latitude of map cutoff. The map extends to infinity opposite the central pole so we '
                             'must cut off the map drawing before then. A value of 0 will draw half the globe. '
                             'Optional, defaults to -30.',
                   'min_latitude': 'The maximum southerly extent of the projection. Optional, defaults to -80 degrees.',
                   'max_latitude': 'The maximum northerly extent of the projection. Optional, defaults to 84 degrees.',
                   'latitude_true_scale': 'The latitude where the scale is 1. Optional, defaults to 0 degrees.',
                   'true_scale_latitude': 'The latitude where the scale is 1. Optional, defaults to 0 degrees.',
                   'scale_factor': 'Scale factor at natural origin. Optional, defaults to unused.',
                   'zone': 'The numeric zone of the UTM required.',
                   'southern_hemisphere': 'Set to True if the zone is in the southern hemisphere. Optional, '
                                          'defaults to False.',
                   'pole_longitude': 'Pole longitude position, in unrotated degrees. Optional, defaults to 0.',
                   'pole_latitude': 'Pole latitude position, in unrotated degrees. Optional, defaults to 0.',
                   'central_rotated_longitude': 'Longitude rotation about the new pole, in degrees. Optional, '
                                                'defaults to 0.',
                   'satellite_height': 'The height of the satellite. Optional, defaults to 35785831 meters (true '
                                       'geostationary orbit).',
                   'sweep_axis': 'Controls which axis is scanned first, and thus which angle is applied first. The '
                                 'default is appropriate for Meteosat, while ‘x’ should be used for GOES. (‘x’ or '
                                 '‘y’, optional. Defaults to ‘y’.)'}
    return object_dict


def line_style_list():
    object_list = ['Dashed', 'Dash-dot', 'Dotted', 'Solid']
    return object_list


def marker_style_dict():
    object_dict = {'Circle': 'o', 'Diamond': 'd', 'Hexagon': 'h', 'Pentagon': 'p', 'Plus': '+', 'Point': '.',
                   'Square': 's', 'Star': '*', 'Triangle': '^', 'X': 'x'}
    return object_dict


def colors_dict():
    object_dict = {'Black': 'k', 'Blue': 'b', 'Cyan': 'c', 'Green': 'g', 'Magenta': 'm', 'Red': 'r', 'Yellow': 'y',
                   'White': 'w'}
    return object_dict


def images_extension_dict():
    object_dict = {'EPS Files (*.eps)': '.eps', 'JPEG Files (*.jpg *.jpeg *.jpe)': '.jpg', 'PDF Files (*.pdf)': '.pdf',
                   'PNG Files (*.png *.pns)': '.png', 'TIFF Files (*.tif *.tiff)': '.tif'}
    return object_dict


def setup_plot_material(self):
    logging.debug('gui - material_functions.py - setup_plot_material')
    self.pw_figureOptions_vl_1 = []
    self.pw_figureOptions_vl_2 = []
    self.pw_figureOptions_gl_1 = []
    self.pw_figureOptions_gl_2 = []
    self.pw_figureOptions_gl_3 = []
    self.pw_figureOptions_gl_4 = []
    self.pw_figureOptions_hl_1 = []
    self.pw_figureOptions_hl_2 = []
    self.pw_figureOptions_hl_3 = []
    self.pw_figureOptions_hl_4 = []
    self.pw_figureOptions_hl_5 = []
    self.pw_figureOptions_hl_12 = []
    self.pw_figureOptions_lb_1 = []
    self.pw_figureOptions_lb_2 = []
    self.pw_figureOptions_lb_3 = []
    self.pw_figureOptions_lb_4 = []
    self.pw_figureOptions_lb_5 = []
    self.pw_figureOptions_lb_6 = []
    self.pw_figureOptions_lb_7 = []
    self.pw_figureOptions_lb_8 = []
    self.pw_figureOptions_lb_9 = []
    self.pw_figureOptions_lb_10 = []
    self.pw_figureOptions_lb_11 = []
    self.pw_figureOptions_lb_12 = []
    self.pw_figureOptions_lb_13 = []
    self.pw_figureOptions_lb_14 = []
    self.pw_figureOptions_lb_15 = []
    self.pw_figureOptions_lb_16 = []
    self.pw_figureOptions_lb_17 = []
    self.pw_figureOptions_lb_18 = []
    self.pw_figureOptions_lb_19 = []
    self.pw_figureOptions_lb_20 = []
    self.pw_figureOptions_lb_21 = []
    self.pw_figureOptions_lb_22 = []
    self.pw_figureOptions_lb_23 = []
    self.pw_figureOptions_lb_24 = []
    self.pw_figureOptions_lb_25 = []
    self.pw_figureOptions_lb_26 = []
    self.pw_figureOptions_lb_27 = []
    self.pw_figureOptions_lb_28 = []
    self.pw_figureOptions_lb_29 = []
    self.pw_figureOptions_lb_30 = []
    self.pw_figureOptions_ln_1 = []
    self.pw_figureOptions_ln_2 = []
    self.pw_figureOptions_ln_3 = []
    self.pw_figureOptions_ln_4 = []
    self.pw_figureOptions_ln_5 = []
    self.pw_figureOptions_ln_6 = []
    self.pw_figureOptions_ln_7 = []
    self.pw_figureOptions_ln_8 = []
    self.pw_figureOptions_ln_9 = []
    self.pw_figureOptions_ln_10 = []
    self.pw_figureOptions_cb_1 = []
    self.pw_figureOptions_cb_2 = []
    self.pw_figureOptions_cb_3 = []
    self.pw_figureOptions_cb_4 = []
    self.pw_figureOptions_cb_5 = []
    self.pw_figureOptions_cb_6 = []
    self.pw_figureOptions_cb_7 = []
    self.pw_figureOptions_cb_8 = []
    self.pw_figureOptions_cb_9 = []
    self.pw_figureOptions_cb_10 = []
    self.pw_figureOptions_bt_1 = []
    self.pw_figureOptions_bt_2 = []
    self.pw_figureOptions_bt_3 = []
    self.pw_figureOptions_bt_4 = []
    self.pw_figureOptions_bt_5 = []
    self.pw_figureOptions_bt_6 = []
    self.pw_figureOptions_bt_7 = []
    self.pw_figureOptions_bt_8 = []
    self.pw_figureOptions_bt_9 = []
    self.pw_figureOptions_ck_1 = []
    self.pw_figureOptions_ck_2 = []
    self.pw_figureOptions_li_1 = []
    self.pw_figureOptions_sl_1 = []
    self.pw_figureOptions_sl_2 = []
    self.pw_figureOptions_sl_3 = []
    self.pw_figureOptions_sl_4 = []
    self.pw_figureOptions_sl_5 = []
    self.figure_option_num = 0
    self.pw_plotOptions_vl_1 = []
    self.pw_plotOptions_hl_1 = []
    self.pw_plotOptions_hl_2 = []
    self.pw_plotOptions_hl_3 = []
    self.pw_plotOptions_hl_4 = []
    self.pw_plotOptions_hl_5 = []
    self.pw_plotOptions_hl_6 = []
    self.pw_plotOptions_hl_7 = []
    self.pw_plotOptions_hl_8 = []
    self.pw_plotOptions_hl_9 = []
    self.pw_plotOptions_lb_1 = []
    self.pw_plotOptions_lb_2 = []
    self.pw_plotOptions_lb_3 = []
    self.pw_plotOptions_lb_4 = []
    self.pw_plotOptions_lb_5 = []
    self.pw_plotOptions_lb_6 = []
    self.pw_plotOptions_lb_7 = []
    self.pw_plotOptions_lb_8 = []
    self.pw_plotOptions_lb_9 = []
    self.pw_plotOptions_bg_1 = []
    self.pw_plotOptions_rb_1 = []
    self.pw_plotOptions_rb_2 = []
    self.pw_plotOptions_cb_1 = []
    self.pw_plotOptions_cb_2 = []
    self.pw_plotOptions_ln_1 = []
    self.pw_plotOptions_ln_2 = []
    self.pw_plotOptions_ln_3 = []
    self.pw_plotOptions_ln_4 = []
    self.pw_plotOptions_ln_5 = []
    self.pw_plotOptions_ln_6 = []
    self.pw_plotOptions_ck_1 = []
    self.pw_plotOptions_ck_2 = []
    self.pw_plotOptions_bt_1 = []
    self.pw_plotOptions_bt_2 = []
    self.pw_plotOptions_bt_3 = []
    self.pw_plotOptions_bt_4 = []
    self.pw_plotOptions_bt_5 = []
    self.pw_plotOptions_bt_6 = []
    self.pw_plotOptions_li_1 = []
    self.plot_option_num = 0


def cmap_default_dimensions():
    object_dict = {0: {'colorbar_height': 0.03, 'colorbar_width': 0.7, 'colorbar_axis_xposition': 0.15,
                       'colorbar_axis_yposition': 0.07, 'orientation': 'horizontal'},
                   1: {'colorbar_height': 0.03, 'colorbar_width': 0.7, 'colorbar_axis_xposition': 0.15,
                       'colorbar_axis_yposition': 0.93, 'orientation': 'horizontal'},
                   2: {'colorbar_height': 0.72, 'colorbar_width': 0.02, 'colorbar_axis_xposition': 0.03,
                       'colorbar_axis_yposition': 0.13, 'orientation': 'vertical'},
                   3: {'colorbar_height': 0.72, 'colorbar_width': 0.02, 'colorbar_axis_xposition': 0.87,
                       'colorbar_axis_yposition': 0.13, 'orientation': 'vertical'}}
    return object_dict


def cmap_default_fig_margins():
    object_dict = {0: {'margin_left': 0.05, 'margin_right': 0.95, 'margin_bottom': 0.2, 'margin_top': 0.9},
                   1: {'margin_left': 0.05, 'margin_right': 0.95, 'margin_bottom': 0.1, 'margin_top': 0.8},
                   2: {'margin_left': 0.2, 'margin_right': 0.95, 'margin_bottom': 0.1, 'margin_top': 0.9},
                   3: {'margin_left': 0.1, 'margin_right': 0.85, 'margin_bottom': 0.1, 'margin_top': 0.9}}
    return object_dict


def cmap_dict():
    object_dict = {1: 'coolwarm', 2: 'jet', 3: 'ocean', 4: 'spectral', 5: 'hot', 6: 'hsv', 7: 'seismic',  8: 'terrain'}
    return object_dict


def transparency_hexa_dict_function():
    logging.debug('gui - utils.py - transparency_hexa_dict_function')
    hexa_dict = {100: 'FF', 99: 'FC', 98: 'FA', 97: 'F7', 96: 'F5', 95: 'F2', 94: 'F0', 93: 'ED', 92: 'EB', 91: 'E8',
                 90: 'E6', 89: 'E3', 88: 'E0', 87: 'DE', 86: 'DB', 85: 'D9', 84: 'D6', 83: 'D4', 82: 'D1', 81: 'CF',
                 80: 'CC', 79: 'C9', 78: 'C7', 77: 'C4', 76: 'C2', 75: 'BF', 74: 'BD', 73: 'BA', 72: 'B8', 71: 'B5',
                 70: 'B3', 69: 'B0', 68: 'AD', 67: 'AB', 66: 'A8', 65: 'A6', 64: 'A3', 63: 'A1', 62: '9E', 61: '9C',
                 60: '99', 59: '96', 58: '94', 57: '91', 56: '8F', 55: '8C', 54: '8A', 53: '87', 52: '85', 51: '82',
                 50: '80', 49: '7D', 48: '7A', 47: '78', 46: '75', 45: '73', 44: '70', 43: '6E', 42: '6B', 41: '69',
                 40: '66', 39: '63', 38: '61', 37: '5E', 36: '5C', 35: '59', 34: '57', 33: '54', 32: '52', 31: '4F',
                 30: '4D', 29: '4A', 28: '47', 27: '45', 26: '42', 25: '40', 24: '3D', 23: '3B', 22: '38', 21: '36',
                 20: '33', 19: '30', 18: '2E', 17: '2B', 16: '29', 15: '26', 14: '24', 13: '21', 12: '1F', 11: '1C',
                 10: '1A', 9: '17', 8: '14', 7: '12', 6: '0F', 5: '0D', 4: '0A', 3: '08', 2: '05', 1: '03', 0: '00'}
    return hexa_dict


def extension_filetype_dict_function():
    logging.debug('gui - utils.py - extension_filetype_dict_function')
    object_dict = {'.nc': 'NetCDF Files (*.nc *.cdf)', '.csv': 'CSV Files (*.csv *.dat *.txt)',
                   '.dat': 'CSV Files (*.csv ''*.dat *.txt)', '.txt': 'CSV Files (*.csv *.dat *.txt)',
                   '.na': 'NASA Ames Files (*.na)', '.h5': 'Hdf Files (*.h5 *.hdf5 *.he5)'}
    return object_dict
