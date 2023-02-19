# -*- python -*-
#
#       image: image manipulation GUI
#
#       Copyright 2006-2023 INRIA - CIRAD - INRA
#
#       File author(s): Jerome Chopard <jerome.chopard@sophia.inria.fr>
#                       Eric Moscardi <eric.moscardi@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
################################################################################
"""
This module defines a widget to animate a sequence of images
"""

__license__= "Cecill-C"
__revision__ = " $Id: __wralea__.py 2245 2010-02-08 17:11:34Z cokelaer $ "

from qtpy import QtCore, QtGui, QtWidgets

from . import icons_rc

def clone_action (ref_action, clone) :
	clone.setText(ref_action.text() )
	clone.setIcon(ref_action.icon() )
	clone.setToolTip(ref_action.toolTip() )
	clone.setShortcuts(ref_action.shortcuts() )

class FrameAnimator (QtWidgets.QMainWindow) :
	"""Animate a list of frames
	"""
	def __init__ (self, parent = None) :
		QtWidgets.QMainWindow.__init__(self,parent)

		self._pix_no_frames = QtGui.QPixmap(":/image/forbidden.png")

		self._frames = [] #list of frame
		self._current_frame = None #currently displayed frame

		self._timer = QtCore.QTimer() #used to animate the display
		self._timer.setInterval(40)
		#QObject.connect(self._timer,SIGNAL("timeout()"),self.step)
		self._timer.timeout.connect(self.step)

		self._view = QtWidgets.QLabel() #widget used to display the current frame
		self.setCentralWidget(self._view)

		#UI
		self._menu = self.menuBar().addMenu("anim")
		self._action_bar = self.addToolBar("movie")
		self._slider_bar = QtWidgets.QToolBar("slider")
		self.addToolBar(QtCore.Qt.BottomToolBarArea,self._slider_bar)

		#close
		self._action_close = QtWidgets.QAction("close",self)
		self._action_close.setShortcut("Escape")
		self._menu.addAction(self._action_close)
		self._action_close.triggered.connect(self.close_window)

		self._menu.addSeparator()

		#clear frames
		self._action_clear = QtWidgets.QAction("clear frames",self)
		self._menu.addAction(self._action_clear)
		self._action_clear.triggered.connect(self.clear_frames)

		self._menu.addSeparator()

		#stop play/pause step
		self._action_stop =self._action_bar.addAction("stop")
		self._action_stop.setIcon(QtGui.QIcon(":image/stop.png") )
		self._action_stop.triggered.connect(self.stop)
		self._menu.addAction(self._action_stop)

		self._action_play = QtWidgets.QAction("play",self)
		self._action_play.setIcon(QtGui.QIcon(":image/play.png") )
		self._action_play.setShortcut("Space")

		self._action_pause = QtWidgets.QAction("pause",self)
		self._action_pause.setIcon(QtGui.QIcon(":image/pause.png") )
		self._action_pause.setShortcut("Space")

		self._toggle_running = self._action_bar.addAction("toggle")
		
		self._toggle_running.triggered.connect(self.toggle_running)
		self._menu.addAction(self._toggle_running)

		self._action_step = QtWidgets.QAction("step",self)
		self._action_step.setIcon(QtGui.QIcon(":image/step.png") )
		self._action_step.setShortcut("Ctrl+Space")
		self._action_step.triggered.connect(self.step)
		self._action_bar.addAction(self._action_step)
		self._menu.addAction(self._action_step)

		self._action_bar.addSeparator()
		self._menu.addSeparator()

		#loop
		self._action_loop = self._action_bar.addAction("loop")
		self._action_loop.setCheckable(True)
		self._action_loop.setChecked(True)
		self._action_loop.setIcon(QtGui.QIcon(":image/loop.png") )
		self._menu.addAction(self._action_loop)

		self._action_loop.triggered.connect(self._loop_changed)

		#fps
		self._fps_edit = QtWidgets.QSpinBox()
		self._fps_edit.setRange(1,99)
		self._fps_edit.setSuffix(" fps")
		self._fps_edit.setValue(25)
		self._action_bar.addWidget(self._fps_edit)

		self._fps_edit.valueChanged.connect(self._fps_changed)

		#slider
		self._frame_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self._slider_bar.addWidget(self._frame_slider)
		self._frame_slider.valueChanged.connect(self._current_frame_changed)

		#init GUI
		self.pause()
		self.set_frames([])

	def close_window (self) :
		self.pause()
		self.window().close()

	############################################
	#
	#	frame management
	#
	############################################
	def clear_frames (self) :
		"""Clear the list of frames
		"""
		self.stop()
		self.set_frames([])

	def set_current_frame (self, ind) :
		"""Set the index of the frame to be displayed

		:Parameters:
		 - `ind` (int) - index of the frame to display
		"""
		self._frame_slider.setValue(ind)

	def _current_frame_changed (self, ind) :
		self._current_frame = ind
		self.update_pix()

	def set_frames (self, frames) :
		"""Set frame names

		:Parameters:
		 - `frames` (list of str or QPixmap) - list of pixmap or frame path
		"""
		self.stop()
		self._frames = [QtGui.QPixmap(fr) for fr in frames]
		self.nb_frame_changed()

	def append_frame (self, frame) :
		"""Append a new frame at the end of current list

		:Parameters:
		 - `frame` (str or QPixmap) - filename or pixmap
		"""
		self._pix.append(QtGui.QPixmap(frame) )
		self.nb_frame_changed()

	def update_pix (self) :
		"""Change currently displayed frame
		"""
		if self._current_frame is None :
			self._view.setPixmap(self._pix_no_frames)
		else :
			self._view.setPixmap(self._frames[self._current_frame])

	def nb_frame_changed (self) :
		"""Function to call when the number of frame has changed
		"""
		if len(self._frames) == 0 :
			self._current_frame = None
			for ob in (self._frame_slider,self._action_bar,
			           self._action_stop,self._action_step,
			           self._toggle_running,self._fps_edit,
			           self._action_loop) :
				ob.setEnabled(False)
			#self._menu.setEnabled(False)

		else :
			self._frame_slider.setRange(0,len(self._frames) - 1)
			for ob in (self._frame_slider,self._action_bar,
			           self._action_stop,self._action_step,
			           self._toggle_running,self._fps_edit,
			           self._action_loop) :
				ob.setEnabled(True)
			#self._menu.setEnabled(True)

			if self._current_frame is None :
				self._current_frame = 0
			else :
				self._current_frame = min(self._current_frame,len(self._frames) )

		self.update_pix()

	############################################
	#
	#	accessors
	#
	############################################
	def set_loop (self, loop) :
		"""Set animation to loop

		:Parameters:
		 - `loop` (bool) - if True animation will restart from start each time
		                   the end is reached
		"""
		self._action_loop.setChecked(loop)

	def _loop_changed (self, loop) :
		pass

	def set_fps (self, fps) :
		"""Set number of frame per second

		:Parameters:
		 - `fps` (int)
		"""
		self._fps_edit.setValue(fps)

	def _fps_changed (self, fps) :
		self._timer.setInterval(int(1000. / fps) )

	############################################
	#
	#	animate
	#
	############################################
	def stop (self) :
		self.pause()
		self.set_current_frame(0)
		self.update_pix()

	def step (self) :
		next_frame = self._current_frame + 1
		if next_frame == len(self._frames) :
			if self._action_loop.isChecked() :
				self.set_current_frame(0)
				self.update_pix()
			else :
				self.pause()
		else :
			self.set_current_frame(next_frame)
			self.update_pix()

	def toggle_running (self) :
		if self._timer.isActive() :
			self.pause()
		else :
			self.play()

	def play (self) :
		self._action_step.setEnabled(False)
		self._fps_edit.setEnabled(False)
		clone_action(self._action_pause,self._toggle_running)
		self._timer.start()

	def pause (self) :
		self._timer.stop()
		self._action_step.setEnabled(True)
		self._fps_edit.setEnabled(True)
		clone_action(self._action_play,self._toggle_running)







