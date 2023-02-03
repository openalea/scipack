# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/visualprint.ui'
#
# Created: Tue Nov 18 17:08:28 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!
"""tobe done"""

__revision__ = "$Id$"
__license__ = "Cecill-C"

from qtpy import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(288,170)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.captionText = QtWidgets.QLabel(Dialog)
        self.captionText.setObjectName("captionText")
        self.gridLayout.addWidget(self.captionText,0,0,1,1)
        self.valueDisplay = QtWidgets.QTextEdit(Dialog)
        self.valueDisplay.setReadOnly(True)
        self.valueDisplay.setTabStopWidth(20)
        self.valueDisplay.setObjectName("valueDisplay")
        self.gridLayout.addWidget(self.valueDisplay,1,0,1,2)
        spacerItem = QtWidgets.QSpacerItem(330,20,QtWidgets.QSizePolicy.Expanding,
                                                  QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem,2,0,1,1)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton,2,1,1,1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Value Display", None, QtWidgets.QApplication.UnicodeUTF8))
        self.captionText.setText(QtWidgets.QApplication.translate("Dialog", "Value is", None, QtWidgets.QApplication.UnicodeUTF8))
        self.okButton.setText(QtWidgets.QApplication.translate("Dialog", "Ok", None, QtWidgets.QApplication.UnicodeUTF8))

