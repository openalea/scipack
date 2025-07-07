# -*- coding: utf-8 -*-
# -*- python -*-
#
#       Copyright 2015 INRIA- CIRAD - INRA
#
#       File author(s): Guillaume Baty <guillaume.baty@inria.fr>
#
#       File contributor(s):
#           Christophe Godin <christophe.godin@inria.fr>
#           Daniel Barbeau <daniel.barbeau@inria.fr>
#           Eric Moscardi <eric.moscardi@sophia.inria.fr>
#           Grégoire Malandain <gregoire.malandain@inria.fr>
#           Guillaume Baty <guillaume.baty@inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       WebSite : http://openalea.github.io
#
###############################################################################

from openalea.core.service.plugin import plugin_function


def image_filtering(original, method=None, **kwds):
    """
    :param original: original image
    :type original: :class:`~openalea.image.spatial_image.SpatialImage`

    :param method: method identifier you want to use (ex: "gaussian_smoothing")
    :type method: :obj:`str`
    """
    if method is None:
        return original

    func = plugin_function('openalea.image', method)
    if func is not None:
        return func(original, **kwds)
    else:
        raise NotImplementedError(method)
