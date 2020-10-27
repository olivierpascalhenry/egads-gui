import math
from PyQt5 import QtCore, QtWidgets, QtGui
from functions.utils import full_path_name_from_treewidget
from collections import OrderedDict


class MyTableWidget(QtWidgets.QTableWidget):

    def __init__(self, parent):
        QtWidgets.QTableWidget.__init__(self, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        drag_item = self.item(self.currentRow(), self.currentColumn())
        drop_item = self.item(self.rowAt(e.pos().y()), self.columnAt(e.pos().x()))
        if not drop_item.text():
            e.accept()
            drop_item.setText(drag_item.text())
        else:
            e.ignore()


class MyTreeWidget(QtWidgets.QTreeWidget):
    dropFile = QtCore.pyqtSignal(list)
    dropFileError = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        QtWidgets.QTreeWidget.__init__(self, parent)
        self.setAcceptDrops(True)
        self.setAnimated(True)
        self.setDropIndicatorShown(True)
        self.item_text = None
        self.item_tooltip = None
        self.old_path = None
        self.new_path = None
        self.hierarchy = OrderedDict()

    def startDrag(self, actions):
        if len(self.selectedItems()) == 1:
            self.old_path, _ = full_path_name_from_treewidget(self)
            self.item_text = self.selectedItems()[0].text(0)
            self.item_tooltip = self.selectedItems()[0].toolTip(0)
            return QtWidgets.QTreeWidget.startDrag(self, actions)

    def dropEvent(self, event):

        # a revoir

        # if 'group' in self.item_tooltip:
        cancel_drop = False
        item_idx = None
        drop_from_item = self.dropIndicatorPosition()
        item = self.itemAt(event.pos())
        if item is None:
            item = self.invisibleRootItem()
        if 'dataset' in item.toolTip(0) or 'dimension' in item.toolTip(0):
            parent = item.parent()
            if parent is None:
                parent = self.invisibleRootItem()
            item_idx = parent.indexOfChild(item)
            if drop_from_item == 0 or drop_from_item == 2:
                item_idx += 1
        else:
            parent = item
        self.new_path, _ = full_path_name_from_treewidget(parent=parent)
        if self.new_path == '/':
            self.new_path = self.item_text
        if self.new_path[0] == '/':
            self.new_path = self.new_path[1:] + '/' + self.item_text
        if self.old_path == '/' + self.new_path:
            cancel_drop = True
        if self.child_exist_same_name(parent):
            cancel_drop = True
        if 'dataset' in self.item_tooltip:
            tooltip_text = 'dataset: ' + self.new_path
        elif 'dimension' in self.item_tooltip:
            tooltip_text = 'dimension: ' + self.new_path
        else:
            tooltip_text = 'group: ' + self.new_path

        if not cancel_drop:
            new_item = QtWidgets.QTreeWidgetItem()
            new_item.setText(0, self.item_text)
            new_item.setToolTip(0, tooltip_text)
            if item_idx is not None:
                parent.insertChild(item_idx, new_item)
            else:
                parent.addChild(new_item)
            if 'group' in self.selectedItems()[0].toolTip(0):
                self.hierarchy = self.get_hierarchy(self.selectedItems()[0])
                if self.hierarchy:
                    self.add_hierarchy(new_item, self.hierarchy, tooltip_text)

        if not cancel_drop:
            event.accept()
            self.dropFile.emit([self.old_path, '/' + self.new_path])
        else:
            event.ignore()
        # else:
        #     event.ignore()

    def get_hierarchy(self, parent):
        ordered_dict = OrderedDict()
        for i in range(parent.childCount()):
            if 'group' in parent.child(i).toolTip(0):
                ordered_dict[parent.child(i).text(0)] = self.get_hierarchy(parent.child(i))
            else:
                ordered_dict[parent.child(i).text(0)] = None
        return ordered_dict

    def add_hierarchy(self, parent, ordered_dict, tooltip_text):
        if ':' in tooltip_text:
            idx = tooltip_text.find(':')
            tooltip_text = tooltip_text[idx + 2:]
        for key, value in ordered_dict.items():
            if value is not None:
                text = 'group: ' + tooltip_text + '/' + key
            else:
                text = 'dataset: ' + tooltip_text + '/' + key
            new_item = QtWidgets.QTreeWidgetItem()
            new_item.setText(0, key)
            new_item.setToolTip(0, text)
            parent.addChild(new_item)
            if value is not None:
                self.add_hierarchy(new_item, value, tooltip_text + '/' + key)

    def child_exist_same_name(self, parent):
        exist = False
        for i in range(parent.childCount()):
            if self.item_text == parent.child(i).text(0):
                exist = True
                break
        return exist


class DropFrame(QtWidgets.QFrame):
    leftClick = QtCore.pyqtSignal()
    dropFile = QtCore.pyqtSignal(str)
    manyFiles = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.LinkAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_events = event.mimeData().urls()
        if len(file_events) > 1:
            self.manyFiles.emit()
        else:
            self.dropFile.emit(file_events[0].toLocalFile())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.leftClick.emit()


class PushButtonRight(QtWidgets.QToolButton):
    rightClick = QtCore.pyqtSignal()

    def __init__(self, string):
        QtWidgets.QToolButton.__init__(self, string)

    def mousePressEvent(self, event):
        QtWidgets.QToolButton.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.RightButton:
            self.rightClick.emit()


class ListWidgetRight(QtWidgets.QListWidget):
    rightClick = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QListWidget.__init__(self, parent)

    def mousePressEvent(self, event):
        QtWidgets.QListWidget.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.RightButton:
            self.rightClick.emit()


class VerticalLabel(QtWidgets.QLabel):

    def __init__(self, *args):
        QtWidgets.QLabel.__init__(self, *args)

    def paintEvent(self, event):
        QtWidgets.QLabel.paintEvent(self, event)
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height()-1)
        painter.rotate(-90)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QtWidgets.QLabel.render(self, painter)
        painter.end()

    def minimumSizeHint(self):
        size = QtWidgets.QLabel.minimumSizeHint(self)
        return QtCore.QSize(size.height(), size.width())

    def sizeHint(self):
        size = QtWidgets.QLabel.sizeHint(self)
        return QtCore.QSize(size.height(), size.width())


class QtWaitingSpinner(QtWidgets.QWidget):
    """
    The MIT License (MIT)

    Copyright (c) 2012-2014 Alexander Turkin
    Copyright (c) 2014 William Hallatt
    Copyright (c) 2015 Jacob Dawid
    Copyright (c) 2016 Luca Weiss

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    def __init__(self, parent, centerOnParent=True, disableParentWhenSpinning=False, modality=QtCore.Qt.NonModal):
        super().__init__(parent)

        self._centerOnParent = centerOnParent
        self._disableParentWhenSpinning = disableParentWhenSpinning

        # WAS IN initialize()
        self._color = QtGui.QColor(QtCore.Qt.black)
        self._roundness = 100.0
        self._minimumTrailOpacity = 3.14159265358979323846
        self._trailFadePercentage = 80.0
        self._revolutionsPerSecond = 1.57079632679489661923
        self._numberOfLines = 20
        self._lineLength = 10
        self._lineWidth = 2
        self._innerRadius = 10
        self._currentCounter = 0
        self._isSpinning = False

        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.rotate)
        self.updateSize()
        self.updateTimer()
        self.hide()
        # END initialize()

        self.setWindowModality(modality)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def paintEvent(self, QPaintEvent):
        self.updatePosition()
        painter = QtGui.QPainter(self)
        painter.fillRect(self.rect(), QtCore.Qt.transparent)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        if self._currentCounter >= self._numberOfLines:
            self._currentCounter = 0

        painter.setPen(QtCore.Qt.NoPen)
        for i in range(0, self._numberOfLines):
            painter.save()
            painter.translate(self._innerRadius + self._lineLength, self._innerRadius + self._lineLength)
            rotateAngle = float(360 * i) / float(self._numberOfLines)
            painter.rotate(rotateAngle)
            painter.translate(self._innerRadius, 0)
            distance = self.lineCountDistanceFromPrimary(i, self._currentCounter, self._numberOfLines)
            color = self.currentLineColor(distance, self._numberOfLines, self._trailFadePercentage,
                                          self._minimumTrailOpacity, self._color)
            painter.setBrush(color)
            painter.drawRoundedRect(QtCore.QRect(0, -self._lineWidth / 2, self._lineLength, self._lineWidth),
                                    self._roundness,
                                    self._roundness, QtCore.Qt.RelativeSize)
            painter.restore()

    def start(self):
        self.updatePosition()
        self._isSpinning = True
        self.show()

        if self.parentWidget and self._disableParentWhenSpinning:
            self.parentWidget().setEnabled(False)

        if not self._timer.isActive():
            self._timer.start()
            self._currentCounter = 0

    def stop(self):
        self._isSpinning = False
        self.hide()

        if self.parentWidget() and self._disableParentWhenSpinning:
            self.parentWidget().setEnabled(True)

        if self._timer.isActive():
            self._timer.stop()
            self._currentCounter = 0

    def setNumberOfLines(self, lines):
        self._numberOfLines = lines
        self._currentCounter = 0
        self.updateTimer()

    def setLineLength(self, length):
        self._lineLength = length
        self.updateSize()

    def setLineWidth(self, width):
        self._lineWidth = width
        self.updateSize()

    def setInnerRadius(self, radius):
        self._innerRadius = radius
        self.updateSize()

    def color(self):
        return self._color

    def roundness(self):
        return self._roundness

    def minimumTrailOpacity(self):
        return self._minimumTrailOpacity

    def trailFadePercentage(self):
        return self._trailFadePercentage

    def revolutionsPersSecond(self):
        return self._revolutionsPerSecond

    def numberOfLines(self):
        return self._numberOfLines

    def lineLength(self):
        return self._lineLength

    def lineWidth(self):
        return self._lineWidth

    def innerRadius(self):
        return self._innerRadius

    def isSpinning(self):
        return self._isSpinning

    def setRoundness(self, roundness):
        self._roundness = max(0.0, min(100.0, roundness))

    def setColor(self, color=QtCore.Qt.black):
        self._color = QtGui.QColor(color)

    def setRevolutionsPerSecond(self, revolutionsPerSecond):
        self._revolutionsPerSecond = revolutionsPerSecond
        self.updateTimer()

    def setTrailFadePercentage(self, trail):
        self._trailFadePercentage = trail

    def setMinimumTrailOpacity(self, minimumTrailOpacity):
        self._minimumTrailOpacity = minimumTrailOpacity

    def rotate(self):
        self._currentCounter += 1
        if self._currentCounter >= self._numberOfLines:
            self._currentCounter = 0
        self.update()

    def updateSize(self):
        size = (self._innerRadius + self._lineLength) * 2
        self.setFixedSize(size, size)

    def updateTimer(self):
        self._timer.setInterval(1000 / (self._numberOfLines * self._revolutionsPerSecond))

    def updatePosition(self):
        if self.parentWidget() and self._centerOnParent:
            self.move(self.parentWidget().width() / 2 - self.width() / 2,
                      self.parentWidget().height() / 2 - self.height() / 2)

    def lineCountDistanceFromPrimary(self, current, primary, totalNrOfLines):
        distance = primary - current
        if distance < 0:
            distance += totalNrOfLines
        return distance

    def currentLineColor(self, countDistance, totalNrOfLines, trailFadePerc, minOpacity, colorinput):
        color = QtGui.QColor(colorinput)
        if countDistance == 0:
            return color
        minAlphaF = minOpacity / 100.0
        distanceThreshold = int(math.ceil((totalNrOfLines - 1) * trailFadePerc / 100.0))
        if countDistance > distanceThreshold:
            color.setAlphaF(minAlphaF)
        else:
            alphaDiff = color.alphaF() - minAlphaF
            gradient = alphaDiff / float(distanceThreshold + 1)
            resultAlpha = color.alphaF() - gradient * countDistance
            # If alpha is out of bounds, clip it.
            resultAlpha = min(1.0, max(0.0, resultAlpha))
            color.setAlphaF(resultAlpha)
        return color