# -*- coding: utf-8 -*-
# -*- python -*-
#
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       File author(s): Guillaume Baty <guillaume.baty@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

from qtpy import QtGui, QtCore, QtWidgets
from openalea.image.gui.slide_viewer_widget import ImageStackViewerWidget, to_image
from openalea.oalab.control.widget import AbstractQtControlWidget
from openalea.oalab.painter import AbstractPainter


class IImageViewer(AbstractQtControlWidget, ImageStackViewerWidget):

    def __init__(self):
        AbstractQtControlWidget.__init__(self)
        ImageStackViewerWidget.__init__(self)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAutoFillBackground(True)
        self.value_changed_signal = self.valueChanged

    def reset(self, value=None, *kargs):
        self.setValue(value)

    def setValue(self, value):
        ImageStackViewerWidget.setValue(self, value)

    def value(self):
        ImageStackViewerWidget.value(self)


class IImagePainter(AbstractPainter):

    def paint_data(self, data, painter, rectangle, option=None, **kwargs):
        if data is None:
            return
        painter.save()
        if option:
            rectangle = option.rect
            pen = QtGui.QPen()
            if option.state & QtWidgets.QStyle.State_Selected:
                pen.setColor(option.palette.highlightedText().color())
                painter.setPen(pen)
                painter.setRenderHint(painter.Antialiasing, True)
                painter.fillRect(rectangle, option.palette.highlight())

        x = rectangle.x()
        y = rectangle.y()
        size = min(rectangle.width(), rectangle.height())
        frame = QtCore.QRectF(x, y, size, size)
        painter.drawImage(frame, to_image(data))
        painter.restore()


class IImageSelector(object):

    @classmethod
    def edit(cls, control, shape=None):
        return IImageViewer()

    @classmethod
    def paint(self, control, shape=None):
        if shape == 'hline':
            return IImagePainter()
