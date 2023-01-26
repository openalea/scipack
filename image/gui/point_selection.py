# -*- python -*-
#
#       image
#
#       Copyright 2006 - 2011 INRIA - CIRAD - INRA
#
#       File author(s): Eric Moscardi <eric.moscardi@gmail.com>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#       http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
################################################################################
"""
This module provide a Control Point Selection Tool
"""

__license__= "Cecill-C"
__revision__=" $Id$ "

__all__ = ["PointSelection","point_selection"]


from openalea.vpltk.qt import QtGui, QtCore, QtWidgets

import numpy as np
from . import icons_rc

from .pixmap_view import PixmapStackView, ScalableGraphicsView
from .palette import palette_names, palette_factory

from openalea.image.serial.basics import load
from openalea.image.spatial_image import SpatialImage
try:
    from openalea.container.utils import IdSetGenerator
except ImportError:
    from .id_generator import IdSetGenerator


class PointSelection (QtWidgets.QMainWindow) :
    points_changed = QtCore.pyqtSignal()
    def __init__ (self) :
        QtWidgets.QMainWindow.__init__(self)

        # points
        self._points = []
        self._id_gen = IdSetGenerator()
#X         self.version = 2

        self._view = PixmapStackView()

        #QGraphicsScene
        self._scene = QtWidgets.QGraphicsScene()

        #QGraphicsPixmapItem
        self._item = QtWidgets.QGraphicsPixmapItem()
        self._item.setTransformationMode(QtCore.Qt.SmoothTransformation)
        self._item.setFlag(self._item.ItemIsSelectable,False)
        self._scene.addItem(self._item)

        #QGraphicsView
        self._widget = ScalableGraphicsView(self._scene)
        self.setCentralWidget(self._widget)

        ################### mouse handling ###################
        self._widget.setMouseTracking(True)
        self._last_mouse_x = 0
        self._last_mouse_y = 0
        self._last_slice = 0

        # self._widget.mouse_press.connect(self.mouse_pressed)
        self._widget.mouse_press.connect(self.on_mouse_pressed)

        # self._widget.mouse_move.connect(self.mouse_moved)
        self._widget.mouse_move.connect(self.on_mouse_moved)

        # self.mouse_moved.connect(self.coordinates) # don't understand mouse_moved have never been a signal?

        ################### menubar ###################
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu('File')

        # Import Points
        self._load_points = self.menu_file.addAction('Import Points')
        self._load_points.triggered.connect(self.load_points)

        # Save points
        self._save_points = self.menu_file.addAction('Save Points')
        self._save_points.triggered.connect(self.save_points)

        ################### toolbar ###################
        self._toolbar = self.addToolBar("tools")
        self._toolgroup = QtWidgets.QActionGroup(self)

        # QWidgetAction : "Rotation Left"
        self._action_left = self._toolbar.addAction("left rotation")
        self._action_left.setIcon(QtGui.QIcon(":/image/rotate_left.png") )
        self._action_left.triggered.connect(self.rotate_left)

        # QWidgetAction : "Rotation Right"
        self._action_right = self._toolbar.addAction("right rotation")
        self._action_right.setIcon(QtGui.QIcon(":/image/rotate_right.png") )
        self._action_right.triggered.connect(self.rotate_right)

        # QWidgetAction : "Add point"
        self._action_add = self._toolbar.addAction("Add point")
        self._action_add.setCheckable(True)
        self._toolgroup.addAction(self._action_add)
        self._action_add.setIcon(QtGui.QIcon(":/image/add.png") )

        # QWidgetAction : "Delete point"
        self._action_delete = self._toolbar.addAction("Delete point")
        self._action_delete.setCheckable(True)
        self._toolgroup.addAction(self._action_delete)
        self._action_delete.setIcon(QtGui.QIcon(":/image/delete.png") )

        ################### palette ###################
        self._palette_select = QtWidgets.QComboBox()
        self._toolbar.addWidget(self._palette_select)
        for palname in palette_names :
            self._palette_select.addItem(palname)

        self._palette_select.currentIndexChanged.connect(
            self.palette_name_changed
        )

        ################### slider ###################
        self._bot_toolbar = QtWidgets.QToolBar("slider")
        self._img_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self._img_slider.setRange(0,self._view.nb_slices() - 1)

        self._img_slider.valueChanged.connect(self.slice_changed)

        self._bot_toolbar.addWidget(self._img_slider)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,self._bot_toolbar)

        ################### statusbar ###################
        self._lab_coord = QtWidgets.QLabel("coords:")
        self._lab_xcoord = QtWidgets.QLabel("% 4d" % 0)
        self._lab_ycoord = QtWidgets.QLabel("% 4d" % 0)
        self._lab_zcoord = QtWidgets.QLabel("% 4d" % 0)
        self._lab_intens = QtWidgets.QLabel("intens: None")

        self.statusbar = self.statusBar()
        self.statusbar.addPermanentWidget(self._lab_coord)
        self.statusbar.addPermanentWidget(self._lab_xcoord)
        self.statusbar.addPermanentWidget(self._lab_ycoord)
        self.statusbar.addPermanentWidget(self._lab_zcoord)
        self.statusbar.addPermanentWidget(self._lab_intens)

    ##############################################
    #
    #               update GUI
    #
    ##############################################
    def update_pix (self) :
        """
        """
        pix = self._view.pixmap()

        if pix is not None :
            self._item.setPixmap(pix)
        else:
            print('None pixmap')
        #update points
        ind = self._view.current_slice()
        for point in self._points :
            if point is not None:
                pid,item, x,y,z,textid = point
                visible = abs(z - ind) < 5
                item.setVisible(visible)
                col = QtGui.QColor.fromHsv( (pid * 10) % 360,255,255)
                if visible :
                    sca = max(0.,(5 - abs(z - ind) ) / 5.)
                    if z == ind :
                        pen = QtGui.QPen(QtGui.QColor(255,255,255) )
                        pen.setWidthF(2.)
                        item.setPen(pen)
                        textid.setVisible(True)
                    else :
                        pen = QtGui.QPen(QtGui.QColor(0,0,0) )
                        pen.setWidthF(2.)
                        item.setPen(pen)
                        textid.setVisible(False)
                else :
                    sca = 1.
                tr = QtGui.QTransform()
                tr.scale(sca,sca)
                item.setTransform(tr)
                item.update()

    def coordinates (self, xxx_todo_changeme) :
        (i,j,k) = xxx_todo_changeme
        self._last_mouse_x,self._last_mouse_y, self._last_slice = i,j,k
        self.fill_infos()

    def get_pixel_value_str(self, img, x, y, z):
        px = img[x,y,z]
        if isinstance(px, np.ndarray):
            return str(px)
        else:
            return "%3d"%px

    def fill_infos (self) :
        x,y,z = self._last_mouse_x, self._last_mouse_y, self._last_slice
        img = self._view.image()
        if img is not None :
            vx,vy,vz = img.resolution
            self._lab_xcoord.setText("% 4d" % x)
            self._lab_ycoord.setText("% 4d" % y)
            self._lab_zcoord.setText("% 4d" % z)
        xmax,ymax,zmax = img.shape[:3]
        if 0 <= x < xmax and 0 <= y < ymax and 0 <= z < zmax :
            px_str = self.get_pixel_value_str(img, x,y,z)
            self._lab_intens.setText("intens: %s" % px_str)
        else :
            self._lab_intens.setText("intens: None")

    def rotate_left (self) :
        self._view.rotate(-1)
        self.update_points()
        self.update_pix()

    def rotate_right (self) :
        self._view.rotate(1)
        self.update_points()
        self.update_pix()

    def update_points(self):
        for pt in self._points:
            if pt is not None:
                pid,item, x,y,z,textid = pt
                i,j = self._view.pixmap_coordinates(x,y)
                item.setPos(i,j)

    ##############################################
    #
    #               accessors
    #
    #############################################
    def set_palette (self, palette, palette_name = None) :
        if palette_name is not None :
            ind = self._palette_select.findText(palette_name)
            self._palette_select.setCurrentIndex(ind)
        self._view.set_palette(palette)
        self.update_pix()

    def set_image (self, img) :
        self._view.set_image(img)
        x,y,z = img.shape[:3]
        self._img_slider.setRange(0, z-1)
        self._img_slider.setEnabled(True)
        self.slice_changed(self._img_slider.value() )

    def load_points (self) :
        # load file
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',
                    '/home')
        if filename :
            loading = True
            pts = self.get_points()
            if pts:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("You are about to load a new file.")
                msgBox.setInformativeText("Do you want to load the file : %s ?" %filename)
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                msgBox.setDefaultButton(QtWidgets.QMessageBox.Yes)
                ret = msgBox.exec_()
                if ret == QtWidgets.QMessageBox.No:
                    loading = False
            if loading == True:
#X                 f = open(str(filename))
#X                 l = f.readline()
#X                 f.close()
#X                 if 'version' not in l:
#X                     self.version= 1
#X                 else: 
#X                     self.version = int(l.split('=')[1].strip())
                new_pts = np.loadtxt(str(filename))
                self.set_points(new_pts)

    def save_points(self):
        pts = self.get_points()
        # load file
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',
                            '/home');
#X         fname = str(filename)
#X         f = open(fname,'w')
#X         f.write('# version = 2\n')
        np.savetxt(filename,np.array(pts),fmt='%d')
#X         f.close()

    def get_points(self):
        """
        Return the list of points in voxels
        """
        _pts = {}
        for pt in self._points :
            if pt is not None:
                pid,item,i,j,k,textid = pt
                _pts [pid] = i,j,k
        points = list(_pts.values())
        return points

    ##############################################
    #
    #               slots
    #
    ##############################################

    def on_mouse_pressed (self):
        pos = self._widget.to_inheritance_event.pos
        if pos is not None :
            sc_coords = self._widget.mapToScene(pos)
            if self._action_add.isChecked() :
                self.add_point(sc_coords)
            elif self._action_delete.isChecked() :
                self.del_point(sc_coords)

    def on_mouse_moved (self):
        event = self._widget.to_inheritance_event
        sc_coords = self._widget.mapToScene(event.pos() )
        item_coords = self._item.mapFromScene(sc_coords)
        img = self._view.image()
        if img is not None :
            i,j,k = self._view.data_coordinates(item_coords.x(),item_coords.y())
            self.emit(QtCore.pyqtSignal("mouse_moved"), (i,j,k))

    def slice_changed (self, ind) :
        self._last_slice = ind
        self._view.set_current_slice(ind)
        self.update_pix()
        self.fill_infos()

    def palette_name_changed (self, palette_index) :
        palname = str(self._palette_select.currentText() )
        img = self._view.image()
        if img is not None :
            self.set_palette(palette_factory(str(palname),img.max() ) )

    def add_point (self, pos, my_pid = None) :
        """Add a new point

        :Parameters:
         - `pos` (QPointF) - position of the point on the screen
        """
        item_coords = self._item.mapFromScene(pos)
        img = self._view.image()
        if img is not None :
            i,j,k = self._view.data_coordinates(pos.x(),pos.y() )
            found_item = False
            if my_pid is None:
                if self._points is not None:
                    pid = len(self._points)
                for pt in range(len(self._points)):
                    if self._points[pt] is None :
                        pid = pt
                        found_item = True
                        break
                if not found_item :
                    pid = self._id_gen.get_id(pid)
            else :
                pid = my_pid
            col = QtGui.QColor.fromHsv( (pid * 10) % 360,255,255)
            item = self._scene.addEllipse(QtCore.QRectF(-2.5,-2.5,5,5),QtGui.QPen(col),QtGui.QBrush(col)  )
            item.setZValue(10)
            item.setPos(pos.x(),pos.y())

            textid = QtWidgets.QGraphicsSimpleTextItem('%s' % pid, item)
            textid.setPos(8,8)
            textid.setPen(QtGui.QPen(col))
            if found_item:
                self._points[pid] = (pid,item, i,j,k,textid)
            else :
                self._points.append( (pid,item,i,j,k,textid) )
            self.update_pix()
            # self.emit(QtCore.pyqtSignal("points_changed"),self)
            self.points_changed.emit()
            return pid,(i,j,k)

    def del_point (self, pos, my_pid = None) :
        """Delete a new point

        :Parameters:
         - `pos` (QPointF) - position of the point on the screen
        """
        ind = None
        point = self._scene.itemAt(pos)
        if my_pid is None :
            for pt in self._points:
                if pt is not None:
                    pid,item, x,y,z,textid = pt
                    if point == item :
                        self._scene.removeItem(point)
                        ind = self._points.index(pt)
                        self._points[ind] = None
        else :
            for pt in self._points:
                if pt is not None:
                    pid,item, x,y,z,textid = pt
                    if my_pid == pid :
                        self._scene.removeItem(item)
                        self._points[pid] = None
        self.update_pix()
        # self.emit(QtCore.pyqtSignal("points_changed"),self)
        self.points_changed.emit()
        return ind

    def set_points (self, points) :
        """Set a point to a new ID

        :Parameters:
         - `pos` (QPointF) - position of the point on the screen
        """
#X         version = self.version
        if self._points :
            for pt in self._points:
                pid,item, x,y,z,textid = pt
                self._scene.removeItem(item)
                self.update_pix()
            self._points = list()
            self._id_gen.clear()
        img = self._view.image()
        if img is not None :
            for i in range(len(points)):
                pid = i
#X                 if version >= 2:
#X                     x,y,z = points[i,0],points[i,1],points[i,2]
#X                 else: 
                x,y,z = points[i,0],points[i,1],points[i,2]
                col = QtGui.QColor.fromHsv( (pid * 10) % 360,255,255)
                item = self._scene.addEllipse(QtCore.QRectF(-10,-10,20,20),
                                              QtGui.QPen(col),QtGui.QBrush(col)  )
                item.setZValue(10)
                i,j,k = self._view.data_coordinates(x,y)
                item.setPos(i,j)
                textid = QtWidgets.QGraphicsSimpleTextItem('%s' % pid, item)
                textid.setPos(8,8)
                textid.setPen(QtGui.QPen(col))
                self._points.append( (pid,item,x,y,z,textid) )
            self.update_pix()
            # self.emit(QtCore.pyqtSignal("points_changed"),self)
            self.points_changed.emit()

def point_selection (image, palette_name = "grayscale", color_index_max = None) :
    
    if not isinstance(image,SpatialImage):
        image = SpatialImage(image)

    w = PointSelection()
    w.set_image(image)
    if color_index_max is None :
        cmax = image.max()
    else :
        cmax = color_index_max
    palette = palette_factory(palette_name,cmax)
    w.set_palette(palette)
    w.show()
    return w
