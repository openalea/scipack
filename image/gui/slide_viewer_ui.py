# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/vmanalysis/visu/slide_viewer.ui'
#
# Created: Tue Jun  8 10:15:01 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from openalea.vpltk.qt import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(100, 150))
        self.im_view = QtWidgets.QWidget(MainWindow)
        self.im_view.setMinimumSize(QtCore.QSize(50, 50))
        self.im_view.setObjectName("im_view")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.im_view)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.im_view)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QtWidgets.QToolBar(MainWindow)
        self.toolbar.setObjectName("toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.action_close = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon)
        self.action_close.setObjectName("action_close")
        self.action_snapshot = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/snapshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_snapshot.setIcon(icon1)
        self.action_snapshot.setObjectName("action_snapshot")
        self.action_rotate_left = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/rotate_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_left.setIcon(icon2)
        self.action_rotate_left.setObjectName("action_rotate_left")
        self.action_rotate_right = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/rotate_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_right.setIcon(icon3)
        self.action_rotate_right.setObjectName("action_rotate_right")
        self.toolbar.addAction(self.action_close)
        self.toolbar.addAction(self.action_snapshot)
        self.toolbar.addAction(self.action_rotate_left)
        self.toolbar.addAction(self.action_rotate_right)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None))
        self.toolbar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None))
        self.action_close.setText(QtWidgets.QApplication.translate("MainWindow", "close", None))
        self.action_close.setToolTip(QtWidgets.QApplication.translate("MainWindow", "close window", None))
        self.action_close.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Esc", None))
        self.action_snapshot.setText(QtWidgets.QApplication.translate("MainWindow", "snapshot", None))
        self.action_snapshot.setToolTip(QtWidgets.QApplication.translate("MainWindow", "take snapshot", None))
        self.action_rotate_left.setText(QtWidgets.QApplication.translate("MainWindow", "rotate left", None))
        self.action_rotate_left.setToolTip(QtWidgets.QApplication.translate("MainWindow", "rotate left", None))
        self.action_rotate_right.setText(QtWidgets.QApplication.translate("MainWindow", "rotate right", None))
        self.action_rotate_right.setToolTip(QtWidgets.QApplication.translate("MainWindow", "rotate right", None))

from . import icons_rc
