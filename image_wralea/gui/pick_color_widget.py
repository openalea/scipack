# -*- python -*-
#
#       OpenAlea.StdLib
#
#       Copyright 2006 - 2023 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : https://openalea.rtfd.io
#
################################################################################
"""
Expose the animator as a visualea node
"""

__revision__ = " $$ "

from qtpy import QtGui, QtCore, QtWidgets

from openalea.core import Node
from openalea.visualea.node_widget import NodeWidget

from openalea.image.gui.all import to_pix,ScalableLabel
from openalea.image.gui import icons_rc

def pick_color (img, col) :
	return img,col

class InteractiveScalableLabel(ScalableLabel) :
	"""Add mouse interaction to a scalable label
	"""
	def __init__ (self, parent = None) :
		ScalableLabel.__init__(self,parent)
		self.setMouseTracking(True)

		self._last_mouse_pos = None

	def mouseDoubleClickEvent (self, event) :
		self._last_mouse_pos = None
		self.emit(QtCore.Signal("mouse_double_click"),event)

	def mousePressEvent (self, event) :
		self._last_mouse_pos = event.pos()

	def mouseReleaseEvent (self, event) :
		if self._last_mouse_pos is not None :
			if self._last_mouse_pos == event.pos() :
				self.emit(QtCore.Signal("mouse_click"),event)

			self._last_mouse_pos = None

	def mouseMoveEvent (self, event) :
		if self._last_mouse_pos is None :
			self.emit(QtCore.Signal("mouse_move"),event)


class PickColorWidget(NodeWidget, QtWidgets.QWidget) :
	"""
	Node widget to pick a color in an image
	"""

	def __init__(self, node, parent) :
		"""
		"""
		QtWidgets.QWidget.__init__(self, parent)
		NodeWidget.__init__(self, node)

		self._img_lab = InteractiveScalableLabel()
		self._img_lab.setCursor(QtGui.QCursor(QtGui.QPixmap(":cursor/pick.png"),9,10) )

		self._col_picked_lab = QtWidgets.QLabel("col")
		self._col_picked_lab.setPixmap(QtGui.QPixmap(32,32) )
		self._col_picked_lab.pixmap().fill(QtGui.QColor(0,0,0) )

		self._col_current_lab = QtWidgets.QLabel("col")
		self._col_current_lab.setPixmap(QtGui.QPixmap(32,32) )
		self._col_current_lab.pixmap().fill(QtGui.QColor(0,0,0) )

		self._h_layout = QtWidgets.QHBoxLayout()
		self._v_layout = QtWidgets.QVBoxLayout()

		self._v_layout.addWidget(self._col_picked_lab)
		self._v_layout.addWidget(self._col_current_lab)
		self._v_layout.addStretch(5)

		self._h_layout.addLayout(self._v_layout)
		self._h_layout.addWidget(self._img_lab,5)

		self.setLayout(self._h_layout)

		self.notify(node,("caption_modified",node.get_caption() ) )
		self.notify(node,("input_modified",0) )
		self.notify(node,("input_modified",1) )

		self._img_lab.mouse_click.connect(self.mouse_click)
		self._img_lab.mouse_move.connect(self.mouse_move)

	def notify(self, sender, event):
		"""Notification sent by node
		"""
		if event[0] == 'caption_modified' :
			self.window().setWindowTitle(event[1])

		elif event[0] == 'input_modified' :
			if event[1] == 0 :
				img = self.node.get_input(0)
				if img is None :
					self._img_lab.setText("no pix")
				else :
					self._img_lab.setPixmap(to_pix(img) )
			if event[1] == 1 :
				col = self.node.get_input(1)
				self._col_picked_lab.pixmap().fill(QtGui.QColor(*col[:3]) )

		self.update()

	def mouse_click (self, event) :
		img = self.node.get_input(0)
		if img is not None :
			j,i = self._img_lab.pixmap_coordinates(event.x(),event.y() )
			col = tuple(img[i,j])
			self.node.set_input(1,col)
			self._col_picked_lab.pixmap().fill(QtGui.QColor(*col[:3]) )
			self._col_picked_lab.update()

	def mouse_move (self, event) :
		img = self.node.get_input(0)
		if img is not None :
			j,i = self._img_lab.pixmap_coordinates(event.x(),event.y() )
			col = img[i,j]
			self._col_current_lab.pixmap().fill(QtGui.QColor(*col[:3]) )
			self._col_current_lab.update()



