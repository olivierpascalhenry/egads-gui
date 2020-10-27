import logging
import time
import datetime
import os
import egads
import math
import simplekml
import numpy
import zipfile
import tempfile
import sys
import collections
from PyQt5 import QtCore
import matplotlib as mpl
from functions.material_functions import transparency_hexa_dict_function


class ReadFileThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(list)
    error = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal(dict)

    def __init__(self, file_path, file_ext, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - ReadFileThread - __init__')
        self.file_path = file_path
        self.file_ext = file_ext
        self.config_dict = config_dict

    def run(self):
        logging.debug('gui - file_functions.py - ReadFileThread - run')
        self.progress.emit(['Standby...', 0])
        raf = self.config_dict['SYSTEM'].getboolean('read_as_float')
        rfv = self.config_dict['SYSTEM'].getboolean('replace_fill_value')
        sfv = self.config_dict['SYSTEM'].getboolean('switch_fill_value')
        f = None
        # dim_list = []
        group_list = []
        var_attr_list = {}
        var_list = []
        glob_attr_list = {}
        unread_var = {}
        self.progress.emit(['Opening file...', 0])
        try:
            if self.file_ext == 'NetCDF Files (*.nc *.cdf)':
                f = egads.input.EgadsNetCdf(self.file_path, 'r')
                var_list = f.get_variable_list(group_walk=True, details=True)
                group_list = f.get_group_list(details=True)
                glob_attr_list = f.get_attribute_list()
            elif self.file_ext == 'NASA Ames Files (*.na)':
                f = egads.input.EgadsNasaAmes(self.file_path, 'r')
                var_list = sorted(f.get_variable_list() + f.get_variable_list(vartype='independant'))
                for attribute in f.get_attribute_list():
                    if attribute != 'V' and attribute != 'X':
                        glob_attr_list[attribute] = f.get_attribute_value(attribute)
                # dim_list = f.get_dimension_list()
            elif self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
                f = egads.input.EgadsHdf(self.file_path, 'r')
                var_list = f.get_variable_list(group_walk=True, details=True)
                group_list = f.get_group_list(details=True)
                glob_attr_list = f.get_attribute_list()
            for i, var in enumerate(var_list):
                text = 'Reading variable <i>' + var + '</i>...'
                self.progress.emit([text, math.floor(100 * float(i) / float(len(var_list)))])
                try:
                    egads_instance = f.read_variable(var, read_as_float=raf, replace_fill_value=rfv)
                    if self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
                        for attr in ['DIMENSION_LABELS', 'DIMENSION_LIST']:
                            if attr in egads_instance.metadata.keys():
                                del egads_instance.metadata[attr]
                    is_dim = False
                    if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
                        var_dim_list = f.get_dimension_list(str(var), details=True)
                        if len(var_dim_list) == 1:
                            if var == list(var_dim_list.keys())[0]:
                                is_dim = True
                        if is_dim:
                            var_attr_list[var] = [egads_instance, None, is_dim]
                        else:
                            var_attr_list[var] = [egads_instance, var_dim_list, is_dim]
                    else:
                        if var in f.get_dimension_list():
                            var_attr_list['/' + var] = [egads_instance, None, True]
                        else:
                            var_dim_list = collections.OrderedDict()
                            for dim, shape in f.get_dimension_list().items():
                                var_dim_list['/' + dim] = shape
                            var_attr_list['/' + var] = [egads_instance, var_dim_list, False]

                except Exception as e:
                    if 'dimensionality' in str(e):
                        reason = 'unit was not handled properly by EGADS'
                    elif 'cannot convert float NaN to integer' in str(e):
                        if sfv:
                            egads_instance = f.read_variable(var, read_as_float=raf, replace_fill_value=False)
                            if self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
                                for attr in ['DIMENSION_LABELS', 'DIMENSION_LIST']:
                                    if attr in egads_instance.metadata.keys():
                                        del egads_instance.metadata[attr]
                            is_dim = False
                            if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
                                var_dim_list = f.get_dimension_list(str(var), details=True)
                                if len(var_dim_list) == 1:
                                    if var == list(var_dim_list.keys())[0]:
                                        is_dim = True
                                var_attr_list[var] = [egads_instance, var_dim_list, is_dim]
                            else:
                                if var in list(dim_list.keys()):
                                    is_dim = True
                                var_attr_list['/' + var] = [egads_instance, f.get_dimension_list(), is_dim]
                            continue
                        else:
                            reason = 'integer can\'t be converted to NaN in INT-type variable'
                    else:

                        # add error type


                        reason = 'no reason detected'
                    unread_var[var] = reason
                    logging.exception('gui - file_functions.py - ReadFileThread : an error occured during the '
                                      'reading of a variable, variable ' + str(var))
            for var in unread_var:
                var_list.remove(var)

            if group_list:
                for group in group_list:
                    var_attr_list[group] = [f.get_attribute_list(group), None,
                                            False]

            final_dict = {'unread_var': unread_var, 'opened_file': f, 'var_attr_list': var_attr_list,
                          'glob_attr_list': glob_attr_list}
            self.finished.emit(final_dict)
        except Exception:
            logging.exception('gui - file_functions.py - ReadFileThread : an error occured during the reading of a '
                              'file')
            etype, evalue, _ = sys.exc_info()
            self.error.emit([etype.__name__, str(evalue)])

    def stop(self):
        logging.debug('gui - file_functions.py - ReadFileThread - stop')
        self.terminate()


class SaveFileThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(list)
    error = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal()

    def __init__(self, file_name, file_ext, open_file_ext, glob_attr, var_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - SaveFileThread - __init__')
        self.file_name = file_name
        self.file_ext = file_ext
        self.open_file_ext = open_file_ext
        self.glob_attr = glob_attr
        self.var_dict = var_dict

    def run(self):
        logging.debug('gui - file_functions.py - SaveFileThread - run')
        if self.file_ext == 'NetCDF Files (*.nc *.cdf)':
            self.run_netcdf()
        elif self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
            self.run_hdf()
        elif self.file_ext == 'NASA Ames Files (*.na)':
            self.run_nasaames()

    def run_netcdf(self):
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short', 'int8': 'byte',
                       'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        if self.open_file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
            try:
                self.progress.emit(['Standby...', 0])
                var_nbr, prog_val = 0, 0
                for val in self.var_dict.values():
                    if isinstance(val[0], egads.EgadsData):
                        var_nbr += 1
                step_val = 100. / (5 + var_nbr)

                # file creation
                new_file = egads.input.EgadsNetCdf(self.file_name, 'w')

                # groups
                prog_val += step_val
                self.progress.emit(['Adding groups...', int(prog_val)])
                for var_name, var_sublist in sorted(self.var_dict.items()):
                    if not isinstance(var_sublist[0], egads.EgadsData):
                        new_file.add_group(var_name)
                        for attr_name, attr_value in self.var_dict[var_name][0].items():
                            new_file.add_attribute(attr_name, attr_value, var_name)

                # dimensions
                prog_val += step_val
                self.progress.emit(['Adding dimensions...', int(prog_val)])
                for var_name, var_sublist in self.var_dict.items():
                    if var_sublist[2]:
                        size = var_sublist[0].shape[0]
                        new_file.add_dim(var_name, size)

                # global attributes
                prog_val += step_val
                self.progress.emit(['Adding global attributes...', int(prog_val)])
                conventions_bool, history_bool = False, False
                for key, value in self.glob_attr.items():
                    if 'Conventions' in key:
                        conventions_bool = True
                    if 'history' in key:
                        history_bool = True
                    try:
                        new_file.add_attribute(key, float(value))
                    except ValueError:
                        new_file.add_attribute(key, str(value))
                if not conventions_bool:
                    new_file.add_attribute('Conventions', 'CF-1.0')
                if not history_bool:
                    history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                               + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                               + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                               + ' - NetCdf file created by EGADS and its GUI.')
                    new_file.add_attribute('history', history)

                # variables
                for var_name, var_sublist in self.var_dict.items():
                    if isinstance(var_sublist[0], egads.EgadsData):
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + var_name + '...', int(prog_val)])
                        data = var_sublist[0]

                        create_variable = True

                        if var_sublist[2]:
                            dim_tuple = tuple([os.path.basename(var_name)])
                        else:
                            if var_sublist[1] is None:
                                create_variable = False
                            else:
                                for dim in var_sublist[1]:
                                    if 'no dimension' in dim:
                                        create_variable = False
                                    else:
                                        if os.path.dirname(var_name) != os.path.dirname(dim):
                                            create_variable = False

                            if create_variable:
                                dim_tuple = tuple([os.path.basename(key) for key in var_sublist[1]])

                        if create_variable:
                            try:
                                var_format = format_dict[str(data.value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(data, var_name, dim_tuple, var_format)

                # close file
                prog_val += step_val
                self.progress.emit(['Closing NetCdf file...', int(prog_val)])
                new_file.close()
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - SaveFileThread : an error occured during the '
                                  'saving of a file')
                etype, evalue, _ = sys.exc_info()
                self.error.emit([etype.__name__, str(evalue)])
        elif self.open_file_ext == 'NASA Ames Files (*.na)':
            try:
                self.progress.emit(['Standby...', 0])
                var_nbr, prog_val = 0, 0
                for val in self.var_dict.values():
                    if isinstance(val[0], egads.EgadsData):
                        var_nbr += 1
                step_val = 100. / (4 + var_nbr)
                prog_val += step_val
                self.progress.emit(['Adding global attributes...', int(prog_val)])
                title = self.glob_attr['MNAME']
                source = self.glob_attr['SNAME']
                institution = self.glob_attr['ORG']
                authors = self.glob_attr['ONAME']
                history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                           + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                           + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                           + ' - NetCDF file created by EGADS and its GUI.')
                rev_date = (str(self.glob_attr['RDATE'][0]) + '-' + str(self.glob_attr['RDATE'][1]) + '-'
                            + str(self.glob_attr['RDATE'][2]))
                scom = ''
                ncom = ''
                if isinstance(self.glob_attr['SCOM'], list):
                    for i in self.glob_attr['SCOM']:
                        scom += i + '\n'
                    scom = scom[:-1]
                else:
                    scom = self.glob_attr['SCOM']
                    if scom[-1:] == '\n':
                        scom = scom[:-1]
                if isinstance(self.glob_attr['NCOM'], list):
                    for i in self.glob_attr['NCOM']:
                        ncom += i + '\n'
                    ncom = ncom[:-1]
                else:
                    ncom = self.glob_attr['NCOM']
                    if ncom[-1:] == '\n':
                        ncom = ncom[:-1]
                new_file = egads.input.EgadsNetCdf(self.file_name, 'w')
                new_file.add_attribute('Conventions', 'CF-1.0')
                new_file.add_attribute('title', title)
                new_file.add_attribute('source', source)
                new_file.add_attribute('special_comments', scom)
                new_file.add_attribute('normal_comments', ncom)
                new_file.add_attribute('institution', institution)
                new_file.add_attribute('authors', authors)
                new_file.add_attribute('history', history)
                new_file.add_attribute('data_date_of_revision', rev_date)
                prog_val += step_val
                self.progress.emit(['Adding dimensions...', int(prog_val)])
                for var_name, var_dict in self.var_dict.items():
                    if var_dict[2]:
                        new_file.add_dim(var_name, var_dict[0].shape[0])
                for var_name, var_dict in self.var_dict.items():
                    prog_val += step_val
                    self.progress.emit(['Adding variable ' + var_name + '...', int(prog_val)])

                    create_variable = True

                    if var_dict[2]:
                        dim_tuple = tuple([os.path.basename(var_name)])
                    else:
                        if var_dict[1] is None:
                            create_variable = False
                        else:
                            for dim in var_dict[1]:
                                if 'no dimension' in dim:
                                    create_variable = False
                                else:
                                    if os.path.dirname(var_name) != os.path.dirname(dim):
                                        create_variable = False

                        if create_variable:
                            dim_tuple = []
                            for dim in var_dict[1].keys():
                                if '/' in dim:
                                    dim_tuple.append(dim[1:])
                                else:
                                    dim_tuple.append(dim)

                            dim_tuple = tuple(dim_tuple)
                    if create_variable:
                        try:
                            var_format = format_dict[str(var_dict[0].value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        new_file.write_variable(var_dict[0], var_name, dim_tuple, var_format)

                prog_val += step_val
                self.progress.emit(['Closing NetCdf file...', int(prog_val)])
                new_file.close()
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - SaveFileThread : an error occured during the '
                                  'saving of a file')
                etype, evalue, _ = sys.exc_info()
                self.error.emit([etype.__name__, str(evalue)])

    def run_hdf(self):
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short', 'int8': 'byte',
                       'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        if self.open_file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
            try:
                self.progress.emit(['Standby...', 0])
                var_nbr, prog_val = 0, 0
                for val in self.var_dict.values():
                    if isinstance(val[0], egads.EgadsData):
                        var_nbr += 1
                step_val = 100. / (5 + var_nbr)
                new_file = egads.input.EgadsHdf(self.file_name, 'w')
                prog_val += step_val
                self.progress.emit(['Adding groups...', int(prog_val)])

                for var_name, var_sublist in sorted(self.var_dict.items()):
                    if not isinstance(var_sublist[0], egads.EgadsData):
                        new_file.add_group(var_name)
                        for attr_name, attr_value in var_sublist[0].items():
                            new_file.add_attribute(attr_name, attr_value, var_name)

                prog_val += step_val
                self.progress.emit(['Adding global attributes...', int(prog_val)])
                history_bool = False
                for key, value in self.glob_attr.items():
                    if 'history' in key:
                        history_bool = True
                    try:
                        new_file.add_attribute(key, float(value))
                    except ValueError:
                        new_file.add_attribute(key, str(value))
                if not history_bool:
                    history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                               + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                               + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                               + ' - Hdf file created by EGADS and its GUI.')
                    new_file.add_attribute('history', history)
                for var_name, var_sublist in self.var_dict.items():
                    if var_sublist[2]:
                        prog_val += step_val
                        self.progress.emit(['Adding dimensions...', int(prog_val)])
                        new_file.add_dim(var_name, var_sublist[0])
                for var_name, var_sublist in self.var_dict.items():
                    if isinstance(var_sublist[0], egads.EgadsData) and not var_sublist[2]:
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + var_name + '...', int(prog_val)])

                        create_variable = True

                        if var_sublist[1] is None:
                            create_variable = False
                        else:
                            for dim in var_sublist[1]:
                                if 'no dimension' in dim:
                                    create_variable = False
                                else:
                                    if os.path.dirname(var_name) != os.path.dirname(dim):
                                        create_variable = False

                        if create_variable:

                            dimensions_tuple = tuple([os.path.basename(key) for key in var_sublist[1]])
                            try:
                                var_format = format_dict[str(var_sublist[0].value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(var_sublist[0], var_name, dimensions_tuple, var_format)
                prog_val += step_val
                self.progress.emit(['Closing Hdf file...', int(prog_val)])
                new_file.close()
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - SaveFileThread : an error occured during the '
                                  'saving of a file')
                etype, evalue, _ = sys.exc_info()
                self.error.emit([etype.__name__, str(evalue)])
        elif self.open_file_ext == 'NASA Ames Files (*.na)':
            try:
                self.progress.emit(['Standby...', 0])
                var_nbr, prog_val = 0, 0
                for val in self.var_dict.values():
                    if isinstance(val[0], egads.EgadsData):
                        var_nbr += 1
                step_val = 100. / (4 + var_nbr)
                prog_val += step_val
                self.progress.emit(['Adding global attributes...', int(prog_val)])
                title = self.glob_attr['MNAME']
                source = self.glob_attr['SNAME']
                institution = self.glob_attr['ORG']
                authors = self.glob_attr['ONAME']
                history = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-'
                           + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().hour) + ':'
                           + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
                           + ' - Hdf file created by EGADS and its GUI.')
                rev_date = (str(self.glob_attr['RDATE'][0]) + '-' + str(self.glob_attr['RDATE'][1]) + '-'
                            + str(self.glob_attr['RDATE'][2]))
                scom = ''
                ncom = ''
                if isinstance(self.glob_attr['SCOM'], list):
                    for i in self.glob_attr['SCOM']:
                        scom += i + '\n'
                    scom = scom[:-1]
                else:
                    scom = self.glob_attr['SCOM']
                    if scom[-1:] == '\n':
                        scom = scom[:-1]
                if isinstance(self.glob_attr['NCOM'], list):
                    for i in self.glob_attr['NCOM']:
                        ncom += i + '\n'
                    ncom = ncom[:-1]
                else:
                    ncom = self.glob_attr['NCOM']
                    if ncom[-1:] == '\n':
                        ncom = ncom[:-1]
                new_file = egads.input.EgadsHdf(self.file_name, 'w')
                new_file.add_attribute('Conventions', 'CF-1.0')
                new_file.add_attribute('title', title)
                new_file.add_attribute('source', source)
                new_file.add_attribute('special_comments', scom)
                new_file.add_attribute('normal_comments', ncom)
                new_file.add_attribute('institution', institution)
                new_file.add_attribute('authors', authors)
                new_file.add_attribute('history', history)
                new_file.add_attribute('data_date_of_revision', rev_date)
                prog_val += step_val
                self.progress.emit(['Adding dimensions...', int(prog_val)])
                for var, sublist in self.var_dict.items():
                    if sublist[2]:
                        new_file.add_dim(var, sublist[0])
                for var, sublist in self.var_dict.items():
                    if not sublist[2]:
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + var + '...', int(prog_val)])

                        create_variable = True

                        if sublist[2]:
                            dim_tuple = tuple([os.path.basename(var)])
                        else:
                            if sublist[1] is None:
                                create_variable = False
                            else:
                                for dim in sublist[1]:
                                    if 'no dimension' in dim:
                                        create_variable = False
                                    else:
                                        if os.path.dirname(var) != os.path.dirname(dim):
                                            create_variable = False

                            if create_variable:
                                dim_tuple = tuple(sublist[1].keys())
                        if create_variable:
                            try:
                                var_format = format_dict[str(sublist[0].value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(sublist[0], var, dim_tuple, var_format)
                self.progress.emit(['Closing Hdf file...', int(prog_val)])
                new_file.close()
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - SaveFileThread : an error occured during the '
                                  'saving of a file')
                etype, evalue, _ = sys.exc_info()
                self.error.emit([etype.__name__, str(evalue)])

    def run_nasaames(self):
        if self.open_file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
            try:
                self.progress.emit(['Standby...', 0])
                var_nbr, prog_val = 0, 0
                for val in self.var_dict.values():
                    if isinstance(val[0], egads.EgadsData):
                        var_nbr += 1
                step_val = 100. / (6 + var_nbr)
                new_file = egads.input.EgadsNasaAmes()
                na_dict = new_file.create_na_dict()
                prog_val += step_val
                self.progress.emit(['Preparing global attributes...', int(prog_val)])
                nlhead, ffi, org, oname, sname, mname, dx = -999, 1001, '', '', '', '', 0.0
                ivol, nvol = 1, 1
                try:
                    org = self.glob_attr['institution']
                except KeyError:
                    org = 'no institution'
                try:
                    oname = self.glob_attr['authors']
                except KeyError:
                    try:
                        oname = self.glob_attr['institution']
                    except KeyError:
                        oname = 'no author'
                try:
                    sname = self.glob_attr['source']
                except KeyError:
                    sname = 'no source'
                try:
                    mname = self.glob_attr['title']
                except KeyError:
                    mname = 'no title'
                rdate = [datetime.datetime.now().year, datetime.datetime.now().month,
                         datetime.datetime.now().day]
                date = None
                niv = 0
                prog_val += step_val
                name_string = ''
                self.progress.emit(['Adding dimensions...', int(prog_val)])
                for ivar, sublist in self.var_dict.items():
                    if sublist[2]:
                        if ivar[0] == '/':
                            ivar = ivar[1:]
                        name_string += ivar + '    '
                        data = sublist[0]
                        new_file.write_variable(data, ivar, vartype='independant', na_dict=na_dict)
                        niv += 1
                        if 'time' in ivar:
                            units = data.metadata['units']
                            ref_time = None
                            try:
                                index = units.index(' since ')
                                ref_time = units[index + 7:]
                            except (KeyError, ValueError):
                                pass
                            try:
                                ref_time = dateutil.parser.parse(ref_time).strftime("%Y%m%dT%H%M%S")
                                isotime = egads.algorithms.transforms.SecondsToIsotime().run(data, ref_time)
                                y, m, d, _, _, _ = egads.algorithms.transforms.IsotimeToElements().run(isotime)
                                date = [y.value[0], m.value[0], d.value[0]]
                                if not date:
                                    date = [999, 999, 999]
                            except Exception:
                                date = [999, 999, 999]
                prog_val += step_val
                self.progress.emit(['Adding global attributes...', int(prog_val)])
                new_file.write_attribute_value('NLHEAD', nlhead, na_dict=na_dict)
                new_file.write_attribute_value('FFI', ffi, na_dict=na_dict)
                new_file.write_attribute_value('ONAME', oname, na_dict=na_dict)
                new_file.write_attribute_value('ONAME', oname, na_dict=na_dict)
                new_file.write_attribute_value('ORG', org, na_dict=na_dict)
                new_file.write_attribute_value('SNAME', sname, na_dict=na_dict)
                new_file.write_attribute_value('MNAME', mname, na_dict=na_dict)
                new_file.write_attribute_value('DATE', date, na_dict=na_dict)
                new_file.write_attribute_value('RDATE', rdate, na_dict=na_dict)
                new_file.write_attribute_value('NIV', niv, na_dict=na_dict)
                new_file.write_attribute_value('DX', dx, na_dict=na_dict)
                ncom = ['==== Normal Comments follow ====']
                for attr in self.glob_attr:
                    if attr != 'institution' and attr != 'authors' and attr != 'source' and attr != 'title':
                        ncom.append(attr + ': ' + str(self.glob_attr[attr]))
                ncom.append('==== Normal Comments end ====')
                ncom.append('=== Data Section begins on the next line ===')
                if self.open_file_ext == 'NetCDF Files (*.nc *.cdf)':
                    file_source = 'NetCDF'
                else:
                    file_source = 'HDF5'
                scom = ['==== Special Comments follow ====',
                        '=== Additional Variable Attributes defined in the source file ===',
                        '== Variable attributes from source (' + file_source + ') file follow ==']
                for var, sublist in self.var_dict.items():
                    if not sublist[2]:
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + var + '...', int(prog_val)])

                        create_variable = True

                        if sublist[1] is None:
                            create_variable = False
                        else:
                            for dim in sublist[1]:
                                if 'no dimension' in dim:
                                    create_variable = False
                                else:
                                    if os.path.dirname(var) != os.path.dirname(dim):
                                        create_variable = False

                        if create_variable:

                            if var[0] == '/':
                                var = var[1:]
                            new_file.write_variable(sublist[0], var, na_dict=na_dict)
                            first_line = True
                            for metadata in sublist[0].metadata:
                                if metadata != '_FillValue' and metadata != 'scale_factor' and metadata != \
                                        'units' and metadata != 'var_name':
                                    if first_line:
                                        first_line = False
                                        scom.append('  Variable ' + var + ':')
                                    scom.append('    ' + metadata + ' = ' + str(sublist[0].metadata[metadata]))
                            name_string += var + '    '
                prog_val += step_val
                self.progress.emit(['Adding last global attributes...', int(prog_val)])
                name_string = name_string[:-4]
                ncom.append(name_string)
                scom.append('== Variable attributes from source (' + file_source + ') file end ==')
                scom.append('==== Special Comments end ====')
                new_file.write_attribute_value('NVOL', nvol, na_dict=na_dict)
                new_file.write_attribute_value('IVOL', ivol, na_dict=na_dict)
                new_file.write_attribute_value('SCOM', scom, na_dict=na_dict)
                new_file.write_attribute_value('NCOM', ncom, na_dict=na_dict)
                new_file.write_attribute_value('NSCOML', len(scom), na_dict=na_dict)
                new_file.write_attribute_value('NNCOML', len(ncom), na_dict=na_dict)
                new_file.save_na_file(self.file_name, na_dict)
                self.progress.emit(['Closing NasaAmes file...', 100])
                new_file.close()
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - SaveFileThread : an error occured during the '
                                  'saving of a file')
                etype, evalue, _ = sys.exc_info()
                self.error.emit([etype.__name__, str(evalue)])
        elif self.open_file_ext == 'NASA Ames Files (*.na)':
            try:
                self.progress.emit(['Standby...', 0])
                var_nbr, prog_val = 0, 0
                for val in self.var_dict.values():
                    if isinstance(val[0], egads.EgadsData):
                        var_nbr += 1
                step_val = 100. / (3 + var_nbr)
                new_file = egads.input.EgadsNasaAmes()
                na_dict = new_file.create_na_dict()
                prog_val += step_val
                self.progress.emit(['Adding global attributes...', int(prog_val)])
                new_file.write_attribute_value('ONAME', self.glob_attr['ONAME'], na_dict=na_dict)
                new_file.write_attribute_value('ORG', self.glob_attr['ORG'], na_dict=na_dict)
                new_file.write_attribute_value('SNAME', self.glob_attr['SNAME'], na_dict=na_dict)
                new_file.write_attribute_value('MNAME', self.glob_attr['MNAME'], na_dict=na_dict)
                new_file.write_attribute_value('DATE', self.glob_attr['DATE'], na_dict=na_dict)
                new_file.write_attribute_value('NIV', 1, na_dict=na_dict)
                new_file.write_attribute_value('NSCOML', len(self.glob_attr['SCOM']), na_dict=na_dict)
                new_file.write_attribute_value('NNCOML', len(self.glob_attr['NCOM']), na_dict=na_dict)
                new_file.write_attribute_value('SCOM', self.glob_attr['SCOM'], na_dict=na_dict)
                new_file.write_attribute_value('NCOM', self.glob_attr['NCOM'], na_dict=na_dict)
                for name, sublist in sorted(self.var_dict.items()):
                    if sublist[2]:
                        prog_val += step_val
                        self.progress.emit(['Adding dimension ' + name + '...', int(prog_val)])
                        new_file.write_variable(sublist[0], vartype="independant", na_dict=na_dict)
                    else:
                        prog_val += step_val
                        self.progress.emit(['Adding variable ' + name + '...', int(prog_val)])

                        create_variable = True

                        if sublist[1] is None:
                            create_variable = False
                        else:
                            for dim in sublist[1]:
                                if 'no dimension' in dim:
                                    create_variable = False
                                else:
                                    if os.path.dirname(name) != os.path.dirname(dim):
                                        create_variable = False

                        if create_variable:

                            new_file.write_variable(sublist[0], vartype="main", na_dict=na_dict)
                self.progress.emit(['Closing NasaAmes file...', 100])
                new_file.save_na_file(self.file_name, na_dict)
                new_file.close()
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - SaveFileThread : an error occured during the '
                                  'saving of a file')
                etype, evalue, _ = sys.exc_info()
                self.error.emit([etype.__name__, str(evalue)])

    def stop(self):
        logging.debug('gui - file_functions.py - SaveFileThread - stop')
        self.terminate()


class ExportThread(QtCore.QThread):
    error = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, export_format, export_dict, var_dict, file_name, file_ext):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - ExportThread - __init__')
        self.export_format = export_format
        self.export_dict = export_dict
        self.var_dict = var_dict
        self.file_name = file_name
        self.file_ext = file_ext

    def run(self):
        logging.debug('gui - file_functions.py - ExportThread - run')
        colormap_dict = {0: {'fig_height': 1, 'fig_width': 8, 'left': 0.05, 'bottom': 0.60, 'width': 0.9,
                             'height': 0.25, 'position': 'bottom', 'orientation': 'horizontal'},
                         1: {'fig_height': 1, 'fig_width': 8, 'left': 0.05, 'bottom': 0.60, 'width': 0.9,
                             'height': 0.25, 'position': 'top', 'orientation': 'horizontal'},
                         2: {'fig_height': 8, 'fig_width': 1, 'left': 0.05, 'bottom': 0.05, 'width': 0.25,
                             'height': 0.9, 'position': 'left', 'orientation': 'vertical'},
                         3: {'fig_height': 8, 'fig_width': 1, 'left': 0.05, 'bottom': 0.05, 'width': 0.25,
                             'height': 0.9, 'position': 'right', 'orientation': 'vertical'}}
        if self.export_format == 'GE-TS':
            try:
                if self.export_dict['Options']['reduce_samples']:
                    redux = int(self.export_dict['Options']['reduce_value'])
                else:
                    redux = 1
                lon = self.var_dict[self.export_dict['Coordinates']['lon']][0].value.tolist()[::redux]
                lat = self.var_dict[self.export_dict['Coordinates']['lat']][0].value.tolist()[::redux]
                if self.export_dict['Coordinates']['alt'] == 'ground':
                    alt = None
                else:
                    alt = self.var_dict[self.export_dict['Coordinates']['alt']][0].value.tolist()[::redux]
                var = self.var_dict[self.export_dict['Variables'][0]][0].value.tolist()[::redux]
                var_units = self.var_dict[self.export_dict['Variables'][0]][0].metadata['units']
                var_name = self.export_dict['Variables'][0]
                var_steps, var_min, var_max, ticks_lbl = None, None, None, None
                if self.export_dict['Colormap']['automatic']:
                    var_min = math.floor(min(var))
                    var_max = math.ceil(max(var))
                    var_steps = 15
                else:

                    if self.export_dict['Colormap']['ticks_list']:
                        var_min = self.export_dict['Colormap']['ticks_list'][0]
                        var_max = self.export_dict['Colormap']['ticks_list'][-1]
                        ticks_lbl = [str(item) for item in self.export_dict['Colormap']['ticks_list']]
                    else:
                        if self.export_dict['Colormap']['min'] is not None:
                            var_min = float(self.export_dict['Colormap']['min'])
                        else:
                            var_min = math.floor(min(var))
                        if self.export_dict['Colormap']['max'] is not None:
                            var_max = float(self.export_dict['Colormap']['max'])
                        else:
                            var_max = math.ceil(max(var))
                        if self.export_dict['Colormap']['steps'] is not None:
                            var_steps = int(self.export_dict['Colormap']['steps'])
                        else:
                            var_steps = 15
                if self.export_dict['Colormap']['auto_dimension']:
                    fig_width = colormap_dict[self.export_dict['Colormap']['position']]['fig_width']
                    fig_height = colormap_dict[self.export_dict['Colormap']['position']]['fig_height']
                    left = colormap_dict[self.export_dict['Colormap']['position']]['left']
                    bottom = colormap_dict[self.export_dict['Colormap']['position']]['bottom']
                    width = colormap_dict[self.export_dict['Colormap']['position']]['width']
                    height = colormap_dict[self.export_dict['Colormap']['position']]['height']
                else:
                    if self.export_dict['Colormap']['fig_width'] is not None:
                        fig_width = self.export_dict['Colormap']['fig_width']
                    else:
                        fig_width = colormap_dict[self.export_dict['Colormap']['position']]['fig_width']
                    if self.export_dict['Colormap']['fig_height'] is not None:
                        fig_height = self.export_dict['Colormap']['fig_height']
                    else:
                        fig_height = colormap_dict[self.export_dict['Colormap']['position']]['fig_height']
                    if self.export_dict['Colormap']['pos_left'] is not None:
                        left = self.export_dict['Colormap']['pos_left']
                    else:
                        left = colormap_dict[self.export_dict['Colormap']['position']]['left']
                    if self.export_dict['Colormap']['pos_bottom'] is not None:
                        bottom = self.export_dict['Colormap']['pos_bottom']
                    else:
                        bottom = colormap_dict[self.export_dict['Colormap']['position']]['bottom']
                    if self.export_dict['Colormap']['width'] is not None:
                        width = self.export_dict['Colormap']['width']
                    else:
                        width = colormap_dict[self.export_dict['Colormap']['position']]['width']
                    if self.export_dict['Colormap']['height'] is not None:
                        height = self.export_dict['Colormap']['height']
                    else:
                        height = colormap_dict[self.export_dict['Colormap']['position']]['height']
                fig = mpl.pyplot.figure(figsize=(fig_width, fig_height))
                ax1 = fig.add_axes([left, bottom, width, height])
                cmap_name = self.export_dict['Colormap']['colormap']
                if self.export_dict['Colormap']['reversed']:
                    cmap_name += '_r'
                cmap = getattr(mpl.cm, cmap_name)
                norm = mpl.colors.Normalize(vmin=var_min, vmax=var_max)
                color_range = []
                if self.export_dict['Colormap']['ticks_list']:
                    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm,
                                                    orientation=colormap_dict[self.export_dict['Colormap']['position']]
                                                    ['orientation'], ticks=self.export_dict['Colormap']['ticks_list'])
                    value_range = self.export_dict['Colormap']['ticks_list']
                    for color in cmap(numpy.linspace(0, 1, len(value_range))):
                        color_range.append(mpl.colors.rgb2hex(color[:3])[1:])
                    cb1.set_label(var_units)
                    if colormap_dict[self.export_dict['Colormap']['position']]['orientation'] == 'vertical':
                        cb1.ax.set_yticklabels(ticks_lbl)
                    else:
                        cb1.ax.set_xticklabels(ticks_lbl)
                else:
                    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm,
                                                    orientation=colormap_dict[self.export_dict['Colormap']['position']]
                                                    ['orientation'])
                    value_range = numpy.linspace(var_min, var_max, var_steps + 1)

                    for color in cmap(numpy.linspace(0, 1, var_steps)):
                        color_range.append(mpl.colors.rgb2hex(color[:3])[1:])
                    cb1.set_label(var_units)

                if self.export_dict['Options']['wall_transparency']:
                    transparency = transparency_hexa_dict_function()[100 - self.export_dict['Options']['transparency']]
                else:
                    transparency = None
                style_list = []
                line_list = []
                for i, color in enumerate(color_range):
                    style_list.append(simplekml.Style())
                    style_list[i].linestyle.color = simplekml.Color.hex(color)
                    style_list[i].linestyle.width = self.export_dict['Options']['path_width']
                    if transparency is not None:
                        style_list[i].polystyle.color = simplekml.Color.hexa(color + transparency)
                    else:
                        style_list[i].polystyle.color = simplekml.Color.hex(color)
                kml = simplekml.Kml(name="Aircraft path & data", open=1)
                doc = kml.newdocument(name='Data', snippet=simplekml.Snippet(str(datetime.datetime.now())))
                fol = doc.newfolder(name=var_name)
                for i, _ in enumerate(var[:-1]):
                    line_list.append(fol.newlinestring(name=var_name))
                    if alt == 'ground':
                        alt_val = [0, 0]
                    else:
                        alt_val = [alt[i], alt[i + 1]]
                    line_list[i].coords = [(lon[i], lat[i], alt_val[0]), (lon[i + 1], lat[i + 1], alt_val[1])]
                    line_list[i].altitudemode = simplekml.AltitudeMode.absolute
                    if self.export_dict['Options']['wall']:
                        line_list[i].extrude = 1
                    else:
                        line_list[i].extrude = 0
                    if self.export_dict['Colormap']['color_value'] == 0:
                        var_moy = float(var[i] + var[i + 1]) / 2.
                    elif self.export_dict['Colormap']['color_value'] == 1:
                        var_moy = var[i]
                    else:
                        var_moy = var[i + 1]
                    idx = None
                    if var_moy < value_range[0]:
                        idx = 0
                    elif var_moy > value_range[-1]:
                        idx = -1
                    else:
                        for j, _ in enumerate(value_range):
                            if value_range[j] <= var_moy < value_range[j + 1]:
                                idx = j
                                break
                    line_list[i].style = style_list[idx]
                cmap_x = 0
                cmap_y = 0
                if colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'bottom':
                    cmap_x = 0.5
                    cmap_y = 0
                elif colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'top':
                    cmap_x = 0.5
                    cmap_y = 1
                elif colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'left':
                    cmap_x = 0
                    cmap_y = 0.5
                elif colormap_dict[self.export_dict['Colormap']['position']]['position'] == 'right':
                    cmap_x = 1
                    cmap_y = 0.5
                screen = doc.newscreenoverlay(name='colormap')
                screen.icon.href = 'colormap.jpg'
                screen.overlayxy = simplekml.OverlayXY(x=cmap_x, y=cmap_y, xunits=simplekml.Units.fraction,
                                                       yunits=simplekml.Units.fraction)
                screen.screenxy = simplekml.ScreenXY(x=cmap_x, y=cmap_y, xunits=simplekml.Units.fraction,
                                                     yunits=simplekml.Units.fraction)
                screen.size.x = -1
                screen.size.y = -1
                screen.size.xunits = simplekml.Units.fraction
                screen.size.yunits = simplekml.Units.fraction
                if self.file_ext == 'Google Earth KMZ (*.kmz)':
                    kmz = zipfile.ZipFile(self.file_name, 'w', zipfile.ZIP_DEFLATED)
                    kml_filename = os.path.basename(self.file_name)[0:-3] + 'kml'
                    kmz.writestr(kml_filename, kml.kml())
                    jpg_filename = tempfile.mkstemp('.jpg')[1]
                    mpl.pyplot.savefig(jpg_filename)
                    kmz.write(jpg_filename, 'colormap.jpg')
                    kmz.close()
                else:
                    mpl.pyplot.savefig(os.path.join(os.path.dirname(self.file_name), 'colormap.jpg'))
                    kml.save(self.file_name)
                self.finished.emit()
            except Exception:
                logging.exception('gui - file_functions.py - ExportThread - run : an error occured during the '
                                  'creation of the file')
                self.error.emit()
        elif self.export_format == 'GE-MP':
            pass

    def stop(self):
        logging.debug('gui - file_functions.py - ExportThread - stop')
        self.terminate()


class PrintingThread(QtCore.QThread):
    started = QtCore.pyqtSignal()
    end = QtCore.pyqtSignal()

    def __init__(self, file_name, option_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - PrintingThread - __init__')
        self.file_name = file_name
        self.option_dict = option_dict

    def run(self):
        logging.debug('gui - file_functions.py - PrintingThread - run')
        self.started.emit()
        mpl.pyplot.savefig(self.file_name, **self.option_dict)
        self.end.emit()

    def stop(self):
        logging.debug('gui - file_functions.py - StatusbarMsgThread - stop')
        self.terminate()
