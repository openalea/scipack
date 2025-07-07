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
"""
Imaging algorithm plugins
#########################

.. autofunc:: openalea.image.algo.all.segmentation.region_segmentation_extension_based

Imaging algorithms plugins
##########################

To add a new algorithm, you need to follow this approach:
    1. Implement algorithm. This algorithm must follow image filtering specification
    2. Write a plugin class that describe algorithm and is able to load it
    3. register algorithm in the right category


For example, to add a gaussian filter, you need to ...

Step 1:

.. code-block:: python
    :filename: mypackage/algo/image_filtering.py
    :linenos:

    def gaussian_filtering(original, std_dev=0.5, **kwds):
        '''
        Applies a gaussian smoothing filter to the image.
        '''
        # applies gaussian filtering
        # filtered = ...
        # return filtered

Then, define a plugin that describe algorithm.

.. code-block:: python
    :filename: mypackage/plugin/image_filtering.py
    :linenos:

    from openalea.core.plugin import PluginDef

    @PluginDef
    class GaussianSmoothingPlugin(object):
        implement = 'filtering'
        title =  'Gaussian smoothing filter'
        inputs = [
            {'name': 'std_deviation', 'default': 0.5, 'interface': 'IFloat', 'alias': 'Standard Deviation'}
        ]
        authors = [{'name': 'John Doe', 'email': 'john.doe@example.org',
                    'institute': 'Doe Laboratory'}]

        def __call__(self):
            from mypackage.algo.image_filtering import gaussian_smoothing
            return gaussian_smoothing

And register this plugin in category `openalea.image.filtering`

.. code-block:: python
    :filename: setup.py
    :linenos:

    setup(
        # Declare scripts and wralea as entry_points (extensions) of your package
        entry_points={
            'openalea.image': [
                'ImagingPlugin =  mypackage.plugin.image_filtering'
            ]
        },
    )


Plugin Categories
#################


openalea.image
==============

algorithm: **filtering**

.. autoclass:: openalea.image.plugin.IImageFilteringPlugin
    :members:

.. autofunc:: openalea.image.algo.all.image_filtering


algorithm: **region_selection**

.. autofunc:: openalea.image.algo.all.segmentation.region_selection

algorithm: **region_extension**

.. autofunc:: openalea.image.algo.all.segmentation.region_extension


algorithm: **region_segmentation**

.. autofunc:: openalea.image.algo.all.segmentation.region_segmentation

"""
from openalea.core.interface import IInterface


class IImageFilteringPlugin(IInterface):
    name = 'python_name'
    title = 'More readable name'
    inputs = []
    authors = []

    def __call__(self):
        """
        return a function following image filtering specification
        """
