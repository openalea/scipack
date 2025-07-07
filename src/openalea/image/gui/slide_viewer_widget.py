# -*- coding: utf-8 -*-
# -*- python -*-
#
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2015-2023 INRIA - CIRAD - INRA
#
#       File author(s): Guillaume Baty <guillaume.baty@inria.fr>
#                       Christophe Pradal
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

import weakref
import numpy as np

from qtpy import QtWidgets, QtCore

from openalea.image.spatial_image import SpatialImage

from .pixmap_view import PixmapStackView, ScalableLabel
from .pixmap import to_img
from .palette import palette_names, palette_factory

if 'bw' in palette_names:
    palette_names.remove('bw')
palette_names.sort()


def to_image(data, axis=2):
    # Manage also colored images.
    if len(data.shape) == 4 and data.shape[-1] in (3, 4):
        if data.dtype != np.uint8:
            raise Exception("Only uint8 RGB[A] images supported, got %s instead" % str(data.dtype))
    pal = None
    for z in range(data.shape[axis]):
        if axis == 0:
            dat = data[z, :,:] 
        elif axis == 1:
            dat = data[:, z, :] 
        else:
            dat = data[:, :, z]

        if pal is not None:
            dat = pal[dat]
            if isinstance(data, SpatialImage):
                dat = SpatialImage(dat)
        #img = QImage(dat,
        #             data.shape[0],
        #             data.shape[1],
        #             QImage.Format_ARGB32)
        return to_img(dat)


def connect(widget, signal, method):
    if signal:
        if hasattr(signal, 'connect') and hasattr(signal, 'disconnect'):
            signal.connect(method)
        elif isinstance(signal, str):
            widget.connect(widget, QtCore.Signal(signal), method)
        else:
            raise NotImplementedError('Signal %s support is not implemented' % signal)


def disconnect(widget, signal, method):
    if signal:
        if hasattr(signal, 'connect') and hasattr(signal, 'disconnect'):
            signal = signal.signal
        elif isinstance(signal, str):
            pass
        else:
            raise NotImplementedError('Signal %s support is not implemented' % signal)
        widget.disconnect(widget, QtCore.Signal(signal), method)


class ImageStackViewerPanel(QtWidgets.QWidget):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QHBoxLayout(self)

        self.palette_select = QtWidgets.QComboBox()
        for palname in palette_names:
            self.palette_select.addItem(palname)

        #axis
        self.axis = QtWidgets.QComboBox()
        self.axis.addItem("Z-axis")
        self.axis.addItem("Y-axis")
        self.axis.addItem("X-axis")

        #slider
        self.img_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.img_slider.setEnabled(False)

        layout.addWidget(self.palette_select)
        layout.addWidget(self.img_slider)
        layout.addWidget(self.axis)

        self._viewer = None

    def set_stack_viewer(self, widget):
        if widget is self._viewer:
            return

        # Disconnect old viewer
        if self._viewer is not None:
            disconnect(self, self.img_slider.valueChanged, self._viewer.slice_changed)
            disconnect(self, self.axis.currentIndexChanged, self._viewer.change_axis)
            disconnect(self, self.palette_select.currentIndexChanged, self._on_palette_name_changed)
            disconnect(self._viewer, self._viewer.valueChanged, self._on_stack_changed)

        # Connect new one
        if widget is not None:
            self._viewer = widget
            connect(self, self.img_slider.valueChanged, self._viewer.slice_changed)
            connect(self, self.axis.currentIndexChanged, self._viewer.change_axis)
            connect(self, self.palette_select.currentIndexChanged, self._on_palette_name_changed)
            connect(self._viewer, self._viewer.stackChanged, self._on_stack_changed)

            self._viewer.emit_stack_changed()

    def _on_palette_name_changed(self, idx):
        palette_name = str(self.palette_select.currentText())
        if self._viewer:
            self._viewer.change_palette(palette_name)

    def _on_stack_changed(self, stack):
        if stack is None:
            return
        axis = stack['axis']
        shape = stack['shape']

        self.img_slider.setRange(0, shape[axis] - 1)
        self.img_slider.setEnabled(True)
        self.img_slider.setValue(stack['slice'])

        palette_name = stack['palette_name']
        if palette_name:
            if palette_name in palette_names:
                self.palette_select.setCurrentIndex(palette_names.index(palette_name))


class ImageStackViewerWidget(QtWidgets.QWidget):

    """
    Widget based on openalea.image.gui.slide_viewer.PixmapStackView
    """
    valueChanged = QtCore.Signal(object)
    stackChanged = QtCore.Signal(object)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self._im_view = PixmapStackView()
        self._label = ScalableLabel()

        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.addWidget(self._label)

        self._label.setMouseTracking(True)
        self._last_mouse_x = 0
        self._last_mouse_y = 0

        self.connect(self._label, QtCore.SIGNAL("mouse_press"), self.mouse_pressed)
        self.connect(self._label, QtCore.SIGNAL("mouse_move"), self.mouse_pressed)

        self.axis = 2
        self.inc = 1 # index increment
        self._palette_name = None

    ##############################################
    #        Qt Control API
    ##############################################

    def setValue(self, img):
        if img is self.value():
            return
        self._im_view.set_image(img)
        try:
            self.resolution = img.resolution[:]
        except AttributeError:
            pass

        self._im_view._reconstruct_pixmaps()
        self.change_axis(0)
        self.slice_changed((0 + self._im_view.nb_slices() - 1) / 2)

        self.emit_stack_changed()

    def value(self):
        return self._im_view.image()

    ##############################################
    #        slots
    ##############################################

    def emit_stack_changed(self):
        img = self.value()
        if img is None:
            self.stackChanged.emit(None)
        else:
            args = dict(shape=img.shape, axis=self.axis,
                        slice=self._im_view.current_slice(),
                        resolution=self.resolution, inc=self.inc,
                        palette_name=self._palette_name)
            self.stackChanged.emit(args)

    def change_axis(self, ind):
        if self.axis == ind:
            return
        try:
            res = list(self.resolution)
            del res[self.axis]
            tr = self._im_view._transform
            print(res)
            if tr % 180:
                self._label._resolution = res[1], res[0]
            else:
                self._label.set_resolution(*res[:2])
        except AttributeError:
            pass
        self._im_view._reconstruct_pixmaps(self.axis)
        self.emit_stack_changed()
        self.update_pix()
        #self.fill_infos()

    def mouse_pressed(self, event):
        self._last_mouse_x = event.x()
        self._last_mouse_y = event.y()

    def change_palette(self, palette_name):
        if palette_name == self._palette_name:
            return

        self._palette_name = palette_name
        self.emit_stack_changed()

        img = self._im_view.image()
        if img is None:
            return

        palette = palette_factory(palette_name, img.max())
        self._im_view.set_palette(palette, self.axis)
        self.update_pix()

    def update_pix(self):
        pix = self._im_view.pixmap()
        if pix is not None:
            self._label.setPixmap(pix)

    def get_pixel_value_str(self, img, x, y, z):
        px = img[x, y, z]
        if isinstance(px, np.ndarray):
            return str(px)
        else:
            return "%3d" % px

    def slice_changed(self, ind):
        img = self.value()
        if img is None:
            return

        if ind >= img.shape[self.axis]:
            ind = img.shape[self.axis] - 1
        if ind < 0:
            ind = 0
        if self._im_view.current_slice() == ind:
            return
        self._im_view.set_current_slice(ind)
        self.emit_stack_changed()
        self.update_pix()

    def snapshot(self):
        """write the current image
        """
        pix = self._im_view.pixmap()
        if pix is not None:
            pix.save("slice%.4d.png" % self.panel.img_slider.value())

    def wheelEvent(self, event):
        self.inc = event.delta() / 8 / 15
        idx = self._im_view.current_slice()
        self.slice_changed(idx + self.inc)

    def rotate_left(self):
        res = self._label._resolution
        self._label._resolution = res[1], res[0]
        self._im_view.rotate(-1)
        self.update_pix()

    def rotate_right(self):
        res = self._label._resolution
        self._label._resolution = res[1], res[0]
        self._im_view.rotate(1)
        self.update_pix()


if __name__ == '__main__':
    from openalea.deploy.shared_data import shared_data
    from openalea.image.serial.basics import imread
    import openalea.oalab
    img_path = shared_data(openalea.oalab, 'icons/Crystal_Clear_app_clock.png')
    img = imread(img_path)

    import numpy
    matrix = numpy.zeros((100, 100, 100), dtype=numpy.uint8)
    matrix[90:100, :10, :10] = 1
    matrix[:10, 90:100, :10] = 2
    matrix[:10, :10, 90:100] = 3
    img3d = SpatialImage(matrix)

    instance = QtWidgets.QApplication.instance()
    if instance is None:
        app = QtWidgets.QApplication([])
    else:
        app = instance

    slider = ImageStackViewerWidget()
    slider.setValue(img)
    slider.show()

    slider_3d = ImageStackViewerWidget()
    slider_3d.setValue(img3d)
    slider_3d.show()

    panel = ImageStackViewerPanel()
    panel.show()
    panel.set_stack_viewer(slider)

    if instance is None:
        app.exec_()
