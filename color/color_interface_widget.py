# -*- python -*-
#
#
#       Copyright 2006-2023 INRIA - CIRAD - INRA
#
#       File author(s): Chopard
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
"""Declaration of IColor interface widget
"""

__license__ = "Cecill-C"
__revision__ = " $Id: interface.py 2245 2010-02-08 17:11:34Z cokelaer $"

from openalea.vpltk.qt import QtCore, QtGui, QtWidgets
from openalea.core.observer import lock_notify
from openalea.core.interface import IInterfaceWidget, make_metaclass
from .color_interface import IColor


class IColorWidget (IInterfaceWidget, QtWidgets.QPushButton,metaclass=make_metaclass()):

    """Interface for colors expressed as triplet of values
    """
    __interface__ = IColor

    def __init__(self, node, parent, parameter_str, interface):
        """Constructor

        :Parameters:
         - `node` (Node) - node that own the widget
         - `parent` (QWidget) - parent widget
         - `parameter_str` (str) - the parameter key the widget is associated to
         - `interface` (Ismth) - instance of interface object
        """
        QtWidgets.QPushButton.__init__(self, parent)
        IInterfaceWidget.__init__(self, node, parent, parameter_str, interface)
        self.setMinimumSize(64, 64)

        self._color = (0, 0, 0)
        self._brush = QtWidgets.QBrush(QtGui.QColor(*self._color[:3]))

        #QtCore.QObject.connect(self, QtCore.pyqtSignal("clicked(bool)"), self.open_color_dialog)
        self.clicked.connect(self.open_color_dialog)
        self.notify(node, ("input_modified", self.param_str))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(event.rect(), self._brush)
        painter.end()

    def color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        self._brush = QtGui.QBrush(QtGui.QColor(*self._color[:3]))

    def open_color_dialog(self):
        old_color = self.color()

        color = None
        if len(old_color) == 3:
            col = QtWidgets.QColorDialog.getColor(QtGui.QColor(*old_color), self)
            if col.isValid():
                color = (col.red(), col.green(), col.blue())
        elif len(old_color) == 4:
            col, ok = QtWidgets.QColorDialog.getRgba(QtGui.qRgba(*old_color), self)
            if ok:
                col = QtGui.QColor.fromRgba(col)
                color = (col.red(), col.green(), col.blue(), col.alpha())
        else:
            msg = "unable to display this color: %s" % str(self._color)
            raise ValueError(msg)

        if color is not None:
            self.set_value(color)

    @lock_notify
    def notify(self, sender, event):
        """Notification sent by node
        """
        if event[0] == "input_modified":
            col = self.node.get_input(self.param_str)
            self.set_widget_value(col)

    @lock_notify
    def valueChanged(self, newval):
        """ todo """
        self.set_value(newval)

    def set_interface(self, interface):
        pass

    def set_widget_value(self, newval):
        self.set_color(newval)

    def get_widget_value(self):
        return self.color()
