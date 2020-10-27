import logging
import pathlib
import datetime
import os
import egads
import math
import copy
import sys
from PyQt5 import QtCore, QtWidgets


class VariableProcessingThread(QtCore.QThread):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, algorithm, list_combobox_input, coefficient_matrix_values, list_edit_output,
                 list_of_variables_and_attributes):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - VariableProcessingThread - __init__')
        self.algorithm = algorithm
        self.list_combobox_input = list_combobox_input
        self.coefficient_matrix_values = coefficient_matrix_values
        self.list_edit_output = list_edit_output
        self.list_of_variables_and_attributes = list_of_variables_and_attributes
        self.list_of_new_variables_and_attributes = dict()

    def run(self):
        logging.debug('gui - file_functions.py - VariableProcessingThread - run')
        self.started.emit()
        try:
            args = []
            dimension_out = None
            path_out = None
            # first_var = True
            for index, item in enumerate(self.list_combobox_input):
                if isinstance(item, QtWidgets.QComboBox):
                    sublist = self.list_of_variables_and_attributes['/' + item.currentText()]
                    args.append(sublist[0])
                    # if first_var:
                    #     dimension_out = sublist[1]
                    #     if os.path.dirname(item.currentText()) == '/':
                    #         path_out = '/'
                    #     else:
                    #         path_out = os.path.dirname(item.currentText()) + '/'
                    #     first_var = False
                elif isinstance(item, QtWidgets.QLineEdit):
                    try:
                        args.append(float(item.text()))
                    except ValueError:
                        args.append(str(item.text()))
                elif isinstance(item, QtWidgets.QHBoxLayout):
                    args.append(self.coefficient_matrix_values[item.itemAt(0).widget().objectName()])
            output = self.algorithm().run(*args)
            if isinstance(output, tuple):
                for index, var_out in enumerate(output):
                    var_name = '/' + str(self.list_edit_output[index].text())
                    # self.list_of_new_variables_and_attributes[var_name] = [var_out, dimension_out, path_out]
                    self.list_of_new_variables_and_attributes[var_name] = [var_out, None, path_out]
            else:
                var_name = '/' + str(self.list_edit_output[0].text())
                # self.list_of_new_variables_and_attributes[var_name] = [output, dimension_out, path_out]
                self.list_of_new_variables_and_attributes[var_name] = [output, None, path_out]
            self.finished.emit(self.list_of_new_variables_and_attributes)
        except Exception:
            logging.exception('gui - file_functions.py - VariableProcessingThread - an exception occurred')
            etype, evalue, _ = sys.exc_info()
            self.error.emit([etype.__name__, str(evalue)])

    def stop(self):
        logging.debug('gui - file_functions.py - VariableProcessingThread - stop')
        self.terminate()


class BatchProcessingThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(list)
    error = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal()

    def __init__(self, batch_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - file_functions.py - BatchProcessingThread - __init__')
        self.batch_dict = batch_dict
        self.config_dict = config_dict

    def run(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - run')
        if self.batch_dict['process'] == 1:
            self.concatenate_files()
        elif self.batch_dict['process'] == 2:
            self.file_conversion()
        elif self.batch_dict['process'] == 3:
            self.delete_metadata()
        elif self.batch_dict['process'] == 4:
            self.delete_variable()
        elif self.batch_dict['process'] == 5:
            self.algorithm_processing()

    def algorithm_processing(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - algorithm_processing')
        self.progress.emit(['Standby...', 0])
        read_as_float = self.config_dict['SYSTEM'].getboolean('read_as_float')
        replace_fill_value = self.config_dict['SYSTEM'].getboolean('replace_fill_value')
        switch_fill_value = self.config_dict['SYSTEM'].getboolean('switch_fill_value')
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        algorithm = self.batch_dict['algorithm']
        input_output = self.batch_dict['processing_options']
        out_format = self.batch_dict['out_format']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                ext = pathlib.Path(file_path).suffix
                filename = self.set_filename(file_path, ext, filename_base, start_nbr, digit_nbr)
                if out_format in ['NetCDF', 'HDF5']:
                    if out_format == 'NetCDF':
                        f = egads.input.EgadsNetCdf(file_path, 'r')
                    else:
                        f = egads.input.EgadsHdf(file_path, 'r')
                    var_list = [var_path for var_path in f.get_variable_list(group_walk=True, details=True)]
                    args = []
                    dimension_out = None
                    path_out = None
                    first_var = True
                    for item in input_output['inputs']:
                        if item in var_list:
                            try:
                                data = f.read_variable(str(item), read_as_float=read_as_float,
                                                       replace_fill_value=replace_fill_value)
                                args.append(data)
                            except ValueError as ve:
                                if 'cannot convert float NaN to integer' in str(ve):
                                    if switch_fill_value:
                                        data = f.read_variable(str(item), read_as_float=read_as_float,
                                                               replace_fill_value=False)
                                        args.append(data)
                                    else:
                                        raise Exception('cannot convert float NaN to integer')
                                else:
                                    raise Exception('')
                            if first_var:
                                dimension_out = f.get_dimension_list(str(item))
                                path_out = os.path.dirname(str(item))
                                first_var = False
                        else:
                            args.append(item)
                        output = algorithm().run(*args)
                        if out_format == 'NetCDF':
                            new_file = egads.input.EgadsNetCdf(str(pathlib.Path(dest_folder).joinpath(filename)), 'w')
                        else:
                            new_file = egads.input.EgadsHdf(str(pathlib.Path(dest_folder).joinpath(filename)), 'w')

                        # global attributes
                        for key, value in f.get_attribute_list().items():
                            new_file.add_attribute(key, value)

                        # groups
                        for group_path in f.get_group_list(details=True):
                            new_file.add_group(group_path)
                            for key, val in f.get_attribute_list(group_path).items():
                                new_file.add_attribute(key, val, group_path)

                        # dimensions
                        dim_list = []
                        for dim_path, size in f.get_dimension_list(group_walk=True, details=True).items():
                            if out_format == 'NetCDF':
                                new_file.add_dim(dim_path, size)
                            else:
                                dim_list.append(dim_path)
                                new_file.add_dim(dim_path, f.read_variable(dim_path))

                        # variables
                        for var_path in var_list:
                            if var_path not in dim_list:
                                var_data = f.read_variable(var_path)
                                dim_tuple = tuple([key for key in f.get_dimension_list(var_path)])
                                try:
                                    var_format = format_dict[str(var_data.value.dtype)]
                                except KeyError:
                                    var_format = 'double'
                                new_file.write_variable(var_data, var_path, dim_tuple, var_format)
                        dim_tuple = tuple([key for key in dimension_out])
                        if isinstance(output, tuple):
                            for index, var in enumerate(output):
                                if path_out != '/':
                                    var_name = path_out + '/' + input_output['outputs'][index]
                                else:
                                    var_name = path_out + input_output['outputs'][index]
                                try:
                                    var_format = format_dict[str(var.value.dtype)]
                                except KeyError:
                                    var_format = 'double'
                                new_file.write_variable(var, var_name, dim_tuple, var_format)
                        else:
                            if path_out != '/':
                                var_name = path_out + '/' + input_output['outputs'][0]
                            else:
                                var_name = path_out + input_output['outputs'][0]
                            try:
                                var_format = format_dict[str(output.value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(output, var_name, dim_tuple, var_format)
                        new_file.close()
                    f.close()
                else:
                    f = egads.input.NasaAmes(file_path, 'r')
                    if len(f.get_dimension_list()) > 1:
                        raise Exception('NASA Ames files with more than 1 dimension can\'t be processed at this time')
                    var_list = f.get_variable_list() + f.get_variable_list(vartype='independant')
                    args = []
                    for item in input_output['inputs']:
                        if item in var_list:
                            try:
                                data = f.read_variable(str(item), read_as_float=read_as_float,
                                                       replace_fill_value=replace_fill_value)
                                args.append(data)
                            except ValueError as ve:
                                if 'cannot convert float NaN to integer' in str(ve):
                                    if switch_fill_value:
                                        data = f.read_variable(str(item), read_as_float=read_as_float,
                                                               replace_fill_value=False)
                                        args.append(data)
                                    else:
                                        raise Exception('cannot convert float NaN to integer')
                                else:
                                    raise Exception('')
                        else:
                            args.append(item)
                    output = algorithm().run(*args)
                    na_dict = copy.deepcopy(f.na_dict)
                    if isinstance(output, tuple):
                        for index, var in enumerate(output):
                            var_name = input_output['outputs'][index]
                            f.write_variable(var, varname=var_name, vartype="main", na_dict=na_dict)
                    else:
                        var_name = input_output['outputs'][0]
                        f.write_variable(output, varname=var_name, vartype="main", na_dict=na_dict)
                    f.save_na_file(str(pathlib.Path(dest_folder).joinpath(filename)), na_dict)
                    f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - algorithm_processing - an '
                                  'exception occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def delete_variable(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - delete_variable')
        self.progress.emit(['Standby...', 0])
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        targeted_variable = [variable[0] for variable in self.batch_dict['processing_options']]
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                ext = pathlib.Path(file_path).suffix
                filename = self.set_filename(file_path, ext, filename_base, start_nbr, digit_nbr)
                if ext in ['.na']:
                    f = egads.input.EgadsNasaAmes(file_path, 'r')
                    if len(f.get_dimension_list()) > 1:
                        raise Exception('NASA Ames files with more than 1 dimension can\'t be processed at this time')
                    na_dict = copy.deepcopy(f.na_dict)
                    na_dict['V'] = []
                    na_dict['NV'] = 0
                    na_dict['VMISS'] = []
                    na_dict['VNAME'] = []
                    na_dict['VSCAL'] = []
                    for var in f.get_variable_list():
                        if var not in targeted_variable:
                            var_data = f.read_variable(var)
                            f.write_variable(var_data, vartype="main", na_dict=na_dict)
                    f.save_na_file(os.path.join(dest_folder, filename), na_dict)
                    f.close()
                else:
                    if ext in ['.nc', '.cdf']:
                        f = egads.input.EgadsNetCdf(file_path, 'r')
                        new_file = egads.input.EgadsNetCdf(os.path.join(dest_folder, filename), 'w')
                    else:
                        f = egads.input.EgadsHdf(file_path, 'r')
                        new_file = egads.input.EgadsHdf(os.path.join(dest_folder, filename), 'w')

                    # global metadata
                    for key, value in f.get_attribute_list().items():
                        new_file.add_attribute(key, value)

                    # groups and attributes
                    group_list = f.get_group_list(details=True)
                    del_group = []
                    for group in group_list:
                        for item in targeted_variable:
                            if group.find(item) == 0:
                                del_group.append(group)
                    for group in group_list:
                        if group not in del_group:
                            new_file.add_group(group)
                            attr = f.get_attribute_list(group)
                            for key, value in attr.items():
                                new_file.add_attribute(key, value, group)

                    # dimensions
                    del_dims = []
                    for dim in list(f.get_dimension_list(group_walk=True, details=True).keys()):
                        for item in targeted_variable:
                            if dim.find(item) == 0:
                                del_dims.append(dim)
                    dim_list = []
                    for dim_path, size in f.get_dimension_list(group_walk=True, details=True).items():
                        if dim_path not in del_dims:
                            if ext in ['.nc', '.cdf']:
                                new_file.add_dim(dim_path, size)
                            else:
                                dim_list.append(dim_path)
                                new_file.add_dim(dim_path, f.read_variable(dim_path))

                    # variables
                    del_vars = []
                    for var in f.get_variable_list(group_walk=True, details=True):
                        for item in targeted_variable:
                            if var.find(item) == 0:
                                del_vars.append(var)
                    for var_path in f.get_variable_list(group_walk=True, details=True):
                        if var_path not in del_vars and var_path not in dim_list:
                            var_data = f.read_variable(var_path)
                            dim_tuple = tuple([os.path.basename(key) for key in f.get_dimension_list(var_path)])
                            try:
                                var_format = format_dict[str(var_data.value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            new_file.write_variable(var_data, var_path, dim_tuple, var_format)

            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - nc_to_na - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def delete_metadata(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - delete_metadata')
        self.progress.emit(['Standby...', 0])
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        targeted_metadata = [metadata[1] for metadata in self.batch_dict['processing_options']]
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                ext = pathlib.Path(file_path).suffix
                filename = self.set_filename(file_path, ext, filename_base, start_nbr, digit_nbr)
                if ext in ['.nc', '.cdf']:
                    f = egads.input.EgadsNetCdf(file_path, 'r')
                    new_file = egads.input.EgadsNetCdf(os.path.join(dest_folder, filename), 'w')
                else:
                    f = egads.input.EgadsHdf(file_path, 'r')
                    new_file = egads.input.EgadsHdf(os.path.join(dest_folder, filename), 'w')

                # global metadata
                for key, value in f.get_attribute_list().items():
                    if key not in targeted_metadata:
                        new_file.add_attribute(key, value)

                # groups and attributes
                for group in f.get_group_list(details=True):
                    new_file.add_group(group)
                    for key, value in f.get_attribute_list(group).items():
                        new_file.add_attribute(key, value, group)

                # dimensions
                dim_list = []
                for dim_path, size in f.get_dimension_list(group_walk=True, details=True).items():
                    if ext in ['.nc', '.cdf']:
                        new_file.add_dim(dim_path, size)
                    else:
                        dim_list.append(dim_path)
                        new_file.add_dim(dim_path, f.read_variable(dim_path))

                # variables
                for var_path in f.get_variable_list(group_walk=True, details=True):
                    if var_path not in dim_list:
                        var_data = f.read_variable(var_path)
                        dim_tuple = tuple([key for key in f.get_dimension_list(var_path)])
                        try:
                            var_format = format_dict[str(var_data.value.dtype)]
                        except KeyError:
                            var_format = 'double'
                        new_file.write_variable(var_data, var_path, dim_tuple, var_format)
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - delete_metadata - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def file_conversion(self):
        if self.batch_dict['processing_options'] == 'HDF5 -> NASA Ames':
            self.h5_to_na()
        elif self.batch_dict['processing_options'] == 'HDF5 -> NetCDF':
            self.h5_to_nc()
        elif self.batch_dict['processing_options'] == 'NASA Ames -> HDF5':
            self.na_to_h5()
        elif self.batch_dict['processing_options'] == 'NASA Ames -> NetCDF':
            self.na_to_nc()
        elif self.batch_dict['processing_options'] == 'NetCDF -> HDF5':
            self.nc_to_h5()
        elif self.batch_dict['processing_options'] == 'NetCDF -> NASA Ames':
            self.nc_to_na()

    def h5_to_na(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - h5_to_na')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                filename = self.set_filename(file_path, '.na', filename_base, start_nbr, digit_nbr)
                f = egads.input.EgadsHdf(file_path, 'r')
                f.convert_to_nasa_ames(na_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - h5_to_na - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def h5_to_nc(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - h5_to_nc')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                filename = self.set_filename(file_path, '.nc', filename_base, start_nbr, digit_nbr)
                f = egads.input.EgadsHdf(file_path, 'r')
                f.convert_to_netcdf(os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - h5_to_nc - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def nc_to_h5(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - nc_to_h5')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                filename = self.set_filename(file_path, '.h5', filename_base, start_nbr, digit_nbr)
                f = egads.input.EgadsNetCdf(file_path, 'r')
                f.convert_to_hdf(hdf_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - nc_to_h5 - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def nc_to_na(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - nc_to_na')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                filename = self.set_filename(file_path, '.na', filename_base, start_nbr, digit_nbr)
                f = egads.input.EgadsNetCdf(file_path, 'r')
                f.convert_to_nasa_ames(na_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - nc_to_na - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def na_to_h5(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - na_to_h5')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                filename = self.set_filename(file_path, '.h5', filename_base, start_nbr, digit_nbr)
                f = egads.input.EgadsNasaAmes(file_path, 'r')
                f.convert_to_hdf(hdf_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - na_to_h5 - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def na_to_nc(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - na_to_nc')
        self.progress.emit(['Standby...', 0])
        stop_processing = self.batch_dict['stop_processing']
        dest_folder = self.batch_dict['destination_folder']
        error = False
        f = None
        filename_base, start_nbr, digit_nbr = self.set_filename_base()
        etype, evalue = None, None
        for i, file_path in enumerate(self.batch_dict['file_list']):
            try:
                self.progress.emit([os.path.split(file_path)[1],
                                    math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                # ext = pathlib.Path(file_path).suffix
                filename = self.set_filename(file_path, '.nc', filename_base, start_nbr, digit_nbr)
                f = egads.input.EgadsNasaAmes(file_path, 'r')
                f.convert_to_netcdf(nc_file=os.path.join(dest_folder, filename))
                f.close()
            except Exception:
                logging.exception('gui - file_functions.py - BatchProcessingThread - na_to_nc - an exception '
                                  'occurred during concatenation - stop_processing ' + str(stop_processing))

                etype, evalue, _ = sys.exc_info()

                if stop_processing == 0:
                    f.close()
                    continue
                else:
                    f.close()
                    error = True
                    break
        if not error:
            self.finished.emit()
        else:
            self.error.emit([etype.__name__, str(evalue)])

    def concatenate_files(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - concatenate_files')
        self.progress.emit(['Standby...', 0])
        format_dict = {'int32': 'int', 'float64': 'double', 'float32': 'float', 'int16': 'short',
                       'int8': 'byte', 'str': 'char', 'unicode': 'char', 'str_': 'char', 'unicode_': 'char'}
        stop_processing = self.batch_dict['stop_processing']
        processing_options = self.batch_dict['processing_options']
        dest_folder = self.batch_dict['destination_folder']
        out_format = self.batch_dict['out_format']
        error = False
        f = None
        etype, evalue = None, None
        if self.batch_dict['filename_options'] is None:
            if out_format == 'NetCDF':
                ext = '.nc'
            elif out_format == 'HDF5':
                ext = '.h5'
            else:
                ext = '.na'
            date_time = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
            final_filename = pathlib.Path(dest_folder).joinpath('concatenated_file_EGADS_' + date_time + ext)
        else:
            filename = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        _, file = os.path.split(self.batch_dict['file_list'][0])
                        filename += str(file)
                    elif 'date' in option:
                        filename += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename += option[6:]
                    else:
                        filename += option
            final_filename = pathlib.Path(dest_folder).joinpath(filename)
        if out_format == 'NetCDF' or out_format == 'HDF5':
            if out_format == 'NetCDF':
                final_file = egads.input.EgadsNetCdf(final_filename, 'w')
            else:
                final_file = egads.input.EgadsHdf(final_filename, 'w')
            global_attributes = {}
            for i, file_path in enumerate(self.batch_dict['file_list']):
                try:
                    self.progress.emit([os.path.split(file_path)[1],
                                        math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                    if out_format == 'NetCDF':
                        f = egads.input.EgadsNetCdf(pathlib.Path(file_path), 'r')
                    else:
                        f = egads.input.EgadsHdf(pathlib.Path(file_path), 'r')

                    # global attributes
                    if i == 0 and processing_options != 2:
                        global_attributes = f.get_attribute_list()
                    elif i > 0 and processing_options == 1:
                        global_attributes = {**global_attributes, **f.get_attribute_list()}

                    # groups
                    for group in f.get_group_list(details=True):
                        try:
                            final_file.add_group(group)
                        except ValueError as e:
                            if 'String match to name in use' in str(e) or 'name already exists' in str(e):
                                logging.warning('gui - file_functions.py - BatchProcessingThread - concatenate_files '
                                                '- group already in file, skipping group')

                    # dimensions
                    dim_list = []
                    for dim_path, size in f.get_dimension_list(group_walk=True, details=True).items():
                        try:
                            if out_format == 'NetCDF':
                                final_file.add_dim(dim_path, size)
                            else:
                                dim_list.append(dim_path)
                                final_file.add_dim(dim_path, f.read_variable(dim_path))
                        except (RuntimeError, OSError) as e:
                            if 'String match to name in use' in str(e) or 'name already exists' in str(e):
                                logging.warning('gui - file_functions.py - BatchProcessingThread - concatenate_files '
                                                '- dimension already in file, skipping dimension')

                    # variables
                    for var_path in f.get_variable_list(group_walk=True, details=True):
                        if var_path not in dim_list:
                            egads_instance = f.read_variable(var_path)
                            dim_tuple = tuple([key for key, _ in f.get_dimension_list(str(var_path)).items()])
                            try:
                                var_format = format_dict[str(egads_instance.value.dtype)]
                            except KeyError:
                                var_format = 'double'
                            final_file.write_variable(egads_instance, var_path, dim_tuple, var_format)
                    f.close()
                except Exception:
                    logging.exception('gui - file_functions.py - BatchProcessingThread - concatenate_files - an '
                                      'exception occurred during concatenation - stop_processing '
                                      + str(stop_processing))

                    etype, evalue, _ = sys.exc_info()

                    if stop_processing == 0:
                        f.close()
                        continue
                    else:
                        f.close()
                        error = True
                        break
            if not error:
                if processing_options == 0 or processing_options == 1:
                    for key, value in global_attributes.items():
                        try:
                            final_file.add_attribute(key, float(value))
                        except ValueError:
                            final_file.add_attribute(key, str(value))
                final_file.close()
                self.finished.emit()
            else:
                final_file.close()
                self.error.emit([etype.__name__, str(evalue)])
        elif out_format == 'NASA Ames':
            final_file = egads.input.NasaAmes()
            na_dict = final_file.create_na_dict()
            global_attributes = None
            for i, file_path in enumerate(self.batch_dict['file_list']):
                try:
                    self.progress.emit([os.path.split(file_path)[1],
                                        math.floor(100 * float(i) / float(len(self.batch_dict['file_list'])))])
                    f = egads.input.NasaAmes(str(pathlib.Path(file_path)), 'r')
                    if i == 0:
                        if processing_options != 2:
                            global_attributes = {'ONAME': f.get_attribute_value('ONAME'),
                                                 'ORG': f.get_attribute_value('ORG'),
                                                 'SNAME': f.get_attribute_value('SNAME'),
                                                 'MNAME': f.get_attribute_value('MNAME'),
                                                 'SCOM': f.get_attribute_value('SCOM'),
                                                 'NCOM': f.get_attribute_value('NCOM')}
                    else:
                        if processing_options == 1:
                            global_attributes['ONAME'] = global_attributes['ONAME'] + ' ' + f.get_attribute_value(
                                'ONAME')
                            global_attributes['ORG'] = global_attributes['ORG'] + ' ' + f.get_attribute_value('ORG')
                            global_attributes['SNAME'] = global_attributes['SNAME'] + ' ' + f.get_attribute_value(
                                'SNAME')
                            global_attributes['MNAME'] = global_attributes['MNAME'] + ' ' + f.get_attribute_value(
                                'MNAME')
                            global_attributes['SCOM'] = global_attributes['SCOM'] + ' ' + f.get_attribute_value('SCOM')
                            global_attributes['NCOM'] = global_attributes['NCOM'] + ' ' + f.get_attribute_value('NCOM')
                    ind_variable_list = f.get_variable_list(vartype='independant')
                    variable_list = f.get_variable_list(vartype='main')
                    if i == 0:
                        for name in ind_variable_list:
                            egads_instance = f.read_variable(name)
                            final_file.write_variable(egads_instance, varname=name, vartype="independant",
                                                      na_dict=na_dict)
                    for name in variable_list:
                        egads_instance = f.read_variable(name)
                        final_file.write_variable(egads_instance, varname=name, vartype="main", na_dict=na_dict)
                    f.close()
                except Exception:
                    logging.exception('gui - file_functions.py - BatchProcessingThread - concatenate_files - an '
                                      'exception occurred during concatenation - stop_processing '
                                      + str(stop_processing))

                    etype, evalue, _ = sys.exc_info()

                    if stop_processing == 0:
                        f.close()
                        continue
                    else:
                        f.close()
                        error = True
                        break
            if not error:
                no_header = False
                if processing_options == 2:
                    no_header = True
                else:
                    date = [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day]
                    final_file.write_attribute_value('ONAME', global_attributes['ONAME'], na_dict=na_dict)
                    final_file.write_attribute_value('ORG', global_attributes['ORG'], na_dict=na_dict)
                    final_file.write_attribute_value('SNAME', global_attributes['SNAME'], na_dict=na_dict)
                    final_file.write_attribute_value('MNAME', global_attributes['MNAME'], na_dict=na_dict)
                    final_file.write_attribute_value('DATE', date, na_dict=na_dict)
                    final_file.write_attribute_value('RDATE', date, na_dict=na_dict)
                    final_file.write_attribute_value('NIV', 1, na_dict=na_dict)
                    final_file.write_attribute_value('NSCOML', len(global_attributes['SCOM']), na_dict=na_dict)
                    final_file.write_attribute_value('NNCOML', len(global_attributes['NCOM']), na_dict=na_dict)
                    final_file.write_attribute_value('SCOM', global_attributes['SCOM'], na_dict=na_dict)
                    final_file.write_attribute_value('NCOM', global_attributes['NCOM'], na_dict=na_dict)
                final_file.save_na_file(final_filename, na_dict, no_header=no_header)
                final_file.close()
                self.finished.emit()
            else:
                final_file.close()
                self.error.emit([etype.__name__, str(evalue)])

    def stop(self):
        logging.debug('gui - file_functions.py - BatchProcessingThread - stop')
        self.terminate()

    @staticmethod
    def set_filename(file_path, out_ext, filename_base, start_nbr, digit_nbr):
        if filename_base is not None:
            filename = filename_base
            if 'original_filename' in filename:
                original_filename = pathlib.Path(file_path).name
                original_filename = original_filename[: original_filename.find(pathlib.Path(file_path).suffix)]
                filename = filename.replace('original_filename', original_filename)
            if 'ndigit' in filename:
                file_nbr = str(start_nbr + i)
                file_nbr_str = '0' * (digit_nbr - len(file_nbr)) + file_nbr
                filename = filename.replace('ndigit', file_nbr_str)
        else:
            filename = pathlib.Path(file_path).name
        if not filename.endswith(out_ext):
            filename += out_ext
        return filename

    def set_filename_base(self):
        filename_base = None
        start_nbr = None
        digit_nbr = None
        if self.batch_dict['filename_options'] is not None:
            filename_base = ''
            for option in self.batch_dict['filename_options']:
                if option != '':
                    if option == 'original_filename':
                        filename_base += str('original_filename')
                    elif 'date' in option:
                        filename_base += datetime.datetime.now().strftime(option[4:])
                    elif 'ndigit' in option:
                        filename_base += 'ndigit'
                        start_nbr = int(option[6:])
                        digit_nbr = len(option[6:])
                    else:
                        filename_base += option
        return filename_base, start_nbr, digit_nbr
