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

__all__ = [
    'region_extension',
    'region_labeling',
    'region_segmentation',
    'region_segmentation_extension_based',
    'region_selection',
]

from openalea.core.service.plugin import plugin_function
from openalea.image.algo.image_filtering import image_filtering


def notimplemented(original, **kwds):
    raise NotImplementedError

import copy


def extract_args(prefix, kwds, default=None):
    """
    >>> kwds = dict(rseb_image_filtering_1_std_dev=0.6)
    >>> default = dict(std_dev=0.5, p2=1)
    >>> kwds = extract_args("rseb_image_filtering_1", kwds=kwds, default=default)
    >>> kwds["std_dev"]
    0.6
    >>> kwds["p2"]
    1
    """
    if default is None:
        default = {}
    default_kwds = copy.copy(default)
    method_kwds = {}
    #generic_kwds = {}
    for k, v in kwds.items():
        if k.startswith(prefix):
            short_name = k[len(prefix) + 1:]
            method_kwds[short_name] = v
        #else:
        #    generic_kwds[k] = v

    #default_kwds.update(generic_kwds)
    default_kwds.update(method_kwds)
    return default_kwds


def region_labeling(original, method, **kwds):
    """
    :param original: original image
    :type original: :class:`~openalea.image.spatial_image.SpatialImage`

    :param method: method identifier you want to use (ex: "seed_extraction")
    :type method: :obj:`str`
    """
    method_dict = {
        "seed_extraction": notimplemented,
        "connected_component_extraction": notimplemented,
    }
    if method in method_dict:
        return method_dict[method](original, **kwds)
    else:
        raise NotImplementedError(method)


def region_selection(segmented, labels, method, **kwds):
    """
    :param segmented: segmented image
    :type segmented: :class:`~openalea.image.spatial_image.SpatialImage`

    :param labels: label image
    :type labels: :class:`~openalea.image.spatial_image.SpatialImage`  

    :param method: method identifier you want to use (ex: "remove_small_cells")
    :type method: :obj:`str`
    """
    func = plugin_function('openalea.image', method)
    if func is not None:
        return func(segmented, labels, **kwds)
    else:
        raise NotImplementedError(method)


def region_extension(segmented, labels, method, **kwds):
    """
    :param segmented: segmented image
    :type segmented: :class:`~openalea.image.spatial_image.SpatialImage`

    :param labels: label image
    :type labels: :class:`~openalea.image.spatial_image.SpatialImage`  

    :param method: method identifier you want to use (ex: "watershed")
    :type method: :obj:`str`
    """
    func = plugin_function('openalea.image', method)
    if func is not None:
        return func(segmented, labels, **kwds)
    else:
        raise NotImplementedError(method)


def region_segmentation_extension_based(original, method, **kwds):
    """
    :param original: original image
    :type original: :class:`~openalea.image.spatial_image.SpatialImage`

    :param method: method identifier you want to use (ex: "extension_based")
    :type method: :obj:`str`
    """
    image_filtering_1_default = dict(
        method='gaussian_smoothing',
        std_dev=0.5
    )
    image_filtering_1_kwds = extract_args(prefix='rseb_image_filtering_1', kwds=kwds, default=image_filtering_1_default)
    filtered = image_filtering(original, **image_filtering_1_kwds)

    image_filtering_2_method = kwds.pop('rseb_image_filtering_2_method', None)
    filtered = image_filtering(filtered, method=image_filtering_2_method, **kwds)

    region_labeling_method = kwds.pop('rseb_region_labeling', 'seed_extraction')
    labels = region_labeling(filtered, method=region_labeling_method, **kwds)

    region_extension_method = kwds.pop('rseb_region_extension', 'watershed')
    segmented = region_extension(filtered, labels, method=region_extension_method, **kwds)

    region_selection_method = kwds.pop('rseb_region_selection', 'remove_small_sized_cells')
    if region_selection_method is not None:
        labels = region_selection(segmented, labels, method=region_selection_method, **kwds)
        segmented = region_extension(filtered, labels, method=region_extension_method, **kwds)

    return segmented


def region_segmentation(original, method, **kwds):
    """
    :param original: original image
    :type original: :class:`~openalea.image.spatial_image.SpatialImage`

    :param method: method identifier you want to use (ex: "extension_based")
    :type method: :obj:`str`
    """
    func = plugin_function('openalea.image', method)
    if func is not None:
        return func(original, **kwds)
    else:
        raise NotImplementedError(method)
