import logging
from PyQt5 import QtWidgets
from functions.window_functions.other_windows_functions import MyInfo


def too_many_files(self):
    logging.debug('gui - gui_support_functions.py - too_many_files')
    info_text = 'It is nos possible to open more than one file with the GUI at this time. If multiple files have to ' \
                'be processed, please use the Batch processing function in the File menu.'
    self.infoWindow = MyInfo(info_text)
    self.infoWindow.exec_()


def move_object_in_variable_dict(self, path_object):
    logging.debug('gui - gui_support_functions.py - move_object_in_variable_dict - path_object: ' + str(path_object))
    var_list = None
    if self.tab_view.currentIndex() == 1:
        var_list = self.list_of_variables_and_attributes
    elif self.tab_view.currentIndex() == 2:
        var_list = self.list_of_new_variables_and_attributes
    for key in list(var_list.keys()):
        if key.find(path_object[0]) == 0:
            new_key = path_object[1] + key[len(path_object[0]):]
            var_list[new_key] = var_list.pop(key)


def add_variable_to_widget_tree(treewidget, path, group=False, dim=False):
    if path[0] == '/':
        path = path[1:]
    path_elem = path.split('/')
    new_item = QtWidgets.QTreeWidgetItem()
    new_item.setText(0, path_elem[-1])
    if group:
        new_item.setToolTip(0, 'group: ' + path)
    else:
        if dim:
            new_item.setToolTip(0, 'dimension: ' + path)
        else:
            new_item.setToolTip(0, 'dataset: ' + path)
    item = treewidget.invisibleRootItem()
    if path:
        for elem in path_elem:
            for j in range(item.childCount()):
                if item.child(j).text(0) == elem:
                    item = item.child(j)
                    break
    item.addChild(new_item)
