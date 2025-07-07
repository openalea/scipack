# -*- coding: utf-8 -*-
# -*- python -*-
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

from openalea.core.plugin.plugin import PluginDef
from openalea.oalab.mimedata.plugin import QMimeCodecPlugin


@PluginDef
class IImageCodecPlugin(QMimeCodecPlugin):
    implement = 'IQMimeCodec'
    qtdecode = [
        ('openalealab/data', 'openalea/interface.IImage'),
        ('text/uri-list', 'openalea/interface.IImage'),
    ]

    def __call__(self):
        from openalea.image.mimedata import IImageCodec
        return IImageCodec


@PluginDef
class IImageWidgetSelectorPlugin(object):
    implement = 'IWidgetSelector'
    controls = ['IImage']
    alias = 'IImage editor'
    required = []
    edit_shape = ['responsive']
    paint = True

    def __call__(self):
        from openalea.image.plugin.control import IImageSelector
        return IImageSelector
