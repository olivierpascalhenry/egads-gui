import logging
import numpy
import re
from functions.window_functions.plot_ts_option_gui_functions import add_figure_options, add_plot_options
from functions.material_functions import marker_style_dict, colors_dict
import matplotlib.pyplot as plt


def plot_ts_single(self):
    logging.debug('gui - plot_ts_main_functions.py - plot_ts_single')
    self.plot_type = 'single_timeseries'
    self.ts_plot = self.figure.add_subplot(1, 1, 1)
    yname = list(self.variables.keys())[0]
    self.ts_plot.plot(self.dimensions[self.variables[yname]['dimensions'][0]]['values'],
                      self.variables[yname]['values'], label=yname)
    self.ts_plot.set_ylabel(self.variables[yname]['units'])
    self.ts_plot.set_xlabel(self.dimensions[self.variables[yname]['dimensions'][0]]['units'])
    self.ts_plot.set_ylim([self.ts_plot.axes.get_yticks()[0], self.ts_plot.axes.get_yticks()[-1]])
    self.ts_plot.set_xlim([self.ts_plot.axes.get_xticks()[0], self.ts_plot.axes.get_xticks()[-1]])
    self.ts_plot.spines['top'].set_visible(False)
    self.ts_plot.spines['right'].set_visible(False)
    leg = self.ts_plot.legend(prop={'family': self.default_font, 'size': '10'})
    try:
        leg.set_draggable(True)
    except AttributeError:
        leg.draggable()
    plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.90, wspace=0.4, hspace=0.4)
    set_single_ts_figure_options(self)
    set_single_ts_plot_options(self)
    self.canvas.draw()
    add_figure_options(self)
    add_plot_options(self, self.ts_plot_options)


def plot_ts_multiple(self, plot_type, pos_dict=None):
    logging.debug('gui - plot_ts_main_functions.py - plot_ts_multiple')
    if plot_type == 'plot':
        self.plot_type = 'multiple_timeseries_single_fig'
        yunits = ''
        xunits = ''
        self.ts_plot = self.figure.add_subplot(1, 1, 1)
        for yname in self.variables:
            yvalues = self.variables[yname]['values']
            yunits = self.variables[yname]['units']
            xname = self.variables[yname]['dimensions'][0]
            xvalues = self.dimensions[xname]['values']
            xunits = self.dimensions[xname]['units']
            self.ts_plot.plot(xvalues, yvalues, label=yname)
        self.ts_plot.set_ylabel(yunits)
        self.ts_plot.set_xlabel(xunits)
        self.ts_plot.set_ylim([self.ts_plot.get_yticks()[0], self.ts_plot.get_yticks()[-1]])
        self.ts_plot.set_xlim([self.ts_plot.get_xticks()[0], self.ts_plot.get_xticks()[-1]])
        self.ts_plot.spines['top'].set_visible(False)
        self.ts_plot.spines['right'].set_visible(False)
        leg = self.ts_plot.legend(prop={'family': self.default_font, 'size': '10'})
        try:
            leg.set_draggable(True)
        except AttributeError:
            leg.draggable()
        plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.90, wspace=0.4, hspace=0.4)
        set_single_ts_figure_options(self)
        set_multiple_ts_plot_options(self)
        self.canvas.draw()
        add_figure_options(self)
        for subplot in self.subplot_ts_plt_list:
            add_plot_options(self, subplot)
    else:
        self.plot_type = 'multiple_timeseries'
        subplot_list = []
        i = 0
        if pos_dict is not None:
            nrow = pos_dict['mpl_nrow']
            ncol = pos_dict['mpl_ncol']
        else:
            nrow = len(self.variables)
            ncol = 1
        for yname in self.variables:
            yvalues = self.variables[yname]['values']
            yunits = self.variables[yname]['units']
            xname = self.variables[yname]['dimensions'][0]
            xvalues = self.dimensions[xname]['values']
            xunits = self.dimensions[xname]['units']
            if pos_dict is not None:
                idx = pos_dict[yname]
            else:
                idx = i + 1
            subplot_list.append(self.figure.add_subplot(nrow, ncol, idx))
            subplot_list[i].plot(xvalues, yvalues, label=yname)
            subplot_list[i].set_ylabel(yunits)
            subplot_list[i].set_xlabel(xunits)
            subplot_list[i].set_ylim([subplot_list[i].get_yticks()[0], subplot_list[i].get_yticks()[-1]])
            subplot_list[i].set_xlim([subplot_list[i].get_xticks()[0], subplot_list[i].get_xticks()[-1]])
            subplot_list[i].spines['top'].set_visible(False)
            subplot_list[i].spines['right'].set_visible(False)
            leg = subplot_list[i].legend(prop={'family': self.default_font, 'size': '10'})
            try:
                leg.set_draggable(True)
            except AttributeError:
                leg.draggable()
            i += 1
        set_multiple_ts_figure_options(self, subplot_list)
        set_multiple_ts_plot_options(self, subplot_list)
        self.canvas.draw()
        for subplot in self.subplot_ts_fig_list:
            add_figure_options(self, subplot['figure_instance'])
        for subplot in self.subplot_ts_plt_list:
            add_plot_options(self, subplot)


def set_single_ts_figure_options(self):
    logging.debug('gui - plot_ts_main_functions.py - set_single_ts_figure_options')
    self.ts_figure_options['title'] = ''
    self.ts_figure_options['title_font'] = self.default_font
    self.ts_figure_options['title_size'] = 10
    self.ts_figure_options['xlabel'] = self.ts_plot.get_xlabel()
    self.ts_figure_options['xlabel_font'] = self.default_font
    self.ts_figure_options['xlabel_size'] = 10
    self.ts_figure_options['ylabel'] = self.ts_plot.get_ylabel()
    self.ts_figure_options['ylabel_font'] = self.default_font
    self.ts_figure_options['ylabel_size'] = 10
    self.ts_figure_options['spine_top'] = False
    self.ts_figure_options['spine_right'] = False
    self.ts_figure_options['margin_left'] = 0.1
    self.ts_figure_options['margin_right'] = 0.95
    self.ts_figure_options['margin_bottom'] = 0.1
    self.ts_figure_options['margin_top'] = 0.90
    self.ts_figure_options['horizontal_space'] = None
    self.ts_figure_options['vertical_space'] = None
    self.ts_figure_options['grid'] = False
    self.ts_figure_options['grid_style'] = '-'
    self.ts_figure_options['grid_size'] = 0.5
    self.ts_figure_options['default_grid_size'] = 0.5
    self.ts_figure_options['grid_color'] = 'Black'
    self.ts_figure_options['display_legend'] = True
    self.ts_figure_options['xlim_max'] = self.ts_plot.get_xlim()[1]
    self.ts_figure_options['xlim_min'] = self.ts_plot.get_xlim()[0]
    self.ts_figure_options['ylim_max'] = self.ts_plot.get_ylim()[1]
    self.ts_figure_options['ylim_min'] = self.ts_plot.get_ylim()[0]
    self.ts_figure_options['xlim_step'] = self.ts_plot.get_xticks()[1] - self.ts_plot.get_xticks()[0]
    self.ts_figure_options['ylim_step'] = self.ts_plot.get_yticks()[1] - self.ts_plot.get_yticks()[0]
    self.ts_figure_options['default_xlim_max'] = self.ts_plot.get_xlim()[1]
    self.ts_figure_options['default_xlim_min'] = self.ts_plot.get_xlim()[0]
    self.ts_figure_options['default_ylim_max'] = self.ts_plot.get_ylim()[1]
    self.ts_figure_options['default_ylim_min'] = self.ts_plot.get_ylim()[0]
    self.ts_figure_options['default_xlim_step'] = self.ts_plot.get_xticks()[1] - self.ts_plot.get_xticks()[0]
    self.ts_figure_options['default_ylim_step'] = self.ts_plot.get_yticks()[1] - self.ts_plot.get_yticks()[0]
    self.ts_figure_options['xticks'] = self.ts_plot.get_xticks()
    self.ts_figure_options['yticks'] = self.ts_plot.get_yticks()


def set_multiple_ts_figure_options(self, subplot_list):
    logging.debug('gui - plot_ts_main_functions.py - set_multiple_ts_figure_options')
    for plot in subplot_list:
        options_dict = {'figure_instance': plot,
                        'title': '',
                        'title_font': self.default_font,
                        'title_size': 10,
                        'xlabel': plot.axes.xaxis.get_label_text(),
                        'xlabel_font': self.default_font,
                        'xlabel_size': 10,
                        'ylabel': plot.axes.yaxis.get_label_text(),
                        'ylabel_font': self.default_font,
                        'ylabel_size': 10,
                        'spine_top': False,
                        'spine_right': False,
                        'margin_left': 0.1,
                        'margin_right': 0.95,
                        'margin_bottom': 0.1,
                        'margin_top': 0.9,
                        'horizontal_space': 0.4,
                        'vertical_space': 0.4,
                        'grid': False,
                        'grid_style': '-',
                        'grid_size': 0.5,
                        'grid_color': 'Black',
                        'display_legend': True,
                        'xlim_max': plot.axes.get_xlim()[1],
                        'xlim_min': plot.axes.get_xlim()[0],
                        'ylim_max': plot.axes.get_ylim()[1],
                        'ylim_min': plot.axes.get_ylim()[0],
                        'xlim_step': plot.axes.get_xticks()[1] - plot.axes.get_xticks()[0],
                        'ylim_step': plot.axes.get_yticks()[1] - plot.axes.get_yticks()[0],
                        'xticks': plot.axes.get_xticks(),
                        'yticks': plot.axes.get_yticks()}
        self.subplot_ts_fig_list.append(options_dict)


def set_single_ts_plot_options(self):
    logging.debug('gui - plot_ts_main_functions.py - set_single_ts_plot_options')
    self.ts_plot_options['line_style'] = self.ts_plot.get_lines()[0].get_linestyle()
    self.ts_plot_options['line_marker'] = 'line'
    self.ts_plot_options['line_color'] = self.ts_plot.get_lines()[0].get_color()
    self.ts_plot_options['default_line_color'] = self.ts_plot.get_lines()[0].get_color()
    self.ts_plot_options['line_width'] = self.ts_plot.get_lines()[0].get_linewidth()
    self.ts_plot_options['default_line_width'] = self.ts_plot.get_lines()[0].get_linewidth()
    self.ts_plot_options['line_antialiased'] = self.ts_plot.get_lines()[0].get_antialiased()
    self.ts_plot_options['line_alpha'] = False
    self.ts_plot_options['line_alpha_perc'] = self.ts_plot.get_lines()[0].get_alpha()
    self.ts_plot_options['default_line_alpha_perc'] = self.ts_plot.get_lines()[0].get_alpha()
    self.ts_plot_options['legend_label'] = self.ts_plot.get_lines()[0].get_label()
    self.ts_plot_options['default_legend_label'] = self.ts_plot.get_lines()[0].get_label()


def set_multiple_ts_plot_options(self, subplot_list=None):
    logging.debug('gui - plot_ts_main_functions.py - set_multiple_ts_plot_options')
    if subplot_list is None:
        for line in self.ts_plot.get_lines():
            plot_options = {'line_style': line.get_linestyle(),
                            'line_marker': 'line',
                            'line_color': line.get_color(),
                            'line_width': line.get_linewidth(),
                            'line_antialiased': line.get_antialiased(),
                            'line_alpha': False,
                            'line_alpha_perc': line.get_alpha(),
                            'legend_label': line.get_label()}
            self.subplot_ts_plt_list.append(plot_options)
    else:
        for plot in subplot_list:
            line = plot.axes.lines[0]
            plot_options = {'figure_instance': plot,
                            'line_style': line.get_linestyle(),
                            'line_marker': 'line',
                            'line_color': line.get_color(),
                            'line_width': line.get_linewidth(),
                            'line_antialiased': line.get_antialiased(),
                            'line_alpha': False,
                            'line_alpha_perc': line.get_alpha(),
                            'legend_label': line.get_label()}
            self.subplot_ts_plt_list.append(plot_options)


def update_single_ts_fig_options(self):
    logging.debug('gui - plot_ts_main_functions.py - update_single_ts_fig_options')
    if "activated" in self.action_pan.objectName():
        self.plot_pan()
    if "activated" in self.action_zoom.objectName():
        self.plot_zoom()
    ts_figure_options = dict()
    ts_figure_options['title'] = str(self.pw_figureOptions_ln_1[0].text())
    ts_figure_options['title_font'] = str(self.pw_figureOptions_cb_1[0].currentText())
    ts_figure_options['title_size'] = int(self.pw_figureOptions_cb_2[0].currentText())
    ts_figure_options['xlabel'] = str(self.pw_figureOptions_ln_2[0].text())
    ts_figure_options['xlabel_font'] = str(self.pw_figureOptions_cb_3[0].currentText())
    ts_figure_options['xlabel_size'] = int(self.pw_figureOptions_cb_4[0].currentText())
    ts_figure_options['ylabel'] = str(self.pw_figureOptions_ln_3[0].text())
    ts_figure_options['ylabel_font'] = str(self.pw_figureOptions_cb_5[0].currentText())
    ts_figure_options['ylabel_size'] = int(self.pw_figureOptions_cb_6[0].currentText())
    try:
        ts_figure_options['xlim_step'] = float(self.pw_figureOptions_ln_6[0].text())
    except ValueError:
        ts_figure_options['xlim_step'] = ''
    try:
        ts_figure_options['xlim_max'] = float(self.pw_figureOptions_ln_5[0].text())
    except ValueError:
        ts_figure_options['xlim_max'] = ''
    try:
        ts_figure_options['xlim_min'] = float(self.pw_figureOptions_ln_4[0].text())
    except ValueError:
        ts_figure_options['xlim_min'] = ''
    try:
        ts_figure_options['xticks'] = numpy.arange(ts_figure_options['xlim_min']
                                                   - ts_figure_options['xlim_step'] * 10,
                                                   ts_figure_options['xlim_max']
                                                   + ts_figure_options['xlim_step'] * 10,
                                                   ts_figure_options['xlim_step'])
    except (ValueError, TypeError):
        ts_figure_options['xticks'] = ''
    try:
        ts_figure_options['ylim_step'] = float(self.pw_figureOptions_ln_9[0].text())
    except ValueError:
        ts_figure_options['ylim_step'] = ''
    try:
        ts_figure_options['ylim_max'] = float(self.pw_figureOptions_ln_8[0].text())
    except ValueError:
        ts_figure_options['ylim_max'] = ''
    try:
        ts_figure_options['ylim_min'] = float(self.pw_figureOptions_ln_7[0].text())
    except ValueError:
        ts_figure_options['ylim_min'] = ''
    try:
        ts_figure_options['yticks'] = numpy.arange(ts_figure_options['ylim_min']
                                                   - ts_figure_options['ylim_step'] * 10,
                                                   ts_figure_options['ylim_max']
                                                   + ts_figure_options['ylim_step'] * 10,
                                                   ts_figure_options['ylim_step'])
    except (ValueError, TypeError):
        ts_figure_options['yticks'] = ''
    if self.pw_figureOptions_ck_1[0].isChecked():
        ts_figure_options['grid'] = True
        ts_figure_options['grid_style'] = str(self.pw_figureOptions_cb_9[0].currentText()).lower()
        try:
            ts_figure_options['grid_size'] = float(self.pw_figureOptions_ln_10[0].text())
        except ValueError:
            ts_figure_options['grid_size'] = self.ts_figure_options['default_grid_size']
        ts_figure_options['grid_color'] = colors_dict()[str(self.pw_figureOptions_cb_10[0].currentText())]
    else:
        ts_figure_options['grid'] = False
        ts_figure_options['grid_style'] = ''
        ts_figure_options['grid_size'] = ''
        ts_figure_options['grid_color'] = ''
    ts_figure_options['display_legend'] = self.pw_figureOptions_ck_2[0].isChecked()
    ts_figure_options['margin_left'] = float(self.pw_commonOptions_lb_5.text())
    ts_figure_options['margin_right'] = 1 - float(self.pw_commonOptions_lb_9.text())
    ts_figure_options['margin_bottom'] = float(self.pw_commonOptions_lb_6.text())
    ts_figure_options['margin_top'] = 1 - float(self.pw_commonOptions_lb_10.text())
    if self.subplot_ts_fig_list:
        ts_figure_options['horizontal_space'] = float(self.pw_commonOptions_lb_12.text())
        ts_figure_options['vertical_space'] = float(self.pw_commonOptions_lb_15.text())
    else:
        ts_figure_options['horizontal_space'] = None
        ts_figure_options['vertical_space'] = None

    if ts_figure_options['title']:
        if (ts_figure_options['title'] != self.ts_figure_options['title'] or
                ts_figure_options['title_font'] != self.ts_figure_options['title_font'] or
                ts_figure_options['title_size'] != self.ts_figure_options['title_size']):
            self.ts_figure_options['title'] = ts_figure_options['title']
            self.ts_figure_options['title_font'] = ts_figure_options['title_font']
            self.ts_figure_options['title_size'] = ts_figure_options['title_size']
            font = {'fontname': ts_figure_options['title_font'], 'fontsize': ts_figure_options['title_size']}
            plt.title(ts_figure_options['title'], y=1.04, **font)
    if ts_figure_options['xlabel']:
        if (ts_figure_options['xlabel'] != self.ts_figure_options['xlabel'] or
                ts_figure_options['xlabel_font'] != self.ts_figure_options['xlabel_font'] or
                ts_figure_options['xlabel_size'] != self.ts_figure_options['xlabel_size']):
            self.ts_figure_options['xlabel'] = ts_figure_options['xlabel']
            self.ts_figure_options['xlabel_font'] = ts_figure_options['xlabel_font']
            self.ts_figure_options['xlabel_size'] = ts_figure_options['xlabel_size']
            font = {'fontname': ts_figure_options['xlabel_font'], 'fontsize': ts_figure_options['xlabel_size']}
            plt.xlabel(ts_figure_options['xlabel'], **font)
    if ts_figure_options['ylabel']:
        if (ts_figure_options['ylabel'] != self.ts_figure_options['ylabel'] or
                ts_figure_options['ylabel_font'] != self.ts_figure_options['ylabel_font'] or
                ts_figure_options['ylabel_size'] != self.ts_figure_options['ylabel_size']):
            self.ts_figure_options['ylabel'] = ts_figure_options['ylabel']
            self.ts_figure_options['ylabel_font'] = ts_figure_options['ylabel_font']
            self.ts_figure_options['ylabel_size'] = ts_figure_options['ylabel_size']
            font = {'fontname': ts_figure_options['ylabel_font'], 'fontsize': ts_figure_options['ylabel_size']}
            plt.ylabel(ts_figure_options['ylabel'], **font)
    if isinstance(ts_figure_options['xticks'], numpy.ndarray):
        if not numpy.array_equal(ts_figure_options['xticks'], self.ts_figure_options['xticks']):
            self.ts_figure_options['xlim_step'] = ts_figure_options['xlim_step']
            self.ts_figure_options['xlim_max'] = ts_figure_options['xlim_max']
            self.ts_figure_options['xlim_min'] = ts_figure_options['xlim_min']
            self.ts_figure_options['xticks'] = ts_figure_options['xticks']
            plt.xticks(ts_figure_options['xticks'])
            plt.xlim([ts_figure_options['xlim_min'], ts_figure_options['xlim_max']])
    if isinstance(ts_figure_options['yticks'], numpy.ndarray):
        if not numpy.array_equal(ts_figure_options['yticks'], self.ts_figure_options['yticks']):
            self.ts_figure_options['ylim_step'] = ts_figure_options['ylim_step']
            self.ts_figure_options['ylim_max'] = ts_figure_options['ylim_max']
            self.ts_figure_options['ylim_min'] = ts_figure_options['ylim_min']
            self.ts_figure_options['yticks'] = ts_figure_options['yticks']
            plt.yticks(ts_figure_options['yticks'])
            plt.ylim([ts_figure_options['ylim_min'], ts_figure_options['ylim_max']])
    if ts_figure_options['grid']:
        if (ts_figure_options['grid'] != self.ts_figure_options['grid'] or
                self.ts_figure_options['grid_style'] != ts_figure_options['grid_style'] or
                self.ts_figure_options['grid_size'] != ts_figure_options['grid_size'] or
                self.ts_figure_options['grid_color'] != ts_figure_options['grid_color']):
            self.ts_figure_options['grid'] = ts_figure_options['grid']
            self.ts_figure_options['grid_style'] = ts_figure_options['grid_style']
            self.ts_figure_options['grid_size'] = ts_figure_options['grid_size']
            self.ts_figure_options['grid_color'] = ts_figure_options['grid_color']
            args = {'linestyle': ts_figure_options['grid_style'],
                    'linewidth': ts_figure_options['grid_size'],
                    'color': ts_figure_options['grid_color']}
            plt.grid(b=True, **args)
    elif not ts_figure_options['grid'] and ts_figure_options['grid'] != self.ts_figure_options['grid']:
        self.ts_figure_options['grid'] = ts_figure_options['grid']
        plt.grid(b=False)
    if ts_figure_options['display_legend']:
        if ts_figure_options['display_legend'] != self.ts_figure_options['display_legend']:
            self.ts_figure_options['display_legend'] = ts_figure_options['display_legend']
            plt.gca().legend(prop={'family': self.default_font, 'size': '10'})
            plt.gca().legend().set_visible(True)
            try:
                plt.gca().legend().set_draggable(True)
            except AttributeError:
                plt.gca().legend().draggable()
    else:
        if ts_figure_options['display_legend'] != self.ts_figure_options['display_legend']:
            self.ts_figure_options['display_legend'] = ts_figure_options['display_legend']
            plt.gca().legend().set_visible(False)

    margin_left, margin_right, margin_bottom, margin_top, wspace, hspace = None, None, None, None, None, None
    if ts_figure_options['margin_left'] != self.ts_figure_options['margin_left']:
        self.ts_figure_options['margin_left'] = ts_figure_options['margin_left']
        margin_left = ts_figure_options['margin_left']
    if ts_figure_options['margin_right'] != self.ts_figure_options['margin_right']:
        self.ts_figure_options['margin_right'] = ts_figure_options['margin_right']
        margin_right = ts_figure_options['margin_right']
    if ts_figure_options['margin_bottom'] != self.ts_figure_options['margin_bottom']:
        self.ts_figure_options['margin_bottom'] = ts_figure_options['margin_bottom']
        margin_bottom = ts_figure_options['margin_bottom']
    if ts_figure_options['margin_top'] != self.ts_figure_options['margin_top']:
        self.ts_figure_options['margin_top'] = ts_figure_options['margin_top']
        margin_top = ts_figure_options['margin_top']
    if ts_figure_options['vertical_space'] != self.ts_figure_options['vertical_space']:
        self.ts_figure_options['vertical_space'] = ts_figure_options['vertical_space']
        hspace = ts_figure_options['vertical_space']
    if ts_figure_options['horizontal_space'] != self.ts_figure_options['horizontal_space']:
        self.ts_figure_options['horizontal_space'] = ts_figure_options['horizontal_space']
        wspace = ts_figure_options['horizontal_space']
    plt.subplots_adjust(left=margin_left, right=margin_right, bottom=margin_bottom, top=margin_top,
                        wspace=wspace, hspace=hspace)
    self.canvas.draw()


def update_multiple_ts_fig_options(self):
    logging.debug('gui - plot_ts_main_functions.py - update_multiple_ts_fig_options')
    if "activated" in self.action_pan.objectName():
        self.plot_pan()
    if "activated" in self.action_zoom.objectName():
        self.plot_zoom()
    for i in range(self.plot_option_num):
        ts_figure_options = dict()
        ts_figure_options['title'] = str(self.pw_figureOptions_ln_1[i].text())
        ts_figure_options['title_font'] = str(self.pw_figureOptions_cb_1[i].currentText())
        ts_figure_options['title_size'] = int(self.pw_figureOptions_cb_2[i].currentText())
        ts_figure_options['xlabel'] = str(self.pw_figureOptions_ln_2[i].text())
        ts_figure_options['xlabel_font'] = str(self.pw_figureOptions_cb_3[i].currentText())
        ts_figure_options['xlabel_size'] = int(self.pw_figureOptions_cb_4[i].currentText())
        ts_figure_options['ylabel'] = str(self.pw_figureOptions_ln_3[i].text())
        ts_figure_options['ylabel_font'] = str(self.pw_figureOptions_cb_5[i].currentText())
        ts_figure_options['ylabel_size'] = int(self.pw_figureOptions_cb_6[i].currentText())
        try:
            ts_figure_options['xlim_step'] = float(self.pw_figureOptions_ln_6[i].text())
        except ValueError:
            ts_figure_options['xlim_step'] = ''
        try:
            ts_figure_options['xlim_max'] = float(self.pw_figureOptions_ln_5[i].text())
        except ValueError:
            ts_figure_options['xlim_max'] = ''
        try:
            ts_figure_options['xlim_min'] = float(self.pw_figureOptions_ln_4[i].text())
        except ValueError:
            ts_figure_options['xlim_min'] = ''
        try:
            ts_figure_options['xticks'] = numpy.arange(ts_figure_options['xlim_min'] - ts_figure_options['xlim_step']
                                                       * 10,
                                                       ts_figure_options['xlim_max'] + ts_figure_options['xlim_step']
                                                       * 10,
                                                       ts_figure_options['xlim_step'])
        except (ValueError, TypeError):
            ts_figure_options['xticks'] = ''
        try:
            ts_figure_options['ylim_step'] = float(self.pw_figureOptions_ln_9[i].text())
        except ValueError:
            ts_figure_options['ylim_step'] = ''
        try:
            ts_figure_options['ylim_max'] = float(self.pw_figureOptions_ln_8[i].text())
        except ValueError:
            ts_figure_options['ylim_max'] = ''
        try:
            ts_figure_options['ylim_min'] = float(self.pw_figureOptions_ln_7[i].text())
        except ValueError:
            ts_figure_options['ylim_min'] = ''
        try:
            ts_figure_options['yticks'] = numpy.arange(ts_figure_options['ylim_min'] - ts_figure_options['ylim_step']
                                                       * 10,
                                                       ts_figure_options['ylim_max'] + ts_figure_options['ylim_step']
                                                       * 10,
                                                       ts_figure_options['ylim_step'])
        except (ValueError, TypeError):
            ts_figure_options['yticks'] = ''
        if self.pw_figureOptions_ck_1[i].isChecked():
            ts_figure_options['grid'] = True
            ts_figure_options['grid_style'] = self.line_styles_dict[str(self.pw_figureOptions_cb_9[i].currentText())]
            ts_figure_options['grid_size'] = float(self.pw_figureOptions_ln_10[i].text())
            ts_figure_options['grid_color'] = self.colors_dict[str(self.pw_figureOptions_cb_10[i].currentText())]
        else:
            ts_figure_options['grid'] = False
            ts_figure_options['grid_style'] = ''
            ts_figure_options['grid_size'] = ''
            ts_figure_options['grid_color'] = ''
        ts_figure_options['display_legend'] = self.pw_figureOptions_ck_2[i].isChecked()
        if i == 0:
            ts_figure_options['margin_left'] = float(self.pw_commonOptions_lb_5.text())
            ts_figure_options['margin_right'] = 1 - float(self.pw_commonOptions_lb_9.text())
            ts_figure_options['margin_bottom'] = float(self.pw_commonOptions_lb_6.text())
            ts_figure_options['margin_top'] = 1 - float(self.pw_commonOptions_lb_10.text())
            ts_figure_options['horizontal_space'] = float(self.pw_commonOptions_lb_12.text())
            ts_figure_options['vertical_space'] = float(self.pw_commonOptions_lb_15.text())
        if ts_figure_options['title']:
            if (ts_figure_options['title'] != self.subplot_ts_fig_list[i]['title'] or
                    ts_figure_options['title_font'] != self.subplot_ts_fig_list[i]['title_font'] or
                    ts_figure_options['title_size'] != self.subplot_ts_fig_list[i]['title_size']):
                self.subplot_ts_fig_list[i]['title'] = ts_figure_options['title']
                self.subplot_ts_fig_list[i]['title_font'] = ts_figure_options['title_font']
                self.subplot_ts_fig_list[i]['title_size'] = ts_figure_options['title_size']
                font = {'fontname': ts_figure_options['title_font'], 'fontsize': ts_figure_options['title_size']}
                self.subplot_ts_fig_list[i]['figure_instance'].set_title(ts_figure_options['title'], **font)
        if ts_figure_options['xlabel']:
            if (ts_figure_options['xlabel'] != self.subplot_ts_fig_list[i]['xlabel'] or
                    ts_figure_options['xlabel_font'] != self.subplot_ts_fig_list[i]['xlabel_font'] or
                    ts_figure_options['xlabel_size'] != self.subplot_ts_fig_list[i]['xlabel_size']):
                self.subplot_ts_fig_list[i]['xlabel'] = ts_figure_options['xlabel']
                self.subplot_ts_fig_list[i]['xlabel_font'] = ts_figure_options['xlabel_font']
                self.subplot_ts_fig_list[i]['xlabel_size'] = ts_figure_options['xlabel_size']
                font = {'fontname': ts_figure_options['xlabel_font'], 'fontsize': ts_figure_options['xlabel_size']}
                self.subplot_ts_fig_list[i]['figure_instance'].set_xlabel(ts_figure_options['xlabel'], **font)
        if ts_figure_options['ylabel']:
            if (ts_figure_options['ylabel'] != self.subplot_ts_fig_list[i]['ylabel'] or
                    ts_figure_options['ylabel_font'] != self.subplot_ts_fig_list[i]['ylabel_font'] or
                    ts_figure_options['ylabel_size'] != self.subplot_ts_fig_list[i]['ylabel_size']):
                self.subplot_ts_fig_list[i]['ylabel'] = ts_figure_options['ylabel']
                self.subplot_ts_fig_list[i]['ylabel_font'] = ts_figure_options['ylabel_font']
                self.subplot_ts_fig_list[i]['ylabel_size'] = ts_figure_options['ylabel_size']
                font = {'fontname': ts_figure_options['ylabel_font'], 'fontsize': ts_figure_options['ylabel_size']}
                self.subplot_ts_fig_list[i]['figure_instance'].set_ylabel(ts_figure_options['ylabel'], **font)
        if isinstance(ts_figure_options['xticks'], numpy.ndarray):
            if not numpy.array_equal(ts_figure_options['xticks'], self.subplot_ts_fig_list[i]['xticks']):
                self.subplot_ts_fig_list[i]['xlim_step'] = ts_figure_options['xlim_step']
                self.subplot_ts_fig_list[i]['xlim_max'] = ts_figure_options['xlim_max']
                self.subplot_ts_fig_list[i]['xlim_min'] = ts_figure_options['xlim_min']
                self.subplot_ts_fig_list[i]['xticks'] = ts_figure_options['xticks']
                self.subplot_ts_fig_list[i]['figure_instance'].set_xticks(ts_figure_options['xticks'])
                self.subplot_ts_fig_list[i]['figure_instance'].set_xlim([ts_figure_options['xlim_min'],
                                                                         ts_figure_options['xlim_max']])
        if isinstance(ts_figure_options['yticks'], numpy.ndarray):
            if not numpy.array_equal(ts_figure_options['yticks'], self.subplot_ts_fig_list[i]['yticks']):
                self.subplot_ts_fig_list[i]['ylim_step'] = ts_figure_options['ylim_step']
                self.subplot_ts_fig_list[i]['ylim_max'] = ts_figure_options['ylim_max']
                self.subplot_ts_fig_list[i]['ylim_min'] = ts_figure_options['ylim_min']
                self.subplot_ts_fig_list[i]['yticks'] = ts_figure_options['yticks']
                self.subplot_ts_fig_list[i]['figure_instance'].set_yticks(ts_figure_options['yticks'])
                self.subplot_ts_fig_list[i]['figure_instance'].set_ylim([ts_figure_options['ylim_min'],
                                                                         ts_figure_options['ylim_max']])
        if ts_figure_options['grid']:
            if (ts_figure_options['grid'] != self.subplot_ts_fig_list[i]['grid'] or
                    self.subplot_ts_fig_list[i]['grid_style'] != ts_figure_options['grid_style'] or
                    self.subplot_ts_fig_list[i]['grid_size'] != ts_figure_options['grid_size'] or
                    self.subplot_ts_fig_list[i]['grid_color'] != ts_figure_options['grid_color']):
                self.subplot_ts_fig_list[i]['grid'] = ts_figure_options['grid']
                self.subplot_ts_fig_list[i]['grid_style'] = ts_figure_options['grid_style']
                self.subplot_ts_fig_list[i]['grid_size'] = ts_figure_options['grid_size']
                self.subplot_ts_fig_list[i]['grid_color'] = ts_figure_options['grid_color']
                args = {'linestyle': ts_figure_options['grid_style'], 'linewidth': ts_figure_options['grid_size'],
                        'color': ts_figure_options['grid_color']}
                self.subplot_ts_fig_list[i]['figure_instance'].grid(b=True, **args)
        elif not ts_figure_options['grid'] and ts_figure_options['grid'] != self.subplot_ts_fig_list[i]['grid']:
            self.subplot_ts_fig_list[i]['grid'] = ts_figure_options['grid']
            self.subplot_ts_fig_list[i]['figure_instance'].grid(b=False)
        if ts_figure_options['display_legend']:
            if ts_figure_options['display_legend'] != self.subplot_ts_fig_list[i]['display_legend']:
                self.subplot_ts_fig_list[i]['display_legend'] = ts_figure_options['display_legend']
                self.subplot_ts_fig_list[i]['figure_instance'].legend(prop={'family': self.default_font, 'size': '10'})
                self.subplot_ts_fig_list[i]['figure_instance'].legend().set_visible(True)
                try:
                    self.subplot_ts_fig_list[i]['figure_instance'].legend().set_draggable(True)
                except AttributeError:
                    self.subplot_ts_fig_list[i]['figure_instance'].legend().draggable()
        else:
            if ts_figure_options['display_legend'] != self.subplot_ts_fig_list[i]['display_legend']:
                self.subplot_ts_fig_list[i]['display_legend'] = ts_figure_options['display_legend']
                self.subplot_ts_fig_list[i]['figure_instance'].legend().set_visible(False)
        if i == 0:
            margin_left, margin_right, margin_bottom, margin_top, wspace, hspace = None, None, None, None, None, None
            if ts_figure_options['margin_left'] != self.subplot_ts_fig_list[i]['margin_left']:
                self.subplot_ts_fig_list[i]['margin_left'] = ts_figure_options['margin_left']
                margin_left = ts_figure_options['margin_left']
            if ts_figure_options['margin_right'] != self.subplot_ts_fig_list[i]['margin_right']:
                self.subplot_ts_fig_list[i]['margin_right'] = ts_figure_options['margin_right']
                margin_right = ts_figure_options['margin_right']
            if ts_figure_options['margin_bottom'] != self.subplot_ts_fig_list[i]['margin_bottom']:
                self.subplot_ts_fig_list[i]['margin_bottom'] = ts_figure_options['margin_bottom']
                margin_bottom = ts_figure_options['margin_bottom']
            if ts_figure_options['margin_top'] != self.subplot_ts_fig_list[i]['margin_top']:
                self.subplot_ts_fig_list[i]['margin_top'] = ts_figure_options['margin_top']
                margin_top = ts_figure_options['margin_top']
            if ts_figure_options['vertical_space'] != self.subplot_ts_fig_list[i]['vertical_space']:
                self.subplot_ts_fig_list[i]['vertical_space'] = ts_figure_options['vertical_space']
                hspace = ts_figure_options['vertical_space']
            if ts_figure_options['horizontal_space'] != self.subplot_ts_fig_list[i]['horizontal_space']:
                self.subplot_ts_fig_list[i]['horizontal_space'] = ts_figure_options['horizontal_space']
                wspace = ts_figure_options['horizontal_space']
            plt.subplots_adjust(left=margin_left, right=margin_right, bottom=margin_bottom, top=margin_top,
                                wspace=wspace, hspace=hspace)
    self.canvas.draw()


def update_single_ts_plt_options(self):
    logging.debug('gui - plot_ts_main_functions.py - update_single_ts_plt_options')
    if "activated" in self.action_pan.objectName():
        self.plot_pan()
    if "activated" in self.action_zoom.objectName():
        self.plot_zoom()
    ts_plot_options = dict()
    ts_plot_options['line_style'] = []
    ts_plot_options['line_marker'] = []
    ts_plot_options['line_color'] = []
    ts_plot_options['line_width'] = []
    ts_plot_options['line_antialiased'] = []
    ts_plot_options['line_alpha'] = []
    ts_plot_options['line_alpha_perc'] = []
    ts_plot_options['legend_label'] = []
    if self.pw_plotOptions_rb_1[0].isChecked():
        ts_plot_options['line_style'] = str(self.pw_plotOptions_cb_1[0].currentText()).lower()
        ts_plot_options['line_marker'] = 'line'
    else:
        ts_plot_options['line_style'] = marker_style_dict()[str(self.pw_plotOptions_cb_1[0].currentText())]
        ts_plot_options['line_marker'] = 'marker'
    if str(self.pw_plotOptions_cb_2[0].currentText()) == 'HEX Color':
        if self.pw_plotOptions_ln_3[0].text():
            hex_code = str(self.pw_plotOptions_ln_3[0].text())
            if '#' not in str(self.pw_plotOptions_ln_3[0].text()):
                hex_code = '#' + hex_code
            if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code):
                ts_plot_options['line_color'] = hex_code
            else:
                ts_plot_options['line_color'] = self.ts_plot_options['default_line_color']
        else:
            ts_plot_options['line_color'] = self.ts_plot_options['default_line_color']
    elif str(self.pw_plotOptions_cb_2[0].currentText()) == 'RGB Color':
        try:
            r = float(self.pw_plotOptions_ln_3[0].text()) / 255.
            g = float(self.pw_plotOptions_ln_5[0].text()) / 255.
            b = float(self.pw_plotOptions_ln_6[0].text()) / 255.
            ts_plot_options['line_color'] = (r, g, b)
        except ValueError:
            ts_plot_options['line_color'] = self.ts_plot_options['default_line_color']
    else:
        ts_plot_options['line_color'] = colors_dict()[str(self.pw_plotOptions_cb_2[0].currentText())]
    try:
        ts_plot_options['line_width'] = float(self.pw_plotOptions_ln_1[0].text())
    except ValueError:
        ts_plot_options['line_width'] = self.ts_plot_options['default_line_width']
    ts_plot_options['line_antialiased'] = self.pw_plotOptions_ck_1[0].isChecked()
    ts_plot_options['line_alpha'] = self.pw_plotOptions_ck_2[0].isChecked()
    if ts_plot_options['line_alpha']:
        try:
            if ' %' in self.pw_plotOptions_ln_2[0].text():
                ts_plot_options['line_alpha_perc'] = float(self.pw_plotOptions_ln_2[0].text()[:-2])
            elif '%' in self.pw_plotOptions_ln_2[0].text():
                ts_plot_options['line_alpha_perc'] = float(self.pw_plotOptions_ln_2[0].text()[:-1])
            else:
                ts_plot_options['line_alpha_perc'] = float(self.pw_plotOptions_ln_2[0].text())
        except ValueError:
            ts_plot_options['line_alpha_perc'] = self.ts_plot_options['default_line_alpha_perc']
    if self.pw_plotOptions_ln_4[0].text():
        ts_plot_options['legend_label'] = str(self.pw_plotOptions_ln_4[0].text())
    else:
        ts_plot_options['legend_label'] = self.ts_plot_options['default_legend_label']

    if ts_plot_options['line_style'] != self.ts_plot_options['line_style']:
        self.ts_plot_options['line_style'] = ts_plot_options['line_style']
        self.ts_plot_options['line_marker'] = ts_plot_options['line_marker']
        if ts_plot_options['line_marker'] == 'line':
            plt.axes().lines[0].set_linestyle(ts_plot_options['line_style'])
            plt.axes().lines[0].set_marker(None)
        else:
            plt.axes().lines[0].set_linestyle('None')
            plt.axes().lines[0].set_marker(ts_plot_options['line_style'])
    if ts_plot_options['line_color'] != self.ts_plot_options['line_color']:
        self.ts_plot_options['line_color'] = ts_plot_options['line_color']
        plt.axes().lines[0].set_color(ts_plot_options['line_color'])
        if self.ts_figure_options['display_legend']:
            try:
                plt.gca().legend().set_draggable(True)
            except AttributeError:
                plt.gca().legend().draggable()
    if ts_plot_options['line_width'] != self.ts_plot_options['line_width']:
        self.ts_plot_options['line_width'] = ts_plot_options['line_width']
        if ts_plot_options['line_marker'] == 'line':
            plt.axes().lines[0].set_linewidth(ts_plot_options['line_width'])
        else:
            plt.axes().lines[0].set_markersize(ts_plot_options['line_width'])
    if ts_plot_options['line_antialiased'] != self.ts_plot_options['line_antialiased']:
        self.ts_plot_options['line_antialiased'] = ts_plot_options['line_antialiased']
        plt.axes().lines[0].set_antialiased(ts_plot_options['line_antialiased'])
    if ts_plot_options['line_alpha']:
        if (ts_plot_options['line_alpha'] != self.ts_plot_options['line_alpha'] or
                ts_plot_options['line_alpha_perc'] != self.ts_plot_options['line_alpha_perc']):
            self.ts_plot_options['line_alpha'] = ts_plot_options['line_alpha']
            self.ts_plot_options['line_alpha_perc'] = ts_plot_options['line_alpha_perc']
            plt.axes().lines[0].set_alpha(float(ts_plot_options['line_alpha_perc']) / 100.)
    else:
        if ts_plot_options['line_alpha'] != self.ts_plot_options['line_alpha']:
            self.ts_plot_options['line_alpha'] = ts_plot_options['line_alpha']
            plt.axes().lines[0].set_alpha(1)
    if ts_plot_options['legend_label'] != self.ts_plot_options['legend_label']:
        self.ts_plot_options['legend_label'] = ts_plot_options['legend_label']
        plt.axes().lines[0].set_label(str(ts_plot_options['legend_label']))
        if self.ts_figure_options['display_legend']:
            try:
                plt.gca().legend().set_draggable(True)
            except AttributeError:
                plt.gca().legend().draggable()
    self.canvas.draw()


def update_multiple_ts_plt_options(self):
    logging.debug('gui - plot_ts_main_functions.py - update_multiple_ts_plt_options')
    if "activated" in self.action_pan.objectName():
        self.plot_pan()
    if "activated" in self.action_zoom.objectName():
        self.plot_zoom()
    plot_options = dict()
    for i in range(self.plot_option_num):
        try:
            plot_options['line_style'] = self.line_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
            plot_options['line_marker'] = 'line'
        except KeyError:
            plot_options['line_style'] = self.marker_styles_dict[str(self.pw_plotOptions_cb_1[i].currentText())]
            plot_options['line_marker'] = 'marker'
        if str(self.pw_plotOptions_cb_2[i].currentText()) == 'HEX Color':
            if '#' not in str(self.pw_plotOptions_ln_3[i].text()):
                plot_options['line_color'] = '#' + str(self.pw_plotOptions_ln_3[i].text())
            else:
                plot_options['line_color'] = str(self.pw_plotOptions_ln_3[i].text())
        elif str(self.pw_plotOptions_cb_2[i].currentText()) == 'RGB Color':
            r = float(self.pw_plotOptions_ln_3[i].text()) / 255.
            g = float(self.pw_plotOptions_ln_5[i].text()) / 255.
            b = float(self.pw_plotOptions_ln_6[i].text()) / 255.
            plot_options['line_color'] = (r, g, b)
        else:
            plot_options['line_color'] = self.colors_dict[str(self.pw_plotOptions_cb_2[i].currentText())]
        plot_options['line_width'] = float(self.pw_plotOptions_ln_1[i].text())
        plot_options['line_antialiased'] = self.pw_plotOptions_ck_1[i].isChecked()
        plot_options['line_alpha'] = self.pw_plotOptions_ck_2[i].isChecked()
        if plot_options['line_alpha']:
            if ' %' in self.pw_plotOptions_ln_2[i].text():
                plot_options['line_alpha_perc'] = float(self.pw_plotOptions_ln_2[i].text()[:-2])
            elif '%' in self.pw_plotOptions_ln_2[i].text():
                plot_options['line_alpha_perc'] = float(self.pw_plotOptions_ln_2[i].text()[:-1])
            else:
                plot_options['line_alpha_perc'] = float(self.pw_plotOptions_ln_2[i].text())
        plot_options['legend_label'] = str(self.pw_plotOptions_ln_4[i].text())

        if self.plot_type == 'multiple_timeseries_single_fig':
            if plot_options['line_style'] != self.subplot_ts_plt_list[i]['line_style']:
                self.subplot_ts_plt_list[i]['line_style'] = plot_options['line_style']
                self.subplot_ts_plt_list[i]['line_marker'] = plot_options['line_marker']
                if plot_options['line_marker'] == 'line':
                    plt.axes().lines[i].set_linestyle(plot_options['line_style'])
                    plt.axes().lines[i].set_marker(None)
                else:
                    plt.axes().lines[i].set_linestyle('None')
                    plt.axes().lines[i].set_marker(plot_options['line_style'])
            if plot_options['line_color'] != self.subplot_ts_plt_list[i]['line_color']:
                self.subplot_ts_plt_list[i]['line_color'] = plot_options['line_color']
                plt.axes().lines[i].set_color(plot_options['line_color'])
                if self.ts_figure_options['display_legend']:
                    leg = plt.legend(prop={'family': self.default_font, 'size': '10'})
                    try:
                        leg.set_draggable(True)
                    except AttributeError:
                        leg.draggable()
            if plot_options['line_width'] != self.subplot_ts_plt_list[i]['line_width']:
                self.subplot_ts_plt_list[i]['line_width'] = plot_options['line_width']
                if plot_options['line_marker'] == 'line':
                    plt.axes().lines[i].set_linewidth(plot_options['line_width'])
                else:
                    plt.axes().lines[i].set_markersize(plot_options['line_width'])
            if plot_options['line_antialiased'] != self.subplot_ts_plt_list[i]['line_antialiased']:
                self.subplot_ts_plt_list[i]['line_antialiased'] = plot_options['line_antialiased']
                plt.axes().lines[i].set_antialiased(plot_options['line_antialiased'])
            if plot_options['line_alpha']:
                if (plot_options['line_alpha'] != self.subplot_ts_plt_list[i]['line_alpha'] or
                        plot_options['line_alpha_perc'] != self.subplot_ts_plt_list[i]['line_alpha_perc']):
                    self.subplot_ts_plt_list[i]['line_alpha'] = plot_options['line_alpha']
                    self.subplot_ts_plt_list[i]['line_alpha_perc'] = plot_options['line_alpha_perc']
                    plt.axes().lines[i].set_alpha(float(plot_options['line_alpha_perc']) / 100.)
            else:
                if plot_options['line_alpha'] != self.subplot_ts_plt_list[i]['line_alpha']:
                    self.subplot_ts_plt_list[i]['line_alpha'] = plot_options['line_alpha']
                    plt.axes().lines[i].set_alpha(1)
            if plot_options['legend_label'] != self.subplot_ts_plt_list[i]['legend_label']:
                self.subplot_ts_plt_list[i]['legend_label'] = plot_options['legend_label']
                plt.axes().lines[i].set_label(str(plot_options['legend_label']))
                if self.ts_figure_options['display_legend']:
                    leg = plt.legend(prop={'family': self.default_font, 'size': '10'})
                    try:
                        leg.set_draggable(True)
                    except AttributeError:
                        leg.draggable()
        else:
            if plot_options['line_style'] != self.subplot_ts_plt_list[i]['line_style']:
                self.subplot_ts_plt_list[i]['line_style'] = plot_options['line_style']
                self.subplot_ts_plt_list[i]['line_marker'] = plot_options['line_marker']
                if plot_options['line_marker'] == 'line':
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_linestyle(plot_options[
                                                                                                   'line_style'])
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_marker(None)
                else:
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_linestyle('None')
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_marker(plot_options['line_style'])
            if plot_options['line_color'] != self.subplot_ts_plt_list[i]['line_color']:
                self.subplot_ts_plt_list[i]['line_color'] = plot_options['line_color']
                self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_color(plot_options['line_color'])
                if self.subplot_ts_fig_list[i]['display_legend']:
                    leg = self.subplot_ts_plt_list[i]['figure_instance'].legend(prop={'family': self.default_font,
                                                                                      'size': '10'})
                    try:
                        leg.set_draggable(True)
                    except AttributeError:
                        leg.draggable()
            if plot_options['line_width'] != self.subplot_ts_plt_list[i]['line_width']:
                self.subplot_ts_plt_list[i]['line_width'] = plot_options['line_width']
                if plot_options['line_marker'] == 'line':
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_linewidth(plot_options[
                                                                                                   'line_width'])
                else:
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_markersize(plot_options[
                                                                                                    'line_width'])
            if plot_options['line_antialiased'] != self.subplot_ts_plt_list[i]['line_antialiased']:
                self.subplot_ts_plt_list[i]['line_antialiased'] = plot_options['line_antialiased']
                self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].\
                    set_antialiased(plot_options['line_antialiased'])
            if plot_options['line_alpha']:
                if (plot_options['line_alpha'] != self.subplot_ts_plt_list[i]['line_alpha'] or
                        plot_options['line_alpha_perc'] != self.subplot_ts_plt_list[i]['line_alpha_perc']):
                    self.subplot_ts_plt_list[i]['line_alpha'] = plot_options['line_alpha']
                    self.subplot_ts_plt_list[i]['line_alpha_perc'] = plot_options['line_alpha_perc']
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].\
                        set_alpha(float(plot_options['line_alpha_perc']) / 100.)
            else:
                if plot_options['line_alpha'] != self.subplot_ts_plt_list[i]['line_alpha']:
                    self.subplot_ts_plt_list[i]['line_alpha'] = plot_options['line_alpha']
                    self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].set_alpha(1)
            if plot_options['legend_label'] != self.subplot_ts_plt_list[i]['legend_label']:
                self.subplot_ts_plt_list[i]['legend_label'] = plot_options['legend_label']
                self.subplot_ts_plt_list[i]['figure_instance'].axes.lines[0].\
                    set_label(str(plot_options['legend_label']))
                if self.subplot_ts_fig_list[i]['display_legend']:
                    leg = self.subplot_ts_plt_list[i]['figure_instance'].legend(prop={'family': self.default_font,
                                                                                      'size': '10'})
                    try:
                        leg.set_draggable(True)
                    except AttributeError:
                        leg.draggable()
    self.canvas.draw()
