import configparser
import logging
import egads
import datetime
import inspect
import pathlib
import os
from PyQt5 import QtCore, QtGui, QtWidgets


def clear_layout(layout):
    logging.debug('gui - utils.py - clear_layout')
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)


def create_option_file(user_path):
    ini_file = open(str(pathlib.Path(user_path).joinpath('egads_gui.ini')), 'w')
    config_dict = configparser.ConfigParser()
    config_dict.add_section('LOG')
    config_dict.add_section('SYSTEM')
    config_dict.add_section('PLOTS')
    config_dict.add_section('OPTIONS')
    config_dict.add_section('FILES_FOLDERS')
    config_dict.set('LOG', 'level', 'DEBUG')
    config_dict.set('LOG', 'path', str(user_path))
    config_dict.set('SYSTEM', 'read_as_float', 'False')
    config_dict.set('SYSTEM', 'replace_fill_value', 'False')
    config_dict.set('SYSTEM', 'switch_fill_value', 'False')
    config_dict.set('PLOTS', 'same_unit_plot', '2')
    config_dict.set('PLOTS', 'subplot_disposition', '0')
    config_dict.set('PLOTS', 'x_info_disabled', 'False')
    config_dict.set('PLOTS', 'manual_axis_distribution', 'False')
    config_dict.set('PLOTS', 'first_dimension_axis', '0')
    config_dict.set('PLOTS', 'second_dimension_axis', '0')
    config_dict.set('PLOTS', 'third_dimension_axis', '0')
    config_dict.set('PLOTS', 'geo_as_standard', 'False')
    config_dict.set('OPTIONS', 'check_update', 'False')
    config_dict.set('FILES_FOLDERS', 'keep_opened_files', 'True')
    config_dict.set('FILES_FOLDERS', 'enable_user_folders', 'True')
    config_dict.write(ini_file)
    ini_file.close()


def update_config_file(user_path):
    option_missing = False
    config_dict = configparser.ConfigParser()
    config_dict.read(str(pathlib.Path(user_path).joinpath('egads_gui.ini')))
    try:
        config_dict['FILES_FOLDERS']
    except KeyError:
        option_missing = True
        config_dict.add_section('FILES_FOLDERS')
    if config_dict['FILES_FOLDERS'].getboolean('keep_opened_files') is None:
        option_missing = True
        config_dict.set('FILES_FOLDERS', 'keep_opened_files', 'True')
    if config_dict['FILES_FOLDERS'].getboolean('enable_user_folders') is None:
        option_missing = True
        config_dict.set('FILES_FOLDERS', 'enable_user_folders', 'True')
    if config_dict['PLOTS'].getboolean('manual_axis_distribution') is None:
        option_missing = True
        config_dict.set('PLOTS', 'manual_axis_distribution', 'False')
        config_dict.set('PLOTS', 'first_dimension_axis', '0')
        config_dict.set('PLOTS', 'second_dimension_axis', '0')
        config_dict.set('PLOTS', 'third_dimension_axis', '0')
        config_dict.set('PLOTS', 'geo_as_standard', 'False')
    if option_missing:
        ini_file = open(str(pathlib.Path(user_path, 'egads_gui.ini')), 'w')
        config_dict.write(ini_file)
        ini_file.close()


def create_logging_handlers(config_dict, filename, default_path):
    using_default_path = False
    if pathlib.Path(config_dict.get('LOG', 'path')).exists():
        log_filename = str(pathlib.Path(config_dict.get('LOG', 'path')).joinpath(filename))
    else:
        using_default_path = True
        log_filename = str(pathlib.Path(default_path).joinpath(filename))
    logging.getLogger('').handlers = []
    logging.basicConfig(filename=log_filename,
                        level=getattr(logging, config_dict.get('LOG', 'level')),
                        filemode='w',
                        format='%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    if using_default_path:
        logging.error('gui - logging system - path from ini file not found, using default path')


def str_format(color, style=''):
    logging.debug('gui - utils.py - str_format')
    _color = QtGui.QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)
    _format = QtGui.QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QtGui.QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    return _format


STYLES = {'keyword': str_format('blue'),
          'operator': str_format('red'),
          'brace': str_format('darkGray'),
          'defclass': str_format('black', 'bold'),
          'string': str_format('magenta'),
          'string2': str_format('darkMagenta'),
          'comment': str_format('darkGreen', 'italic'),
          'self': str_format('black', 'italic'),
          'numbers': str_format('brown')}


class Highlighter(QtGui.QSyntaxHighlighter):
    """ the following code is based on the work of David Boddie
        https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
    """

    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False']

    operators = [
        '=', '==', '!=', '<', '<=', '>', '>=',
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        '\+=', '-=', '\*=', '/=', '\%=',
        '\^', '\|', '\&', '\~', '>>', '<<']

    braces = ['\{', '\}', '\(', '\)', '\[', '\]']

    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        self.tri_single = (QtCore.QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QtCore.QRegExp('"""'), 2, STYLES['string2'])

        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                  for w in Highlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                  for o in Highlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                  for b in Highlighter.braces]

        rules += [
            (r'\bself\b', 0, STYLES['self']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),
            (r'#[^\n]*', 0, STYLES['comment']),
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers'])]

        self.rules = [(QtCore.QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, string_format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, string_format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)

    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False


def create_algorithm_dict():
    logging.debug('gui - utils.py - create_algorithm_dict')
    algorithm_list = {}
    rep_list = [item for item in dir(egads.algorithms) if '__' not in item]
    rep_list.remove('egads')
    for rep in rep_list:
        tmp = [item for item in dir(getattr(egads.algorithms, rep)) if '__' not in item]
        for algo in tmp:
            try:
                _ = getattr(getattr(egads.algorithms, rep), algo)().run
                item = str(inspect.getmodule(getattr(getattr(egads.algorithms, rep), algo)))
                algorithm_list[rep + ' - ' + algo] = {'name': algo, 'folder': rep, 'user': False,
                                                      'path': str(pathlib.Path(item[item.find(' from ') + 7: -2])),
                                                      'method': getattr(getattr(egads.algorithms, rep), algo)}
            except (TypeError, AttributeError):
                pass
    rep_list = [item for item in dir(egads.user_algorithms) if '__' not in item]
    rep_list.remove('user_algorithms')
    for rep in rep_list:
        tmp = [item for item in dir(getattr(egads.user_algorithms, rep)) if '__' not in item]
        for algo in tmp:
            try:
                _ = getattr(getattr(egads.user_algorithms, rep), algo)().run
                item = str(inspect.getmodule(getattr(getattr(egads.user_algorithms, rep), algo)))
                algorithm_list[rep + ' - ' + algo] = {'name': algo, 'folder': rep, 'user': True,
                                                      'path': str(pathlib.Path(item[item.find(' from ') + 7: -2])),
                                                      'method': getattr(getattr(egads.user_algorithms, rep), algo)}
            except (TypeError, AttributeError):
                pass
    return algorithm_list


def prepare_algorithm_categories(algorithm_list):
    logging.debug('gui - utils.py - prepare_algorithm_categories')
    algorithm_categories = []
    for key in algorithm_list.keys():
        algorithm_categories.append(key[:key.find(' - ')].title())
    return sorted(list(dict.fromkeys(algorithm_categories)))


def prepare_output_categories(algorithm_list):
    logging.debug('gui - utils.py - prepare_output_categories')
    output_categories = []
    for key, algo_dict in algorithm_list.items():
        output_metadata = algo_dict['method']().output_metadata
        if isinstance(output_metadata, list):
            for metadata in output_metadata:
                if isinstance(metadata['Category'], list):
                    for category in metadata['Category']:
                        output_categories.append(category)
                else:
                    output_categories.append(metadata['Category'])
        else:
            if isinstance(output_metadata['Category'], list):
                for category in output_metadata['Category']:
                    output_categories.append(category)
            else:
                output_categories.append(output_metadata['Category'])
    output_categories = sorted(list(dict.fromkeys(output_categories)))
    try:
        output_categories.remove('')
    except ValueError:
        pass
    return output_categories


def create_datestring():
    logging.debug('gui - utils.py - create_datestring')
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    date_string = year + '-' + month + '-' + day + ' ' + hour + ':' + minute
    return date_string


def prepare_long_string(string, length, space_num):
    logging.debug('gui - utils.py - prepare_long_string')
    new_string = ''
    i = 0
    while len(string) > length:
        if i > 0:
            new_string += ' ' * space_num
        new_string += string[:length] + '\n'
        string = string[length:]
        i += 1
    else:
        if i > 0:
            new_string += ' ' * space_num + string
        else:
            new_string += string
    return new_string


def check_string_max_length(string_list):
    logging.debug('gui - utils.py - check_string_max_length')
    max_length = 0
    for string in string_list:
        if len(string) > max_length:
            max_length = len(string)
    return max_length


def write_algorithm(filename, string, category, author):
    logging.debug('gui - utils.py - write_algorithm : filename ' + str(filename) + ', category' + str(category)
                  + ', author ' + str(author) + ', string ' + str(string))
    category = category.lower()
    algorithm_path = egads.user_path + '/user_algorithms/' + category
    addendum = '    from .' + filename + ' import *'
    if pathlib.Path(algorithm_path).is_dir():
        with open(algorithm_path + '/__init__.py', 'r') as in_file:
            init_file = in_file.readlines()
        import_num, add_num, exist = 0, 0, False
        for line in init_file:
            if '    from ' in line:
                import_num += 1
            if addendum in line:
                exist = True
        if import_num == 0:
            with open(algorithm_path + '/__init__.py', 'w') as out_file:
                for line in init_file:
                    if 'try:' in line:
                        line = line + addendum + '\n'
                    out_file.write(line)
        else:
            if not exist:
                with open(algorithm_path + '/__init__.py', 'w') as out_file:
                    for line in init_file:
                        if '    from ' in line:
                            add_num += 1
                            if add_num == import_num:
                                line = line + addendum + '\n'
                        out_file.write(line)
        algorithm_file = open(algorithm_path + '/' + filename + '.py', 'w')
        algorithm_file.write(string)
        algorithm_file.close()
    else:
        pathlib.Path(algorithm_path).mkdir()
        init_string = ('__author__ = "' + author + '"\n'
                       + '__date__ = "' + create_datestring() + '"\n'
                       + '__version__ = "1.0"\n\n'
                       + 'import logging\n\n'
                       + 'try:\n'
                       + '    from .' + filename + ' import *\n'
                       + "    logging.info('egads [user_algorithms/" + category + "] algorithms have been "
                       + "loaded')\nexcept Exception as e:\n"
                       + "    logging.error('an error occured during the loading of a " + frozen_egads + category
                       + "] algorithm: ' + str(e))\n")
        init_file = open(algorithm_path + '/__init__.py', 'w')
        init_file.write(init_string)
        init_file.close()
        init_addendum = 'import user_algorithms.' + category
        with open(egads.user_path + '/user_algorithms/__init__.py', 'r') as in_file:
            init_file = in_file.readlines()
        import_num, add_num = 0, 0
        for line in init_file:
            if 'import ' in line:
                import_num += 1
        with open(egads.user_path + '/user_algorithms/__init__.py', 'w') as out_file:
            for line in init_file:
                if 'import ' in line:
                    add_num += 1
                    if add_num == import_num:
                        line = line + '\n' + init_addendum
                out_file.write(line)
        algorithm_file = open(algorithm_path + '/' + filename + '.py', 'w')
        algorithm_file.write(string)
        algorithm_file.close()


def humansize(nbytes):
    logging.debug('gui - utils.py - humansize : nbytes ' + str(nbytes))
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if nbytes == 0:
        return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def populate_combobox(combobox, item_list, make_choice=True, set_index=None):
    logging.debug('gui - utils.py - populate_combobox')
    if make_choice:
        combobox.addItem("Make a choice...")
    if isinstance(item_list, dict):
        item_list = [key for key in sorted(item_list)]
    combobox.addItems(item_list)
    if set_index is not None:
        if isinstance(set_index, str):
            combobox.setCurrentIndex(combobox.findText(set_index))
        else:
            combobox.setCurrentIndex(set_index)


def set_size(bytes_size):
    logging.debug('gui - utils.py - set_size')
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while bytes_size >= 1024 and i < len(suffixes)-1:
        bytes_size /= 1024.
        i += 1
    f = ('%.2f' % bytes_size).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def add_element(doc, element_name, parent, value=None):
    logging.debug('gui - utils.py - add_element')
    new_element = doc.createElementNS('EGADSLineageGui', element_name)
    if value:
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element


def get_element_value(parent, element_name):
    logging.debug('gui - utils.py - get_element_value')
    elements = parent.getElementsByTagName(element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()


def icon_creation_function(icon_filename):
    logging.debug('gui - utils.py - icon_creation_function')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap('icons/' + str(icon_filename)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon


def font_creation_function(font_style):
    logging.debug('gui - utils.py - font_creation_function')
    font = QtGui.QFont()

    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    if font_style == 'normal':
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
    elif font_style == 'big':
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(11)
        # font.setBold(True)
        # font.setWeight(75)
    elif font_style == 'small':
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
    elif font_style == 'small-italic':
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        font.setItalic(True)
    return font


def stylesheet_creation_function(stylesheet):
    logging.debug('gui - utils.py - stylesheet_creation_function')
    stylesheet = 'graphic_materials/style_sheets/' + stylesheet + '_stylesheet.dat'
    f = open(stylesheet, 'r')
    stylesheet_str = ''.join(f.readlines())
    f.close()
    return stylesheet_str


def full_path_name_from_treewidget(treewidget=None, parent=None):
    if parent is None:
        parent = treewidget.selectedItems()[0]
    path = parent.text(0)
    var = parent.text(0)
    while parent:
        parent = parent.parent()
        if parent is not None:
            path = parent.text(0) + '/' + path
    path = '/' + path
    return path, var


def multi_full_path_name_from_treewidget(treewidget):
    multi_list = []
    for parent in treewidget.selectedItems():
        path = parent.text(0)
        var = parent.text(0)
        while parent:
            parent = parent.parent()
            if parent is not None:
                path = parent.text(0) + '/' + path
        path = '/' + path
        multi_list.append([path, var])
    return multi_list


def replace_old_path_by_new_path(var_dict, old_path, new_path):
    for key in list(var_dict.keys()):
        if key.find(old_path) == 0 and key != new_path:
            new_key = new_path + key[len(old_path):]
            var_dict[new_key] = var_dict.pop(key)
    return var_dict


def replace_old_path_by_new_path_tooltip(treewidget, new_path):

    def replace_old_path(parent):
        for i in range(parent.childCount()):
            if 'group' in parent.child(i).toolTip(0):
                tooltip = 'group: ' + parent.toolTip(0)[7:] + '/' + parent.child(i).text(0)
            else:
                tooltip = 'dataset: ' + parent.toolTip(0)[7:] + '/' + parent.child(i).text(0)
            parent.child(i).setToolTip(0, tooltip)
            replace_old_path(parent.child(i))

    item = treewidget.selectedItems()[0]
    old_tooltip = item.toolTip(0)
    if 'group' in old_tooltip:
        new_tooltip = 'group: ' + new_path[1:]
    else:
        new_tooltip = 'dataset: ' + new_path[1:]
    item.setToolTip(0, new_tooltip)
    replace_old_path(item)
