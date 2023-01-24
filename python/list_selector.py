# -*- python -*-
#
#       OpenAlea.StdLib
#
#       Copyright 2006-2023 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.rtfd.io
#
################################################################################
# Widgets

from openalea.vpltk.qt import QtGui, QtCore, QtWidgets

from openalea.core.observer import lock_notify
from openalea.visualea.node_widget import NodeWidget

class ListSelectorWidget(QtWidgets.QListWidget, NodeWidget):
    """ This Widget allows to select an element in a list
    or in a dictionnary """

    def __init__(self, node, parent):
        """
        @param node
        @param parent
        """

        QtWidgets.QListWidget.__init__(self, parent)
        NodeWidget.__init__(self, node)
        # self.connect(self, QtCore.pyqtSignal("currentRowChanged(int)"), self.changed)
        self.currentRowChanged.connect(self.changed)

        self.mode = None
        self.notify(node, ("input_modified", 0))
        self.notify(node, ("input_modified", 1))

    def notify(self, sender, event):
        """ Notification sent by node """

        if(event[0] != "input_modified"):
            return

        # Read Inputs
        seq = self.node.get_input(0)

        index = self.node.get_input(1)

        if(event[1] == 0): # index of modified input

            # Define the mode depending of the type of input
            if(isinstance(seq, dict)):
                self.mode = "DICT"
            else:
                self.mode = None

            self.update_list(seq)

        elif(event[1] == 1): # index == 1

            if(self.mode == "DICT"):
                try:
                    i = list(seq.keys()).index(index)
                    self.setCurrentRow(i)
                except:
                    pass
            else:
                try:
                    self.setCurrentRow(index)
                except:
                    pass

    def update_list(self, seq):
        """ Rebuild the list """

        self.clear()
        if(not seq):
            return

        if(self.mode == "DICT"):
            seq = list(seq.keys())

        for elt in seq:

            item = QtWidgets.QListWidgetItem(str(elt))
            item.setFlags(QtCore.Qt.ItemIsEnabled |
                          QtCore.Qt.ItemIsSelectable)
            self.addItem(item)

    @lock_notify
    def changed(self, p):
        """ Update the index"""

        row = self.currentRow()
        item = self.currentItem()

        key = None
        if (item and self.mode == "DICT"):
            key = str(item.text())
        elif row >= 0:
            key = row

        if key is not None:
            self.node.set_input(1, key)
