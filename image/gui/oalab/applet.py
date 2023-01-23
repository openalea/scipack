# -*- coding: utf-8 -*-
# -*- python -*-
#
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2015-2023 INRIA - CIRAD - INRA
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

from openalea.vpltk.qt import QtWidgets, QtCore
from openalea.image.gui.slide_viewer_widget import ImageStackViewerWidget, ImageStackViewerPanel, connect, disconnect
from openalea.core.observer import AbstractListener
from openalea.core.world import World
from openalea.image.spatial_image import SpatialImage


class ImageStackViewer(QtWidgets.QTabWidget, AbstractListener):

    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        AbstractListener.__init__(self)

        self.setAcceptDrops(True)

        self._image = {}
        self._viewer = {}

        self._create_connections()

    def initialize(self):
        self.world = World()
        self.world.register_listener(self)

    def notify(self, sender, event=None):
        signal, data = event
        if signal == 'world_sync':
            self.set_world(data)
        elif signal == 'world_object_removed':
            world, old = data
            self.remove_world_object(world, old)
        elif signal == 'world_object_changed':
            world, old, new = data
            self.set_world_object(world, new)
        elif signal == 'world_object_item_changed':
            world, obj, item, old, new = data
            if item == 'attribute':
                self.update_world_object(world, obj, item, old, new)

    def set_image(self, name, image):
        if name in self._viewer:
            viewer = self._viewer[name]
        else:
            viewer = ImageStackViewerWidget()
            viewer.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            connect(viewer, viewer.stackChanged, self._on_stack_changed)
            self._viewer[name] = viewer
            self._image[viewer] = name
            self.addTab(viewer, name)

        viewer.setValue(image)

    def remove_image(self, name):
        if name in self._viewer:
            viewer = self._viewer[name]
            disconnect(viewer, viewer.stackChanged, self._on_stack_changed)
            self.removeTab(self.indexOf(viewer))
            viewer.close()
            del self._image[viewer]
            del self._viewer[name]

    def set_world_object(self, world, world_object):
        if not isinstance(world_object.data, SpatialImage):
            return
        self.set_image(world_object.name, world_object.data)

    def remove_world_object(self, world, world_object):
        if not isinstance(world_object.data, SpatialImage):
            return
        self.set_image(world_object.name, world_object.data)

    def set_world(self, world):
        # Clear viewer
        for image in self._viewer.keys():
            self.remove_image(image)

        # Set object in viewer
        for obj_name, world_object in world.items():
            self.set_world_object(world, world_object)

    def update_world_object(self, world, obj, item, old, new):
        attr_name = new['name']
        if attr_name.endswith('plane_position'):
            axis = list('xyz').index(attr_name[0])
            position = new['value']
            if obj.name in self._viewer:
                viewer = self._viewer[obj.name]
                viewer.change_axis(axis)
                viewer.slice_changed(position)

    def _create_connections(self):
        self.currentChanged.connect(self._on_current_image_changed)

    def _on_current_image_changed(self, idx):
        pass

    def _on_stack_changed(self, stack):
        name = self._image[self.sender()]
        if stack:
            world_object = self.world[name]
            cut_plane = '%s_plane_position' % ('xyz'[stack['axis']])
            world_object.set_attribute(cut_plane, stack['slice'])
